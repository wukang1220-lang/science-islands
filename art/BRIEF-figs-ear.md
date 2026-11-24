# Brief: 25 teaching diagrams for the earth-science and cross-subject islands (junior high, Taiwan)

You are drawing original explanatory diagrams for a junior-high science learning page
(Traditional Chinese, Taiwan). Each diagram sits inside a lesson card above the key points and
is read on phones (about 340 px wide) and desktops (up to about 560 px wide). Draw everything
yourself as clean schematic diagrams — do not trace or imitate any textbook figure or map.
Accuracy matters more than decoration: these are for 13–15-year-olds studying for exams.

Two people work on this brief at the same time. **Write only the files in the list your prompt
gives you** (list A = diagrams 1–13, list B = diagrams 14–25). Do not create, modify or delete
any other file; every existing file in `figs/` and `examples/` is read-only.

## MUST follow (checked by `python check_svg.py figs`)

- `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 H" role="img">` where H is between
  140 and 280. No width/height on the root.
- First child: `<title>` with one plain sentence in Traditional Chinese describing the diagram.
- Allowed elements only: g path circle ellipse rect line polyline polygon text tspan title defs
  marker. No gradients, filters, style, script, image, href or comments.
- Colours: every fill/stroke is `none` or one of: `var(--fig-ink)` (text, outlines, arrows),
  `var(--fig-soft)` (secondary text, dashed guides), `var(--fig-line)` (faint lines, panel
  borders), `var(--fig-paper)` (panel fills), `var(--ic)` (the one highlight — outlines and
  lines only, never put text on a `var(--ic)` fill), `var(--fig-land)` (land, plants),
  `var(--fig-sea)`, `var(--fig-deep)` (sea, water), `var(--fig-sand)` (rock, soil, sand),
  `var(--fig-warm)` (sun, heat, magma, warm currents), `var(--fig-cool)` (air, ice, cold).
- Text: `font-size` 11 to 14, `fill="var(--fig-ink)"` or `var(--fig-soft)`, no font-family,
  use `text-anchor`, stay inside the viewBox, never overlap other text or lines (budget 1 em
  per Chinese character). No transform on `<text>`; groups may use `translate()` only.
- Symbols: write them with these Unicode characters exactly (CO₂, km, μm, °C, %, ～, →, ＞, ＜).
  Do not use `<tspan>` baseline shifts.
- Every id starts with the file name (e.g. `ear-moon-arr`). Under 9 KB per file; numbers ≤ 1 decimal.
- Use the exact label wording given below. Never add facts, numbers or names not listed.
- Where marked `示意圖`, include that small soft-grey note in a corner.
- The palette cannot show real colours; never rely on colour alone — the words carry the meaning.
- Science must be right: arrows point the stated way; the Earth's axis keeps the same tilt
  direction at every orbit position; the Moon's lit half always faces the Sun.

## Layout suggestions (you may adjust)

- Calm and readable: thin ink outlines (1.5), soft fills, white space, one `var(--ic)` highlight
  per panel. If text does not fit, keep main labels first; table cells may wrap to two lines.
- Approved examples to match (read them first): `examples/geo-koreas.svg` (table),
  `examples/geo-cnclimate.svg` (flowchart), `figs/phy-reflect.svg`, `figs/phy-transfer.svg`
  (three panels), `figs/phy-magfield.svg`, `figs/chem-classify.svg` (tree), `figs/bio-energy.svg`.
- Judge legibility at about 340 px wide on a phone.

## List A (diagrams 1–13)

1. **ear-water** — title `水循環`. A cross-section: sea on the right, a mountain on the left, a
   sun in the top-left corner labelled `太陽提供能量`, a cloud in the middle. Arrows with labels:
   from sea up to the cloud `蒸發`; at the cloud `凝結`; from the cloud down onto the mountain
   `降水`; along the ground back to the sea `逕流`; down into the ground `入滲`. Strip at the
   bottom: `地球上的水：海水約 97%，淡水約 3%（多為冰川）`.
