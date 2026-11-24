"""Write structure.json: five groups, 33 islands, 132 sections, grouped by subject nature (not by grade).

python -I make_structure.py

Section titles come from the file names in the question bank's 01_試題 folders
(D:\\cluade\\國中題庫\\國中自然科學\\題本檔案\\0N_第N冊\\01_試題). Only the names are read.
Section id: s<volume>-<chapter>-<section>, cross-subject topics s<volume>-x, lab equipment s3-lab.
The volume numbers stay inside the ids; the page never shows them.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = r"D:\cluade\國中題庫\國中自然科學\題本檔案"

# group -> list of (island id, name, tag, colour, light colour, [(unit name, [section ids])])
ISLES = {
 "bio": [
  ("cell", "生命與細胞島", "生物的特徵、細胞構造與組成層次", "#2c8a56", "#6fd29b",
   [("生命世界", ["s1-1-1"]), ("細胞與組成層次", ["s1-2-1", "s1-2-2", "s1-2-3", "s1-2-4"])]),
  ("food", "養分島", "養分與能量、酵素、光合作用與消化", "#3c8c2e", "#8fd47e",
   [("食物與酵素", ["s1-3-1", "s1-3-2"]), ("養分的製造與獲得", ["s1-3-3", "s1-3-4"])]),
  ("flow", "運輸與循環島", "植物的維管束與人體的血液循環", "#b8322a", "#ff8a7e",
   [("植物的運輸", ["s1-4-1", "s1-4-2"]), ("人體的循環", ["s1-4-3", "s1-4-4"])]),
  ("sense", "協調與感應島", "刺激與反應、神經、內分泌與行為", "#8a4fb3", "#c79be6",
   [("刺激、協調與行為", ["s1-5-1", "s1-5-2", "s1-5-3", "s1-5-4"])]),
  ("homeo", "恆定島", "氣體、水分、體溫與血糖的恆定", "#1a8aa0", "#6fd6e6",
   [("體內的恆定", ["s1-6-1", "s1-6-2", "s1-6-3"])]),
  ("repro", "生殖島", "細胞分裂、無性生殖與有性生殖", "#c2502a", "#ff9a73",
   [("細胞分裂與生殖", ["s2-1-1", "s2-1-2", "s2-1-3"])]),
  ("gene", "遺傳島", "基因與染色體、人類遺傳與生物技術", "#6a4bb0", "#b39cf0",
   [("遺傳與生物技術", ["s2-2-1", "s2-2-2", "s2-2-3", "s2-2-4"])]),
  ("evo", "演化與分類島", "化石與演化、命名分類與五界", "#8a5a2b", "#d7a06a",
   [("演化", ["s2-3-1"]), ("分類與五界", ["s2-3-2", "s2-3-3", "s2-3-4", "s2-3-5"])]),
  ("eco", "生態島", "族群群集、生物的互動與生態系", "#2f7d6b", "#7fd6c0",
   [("族群與互動", ["s2-4-1", "s2-4-2"]), ("生態系", ["s2-4-3", "s2-4-4"])]),
  ("bdiv", "多樣性與保育島", "生物多樣性、面臨的危機與保育", "#4f7f2a", "#a9d77e",
   [("生物多樣性與保育", ["s2-5-1", "s2-5-2", "s2-5-3"])]),
 ],
 "phy": [
  ("meas", "測量島", "長度、質量、時間、體積與密度", "#2f6fb5", "#7fb4ee",
   [("測量", ["s3-1-1", "s3-1-2", "s3-1-3"])]),
  ("wave", "波與聲音島", "波的特徵、聲音的產生與傳播", "#1a8aa0", "#6fd6e6",
   [("波與聲音", ["s3-3-1", "s3-3-2", "s3-3-3", "s3-3-4"])]),
  ("light", "光島", "光的傳播、反射、折射與透鏡成像", "#b07a12", "#f0c550",
   [("光的性質與成像", ["s3-4-1", "s3-4-2", "s3-4-3", "s3-4-4", "s3-4-5"])]),
  ("heat", "熱島", "溫度、熱量、比熱與熱的傳播", "#c2502a", "#ff9a73",
   [("溫度與熱", ["s3-5-1", "s3-5-2", "s3-5-3", "s3-5-4", "s3-5-5"])]),
  ("press", "力與壓力島", "力的平衡、摩擦力、壓力與浮力", "#5a5fb0", "#a3a8f0",
   [("力、壓力與浮力", ["s4-6-1", "s4-6-2", "s4-6-3", "s4-6-4"])]),
  ("motion", "直線運動島", "位移、速度、加速度與自由落體", "#2c7fa8", "#79c3ea",
   [("直線運動", ["s5-1-1", "s5-1-2", "s5-1-3", "s5-1-4"])]),
  ("force", "力與運動島", "牛頓三大運動定律、圓周運動與力矩", "#3a5f9a", "#8fb2ea",
   [("運動定律", ["s5-2-1", "s5-2-2", "s5-2-3"]), ("圓周運動與力矩", ["s5-2-4", "s5-2-5"])]),
  ("energy", "功與能島", "功與功率、動能位能與能量守恆", "#9a6a00", "#f2c94c",
   [("功與能", ["s5-3-1", "s5-3-2", "s5-3-3", "s5-3-4"])]),
  ("circuit", "電路島", "靜電、電流、電壓、電阻與生活用電", "#b8452a", "#f2ab85",
   [("電荷與電路", ["s5-4-1", "s5-4-2", "s5-4-3", "s5-4-4"]), ("電流的熱效應與用電", ["s6-1-1", "s6-1-2"])]),
  ("magnet", "電與磁島", "磁場、電流磁效應與電磁感應", "#6a4bb0", "#b39cf0",
   [("電與磁", ["s6-2-1", "s6-2-2", "s6-2-3", "s6-2-4"])]),
 ],
 "chem": [
  ("matter", "物質與溶液島", "物質的性質、溶液濃度與混合物分離", "#1a8aa0", "#6fd6e6",
   [("物質與溶液", ["s3-2-1", "s3-2-2", "s3-2-3"])]),
  ("atom", "原子與元素島", "元素與化合物、原子結構與週期表", "#6a4bb0", "#b39cf0",
   [("元素、原子與分子", ["s3-6-1", "s3-6-2", "s3-6-3", "s3-6-4", "s3-6-5"])]),
  ("react", "化學反應島", "質量守恆、化學反應式、速率與平衡", "#c2502a", "#ff9a73",
   [("化學反應與表示法", ["s4-1-1", "s4-1-2"]), ("反應速率與平衡", ["s4-4-1", "s4-4-2"])]),
  ("redox", "氧化還原與電池島", "氧化與活性、還原反應、電池與電解", "#b8322a", "#ff8a7e",
   [("氧化與還原", ["s4-2-1", "s4-2-2"]), ("電池與電流的化學效應", ["s6-1-3", "s6-1-4"])]),
  ("acid", "酸鹼島", "電解質、酸與鹼、pH 值與酸鹼反應", "#3c8c2e", "#8fd47e",
   [("電解質與酸鹼", ["s4-3-1", "s4-3-2", "s4-3-3", "s4-3-4"])]),
  ("organic", "有機化合物島", "有機物的組成、聚合物與清潔劑", "#8a5a2b", "#d7a06a",
   [("有機化合物", ["s4-5-1", "s4-5-2", "s4-5-3", "s4-5-4"])]),
 ],
 "ear": [
  ("surface", "地表與岩石島", "地球的組成、風化侵蝕與岩石礦物", "#8a5a2b", "#d7a06a",
   [("地表與岩石", ["s5-5-1", "s5-5-2", "s5-5-3"])]),
  ("plate", "板塊與岩層島", "地球構造、板塊運動與岩層紀錄", "#b8452a", "#f2ab85",
   [("板塊與岩層", ["s5-6-1", "s5-6-2", "s5-6-3"])]),
  ("astro", "天文島", "宇宙與太陽系、晝夜四季與日地月", "#3a4f9a", "#8fa2ea",
   [("宇宙與日地月", ["s5-7-1", "s5-7-2", "s5-7-3"])]),
  ("weather", "天氣島", "大氣、天氣現象、氣團鋒面與災變天氣", "#2c7fa8", "#79c3ea",
   [("大氣與天氣", ["s6-3-1", "s6-3-2", "s6-3-3", "s6-3-4"])]),
  ("climate", "海洋與全球變遷島", "海氣互動、全球變遷與人和自然", "#1a8aa0", "#6fd6e6",
   [("海洋、氣候與人類", ["s6-4-1", "s6-4-2", "s6-4-3"])]),
 ],
 "x": [
  ("lab", "探究與實驗島", "科學方法、實驗室安全與常用器材", "#6a4bb0", "#b39cf0",
   [("探究與實驗", ["s1-1-2", "s1-1-3", "s3-lab"])]),
  ("cross", "跨科主題島", "尺度、太陽、能源、永續與氣候變遷", "#2c8a56", "#6fd29b",
   [("跨科主題", ["s1-x", "s2-x", "s3-x", "s4-x", "s5-x", "s6-x"])]),
 ],
}
GROUP = {"bio": "生物群島", "phy": "物理群島", "chem": "化學群島", "ear": "地科群島", "x": "跨科航道"}


def read_titles():
    titles = {}
    pat = re.compile(r"^\d+_(\d+)_(\d+)-(\d+)[ _](.+)\.doc$")
    for v in range(1, 7):
        folder = next(d for d in os.listdir(BANK) if d.startswith(f"0{v}_"))
        for f in os.listdir(os.path.join(BANK, folder, "01_試題")):
            m = pat.match(f)
            if m:
                ch, a, b, t = m.groups()
                assert int(ch) == int(a), f
                titles[f"s{v}-{int(a)}-{int(b)}"] = t.strip()
            elif "跨科主題" in f:
                titles[f"s{v}-x"] = re.sub(r"^\d+_跨科主題[：:]", "", f)[:-4].strip()
            elif "實驗室常用器材" in f:
                titles[f"s{v}-lab"] = "實驗室常用器材"
            else:
                sys.exit(f"unexpected file name {f}")
    return titles


def main():
    titles = read_titles()
    used, out = [], {}
    for g, isles in ISLES.items():
        G = {"name": GROUP[g], "isles": [], "ch": []}
        for iid, name, tag, c, cl, units in isles:
            G["isles"].append({"id": iid, "name": name, "tag": tag, "c": c, "cl": cl})
            n = 0
            for k, (uname, sids) in enumerate(units, 1):
                secs = []
                for sid in sids:
                    n += 1
                    secs.append({"id": sid, "no": str(n), "t": titles[sid]})
                    used.append(sid)
                G["ch"].append({"isle": iid, "u": k, "name": uname, "secs": secs})
        out[g] = G
    assert len(used) == len(set(used)), "a section is listed twice"
    missing = set(titles) - set(used)
    assert not missing, f"sections not placed on any island: {sorted(missing)}"
    json.dump(out, open(os.path.join(HERE, "structure.json"), "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print(f"wrote structure.json: {sum(len(v['isles']) for v in out.values())} islands, {len(used)} sections")


main()
