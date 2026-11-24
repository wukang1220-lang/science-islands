# Brief: 24 teaching diagrams for the chemistry islands (junior-high chemistry, Taiwan)

You are drawing original explanatory diagrams for a junior-high science learning page
(Traditional Chinese, Taiwan). Each diagram sits inside a lesson card above the key points and
is read on phones (about 340 px wide) and desktops (up to about 560 px wide). Draw everything
yourself as clean schematic diagrams — do not trace or imitate any textbook figure. Accuracy
matters more than decoration: these are for 13–15-year-olds studying for exams.

Two people work on this brief at the same time. **Write only the files in the list your prompt
gives you** (list A = diagrams 1–12, list B = diagrams 13–24). Do not create, modify or delete
any other file; every existing file in `figs/` and `examples/` is read-only.

## MUST follow (checked by `python check_svg.py figs`)

- `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 H" role="img">` where H is between
  140 and 280. No width/height on the root.
- First child: `<title>` with one plain sentence in Traditional Chinese describing the diagram.
- Allowed elements only: g path circle ellipse rect line polyline polygon text tspan title defs
  marker. No gradients, filters, style, script, image, href or comments.
- Colours: every fill/stroke is `none` or one of: `var(--fig-ink)` (text, outlines, arrows),
  `var(--fig-soft)` (secondary text, dashed guides), `var(--fig-line)` (faint lines, panel
  borders), `var(--fig-paper)` (panel fills), `var(--ic)` (the one highlight — outlines only,
  never put text on a `var(--ic)` fill), `var(--fig-land)`, `var(--fig-sea)`, `var(--fig-deep)`
  (liquids), `var(--fig-sand)`, `var(--fig-warm)` (heat, flames, metal copper-ish),
  `var(--fig-cool)` (gases, cold).
- Text: `font-size` 11 to 14, `fill="var(--fig-ink)"` or `var(--fig-soft)`, no font-family,
  use `text-anchor`, stay inside the viewBox, never overlap other text (budget 1 em per Chinese
  character). No transform on `<text>`; groups may use `translate()` only.
- Chemical formulas: write subscripts and charges with these Unicode characters, exactly as given
  below (H₂O, CO₂, O₂, H⁺, OH⁻, Cu²⁺, Zn²⁺, Na⁺, Cl⁻, C₆₀). Do not use `<tspan>` baseline shifts.
- Every id starts with the file name (e.g. `chem-cell-arr`). Under 9 KB per file; numbers ≤ 1 decimal.
- Use the exact label wording given below. Never add facts, numbers or names not listed.
- Where marked `示意圖`, include that small soft-grey note in a corner.
- The palette cannot show real colours; never rely on colour alone — the words carry the meaning.

## Layout suggestions (you may adjust)

- Calm and readable: thin ink outlines (1.5), soft fills, white space, one `var(--ic)` highlight
  per panel. If text does not fit, keep main labels first; table cells may wrap to two lines.
- Approved examples to match (read them first): `examples/geo-koreas.svg` (table),
  `examples/geo-cnclimate.svg` (flowchart), `figs/bio-heart.svg`, `figs/bio-osmosis.svg`,
  `figs/bio-plants.svg`, `figs/bio-energy.svg`, `figs/bio-enzyme.svg` (line chart).
- Judge legibility at about 340 px wide on a phone.

## List A (diagrams 1–12)

1. **chem-states** — title `物質的三態`, three panels `固態`, `液態`, `氣態`, each a small box of
   particles (circles): solid = tight regular grid; liquid = close but irregular; gas = few,
   far apart with short motion lines. Under each two lines: `體積：一定`／`形狀：一定`;
   `體積：一定`／`形狀：隨容器改變`; `體積：不一定`／`形狀：隨容器改變`. `示意圖`.
2. **chem-solubility** — a line chart titled `溶解度與溫度`. x-axis `溫度（°C）` ticks `0`, `20`,
   `40`, `60`; y-axis label `溶解度（g／100 g 水）` ticks `0`, `50`, `100`. Curve `硝酸鉀` through
   (0, 13.3), (20, 31.6), (40, 63.9), (60, 110) in `var(--ic)`; curve `食鹽` nearly flat through
   (0, 35.7), (20, 36), (40, 36.6), (60, 37.3). Note `曲線上的點都是飽和溶液`.
