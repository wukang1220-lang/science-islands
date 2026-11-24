"""Build science-islands.html from structure.json + content/*.json + extras.json + weights.json + art/ + tpl.html.

python -I build.py [preview_out]
Writes ../science-islands.html (published as the claude.ai artifact, which adds its own page
skeleton) and docs/index.html (the same page as a full document).

content/*.json: {"<section id>": {"k": [10-20 key points, each with 1-2 **red terms**],
                                  "q": [6 practice questions], "c": [2 exam-style questions]}}
A question is [stem, [4 options], answer index 0-3, explanation]. Options are shuffled per
question with a fixed seed so answers spread over A-D; questions whose options are all numbers
keep their order. Sections with no content yet are shown as "建造中" (under construction);
an island opens only when every one of its sections has content.
extras.json maps a section id to {"fig": [diagram ids], "w": widget name, "wd": widget data}.
weights.json (optional) maps an island id to its share of past 會考 items (any positive scale).
qbase.json (optional, written after the first publish) holds each section's question counts;
questions may only be appended, never removed or reordered, because progress is stored per
question id.
"""
import glob, json, os, random, re, sys, zlib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "science-islands.html")
DOCS = os.path.join(HERE, "docs", "index.html")
HEAD = ('<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" '
        'content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}'
        'body{margin:0;font:14px system-ui,sans-serif}[hidden]{display:none!important}</style></head><body>')
sys.path.insert(0, os.path.join(HERE, "art"))
from check_svg import check  # noqa: E402

WIDGETS = {"enzyme", "osmosis", "transpire", "circulation", "reaction", "tropism", "breathing", "sugar", "division",
           "punnett", "abo", "capture", "energy", "states", "dissolve", "atombuild", "massbal", "eqbalance", "rate", "equil", "displace", "cellbuild", "electrolysis", "phscale", "titrate", "wavelab", "soundlab", "refractlab", "lenslab", "colorlab", "mixlab", "springlab", "buoylab", "motionlab", "cartlab", "torquelab", "energylab", "circuitlab", "billlab", "inductlab", "moonlab", "seasonlab", "faultlab", "stratalab", "rockkey", "lapselab", "windlab", "slopelab", "fairlab", "scalelab", "footprint"}
st = json.load(open(os.path.join(HERE, "structure.json"), encoding="utf-8"))
content = {}
for f in sorted(glob.glob(os.path.join(HERE, "content", "*.json"))):
    d = json.load(open(f, encoding="utf-8"))
    dup = set(d) & set(content)
    assert not dup, f"{os.path.basename(f)} repeats sections {sorted(dup)}"
    content.update(d)
def load_opt(name):
    p = os.path.join(HERE, name)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None
extras = load_opt("extras.json") or {}
weights = load_opt("weights.json")
qbase = load_opt("qbase.json") or {}
# scenes.json: the walkable 3D island. One booth per section:
# {"<section id>": {"b": booth kind, "sign": booth name, "npc": {"n": name, "r": role, "body": colour, "hat": kind}, "say": [lines]}}
# Sections without an entry get a plain kiosk and a generic islander.
scenes = load_opt("scenes.json") or {}
# guides.json: each island's 領航員 {"<isle id>": {"n": name, "hs": hair style, "hat": kind}}; names must differ from every islander
guides = load_opt("guides.json") or {}
BOOTHS = {"market", "lab", "greenhouse", "train", "kiosk", "scope", "heart", "garden", "pond", "fossil", "helix",
          "breath", "tree", "brain", "beaker", "blocks", "eye", "still", "atom", "periodic", "molecule",
          "balance", "seesaw", "fire", "furnace", "battery", "ph", "loom", "soap", "pendulum", "ruler", "cylinder", "wave", "drum", "harp", "sonar", "pinhole", "mirror", "tank", "lens", "prism", "thermo", "kettle", "ice", "convect", "spring", "sled", "jack", "float", "track", "ramp", "drop", "rocket", "orbit", "lever", "turbine", "pulley", "spark", "bulb", "house", "compass", "coil", "motor", "dynamo", "watercycle", "river", "crystal", "plates", "volcano", "solar", "tilt", "moonphase", "balloon", "windvane", "front", "typhoon", "current", "icecap", "landslide", "burner", "shelf", "sdgwheel", "sunpanel", "recycle", "seawall"}
