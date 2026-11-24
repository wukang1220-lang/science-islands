"""Count past 會考 items per section and write weights.json (items per island).

python -I tally_weights.py <folder of text files>
The folder holds the question bank's 各章節會考試題 files converted to text (antiword -m UTF-8.txt),
named v<volume>__<original name>.txt. Only the number of items is used: each item ends with a
"出處：" line. No question text is copied into this project.
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
st = json.load(open(os.path.join(HERE, "structure.json"), encoding="utf-8"))
isle_of = {s["id"]: ch["isle"] for g in st.values() for ch in g["ch"] for s in ch["secs"]}
pat = re.compile(r"^v0(\d)__\d+_(\d+)_(\d+)-(\d+)[ _]")
per_sec, unknown = {}, []
for f in sorted(glob.glob(os.path.join(sys.argv[1], "*.txt"))):
    name = os.path.basename(f)
    m = pat.match(name)
    if m:
        v, ch, a, b = m.groups()
        sid = f"s{v}-{int(a)}-{int(b)}"
    elif "跨科" in name:
        sid = f"s{name[2]}-x"
    elif "實驗室常用器材" in name:
        sid = f"s{name[2]}-lab"
    else:
        unknown.append(name)
        continue
    if sid not in isle_of:
        unknown.append(name)
        continue
    n = sum(1 for line in open(f, encoding="utf-8", errors="replace") if line.startswith("出處"))
    per_sec[sid] = per_sec.get(sid, 0) + n
if unknown:
    sys.exit(f"could not place: {unknown}")
w = {}
for g in st.values():
    for i in g["isles"]:
        w[i["id"]] = sum(n for sid, n in per_sec.items() if isle_of[sid] == i["id"])
json.dump(w, open(os.path.join(HERE, "weights.json"), "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=0)
tot = sum(w.values())
print(f"{len(per_sec)} sections, {tot} items")
for g, gd in st.items():
    print(g, sum(w[i["id"]] for i in gd["isles"]), {i["id"]: w[i["id"]] for i in gd["isles"]})