2. **ear-erosion** — title `河流的作用`. A river profile from a mountain (left) to the sea (right).
   Labels along it: `上游：侵蝕為主，V 形谷`, `中游：搬運`, `下游：沉積`, a fan shape where the river
   leaves the mountain `沖積扇`, a fan at the river mouth `三角洲`. Strip:
   `風化 → 侵蝕 → 搬運 → 沉積`.
3. **ear-rockcycle** — title `岩石循環`. Four boxes: `岩漿` (top), `火成岩`, `沉積岩`, `變質岩`.
   Arrows: `岩漿`→`火成岩` labelled `冷卻凝固`; `火成岩`→`沉積岩` and `變質岩`→`沉積岩` labelled
   `風化、侵蝕、沉積`; `火成岩`→`變質岩` and `沉積岩`→`變質岩` labelled `高溫高壓`; `變質岩`→`岩漿`
   labelled `熔融`. Small soft examples under the rock boxes: `玄武岩、花岡岩`;
   `礫岩、砂岩、頁岩、石灰岩`; `板岩、片岩、大理岩`.
4. **ear-plates** — title `地球構造與板塊邊界`. Left: a quarter cross-section of the Earth with
   layers labelled `地殼`, `地函`, `外核（液態）`, `內核（固態）`. Right: three small stacked
   sketches of two blocks: arrows apart `張裂性：中洋脊、裂谷`; arrows together with one block
   diving under the other `聚合性：海溝、島弧、山脈`; arrows sliding past each other
   `錯動性：平移錯開`. Strip `板塊移動的動力：地函的熱對流`.
5. **ear-faults** — title `褶皺、斷層與地震`, 2×2 panels: `褶皺` (folded layers: an upward arch
   labelled `背斜` next to a downward trough labelled `向斜`); `正斷層` (a block pair with arrows
   pulling apart, the hanging wall moved down, caption `張力，上盤下滑`); `逆斷層` (arrows pushing
   together, hanging wall moved up, caption `擠壓，上盤上移`); `震源與震央` (a point underground
   `震源`, a dashed vertical line to the surface point `震央`, the dashed line labelled `震源深度`).
6. **ear-strata** — title `岩層的紀錄`. A column of four layers labelled from bottom to top `甲`,
   `乙`, `丙`, `丁`; a shell fossil drawn in `乙`; a fault line cutting `甲` and `乙` only. Notes:
   `疊置定律：下層較老、上層較新`, `斷層比它切過的岩層年輕`. Bottom time strip with four boxes:
   `前寒武紀` → `古生代 三葉蟲` → `中生代 恐龍、菊石` → `新生代 哺乳類、人類`.
7. **ear-solar** — title `太陽系`. The Sun at the left edge, eight planets in order to the right
   (not to scale) labelled `水星`, `金星`, `地球`, `火星`, `木星`, `土星` (with a ring), `天王星`,
   `海王星`; a dotted band between Mars and Jupiter labelled `小行星帶`. Brackets: under the first
   four `類地行星：岩石、密度大`; under the last four `類木行星：氣體和冰、體積大`. `示意圖`
   and a small note `大小和距離不按比例`.
8. **ear-seasons** — title `四季的成因`. Top view: a Sun in the centre and an elliptical orbit
   with an arrow showing counter-clockwise motion. The Earth at four positions — left, bottom,
   right, top — each with its axis drawn tilted toward the right of the page by the same angle.
   Labels: left `夏至`, bottom `秋分`, right `冬至`, top `春分`. Notes: `夏至：直射北回歸線`,
   `冬至：直射南回歸線`, `春分、秋分：直射赤道`. Strip `地軸傾斜 23.5°，方向不變`. `示意圖`.
9. **ear-moon** — title `月相`. The Sun's rays coming from the left edge (label `陽光`). The Earth
   in the centre, the Moon at four positions on a circle around it, each Moon's left half lit and
   right half dark (lit side toward the Sun). Positions and labels: left `新月（初一）`, bottom
   `上弦月（初七、八）`, right `滿月（十五）`, top `下弦月（二十二、二十三）`; an arrow showing the
   Moon moving counter-clockwise. Beside each label a small icon of how it looks from Earth:
   new = all dark, 上弦 = right half bright, full = all bright, 下弦 = left half bright. Strip:
   `日食在初一（月球在日、地之間）；月食在十五（地球在日、月之間）`.