HATS = {"chef", "goggles", "straw", "cap", "none", "beanie", "explorer", "flower", "crown"}
warn = []
errs = []


def svg(kind, name):
    path = os.path.join(HERE, "art", kind, name + ".svg")
    if not os.path.exists(path):
        warn.append(f"missing art/{kind}/{name}.svg")
        return None
    e = check(path, kind)
    if e:
        warn.append(f"skipped art/{kind}/{name}.svg: {e[0]}")
        return None
    s = open(path, encoding="utf-8").read().strip()
    s = re.sub(r">\s+<", "><", s)
    s = re.sub(r"\s+", " ", s)
    if kind == "isles":
        s = re.sub(r"<title>.*?</title>", "", s)
        s = s.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)
    return s


# 提示卡：每題配一條最相關的重點（和題幹、正解重疊最多的雙字詞），把正解字詞挖空成＿＿
HPUNC = re.compile(r"[\s，。、；：「」『』（）()？！,.?!*]")
def grams(t):
    t = HPUNC.sub("", t)
    return {t[i:i + 2] for i in range(len(t) - 1)}
def make_hint(stem, ans, kps):
    tg, ag = grams(stem), grams(ans)
    best, score = kps[0], -1
    for kp in kps:
        g = grams(kp)
        sc = len(g & tg) + 2 * len(g & ag)
        if sc > score:
            best, score = kp, sc
    a = ans.strip("。")
    out, hit = best, False
    for r in re.findall(r"\*\*(.+?)\*\*", best):
        if r in a or (len(a) >= 2 and a in r):
            out, hit = out.replace(f"**{r}**", "＿＿"), True
    out = out.replace("**", "")
    if not hit and len(a) >= 2 and a in out:
        out = out.replace(a, "＿＿", 1)
    return out

def check_q(sid, kind, qi, q):
    where = f"{sid} {kind}[{qi}]"
    if not (isinstance(q, list) and len(q) == 4):
        errs.append(f"{where}: must be [stem, options, answer, explanation]")
        return False
    stem, opts, ans, exp = q
    if not (isinstance(opts, list) and len(opts) == 4 and all(isinstance(o, str) and o.strip() for o in opts)):
        errs.append(f"{where}: needs 4 non-empty options")
        return False
    if len(set(opts)) != 4:
        errs.append(f"{where}: options repeat")
    if ans not in (0, 1, 2, 3):
        errs.append(f"{where}: answer must be 0-3")
        return False
    if not (stem.strip() and exp.strip()):
        errs.append(f"{where}: empty stem or explanation")
    return True