3. **chem-separate** — table titled `混合物的分離`, columns `方法`, `利用的性質差異`, `例子`.
   Rows: `過濾` / `顆粒大小` / `沙子和食鹽水`; `蒸發` / `沸點高低` / `由食鹽水得到食鹽`;
   `結晶` / `溶解度隨溫度變化` / `冷卻硝酸鉀溶液`; `蒸餾` / `沸點高低` / `由海水得到淡水`;
   `色層分析` / `在濾紙上移動的快慢` / `分出墨水的色素`; `磁鐵吸引` / `磁性` / `鐵粉和沙子`.
4. **chem-classify** — title `物質的分類`, a tree: `物質` splits into `純物質` and `混合物`
   (example `空氣、海水`). `純物質` splits into `元素` and `化合物` (example `水、二氧化碳、食鹽`).
   `元素` splits into `金屬`（`鐵、銅、汞`）and `非金屬`（`氧、碳、硫`）. Outline `化合物` with
   `var(--ic)`. Small note under the tree: `化合物可用化學方法分解成元素`.
5. **chem-carbon** — title `碳的同素異形體`, three panels. `石墨`: stacked flat layers of hexagons;
   notes `層狀、能導電`, `鉛筆芯、電極`. `鑽石`: a small 3D-looking lattice; notes `最硬`,
   `切割玻璃`. `巴克球 C₆₀`: a sphere outline with a pentagon/hexagon pattern; notes
   `60 個碳原子`. `示意圖`.
6. **chem-atom** — title `原子的構造`. Left: an atom — a small nucleus cluster of circles marked
   `＋` (質子) and plain circles (中子), with two elliptical electron paths and small circles
   marked `－`. Labels with leaders: `原子核`, `質子`, `中子`, `電子`. Right: a table with columns
   `粒子`, `電性`, `位置`, `發現者`: `電子` / `負電` / `原子核外` / `湯姆森`; `質子` / `正電` /
   `原子核內` / `拉塞福`; `中子` / `不帶電` / `原子核內` / `查兌克`. Under: `質子數＝原子序；
   質子數＋中子數＝質量數`. `示意圖`.
7. **chem-periodic** — title `週期表的分區`. A simplified periodic-table outline: 7 rows, 18
   columns of small empty cells in the real shape (row 1 has cells only in columns 1 and 18;
   rows 2–3 have columns 1–2 and 13–18; rows 4–7 have all 18). Label column 1 `鹼金屬`
   (note `氫除外`), column 2 `鹼土金屬`, column 17 `鹵素`, column 18 `鈍氣` (outline column 18
   with `var(--ic)`). A thick stepped line separating `金屬` (left) from `非金屬` (right).
   Side labels: an arrow along a row labelled `週期（橫列，共 7 個）` and along a column
   `族（直行，共 18 族）`. Note `依原子序排列`. `示意圖`.
8. **chem-formula** — title `化學式的意義`. Top: `H₂O` with leader labels `元素符號`
   (pointing at H) and `原子數目`（pointing at the subscript 2）; `CO₂` beside it. Below: a
   row of particle models with labels: `O₂ 氧氣` (two joined circles), `O₃ 臭氧` (three),
   `H₂O 水` (one big + two small), `CO₂ 二氧化碳` (small dark centre + two), `Fe 鐵` (a small
   grid of identical circles, note `金屬以原子堆積`). Outline `Fe` group with `var(--ic)`.
9. **chem-mass** — title `質量守恆定律`, two panels. `密閉容器`: a flask on a balance with a
   balloon tied over the mouth, the balloon inflated; balance reading text `反應前 150.0 g` and
   `反應後 150.0 g`. `開放容器`: a beaker on a balance with gas bubbles leaving the top (arrows
   out), readings `反應前 150.0 g` and `反應後 149.2 g`, note `二氧化碳逸散`. Footer:
   `兩者都遵守質量守恆：反應前後原子的種類和數目不變`.