10. **ear-atmos** — title `大氣的分層`. A vertical chart: y-axis `高度（km）` with ticks `0`, `12`,
    `50`, `85`; x-axis `溫度`. Horizontal bands labelled `對流層`, `平流層`, `中氣層`, `增溫層`; a
    temperature line that falls in 對流層, rises in 平流層, falls in 中氣層, rises in 增溫層. Note in
    平流層 `臭氧層：吸收紫外線`; note in 對流層 `天氣現象都在這一層`. Side box: `氮氣 約 78%`,
    `氧氣 約 21%`, `其他 約 1%`.
11. **ear-pressure** — title `高氣壓與低氣壓（北半球）`. Left: a centre `H` with closed isobars and
    arrows spiralling outward clockwise, caption `順時鐘向外吹，空氣下沉，多晴朗`. Right: a centre
    `L` with arrows spiralling inward counter-clockwise, caption `逆時鐘向內吹，空氣上升，易下雨`.
    Strip `風由高氣壓吹向低氣壓；等壓線愈密，風愈強`.
12. **ear-fronts** — title `鋒面`. Top: cross-section of a cold front — a wedge of `冷空氣`
    pushing under `暖空氣`, steep boundary, a tall cloud, caption `冷鋒：降雨強、範圍窄，過後氣溫下降`.
    Middle: a warm front — `暖空氣` gliding up over `冷空氣` on a gentle slope, a long flat cloud,
    caption `暖鋒：降雨緩、範圍廣`. Bottom legend of map symbols: a line with triangles `冷鋒`, a
    line with half-circles `暖鋒`, a line with both on alternating sides `滯留鋒（梅雨）`.
13. **ear-typhoon** — title `颱風與災變天氣`. Left: top view of a typhoon — spiral cloud bands, a
    small clear centre `颱風眼`, a ring around it `眼牆（風雨最強）`, curved arrows counter-clockwise
    with caption `北半球逆時鐘旋轉`. Right: a table with two columns `災害`, `特點`: `颱風` /
    `7～9 月，強風豪雨`; `梅雨` / `5～6 月，滯留鋒`; `寒流` / `冬季，氣溫驟降`; `乾旱` / `降雨少`.

## List B (diagrams 14–25)

14. **ear-currents** — title `臺灣附近的洋流`. A schematic (not a real map) of Taiwan as a simple
    leaf-shaped island with the Taiwan Strait on its left. Arrows: along the east coast going north
    `黑潮（暖流）`; a smaller branch entering the southern strait `黑潮支流（冬季）`; along the west
    side of the strait going south `中國沿岸流（冬季，水溫較低）`. Side note: `暖流：低緯 → 高緯`,
    `寒流：高緯 → 低緯`. `示意圖`.
15. **ear-greenhouse** — title `溫室效應`. A sun on the left with straight arrows down to the
    ground `太陽輻射`; wavy arrows up from the ground `地表放出的熱`; a band across the sky
    `溫室氣體（二氧化碳、甲烷、水氣）`; some wavy arrows bending back down at the band
    `吸收後再放出，使地表保溫`. Right column: `暖化的影響` with three lines `海平面上升`,
    `極端天氣增加`, `珊瑚白化`.
16. **ear-hazard** — title `土石流與水土保持`. A slope with loose rocks and water flowing down into a
    valley. A box `形成三條件` listing `鬆散的土石`, `充足的水`, `足夠的坡度`. On the other side of the
    slope: trees labelled `植生：樹根抓住土壤`, a short wall `擋土牆`, a ditch `排水設施`. Small note
    near a low area `滯洪池：暫存雨水`.
17. **x-method** — title `科學探究的流程`. A flow of boxes: `觀察` → `提出問題` → `蒐集資料` →
    `提出假說` → `設計實驗` → `進行實驗` → `分析結果` → `結論` (two rows if needed), and a return arrow
    from `分析結果` back to `提出假說` labelled `不支持：修正假說`. Bottom strip with three small boxes:
    `操縱變因：刻意改變的條件`, `應變變因：觀察的結果`, `控制變因：保持相同的條件`.
