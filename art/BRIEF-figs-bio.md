# Brief: 36 teaching diagrams for the biology islands (junior-high biology, Taiwan)

You are drawing original explanatory diagrams for a junior-high science learning page
(Traditional Chinese, Taiwan). Each diagram sits inside a lesson card above the key points and
is read on phones (about 340 px wide) and desktops (up to about 560 px wide). Draw everything
yourself as clean schematic diagrams — do not trace or imitate any textbook figure. Accuracy
matters more than decoration: these are for 12–14-year-olds studying for exams.

Two people work on this brief at the same time. **Write only the files in the list your prompt
gives you** (list A = diagrams 1–18, list B = diagrams 19–36). Do not create, modify or delete
any other file; `figs/bio-nutrients.svg` … `figs/bio-digest.svg` and `examples/` are read-only.

## MUST follow (checked by `python check_svg.py figs`)

- `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 H" role="img">` where H is between
  140 and 280 (pick what the content needs). No width/height on the root.
- First child: `<title>` with one plain sentence in Traditional Chinese describing the diagram.
  The `<title>` is for screen readers only; the visible heading is a normal `<text>`.
- Allowed elements only: g path circle ellipse rect line polyline polygon text tspan title defs
  marker. No gradients, filters, style, script, image, href or comments.
- Colours: every fill/stroke is `none` or one of these CSS variables (they switch for dark mode):
  - `var(--fig-ink)` all text, outlines and arrows
  - `var(--fig-soft)` secondary text, dashed guide lines
  - `var(--fig-line)` faint grid lines and panel borders
  - `var(--fig-paper)` panel/background fills that must contrast with ink
  - `var(--ic)` the highlight colour for the one thing the diagram is about (an island colour;
    may be dark in dark mode, so never put text on a `var(--ic)` fill — use it for outlines)
  - `var(--fig-land)` green plant tissue, leaves; `var(--fig-sea)` water, `var(--fig-deep)`
    deeper water / liquids; `var(--fig-sand)` soil, tan fills, rock layers;
    `var(--fig-warm)` light, sun, heat, blood-ish warm fills; `var(--fig-cool)` air, gases, cold
- Text: `<text>` with `font-size` 11 to 14 (labels 12–13, titles 13–14) and
  `fill="var(--fig-ink)"` or `var(--fig-soft)`. Do not set font-family. Use `text-anchor`.
  Text must stay inside the viewBox and must not overlap other text. Budget 1 em per Chinese
  character (13 px wide at size 13). Prefer labels in clear space with a short leader line.
  No transform on `<text>`; groups may use `translate()` only.
- Every id starts with the file name (e.g. marker id `bio-heart-arr` in `bio-heart.svg`).
- Under 9 KB per file; round numbers to at most 1 decimal.
- Use the exact label wording given below. Never add facts, numbers or names not listed.
- Where marked `示意圖`, include that small soft-grey note in a corner.
- The palette cannot show real colours (blood red, etc.); never rely on colour alone — the words
  carry the meaning.

## Layout suggestions (you may adjust)

- Calm and readable: thin ink outlines (1.5), soft fills, generous white space, at most one
  `var(--ic)` highlight per panel. Multi-panel diagrams: equal-width panels, short title on top.
- If text does not fit, keep in this order: (1) main labels, (2) arrows and what they connect,
  (3) secondary notes; shorten only text marked "(may shorten)". Long table cells may wrap to two
  lines (use two `<text>` lines, never smaller than 11 px).
- Approved examples to match in style, size and spacing (read them first): table —
  `examples/geo-koreas.svg`; timeline — `examples/his-songyuan.svg`; two-panel schematic —
  `examples/geo-cnmonsoon.svg`; flowchart — `examples/geo-cnclimate.svg`. Also look at the
  approved biology diagrams `figs/bio-leaf.svg`, `figs/bio-photosyn.svg`, `figs/bio-digest.svg`.
- Judge legibility at about 340 px wide on a phone.

## List A (diagrams 1–18)

1. **bio-biosphere** — title `生物圈的範圍`. A cross-section: sky band at top labelled `大氣圈`,
   below it land on the left and sea on the right, and soil/rock below labelled `岩石圈`; the sea
   labelled `水圈`. Tiny simple icons: a bird in the low sky, a tree on land, a fish in the sea,
   a worm in the soil. On the right a tall bracket in `var(--ic)` labelled `生物圈`, spanning from
   `大氣圈下層` (top tick label) through `整個水圈` to `岩石圈表層（土壤）` (bottom tick label).
   `示意圖`.