10. **chem-mole** — title `化學反應式的意義`, a three-column table under the equation
    `2H₂ ＋ O₂ → 2H₂O` (equation centred, large). Rows: `分子數` / `2` / `1` / `2`;
    `莫耳數` / `2 莫耳` / `1 莫耳` / `2 莫耳`; `質量` / `4 g` / `32 g` / `36 g`. Footer:
    `原子量：H＝1，O＝16；反應前 4＋32＝36 g，反應後 36 g`. Outline the `質量` row with `var(--ic)`.
11. **chem-rate** — title `影響反應速率的因素`, a 2×2 grid of small panels plus a strip at the
    bottom. `接觸面積`: a block vs a pile of powder, note `顆粒愈細愈快`. `濃度`: two beakers with
    few vs many dots, note `濃度愈高愈快`. `溫度`: a thermometer with a flame, note `溫度愈高愈快`.
    `催化劑`: arrows `慢 → 快`, note `速率變快、產量不變`. Bottom strip: `粒子碰撞次數愈多、能量愈高，
    反應愈快`. `示意圖`.
12. **chem-equilibrium** — a line chart titled `可逆反應達到平衡`. x-axis `時間`, y-axis
    `反應速率`. Curve `正反應` starting high and decreasing; curve `逆反應` starting at zero and
    increasing; both level off at the same value after a dashed vertical line labelled `達到平衡`.
    Note right of the flat part: `正、逆反應速率相等（動態平衡）`. No numbers on the axes. `示意圖`.

## List B (diagrams 13–24)

13. **chem-activity** — title `金屬的活性`. A long horizontal arrow labelled `活性大` at the left
    end and `活性小` at the right end, with the sequence written along it in two lines if needed:
    `鉀 鈉 鈣 鎂 鋁 碳 鋅 鐵 錫 鉛 氫 銅 汞 銀 鉑 金` (碳 and 氫 in `var(--fig-soft)` text because
    they are not metals). Below, a small two-column table: `金屬氧化物` / `溶於水呈鹼性`;
    `非金屬氧化物` / `溶於水呈酸性`.
14. **chem-redox** — title `氧化還原反應`. The equation `2CuO ＋ C → 2Cu ＋ CO₂` centred. An arc
    arrow above from `C` to `CO₂` labelled `得到氧：被氧化（還原劑）`; an arc arrow below from
    `2CuO` to `2Cu` labelled `失去氧：被還原（氧化劑）`. Footer: `氧化和還原同時發生`.
    Small notes under the products: `CO₂ 使石灰水變混濁`, `Cu 紅棕色`.
15. **chem-cell** — title `鋅銅電池`. Two beakers: left `鋅片` in `硫酸鋅溶液`, right `銅片` in
    `硫酸銅溶液`, joined at the top by a U-shaped tube labelled `鹽橋`. A wire over the top from
    the zinc to the copper with a bulb in the middle, and an arrow along the wire labelled
    `電子流`. Labels: `負極：鋅失去電子（氧化）` under the left beaker, `正極：Cu²⁺ 得到電子析出銅
    （還原）` under the right beaker (may wrap). Outline the zinc plate with `var(--ic)`.
16. **chem-electrolysis** — two panels. `電解水`: two inverted tubes over two electrodes in a
    beaker; the left tube about twice as full of gas `負極：氫氣`, the right `正極：氧氣`; note
    `體積比 2：1`, `加入少量氫氧化鈉幫助導電`. `電鍍（在湯匙上鍍銅）`: beaker with `硫酸銅溶液`,
    `銅片` on the positive side labelled `接正極`, a spoon labelled `接負極（被鍍物）`; a small
    `直流電源` box above connected to both. Outline the spoon with `var(--ic)`.
17. **chem-ions** — title `電解質溶液導電`. A beaker with two electrodes connected to a battery
    symbol and a bulb. Circles marked `＋` moving (arrows) toward the electrode labelled `負極`,
    circles marked `－` moving toward `正極`. Labels `陽離子 → 負極`, `陰離子 → 正極`. Footer:
    `正、負電量相等，溶液呈電中性`. `示意圖`.