18. **x-safety** — title `實驗室安全`, 2×2 panels with simple drawings: `酒精燈` caption
    `酒精 1/3～2/3，用燈罩蓋熄`; `聞氣味` (a hand waving above a bottle) caption `用手搧聞`;
    `加熱試管` (a test tube held by a clamp, an arrow showing the mouth pointing away from a person)
    caption `管口朝向無人處`; `稀釋濃硫酸` (acid poured along a glass rod into water) caption
    `酸慢慢加入水中`.
19. **x-glassware** — title `常用的實驗器材`, six cards (3 rows × 2) each with a small outline drawing
    and two lines: `燒杯` / `配製溶液，加熱要墊網`; `量筒` / `量體積，不可加熱`; `錐形瓶` /
    `搖晃時不易濺出`; `漏斗` / `搭配濾紙過濾`; `滴管` / `吸取少量液體，不可倒持`; `玻棒` /
    `攪拌、引流`.
20. **x-scale** — title `從奈米到公里`. A horizontal scale with ticks `1 nm`, `1 μm`, `1 mm`, `1 m`,
    `1 km` (equal spacing; each step is ×1000). Examples placed on it: `病毒 約 100 nm`,
    `細菌 約 1 μm`, `細胞 約 10～100 μm`, `螞蟻 約 5 mm`, `人 約 1.6 m`, `臺北 101 約 500 m`. Under the
    scale, tool bands: `電子顯微鏡` (nm range), `複式顯微鏡` (μm range), `放大鏡、解剖顯微鏡` (mm),
    `肉眼` (m). Note: `看遠方的大物體用望遠鏡`. Strip `1 km＝1000 m　1 mm＝1000 μm　1 μm＝1000 nm`.
21. **x-carbon** — title `碳循環`. Centre: `大氣中的 CO₂`. Around it: `植物` (arrow from air
    `光合作用`), `動物` (arrow from plants `吃`), arrows from plants and animals back to the air
    `呼吸作用`; `遺骸、土壤` with an arrow to air `分解者分解`; `化石燃料` with an arrow to air
    `燃燒`; `海洋` with a two-way arrow `吸收、釋放`. Highlight the `燃燒` arrow with `var(--ic)` and a
    note `人類活動使 CO₂ 增加`.
22. **x-sun** — title `太陽：地球的能量來源`. A sun on the left labelled `核融合`; four arrows to
    the right, each to a box: `植物光合作用 → 食物鏈的能量`; `古代生物 → 化石燃料`;
    `空氣受熱、水循環 → 風力、水力`; `太陽能板：光能 → 電能`. Corner note:
    `紅外線：赫歇爾在紅光外側發現`.
23. **x-5r** — title `資源使用的 5R`. A vertical ladder or stacked boxes from top to bottom:
    `Refuse 拒絕`, `Reduce 減量`, `Reuse 重複使用`, `Repair 修理`, `Recycle 回收`, with an arrow
    `愈上面愈優先`. Right side strip box: `酸雨`: `二氧化硫、氮氧化物＋雨水 → 酸雨（pH＜5.0）`, and
    `會腐蝕大理石、使湖泊酸化`.
24. **x-energy** — title `能源的分類`. Two columns: `再生能源` with items `太陽能`, `風力`, `水力`,
    `地熱`, `生質能`; `非再生能源` with items `煤`, `石油`, `天然氣`, `核燃料`. Under the second
    column: `燃燒化石燃料會排放 CO₂`. Bottom strip: `能量守恆：轉換時總量不變，部分變成熱散失`.
25. **x-climate** — title `氣候變遷的因應`. A centre box `氣候變遷`. Left branch `減緩：減少溫室氣體`
    with items `發展再生能源`, `節約能源`, `植樹造林`. Right branch `調適：降低衝擊` with items
    `加高海堤`, `興建滯洪池`, `種植耐旱作物`, `建立預警系統`. Bottom strip:
    `淨零排放：排放量＝移除量`.