2. **bio-cellshape** — title `細胞的形態與功能`, three equal panels. `神經細胞`: a cell body with
   short branches and one long process; note `長突起，傳遞訊息`. `紅血球`: a disk shown from the
   side as a dumbbell-like biconcave outline; note `雙凹圓盤，運送氧氣`. `保衛細胞`: two
   bean-shaped cells facing each other around a gap; label the gap `氣孔`; note `控制氣體進出`.
   `示意圖`.
3. **bio-cells** — two panels `動物細胞` and `植物細胞`. Animal: rounded cell with labels
   `細胞膜`, `細胞質`, `細胞核`, `粒線體`. Plant: box-shaped cell with a thick wall, labels
   `細胞壁`, `細胞膜`, `細胞核`, `葉綠體` (small `var(--fig-land)` ovals), `液胞` (large clear
   area), `粒線體`. Outline the plant-only structures (wall, chloroplast, vacuole) with
   `var(--ic)`. Bottom line: `植物細胞特有：細胞壁、葉綠體、大型液胞`. `示意圖`.
4. **bio-osmosis** — title `紅血球與滲透作用`, three panels. `清水`: a swollen cell with water
   arrows pointing in; result `膨脹甚至破裂`. `生理食鹽水（約 0.9%）` (may shorten to
   `生理食鹽水`): a normal cell with arrows both ways; result `形狀不變`. `濃鹽水`: a shrunken
   wrinkled cell with arrows pointing out; result `皺縮`. Footer:
   `水由濃度低的一側，往濃度高的一側移動`. `示意圖`.
5. **bio-levels** — title `生物體的組成層次`. Row 1 heading `動物`: boxes linked by arrows
   `細胞` → `組織` → `器官` → `器官系統` → `個體`, with small examples under each:
   `肌肉細胞`, `肌肉組織`, `胃`, `消化系統`, `人`. Row 2 heading `植物`: `細胞` → `組織` →
   `器官` → `個體` with `表皮細胞`, `表皮`, `葉`, `植物`; in the place where 器官系統 would be,
   a dashed empty box with `沒有器官系統`. Outline the animal `器官系統` box with `var(--ic)`.
6. **bio-stems** — title `莖的橫切面`, two circular cross-sections. Left `雙子葉植物`: small
   vascular bundles arranged in a ring; on one bundle label the inner part `木質部`, the outer
   part `韌皮部` and the thin line between them `形成層` (outline the 形成層 in `var(--ic)`);
   note `維管束排成環狀`. Right `單子葉植物`: bundles scattered all over; notes `維管束散生`
   and `沒有形成層`. `示意圖`.
7. **bio-transpire** — title `植物體內物質的運輸`. A simple plant: roots, stem, two leaves.
   Labels with leaders: at roots `根毛：吸收水分和礦物質`; an upward arrow along the stem
   `木質部：水分往上運送`; at a leaf `氣孔：水蒸氣散失（蒸散作用）` with small wavy vapour marks;
   a downward arrow on the other side of the stem `韌皮部：運送葉製造的養分`. Highlight the
   upward water arrow in `var(--ic)`. `示意圖`.
8. **bio-heart** — title `心臟的構造`. A schematic heart divided into four chambers, drawn as seen
   from the front (the heart's right side is on the viewer's left). Chamber labels: upper left
   `右心房`, lower left `右心室`, upper right `左心房`, lower right `左心室`. Vessels with arrows:
   `大靜脈` into 右心房, `肺動脈` out of 右心室, `肺靜脈` into 左心房, `主動脈` out of 左心室.
   Mark one valve between 房 and 室 with a short label `瓣膜`. Make the 左心室 wall visibly
   thickest and outline it with `var(--ic)`, note `左心室壁最厚`. Small notes
   `圖中的左右是心臟本身的左右` and `示意圖`.
9. **bio-circulation** — title `人體的血液循環`. A central heart block divided into four cells
   (same left/right convention as diagram 8). Upper loop `肺循環`: 右心室 → `肺動脈` →
   `肺部微血管` → `肺靜脈` → 左心房. Lower loop `體循環`: 左心室 → `主動脈` → `全身微血管`
   → `大靜脈` → 右心房. Small tags: `充氧血` beside 肺靜脈 and beside 主動脈; `減氧血` beside
   肺動脈 and beside 大靜脈. Draw the 體循環 loop line in `var(--ic)`.
