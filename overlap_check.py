"""Flag new text that copies long runs from source material (question bank, summary books).
python -I overlap_check.py <content json> <source txt>... ; prints runs of >= MIN chars.
Source files may be UTF-8 or UTF-16 (Word's "Unicode text" export)."""
import json, re, sys
MIN = 14


def read(p):
    raw = open(p, "rb").read()
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return raw.decode("utf-16")
    return raw.decode("utf-8-sig", errors="replace")


new = json.load(open(sys.argv[1], encoding="utf-8"))
src = "".join(read(p) for p in sys.argv[2:])
norm = lambda t: re.sub(r"[\s\*「」『』《》【】（）()，。、；：！？,.;:!?─—…·\-]", "", t)
S = norm(src)
hits = 0
for sid, v in new.items():
    texts = [("k", t) for t in v["k"]] + [(kind, " ".join([q[0]] + q[1] + [q[3]])) for kind in ("q", "c") for q in v.get(kind, [])]
    for kind, t in texts:
        n = norm(t)
        best = ""
        i = 0
        while i + MIN <= len(n):
            L = MIN
            if n[i:i+L] in S:
                while i + L < len(n) and n[i:i+L+1] in S:
                    L += 1
                if L > len(best):
                    best = n[i:i+L]
                i += L
            else:
                i += 1
        if best:
            hits += 1
            print(f"{sid} {kind} [{len(best)}] {best}")
print("flagged:", hits)