18. **chem-acidbase** — table titled `酸和鹼的性質`, columns `性質`, `酸`, `鹼`. Rows:
    `溶於水產生` / `H⁺` / `OH⁻`; `石蕊試紙` / `藍色變紅色` / `紅色變藍色`;
    `加入鎂帶` / `產生氫氣` / `沒有反應`; `加入大理石` / `產生二氧化碳` / `沒有反應`;
    `其他` / `濃酸有腐蝕性` / `溶解油脂、有滑膩感`; `例子` / `鹽酸、硫酸、醋酸` /
    `氫氧化鈉、氨水、石灰水`.
19. **chem-ph** — title `pH 值`. A horizontal bar divided into 15 tick marks `0` to `14`, with
    `7` labelled `中性`. Left part labelled `酸性（pH＜7）`, right part `鹼性（pH＞7）`. Arrows
    under the bar: pointing left `酸性愈強`, pointing right `鹼性愈強`. Above the bar, short
    example tags placed at approximate positions: `胃液` (about 2), `檸檬汁` (about 2.5),
    `純水` (7), `小蘇打水` (about 8.5), `肥皂水` (about 10). Below, a row of indicator notes:
    `廣用試紙：紅 → 橙 → 黃 → 綠 → 藍 → 靛 → 紫`; `酚酞：酸性、中性無色，鹼性紅色`.
    Note `pH 相差 1，H⁺ 濃度相差 10 倍` and `示意圖`.
20. **chem-neutral** — a line chart titled `酸鹼中和`. x-axis `加入氫氧化鈉的體積（mL）` ticks
    `0`, `5`, `10`, `15`, `20`; y-axis `pH` ticks `1`, `7`, `13`. Curve starting near pH 1, rising
    slowly, a steep jump around 10 mL through pH 7, then leveling near pH 13. Mark the point at
    (10, 7) with a dot outlined in `var(--ic)` labelled `恰好中和`. Notes: `酚酞：無色` on the left
    part, `酚酞：紅色` on the right part. Footer: `H⁺ ＋ OH⁻ → H₂O`. `示意圖`.
21. **chem-organic** — title `有機化合物和無機化合物`. Two boxes side by side. Left
    `有機化合物（含碳）`: examples `葡萄糖、酒精、甲烷、蛋白質、塑膠`. Right `無機化合物`:
    examples `水、食鹽`, and a highlighted sub-box `雖然含碳，仍屬無機：CO、CO₂、碳酸鹽` outlined
    with `var(--ic)`. Footer: `有機物一定含碳，含碳的不一定是有機物`.
22. **chem-groups** — table titled `常見的有機化合物`, columns `類別`, `特徵`, `例子`.
    Rows: `烴` / `只含碳和氫` / `甲烷 CH₄、丙烷`; `醇` / `含 −OH` / `乙醇（酒精）、甲醇`;
    `有機酸` / `含 −COOH` / `乙酸（醋酸）、甲酸（蟻酸）`; `酯` / `醇＋有機酸 → 酯＋水` /
    `有香味，例如香料`. Footer: `油脂是甘油和脂肪酸形成的酯`.
23. **chem-fibers** — title `衣料纖維`, a tree. `纖維` → `天然纖維` and `人造纖維` and `合成纖維`.
    `天然纖維` → `植物纖維：棉、麻（燒紙味）` and `動物纖維：羊毛、蠶絲（燒羽毛味）`.
    `人造纖維` → `嫘縈（植物纖維溶解再抽絲）`. `合成纖維` → `尼龍、聚酯（石油製成，熔成硬球）`.
    Outline `合成纖維` with `var(--ic)`.
24. **chem-soap** — title `肥皂如何去油汙`. Left: one soap molecule drawn as a long tail line
    labelled `親油端` and a round head labelled `親水端（帶負電）`. Right: an oil droplet
    (`var(--fig-sand)` fill) labelled `油汙`, surrounded by many soap molecules with tails
    pointing into the oil and heads pointing out into the water (`var(--fig-sea)` background area
    labelled `水`). Footer: `親油端抓住油汙，親水端被水帶走`. `示意圖`.

## Finish

Run `python check_svg.py figs` and fix every failure in your own files (failures in the other
list's files are not yours — ignore them). Then list the files you wrote and anything you could
not draw exactly as described.