10. **bio-receptors** — table titled `受器與刺激`, columns `受器`, `接受的刺激`, `產生的感覺`.
    Rows: `眼` / `光` / `視覺`; `耳` / `聲音` / `聽覺`; `鼻` / `化學物質` / `嗅覺`;
    `舌` / `化學物質` / `味覺`; `皮膚` / `冷、熱、觸、壓、痛` / `冷覺、觸覺等`. Footer
    `受器接受刺激，感覺在大腦產生`.
11. **bio-reflex** — title `神經傳導的路徑`, two rows of linked boxes. Row 1 `有意識的反應`:
    `受器` → `感覺神經` → `大腦` → `運動神經` → `動器`, example under the row
    `例：看到紅燈停下腳步`. Row 2 `反射`: `受器` → `感覺神經` → `脊髓` → `運動神經` → `動器`,
    example `例：碰到燙的東西立刻縮手`. Outline the row-2 `脊髓` box with `var(--ic)`.
    Small note `反射不經大腦思考，反應快`.
12. **bio-glands** — title `人體的內分泌腺`. A simple front body outline (head, trunk). Dots at
    the gland positions with leader lines to labels on both sides: `腦垂腺：生長激素`,
    `甲狀腺：甲狀腺素`, `副甲狀腺：調節血鈣`, `腎上腺：腎上腺素`, `胰島：胰島素、升糖素`,
    `睪丸／卵巢：性激素`. `示意圖`.
13. **bio-tropism** — two panels. `向光性`: a potted seedling beside a lamp (`var(--fig-warm)`)
    with the stem bending toward the lamp; label `莖彎向光源`. `向地性`: a seedling lying on its
    side; the root curves downward, label `根向下長（向地性）`; the stem curves upward, label
    `莖向上長（背地性）`. Footer `和植物激素分布不均有關`. `示意圖`.
14. **bio-breathing** — two panels `吸氣` and `呼氣`. Each shows a simple chest outline with rib
    arcs, two lungs and a diaphragm curve under them. 吸氣: notes `肋骨上舉`, `橫膈下降`,
    `胸腔變大`, an air arrow going in through the windpipe. 呼氣: `肋骨下降`, `橫膈上升`,
    `胸腔變小`, an air arrow going out. Highlight the 吸氣 diaphragm in `var(--ic)`. `示意圖`.
15. **bio-urinary** — title `泌尿系統`. Two kidneys at the top, each with a tube (ureter) down to
    a bladder, then one tube (urethra) down. Labels: `腎臟：過濾血液，形成尿液`, `輸尿管`,
    `膀胱：暫時儲存尿液`, `尿道`. To one side a small box `肝臟：把氨轉變成尿素` with an arrow
    labelled `血液運送尿素` pointing to a kidney. Outline the kidneys in `var(--ic)`. `示意圖`.
16. **bio-sugar** — title `血糖的恆定`, a two-branch flowchart around a centre box `血糖`.
    Upper branch: `飯後血糖升高` → `胰島分泌胰島素` → `葡萄糖進入細胞，或轉成肝醣儲存` →
    `血糖下降`. Lower branch: `飢餓時血糖降低` → `胰島分泌升糖素` → `肝醣分解成葡萄糖` →
    `血糖上升`. Outline `胰島分泌胰島素` with `var(--ic)`.
17. **bio-division** — title `細胞分裂與減數分裂`, two columns. Left `細胞分裂`: one cell with
    4 short rods inside labelled `4 條染色體` → arrow → two cells each with 4 rods, label `各 4 條`;
    note `身體生長、修補組織`. Right `減數分裂`: one cell with 4 rods → arrow → four cells each
    with 2 rods, label `各 2 條`; note `產生精子和卵`. Bottom line (human example):
    `精子（23 條）＋ 卵（23 條）→ 受精卵（46 條）`. Outline the four meiosis cells with `var(--ic)`.
    `示意圖`.
18. **bio-asexual** — table titled `無性生殖的方式`, columns `方式`, `例子`. Rows:
    `分裂生殖` / `細菌、草履蟲`; `出芽生殖` / `酵母菌、水螅`; `斷裂生殖` / `渦蟲、海星`;
    `孢子繁殖` / `黴菌、蕨類`; `營養器官繁殖` / `馬鈴薯（塊莖）、甘薯（塊根）、落地生根（葉）`;
    `人為方法` / `扦插、壓條、嫁接、組織培養`. Footer `子代和親代的遺傳特徵幾乎相同`.

## List B (diagrams 19–36)

19. **bio-flower** — title `花的構造`. A flower in vertical section. Labels with leaders:
    `花瓣`, `花萼`, `雄蕊` with sub-labels `花藥` and `花絲`, `雌蕊` with sub-labels `柱頭`,
    `花柱`, `子房`, and small ovals inside the ovary labelled `胚珠`. Outline the 子房 in
    `var(--ic)`. Bottom line: `授粉 → 受精 → 子房發育成果實，胚珠發育成種子`. `示意圖`.
