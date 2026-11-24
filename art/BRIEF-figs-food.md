# Brief: 6 teaching diagrams for the 養分島 (nutrition island, junior-high biology)

You are drawing original explanatory diagrams for a junior-high science learning page
(Traditional Chinese, Taiwan). Each diagram sits inside a lesson card, above the key points,
and is read on phones (about 340 px wide) and desktops (up to about 560 px wide). Draw
everything yourself as clean schematic diagrams — do not trace or imitate any textbook figure.
Accuracy matters more than decoration: these are for 12–13-year-olds studying for exams.

## Output

Write exactly these 6 files into `figs/` and nothing else:
`figs/bio-nutrients.svg`, `figs/bio-foodtest.svg`, `figs/bio-enzyme.svg`,
`figs/bio-leaf.svg`, `figs/bio-photosyn.svg`, `figs/bio-digest.svg`.
Do not create, modify or delete any other file (the `examples/` folder is read-only reference).

## MUST follow (checked by `python check_svg.py figs`)

- `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 H" role="img">` where H is
  between 140 and 280 (pick what the content needs). No width/height on the root.
- First child: `<title>` with one plain sentence in Traditional Chinese describing the diagram.
  The `<title>` is for screen readers only; the visible heading (if any) is a normal `<text>`.
- Allowed elements only: g path circle ellipse rect line polyline polygon text tspan title
  defs marker. No gradients, filters, style, script, image, href or comments.
- Colours: every fill/stroke is `none` or one of these CSS variables (they switch for dark mode):
  - `var(--fig-ink)` all text, outlines and arrows
  - `var(--fig-soft)` secondary text, axis ticks, dashed guide lines
  - `var(--fig-line)` faint grid lines and panel borders
  - `var(--fig-paper)` panel/background fills that must contrast with ink
  - `var(--ic)` the highlight colour for the one thing the diagram is about (an island green;
    may be dark in dark mode, so never put text on a `var(--ic)` fill)
  - `var(--fig-land)` green plant tissue, leaves, chloroplasts
  - `var(--fig-sea)` water, `var(--fig-deep)` deeper water / liquids
  - `var(--fig-sand)` food, soil, tan fills; `var(--fig-warm)` light, sun, heat;
    `var(--fig-cool)` air, gases, cold
- Text: `<text>` with `font-size` 11 to 14 (labels 12–13, panel titles 13–14) and
  `fill="var(--fig-ink)"` or `var(--fig-soft)`. Do not set font-family. Use `text-anchor`.
  Text must stay inside the viewBox and must not overlap other text. Budget 1 em per Chinese
  character (13 px wide at size 13). Prefer labels in clear space with a short leader line.
  No transform on `<text>`; groups may use `translate()` only.
- Every id starts with the file name (e.g. marker id `bio-digest-arr` in `bio-digest.svg`).
- Under 9 KB per file; round numbers to at most 1 decimal.
- Use the exact label wording given below. Never add facts, numbers or names not listed.
- Where marked, include the small soft-grey note `示意圖` in a corner.

## Layout suggestions (you may adjust)

- Calm and readable: thin ink outlines (1.5), soft fills, generous white space, at most one
  `var(--ic)` highlight per panel. Multi-panel diagrams: equal-width panels, short title on top.
- If text does not fit, keep in this order of priority: (1) the main labels, (2) the arrows and
  what they connect, (3) secondary notes; shorten only text marked "(may shorten)".
- Approved examples to match in style, size and spacing (read them first):
  table — `examples/geo-koreas.svg`; timeline — `examples/his-songyuan.svg`;
  two-panel schematic — `examples/geo-cnmonsoon.svg`; flowchart — `examples/geo-cnclimate.svg`.
- Judge legibility at about 340 px wide on a phone.

## The 6 diagrams