numeric = re.compile(r"^[0-9０-９\-−.]")
spread = [0, 0, 0, 0]
nsec = nready = nq = nc = nfig = nw = npts = nkey = 0
known = set()
for g, gd in st.items():
    for isle in gd["isles"]:
        a = os.path.exists(os.path.join(HERE, "art", "isles", f"{g}-{isle['id']}.svg")) and svg("isles", f"{g}-{isle['id']}")
        if a:
            isle["svg"] = a
    for ch in gd["ch"]:
        for s in ch["secs"]:
            sid = s["id"]
            known.add(sid)
            nsec += 1
            c = content.get(sid)
            if not c:
                continue
            nready += 1
            k = c.get("k", [])
            if not 10 <= len(k) <= 20:
                errs.append(f"{sid}: {len(k)} key points (need 10-20)")
            for t in k:
                n = t.count("**")
                if n % 2:
                    errs.append(f"{sid}: unclosed ** in {t[:30]}")
                elif not 2 <= n <= 4:
                    errs.append(f"{sid}: {n // 2} red terms in {t[:30]} (need 1-2)")
                if "****" in t:
                    errs.append(f"{sid}: two red terms touch in {t[:30]}")
            nkey += sum(t.count("**") // 2 for t in k)
            npts += len(k)
            s["k"] = k
            for kind, need in (("q", 6), ("c", 2)):
                qs = c.get(kind, [])
                if len(qs) != need:
                    errs.append(f"{sid}: {len(qs)} {kind} questions (need {need})")
                base = qbase.get(sid, {}).get(kind, 0)
                if len(qs) < base:
                    errs.append(f"{sid}: {kind} lost questions ({len(qs)} < {base}); only append new ones")
                out = []
                for qi, q in enumerate(qs):
                    if not check_q(sid, kind, qi, q):
                        continue
                    stem, opts, ans, exp = q
                    order = list(range(4))
                    if not all(numeric.match(o) for o in opts):
                        random.Random(zlib.crc32(f"{sid}.{kind}{qi}".encode())).shuffle(order)
                    out.append([stem, [opts[i] for i in order], order.index(ans), exp, make_hint(stem, opts[ans], k)])
                    spread[order.index(ans)] += 1
                s[kind] = out
                if kind == "q":
                    nq += len(out)
                else:
                    nc += len(out)
            ex = extras.get(sid, {})
            figs = [f for f in (svg("figs", n) for n in ex.get("fig", [])) if f]
            if figs:
                s["fig"] = figs
                nfig += len(figs)
            if ex.get("w"):
                if ex["w"] not in WIDGETS:
                    errs.append(f"{sid}: unknown widget {ex['w']}")
                else:
                    s["w"] = ex["w"]
                    if "wd" in ex:
                        s["wd"] = ex["wd"]
                    nw += 1
for sid, sc in scenes.items():
    npc = sc.get("npc", {})
    if sc.get("b") not in BOOTHS:
        errs.append(f"scenes.json {sid}: unknown booth {sc.get('b')}")
    if not (sc.get("sign") and len(sc["sign"]) <= 6):
        errs.append(f"scenes.json {sid}: sign must be 1-6 characters")
    if not (npc.get("n") and npc.get("r") and re.fullmatch(r"#[0-9a-fA-F]{6}", npc.get("body", "")) and npc.get("hat") in HATS):
        errs.append(f"scenes.json {sid}: npc needs n, r, body (#rrggbb) and hat in {sorted(HATS)}")
    if not (isinstance(sc.get("say"), list) and 2 <= len(sc["say"]) <= 5 and all(isinstance(t, str) and t.strip() for t in sc["say"])):
        errs.append(f"scenes.json {sid}: say needs 2-5 lines")
unknown = (set(extras) | set(content) | set(scenes)) - known
if unknown:
    errs.append(f"unknown section ids: {sorted(unknown)}")
isle_ids = {i["id"] for gd in st.values() for i in gd["isles"]}
if weights is not None:
    bad = set(weights) - isle_ids
    if bad:
        errs.append(f"weights.json has unknown islands: {sorted(bad)}")
npc_names = {sc.get("npc", {}).get("n") for sc in scenes.values()}
seen = {}
for iid in sorted(isle_ids):
    gd = guides.get(iid)
    if not gd:
        errs.append(f"guides.json: no guide for island {iid}")
        continue
    n = gd.get("n", "")
    if not (1 <= len(n) <= 3) or n in npc_names or n in seen or gd.get("hat") not in HATS or gd.get("hs") not in {"short", "pony", "bob", "spiky", "bun"}:
        errs.append(f"guides.json {iid}: name must be 1-3 characters, unique and not an islander's name; hat in HATS; hs short/pony/bob/spiky/bun")
    seen[n] = iid
for iid in set(guides) - isle_ids:
    errs.append(f"guides.json has unknown island {iid}")
# halls/*.json: each section's 展覽館 {"<sid>": {"n": hall name, "st": style, "o": roof ornament, "c": wall colour?, "d": description, "m": [[迷思, 正解], ...]}}
HSTYLES = {"gable", "dome", "glass", "factory", "vault", "modern", "tower"}
HORNS = {"frog", "lens", "cell", "drop", "cube", "apple", "flask", "sun", "train", "tree", "leaf", "heart", "eye", "bolt",
         "bulb", "lungs", "thermo", "egg", "dna", "shell", "butterfly", "mushroom", "flower", "fish", "bee", "bird", "paw",
         "clock", "ruler", "wave", "note", "flame", "mirror", "rainbow", "snow", "spring", "gear", "boat", "arrow",
         "feather", "rocket", "planet", "scale", "wind", "battery", "magnet", "crystal", "atom", "molecule", "bubble",
         "yarn", "cloud", "mountain", "globe", "volcano", "moon", "balloon", "swirl", "recycle"}
halls = {}
hdir = os.path.join(HERE, "halls")
for fn in sorted(os.listdir(hdir)) if os.path.isdir(hdir) else []:
    if fn.endswith(".json"):
        for sid, h in json.load(open(os.path.join(hdir, fn), encoding="utf-8")).items():
            if sid in halls:
                errs.append(f"halls/{fn}: {sid} defined twice")
            halls[sid] = h
hnames = {}
for sid in sorted(known):
    h = halls.get(sid)
    if not h:
        errs.append(f"halls: no hall for {sid}")
        continue
    n = h.get("n", "")
    if not (2 <= len(n) <= 7) or n in hnames:
        errs.append(f"halls {sid}: name must be 2-7 characters and unique ({n})")
    hnames[n] = sid
    if h.get("st") not in HSTYLES or h.get("o") not in HORNS:
        errs.append(f"halls {sid}: st must be in {sorted(HSTYLES)}, o in HORNS")
    if "c" in h and not re.fullmatch(r"#[0-9a-fA-F]{6}", h["c"]):
        errs.append(f"halls {sid}: c must be #rrggbb")
    if not (25 <= len(h.get("d", "")) <= 90 and h["d"].endswith("。")):
        errs.append(f"halls {sid}: d must be 25-90 characters ending with 。 ({len(h.get('d', ''))})")
    m = h.get("m")
    if not (isinstance(m, list) and 2 <= len(m) <= 3 and all(isinstance(x, list) and len(x) == 2 and all(isinstance(t, str) and len(t) >= 6 and t.endswith("。") for t in x) for x in m)):
        errs.append(f"halls {sid}: m needs 2-3 [迷思, 正解] pairs, each ending with 。")
for sid in set(halls) - known:
    errs.append(f"halls has unknown section {sid}")
for w in warn:
    print("warning:", w)
if errs:
    for e in errs:
        print("ERROR:", e)
    sys.exit(f"{len(errs)} errors; nothing written")

data = json.dumps(st, ensure_ascii=False, separators=(",", ":"))
wdata = json.dumps(weights, ensure_ascii=False, separators=(",", ":")) if weights else "null"
sdata = json.dumps(scenes, ensure_ascii=False, separators=(",", ":"))
gdata = json.dumps(guides, ensure_ascii=False, separators=(",", ":"))
hdata = json.dumps(halls, ensure_ascii=False, separators=(",", ":"))
assert "</script" not in (data + wdata + sdata + gdata + hdata).lower()
tpl = open(os.path.join(HERE, "tpl.html"), encoding="utf-8").read()
for mark in ("/*@DATA@*/null", "/*@WEIGHT@*/null", "/*@SCENE@*/null", "/*@GUIDE@*/null", "/*@HALL@*/null"):
    assert mark in tpl, mark
html = tpl.replace("/*@DATA@*/null", data).replace("/*@WEIGHT@*/null", wdata).replace("/*@SCENE@*/null", sdata).replace("/*@GUIDE@*/null", gdata).replace("/*@HALL@*/null", hdata)
open(OUT, "w", encoding="utf-8", newline="\n").write(html)
print(f"wrote {os.path.normpath(OUT)}: {len(html):,} chars, {nready}/{nsec} sections ready, {npts} key points "
      f"({nkey} red terms), {nq} practice + {nc} exam-style questions, {nfig} diagrams, {nw} widgets, answer spread A-D {spread}")
os.makedirs(os.path.dirname(DOCS), exist_ok=True)
open(DOCS, "w", encoding="utf-8", newline="\n").write(HEAD + html + "</body></html>")
open(os.path.join(HERE, "docs", ".nojekyll"), "w").close()
print("wrote", os.path.normpath(DOCS))
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8", newline="\n").write(HEAD + html + "</body></html>")
    print("preview", sys.argv[1])