20. **bio-punnett** — title `棋盤方格法`. Above the grid `Aa（父）` with the two columns headed
    `A` and `a`; left of the grid `Aa（母）` with rows headed `A` and `a`. Cells: `AA`, `Aa`,
    `Aa`, `aa`. Outline the `aa` cell with `var(--ic)`. Two lines below:
    `基因型　AA：Aa：aa = 1：2：1` and `表現型　顯性：隱性 = 3：1`.
21. **bio-sex** — title `性別的決定`, a 2×2 grid. Top `父親 XY` with columns `X` and `Y`; left
    `母親 XX` with rows `X` and `X`. Cells: `XX 女`, `XY 男`, `XX 女`, `XY 男`. Outline the `Y`
    column header with `var(--ic)`. Footer `卵都帶 X，精子帶 X 或 Y；生男、生女的機率各約 50%`
    (may break into two lines).
22. **bio-abo** — table titled `ABO 血型`, columns `血型`, `可能的基因型`. Rows: `A 型` /
    `IᴬIᴬ、Iᴬi`; `B 型` / `IᴮIᴮ、Iᴮi`; `AB 型` / `IᴬIᴮ`; `O 型` / `ii`. Footer
    `Iᴬ 和 Iᴮ 對 i 是顯性；Iᴬ、Iᴮ 同時存在時都會表現`. (Use these exact characters: capital I
    followed by the superscript letters ᴬ U+1D2C and ᴮ U+1D2E.)
23. **bio-mutation** — title `突變與遺傳疾病`. A small box at top `誘發突變的因子` listing
    `紫外線、X 射線等輻射` and `某些化學物質（如香菸中的物質）`. Below a table with columns
    `疾病`, `原因`: `白化症` / `隱性遺傳，無法製造黑色素`; `紅綠色盲` /
    `基因在 X 染色體上，男性較多`; `唐氏症` / `第 21 對染色體多了一條`; `海洋性貧血` /
    `隱性遺傳，臺灣常見`.
24. **bio-clone** — title `複製羊的過程`, a flowchart. Box `甲羊（白臉）：提供乳腺細胞的細胞核`
    and box `乙羊（黑臉）：提供去除細胞核的卵` both arrow into `細胞核放入卵中` → `胚胎` →
    `植入丙羊（黑臉）的子宮` → `出生的小羊：白臉，和甲羊相同`. Outline the 甲羊 box and the
    last box with `var(--ic)`. `示意圖`.
25. **bio-strata** — title `地層與化石`. A column of four horizontal rock layers (`var(--fig-sand)`
    fills with slightly different patterns), labelled from top to bottom `哺乳類化石`,
    `爬蟲類化石`, `魚類化石`, `三葉蟲化石`, each with a tiny simple fossil sketch. A vertical
    arrow beside the column pointing down labelled `愈下層愈古老`, with `新` at top and `舊` at
    bottom. Note `未經擾動的地層` and `示意圖`.
26. **bio-taxa** — title `生物的分類階層`. Seven stacked bars getting narrower from top to bottom:
    `界`, `門`, `綱`, `目`, `科`, `屬`, `種`. To the right of each bar the example for the house
    dog: `動物界`, `脊索動物門`, `哺乳綱`, `食肉目`, `犬科`, `犬屬`, `家犬`. A side arrow pointing
    down labelled `階層愈小，共同特徵愈多，親緣關係愈近`. Outline the `種` bar with `var(--ic)`.
27. **bio-kingdoms** — table titled `原核生物、原生生物和真菌`, columns `原核生物界`,
    `原生生物界`, `真菌界` plus a first label column. Rows: `細胞核` / `沒有核膜包住` / `有` /
    `有`; `例子` / `細菌、藍綠菌` / `草履蟲、眼蟲、藻類` / `酵母菌、黴菌、香菇`; `養分` /
    `有的能行光合作用` / `有的能行光合作用` / `分解或吸收其他生物的養分`.
28. **bio-plants** — title `植物的分類`, a tree diagram from a top box `植物界`. First split:
    `沒有維管束` → leaf box `蘚苔植物`（example `地錢`）; `有維管束` → second split:
    `不產生種子` → `蕨類植物`（`用孢子繁殖`）; `產生種子` → third split: `裸子植物`
    （`種子外沒有果實`, example `松`）and `被子植物`（`會開花結果`）→ fourth split:
    `雙子葉植物`（`網狀脈`）and `單子葉植物`（`平行脈`）. Outline `被子植物` with `var(--ic)`.