1. **bio-nutrients** — a two-column table titled `六大類養分`. Left column header
   `能產生能量`, rows: `醣類` / `米飯、麵包`; `蛋白質` / `蛋、豆、魚、肉`; `脂質` / `油脂、堅果`.
   Right column header `不能產生能量`, rows: `水` / `體內含量最多`; `維生素` / `調節生理機能`;
   `礦物質` / `鈣、鐵、磷等`. Highlight the left header cell outline with `var(--ic)`.
   Under the table a small row: `大分子 → 小分子：澱粉 → 葡萄糖・蛋白質 → 胺基酸・脂質 → 脂肪酸、甘油`
   (may break into two lines).

2. **bio-foodtest** — two panels. Left title `檢測澱粉`: a test tube labelled `澱粉溶液`, a dropper
   labelled `碘液`, an arrow to the result tube labelled `藍黑色`; under it `不需加熱`.
   Right title `檢測葡萄糖`: a test tube labelled `葡萄糖溶液`, a dropper labelled `本氏液`,
   a beaker of water under/around the tube labelled `隔水加熱`, an arrow to the result tube
   labelled `黃 → 橙 → 紅`; under it `需要隔水加熱`. Note `示意圖`.
   (The palette cannot show real colours; the colour names are text labels.)

3. **bio-enzyme** — two small line charts side by side, note `示意圖`.
   Left title `溫度與活性`: x-axis `溫度（°C）` with ticks `0`, `37`, `60`; y-axis label `活性`.
   One curve rising slowly from 0, peaking at 37, then dropping steeply to near zero by 60.
   Dashed vertical guide at 37 labelled `最適溫度`. A small note near the right tail
   `高溫：酵素變性`.
   Right title `pH 值與活性`: x-axis `pH 值` with ticks `1`, `7`, `13`; two bell curves, one
   peaking near pH 2 labelled `胃蛋白酶`, one peaking at pH 7 labelled `唾液澱粉酶`
   (the second one in `var(--ic)`).

4. **bio-leaf** — a schematic cross-section of a leaf (a horizontal slab), note `示意圖`.
   From top to bottom: a thin top line `角質層`; a row of rectangular cells `上表皮`;
   a middle layer of rounded cells with small green dots (`var(--fig-land)`) labelled `葉肉`
   with a leader to one dot labelled `葉綠體`; a vein bundle (circle of small cells) in the
   middle labelled `葉脈（維管束）`; a bottom row of cells `下表皮` with one gap flanked by two
   bean-shaped cells: label the gap `氣孔` and the pair `保衛細胞`. All labels outside the slab
   on the right or left with short leader lines.

5. **bio-photosyn** — a flow diagram titled `光合作用`. Centre box `葉綠體` with a sub-label
   `葉綠素吸收光能`. A sun symbol (`var(--fig-warm)`) above with an arrow into the box labelled
   `光能`. Inputs on the left with arrows into the box: `水`（sub-label `由根吸收，經葉脈運送`）
   and `二氧化碳`（sub-label `由氣孔進入`）. Outputs on the right with arrows out of the box:
   `葡萄糖`（sub-label `可轉變成澱粉儲存`）, `氧氣`（sub-label `由氣孔釋出`）and `水`.
   Highlight the centre box outline with `var(--ic)`.

6. **bio-digest** — a two-column flowchart titled `人體的消化系統` (height up to 280).
   Left column, top to bottom, connected by down arrows (the 消化道): `口腔`, `咽`, `食道`, `胃`,
   `小腸`, `大腸`, `肛門`. Right column (the 消化腺), each with an arrow pointing left into its
   organ: `唾腺：唾液，分解澱粉` → 口腔; `胃腺：胃液，分解蛋白質` → 胃;
   `肝臟：膽汁，乳化脂質` → 小腸 (via a small box `膽囊` labelled `儲存膽汁` — may shorten);
   `胰臟：胰液，分解醣類、蛋白質、脂質` → 小腸; `腸腺：腸液` → 小腸.
   Small tags beside the left column: next to 小腸 `消化、吸收的主要場所`, next to 大腸 `吸收水分`.
   Column headers `消化道` and `消化腺`. Highlight the 小腸 box outline with `var(--ic)`.
   If space is tight, the gland labels may wrap to two lines (organ name on line 1).

## Finish

Run `python check_svg.py figs` and fix every failure. Then list the files you wrote and anything
you could not draw exactly as described.