29. **bio-animals** — table titled `脊椎動物五大類`, columns `類別`, `呼吸`, `體表`, `生殖`.
    Rows: `魚類` / `鰓` / `鱗片` / `體外受精、卵生`; `兩生類` / `幼體用鰓，成體用肺和皮膚` /
    `皮膚溼潤` / `體外受精、卵生`; `爬蟲類` / `肺` / `鱗片或骨板` / `體內受精、有殼卵`;
    `鳥類` / `肺` / `羽毛` / `體內受精、有殼卵`; `哺乳類` / `肺` / `毛髮` /
    `體內受精、大多胎生`.
30. **bio-capture** — title `捉放法估算族群數量`, three step boxes left to right (or top to
    bottom): `① 捕捉 40 隻，做記號後放回`, `② 再捕捉 50 隻，其中 8 隻有記號`,
    `③ 族群總數 ≈ 40 × 50 ÷ 8 = 250 隻`. Tiny animal dots, some marked with a ring. Outline step ③
    with `var(--ic)`. `示意圖`.
31. **bio-relations** — table titled `生物間的互動關係`, columns `關係`, `甲`, `乙`, `例子`.
    Rows: `掠食` / `＋` / `－` / `貓頭鷹捕食老鼠`; `競爭` / `－` / `－` / `稗草和水稻`;
    `寄生` / `＋` / `－` / `跳蚤和狗`; `互利共生` / `＋` / `＋` / `豆科植物和根瘤菌`;
    `片利共生` / `＋` / `0` / `印魚和鯊魚`. Footer `＋ 得到好處　－ 受到損害　0 沒有明顯影響`.
32. **bio-energy** — title `能量塔`. A pyramid of four stacked trapezoids, bottom to top:
    `生產者　10000 kJ`, `初級消費者　1000 kJ`, `次級消費者　100 kJ`, `高級消費者　10 kJ`
    (labels may sit beside the narrow top levels with leaders). Side notes
    `能量逐層減少，大約只剩 10%` and `大部分以熱的形式散失`. Outline the bottom level with
    `var(--ic)`. Note `數值為示意`.
33. **bio-ecosystems** — table titled `生態系的類型`, columns `生態系`, `環境特色`, `例子`.
    Rows: `森林` / `雨量多，生物種類多` / `闊葉林、針葉林`; `草原` / `雨量較少，以草為主` /
    `大型草食動物`; `沙漠` / `雨量稀少，日夜溫差大` / `仙人掌`; `凍原` /
    `氣溫很低，地下長年結冰` / `地衣、蘚苔`; `河口` / `鹽度變化大，養分豐富` /
    `紅樹林（水筆仔）`; `海洋` / `面積最大` / `浮游藻類、珊瑚礁`.
34. **bio-diversity** — title `生物多樣性的三個層次`, three stacked boxes, each with a tiny
    simple icon on the left: `遺傳多樣性` / `同種生物個體之間基因的差異`（icon: three ladybird
    shapes with different spot counts）; `物種多樣性` / `一個地區內生物種類的多寡`（icon: a
    leaf, a fish, a bird）; `生態系多樣性` / `森林、草原、海洋等不同的生態系`（icon: tree,
    wave）. Outline the middle box with `var(--ic)`.
35. **bio-magnify** — title `生物放大作用`. A vertical food chain from bottom to top, each step a
    small box with the value: `湖水　0.00005 ppm`, `浮游生物　0.04 ppm`, `小魚　0.5 ppm`,
    `大魚　2 ppm`, `食魚的鳥　25 ppm`, connected by upward arrows. A tall side arrow
    `愈往上層，濃度愈高`. Outline the top box with `var(--ic)`. Note `難分解的汙染物`.
36. **bio-conserve** — title `保育的方式`, two columns. Left `就地保育`: `在生物原本的棲地保護`,
    examples `國家公園、自然保留區、野生動物保護區`. Right `移地保育`: `把生物移到其他地方保護`,
    examples `動物園、植物園、種子庫`. Outline the left column header with `var(--ic)`.
    Bottom row: `國際公約：華盛頓公約（管制瀕危物種貿易）、生物多樣性公約、拉姆薩公約（溼地）`
    (may break into two lines).

## Finish

Run `python check_svg.py figs` and fix every failure in your own files (failures in the other
list's files are not yours — ignore them). Then list the files you wrote and anything you could
not draw exactly as described.
