# Brief: 44 teaching diagrams for the physics islands (junior-high physics, Taiwan)

You are drawing original explanatory diagrams for a junior-high science learning page
(Traditional Chinese, Taiwan). Each diagram sits inside a lesson card above the key points and
is read on phones (about 340 px wide) and desktops (up to about 560 px wide). Draw everything
yourself as clean schematic diagrams — do not trace or imitate any textbook figure. Accuracy
matters more than decoration: these are for 13–15-year-olds studying for exams.

Two people work on this brief at the same time. **Write only the files in the list your prompt
gives you** (list A = diagrams 1–22, list B = diagrams 23–44). Do not create, modify or delete
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
  lines only, never put text on a `var(--ic)` fill), `var(--fig-land)`, `var(--fig-sea)`,
  `var(--fig-deep)` (water, liquids), `var(--fig-sand)`, `var(--fig-warm)` (heat, flames, light
  rays, copper), `var(--fig-cool)` (air, cold, glass).
- Text: `font-size` 11 to 14, `fill="var(--fig-ink)"` or `var(--fig-soft)`, no font-family,
  use `text-anchor`, stay inside the viewBox, never overlap other text or lines (budget 1 em
  per Chinese character). No transform on `<text>`; groups may use `translate()` only.
- Units and symbols: write them with these Unicode characters exactly (m/s², cm³, 10⁻⁹, λ, °C,
  °F, Ω, ½, ×, ÷, ≈, →). Do not use `<tspan>` baseline shifts.
- Every id starts with the file name (e.g. `phy-lens-arr`). Under 9 KB per file; numbers ≤ 1 decimal.
- Use the exact label wording given below. Never add facts, numbers or names not listed.
- Where marked `示意圖`, include that small soft-grey note in a corner.
- The palette cannot show real colours; never rely on colour alone — the words carry the meaning
  (for example write `N` and `S` on magnets, write colour names on prism rays).
- Physics must be right: angles of incidence and reflection equal; refracted ray bends toward
  the normal going from air into water; field lines leave N and enter S outside a magnet;
  arrows point the stated way.

## Layout suggestions (you may adjust)

- Calm and readable: thin ink outlines (1.5), soft fills, white space, one `var(--ic)` highlight
  per panel. If text does not fit, keep main labels first; table cells may wrap to two lines.
- Approved examples to match (read them first): `examples/geo-koreas.svg` (table),
  `examples/geo-cnclimate.svg` (flowchart), `figs/chem-cell.svg`, `figs/chem-electrolysis.svg`,
  `figs/chem-ph.svg` (scale), `figs/chem-neutral.svg` (line chart), `figs/bio-heart.svg`.
- Judge legibility at about 340 px wide on a phone. Two or three panels side by side is fine;
  four small panels in a 2×2 grid is fine.

## List A (diagrams 1–22)

1. **phy-units** — table titled `長度、質量與時間`, columns `物理量`, `SI 單位`, `常用換算`.
   Rows: `長度` / `公尺（m）` / `1 km＝1000 m，1 m＝100 cm`; `質量` / `公斤（kg）` /
   `1 kg＝1000 g`; `時間` / `秒（s）` / `1 h＝3600 s`. Strip below:
   `1 m＝1000 mm　1 mm＝1000 μm　1 μm＝1000 nm`.
2. **phy-estimate** — title `測量與估計`. A ruler from `0` to `5` cm with millimetre ticks; a pencil
   from 0 ending between 3.4 and 3.5. Labels: `最小刻度 1 mm`, `讀數 3.46 cm`, leader to `3.4`
   with `準確值`, leader to the last digit with `估計值`. Strip: `完整紀錄＝數字＋單位，估到最小刻度的下一位`.
3. **phy-density** — title `排水法與密度`. Left: two measuring cylinders, `V₁＝30 mL` (water only)
   and `V₂＝50 mL` (with a stone), note `讀凹面最低處`, result `物體體積＝V₂－V₁＝20 cm³`.
   Right: a small graph `質量` (y) vs `體積` (x), two straight lines from the origin, steeper one
   labelled `甲：密度較大`, gentler `乙`. Strip: `密度＝質量÷體積（D＝M÷V）`.
4. **phy-wave** — title `波的特徵`. Top: a transverse wave (sine) with labels `波峰`, `波谷`,
   `振幅` (vertical arrow from the centre line to a crest), `波長 λ` (crest to crest), arrow
   `前進方向`. Bottom: a row of dots dense and sparse labelled `密部`, `疏部`, caption `縱波（疏密波）`.
   Top caption `橫波（高低波）`. Strip: `波速＝頻率×波長（v＝f×λ）`.
5. **phy-sound** — title `聲音的傳播`. Left: a tuning fork with compression arcs, note
   `發音體振動`. Right: a horizontal bar chart `聲速比較`: `空氣　約 340 m/s`, `水　約 1500 m/s`,
   `鋼鐵　約 5000 m/s` (bars in proportion), and a row `真空　無法傳聲`. Strip:
   `空氣中：v＝331＋0.6T（T 為攝氏溫度）`.
6. **phy-pitch** — title `聲音三要素`, three panels each with two small waveforms on short axes:
   `音調` (same height, one denser) caption `頻率愈高，音調愈高`; `響度` (same spacing, one taller)
   caption `振幅愈大，響度愈大`; `音色` (one smooth sine, one jagged repeating shape) caption
   `波形不同，音色不同`.
7. **phy-echo** — title `回聲與超聲波`. Top: a person on the left, a cliff on the right, an arrow
   `聲音傳出` above and `反射回來` below, formula `距離＝聲速×時間÷2`. Bottom: a frequency band
   with three segments `低於 20 Hz`, `人耳聽得到 20～20000 Hz`, `超聲波 高於 20000 Hz`;
   note under the last: `蝙蝠、聲納、超音波檢查`.
8. **phy-pinhole** — title `針孔成像`. A candle (upright), a box with a small hole labelled
   `針孔`, a screen labelled `紙屏` with the candle image upside down; two rays from the flame
   top and base crossing at the hole. Labels `倒立的實像`, note `物體離針孔愈近，像愈大`. `示意圖`.
9. **phy-reflect** — title `光的反射`. Left: a mirror line labelled `鏡面`, a dashed normal `法線`,
   incident ray and reflected ray at equal angles, arcs labelled `入射角` and `反射角`, caption
   `入射角＝反射角`. Right: a plane mirror (vertical line), an object arrow in front and a dashed
   image arrow behind, labels `物`, `像（虛像）`, `物距＝像距`.
10. **phy-refract** — title `光的折射`. A horizontal boundary, `空氣` above and `水` below (water
    fill), dashed normal `法線`. Incident ray from upper left, refracted ray in the water bent
    toward the normal; arcs `入射角` (larger) and `折射角` (smaller). Caption
    `空氣→水：偏向法線`. Small inset on the right: an eye above water looking at a coin, the coin's
    apparent position higher, label `看起來比較淺`.
11. **phy-lens** — title `透鏡成像`. Top: a convex lens on a principal axis, three parallel rays
    converging at a dot `焦點 F`, caption `凸透鏡：會聚`. Small: a concave lens with diverging rays,
    caption `凹透鏡：發散`. Bottom table, columns `物體位置`, `成像`, `應用`: `2F 外` / `倒立縮小實像`
    / `照相機`; `F～2F 之間` / `倒立放大實像` / `投影`; `F 內` / `正立放大虛像` / `放大鏡`.
12. **phy-color** — title `色散與顏色`. Left: white light entering a triangular prism and leaving
    as a fan of seven rays labelled `紅`, `橙`, `黃`, `綠`, `藍`, `靛`, `紫` (紅 bends least, at the
    top of the fan). Right: a table titled `在不同色光下看起來的顏色`, columns `照射的光`, `白色上衣`,
    `紅色蘋果`; rows `白光` / `白色` / `紅色`; `紅光` / `紅色` / `紅色`; `綠光` / `綠色` / `黑色`.
13. **phy-thermo** — title `攝氏與華氏`. Two thermometers side by side, `攝氏 °C` and `華氏 °F`.
    Marks: `沸點` at `100 °C` and `212 °F`; `冰點` at `0 °C` and `32 °F`; between them `100 等分`
    and `180 等分`. Strip: `°F＝9／5×°C＋32`.
14. **phy-heat** — title `熱量與熱平衡`. Left a cup `80 °C`, right a cup `20 °C`, a thick arrow from
    hot to cold `熱量`, then arrow to two cups both at `平衡溫度`, note `介於兩者之間`. Strip:
    `1 卡：1 g 的水升高 1 °C 所吸收的熱量`; second strip `不計散失：高溫放出的熱＝低溫吸收的熱`.
15. **phy-specific** — a line chart titled `比熱：水和沙`. x-axis `加熱時間`, y-axis `溫度`; same heat
    source and mass. Steeper line `沙（比熱小）`, gentler line `水（比熱大）`. Note
    `比熱小：易熱也易冷`. Strip `H＝M×S×ΔT`. No numbers on the axes.
16. **phy-states** — title `三態變化`. Three boxes `固態`, `液態`, `氣態` in a triangle (固態
    bottom-left, 液態 bottom-right, 氣態 top). Arrows with labels: 固態→液態 `熔化`, 液態→固態
    `凝固`, 液態→氣態 `汽化`, 氣態→液態 `凝結`, 固態→氣態 `昇華`. Mark `熔化`, `汽化`, `昇華` with
    a small `吸熱` and `凝固`, `凝結` with `放熱`. Note `正在改變狀態時，溫度不變`.
17. **phy-transfer** — title `熱的傳播`, three panels: `傳導` (a spoon in a hot cup, arrows along
    the spoon) caption `沿著物體傳遞，固體為主`; `對流` (a pot over a flame with a circular flow,
    rising in the middle) caption `液體、氣體流動傳熱`; `輻射` (sun on the left, wavy rays to a
    planet) caption `不需要介質`.
18. **phy-force** — title `力與平衡`. Left: a line chart `外力` (x) vs `伸長量` (y), a straight line
    from the origin, then curving after a point marked `彈性限度`, caption `限度內成正比（虎克定律）`.
    Right: a book on a table with two equal arrows, `支撐力` up and `重量` down, caption
    `兩力平衡：大小相等、方向相反、同一直線`.
19. **phy-friction** — a line chart titled `摩擦力的變化`. x-axis `外力`, y-axis `摩擦力`. A line
    rising at 45° labelled `靜摩擦力＝外力（推不動）`, reaching a peak marked `最大靜摩擦力`, then
    dropping slightly to a flat line `動摩擦力（滑動後大小固定）`. No numbers.
20. **phy-pressure** — title `液體壓力與大氣壓力`. Left: a tall water container with three small
    holes at different heights, water jets longer from lower holes, caption `愈深，壓力愈大`.
    Right: a mercury tube upside down in a dish, column height labelled `76 cm`, arrows on the
    dish surface `大氣壓力`, caption `一大氣壓約可撐起 76 cm 水銀柱`. Strip `壓力＝作用力÷受力面積`.
21. **phy-buoyancy** — title `浮力`. Left: a spring scale holding a block in air `50 gw` and in water
    `30 gw`, result `浮力＝20 gw`. Right: a water tank with three balls: one on the bottom
    `下沉：密度＞水`, one in the middle `懸浮：密度＝水`, one at the surface `漂浮：密度＜水`.
    Strip `浮力＝排開液體的重量`.
22. **phy-displace** — title `路徑長與位移`. A number line with ticks from `−2` to `8` (unit m). A path
    drawn above it: start at `+2` (dot `起點`), arrow to `+7`, then arrow back to `+4` (dot
    `終點`). Results: `路徑長＝5＋3＝8 m`, `位移＝4－2＝＋2 m（向右）`.

## List B (diagrams 23–44)

23. **phy-velocity** — title `等速度運動的圖形`. Left: an x–t chart (`位置` vs `時間`) with a
    straight sloping line `等速度：斜率＝速度` and a horizontal line `靜止`. Right: a v–t chart
    (`速度` vs `時間`) with a horizontal line and the area under it shaded `面積＝位移`.
24. **phy-accel** — title `等加速度運動`. Left: v–t chart with a line rising from the origin,
    `斜率＝加速度`, triangle under it shaded `面積＝位移`. Right: a paper tape with dots whose gaps
    grow, caption `點的間隔愈來愈大：加速`. Strip `加速度＝速度變化÷時間（m/s²）`.
25. **phy-freefall** — title `自由落體`. Left: a ball at five positions at equal time steps with gaps
    growing (ratio 1：3：5：7), label `每隔相同時間`. Middle: a v–t straight line from the origin,
    `斜率＝g≈9.8 m/s²`. Right: a tall tube `真空` with a feather and a coin side by side,
    caption `同時落下`.
26. **phy-inertia** — title `慣性`, two panels: a bus with a standing passenger leaning forward,
    arrow `煞車`, caption `身體向前傾`; the same bus with the passenger leaning back, arrow `起動`,
    caption `身體向後傾`. Strip `物體會保持原來的運動狀態；質量愈大，慣性愈大`. `示意圖`.
27. **phy-newton2** — title `運動定律 F＝m×a`. Left: small chart `加速度` vs `合力`, straight line
    from origin, caption `m 固定：a 和 F 成正比`. Right: small chart `加速度` vs `質量`, a falling
    curve, caption `F 固定：a 和 m 成反比`. Strip `1 N＝使 1 kg 產生 1 m/s² 的力`.
28. **phy-newton3** — title `作用力與反作用力`. Left: a rocket with exhaust, arrow on the gas
    downward `火箭推氣體`, arrow on the rocket upward `氣體推火箭`. Right: two skaters pushing
    hands, each with an arrow pointing away from the other, equal length. Strip
    `大小相等、方向相反、作用在不同物體上`.
29. **phy-circular** — title `圓周運動與萬有引力`. Left: a circular path with a ball, a tangent
    arrow `速度（切線方向）`, an inward arrow `向心力（指向圓心）`, a dashed tangent line
    `繩斷：沿切線飛出`. Right: Earth and Moon with a pair of opposite arrows `萬有引力`, note
    `距離變 2 倍，引力變 1／4`.
30. **phy-torque** — title `力矩與槓桿原理`. A lever on a triangular fulcrum `支點`; a downward arrow
    `抗力 40 kgw` at `1.5 m` from the fulcrum on the left and a downward arrow `施力 30 kgw` at
    `2 m` on the right; brackets `抗力臂`, `施力臂`. Strip
    `施力×施力臂＝抗力×抗力臂　40×1.5＝30×2`.
31. **phy-work** — title `功與功率`, three panels: `有作功` (a person pushing a box, force arrow and
    displacement arrow both right); `不作功` (pushing a wall, no movement, note `沒有位移`);
    `不作功` (carrying a bag while walking, force arrow up, motion arrow right, note
    `力和位移垂直`). Strip `W＝F×S（焦耳）　P＝W÷t（瓦特）`.
32. **phy-mechenergy** — title `動能與位能`. A pendulum with three positions: left high
    `位能最大，動能最小`, bottom `動能最大，位能最小`, right high (same height as left). Strip
    `重力位能 U＝m×g×h　動能 K＝½×m×v²`.
33. **phy-conserve** — title `能量的轉換`, three flow rows with arrows:
    `水力發電：重力位能 → 動能 → 電能`; `火力發電：化學能 → 熱能 → 動能 → 電能`;
    `太陽能板：光能 → 電能`. Bottom strip in a box outlined with `var(--ic)`:
    `能量守恆：能量只會轉換形式，總量不變`.
34. **phy-machines** — title `簡單機械`, 2×2 panels: `定滑輪` (fixed pulley) caption
    `改變施力方向，不省力`; `動滑輪` caption `省一半的力，繩子拉 2 倍長`; `斜面` caption
    `愈平緩愈省力`; `輪軸` caption `施力在輪上省力`. Strip `省力必費時，不能省功`.
35. **phy-static** — title `靜電`. Left: a balloon and a piece of fur after rubbing, `−` signs on the
    balloon and `＋` signs on the fur, arrow `電子`, labels `氣球帶負電`, `毛皮帶正電`. Right: a
    negatively charged rod `−−−` near (not touching) a metal sphere; sphere near side `＋＋`, far
    side `−−`, caption `靜電感應`. Strip `同性電相斥、異性電相吸`.
36. **phy-current** — title `電流與電路`. Top: a circuit drawn with standard symbols — battery
    (`＋` and `−` marked), switch, bulb, ammeter `A` in series; an arrow along the wire
    `電流：正極→負極` and an opposite arrow `電子流`. Bottom, two small circuits: `串聯：電流處處相等`
    and `並聯：總電流＝各分路電流和`.
37. **phy-voltage** — title `電壓`. Left: a bulb with a voltmeter `V` connected across it, caption
    `伏特計並聯`. Right top: three cells in series `1.5 V×3＝4.5 V`; right bottom: three cells in
    parallel `仍為 1.5 V，用得較久`. Note `一般乾電池約 1.5 V`.
38. **phy-ohm** — title `歐姆定律與電阻`. Left: a V–I chart (`電壓` vs `電流`): a straight line
    from the origin `歐姆式導體：V＝I×R`, and a curve bending upward `燈泡（電阻隨溫度變大）`.
    Right: a small table `影響電阻的因素`: `導線愈長` / `電阻愈大`; `導線愈粗` / `電阻愈小`;
    `溫度愈高（金屬）` / `電阻愈大`.
39. **phy-power** — title `電流的熱效應`. A heating coil glowing (warm fill) with wavy heat lines,
    caption `電能→熱能`. Formula box: `P＝I×V（瓦特）`, `E＝P×t`, `1 度＝1 kW×1 h`. Warning
    strip: `110 V 的電器接 220 V：電功率變大，可能燒毀`.
40. **phy-home** — title `電力輸送與家庭用電`. A flow left to right: `發電廠` → `升壓` →
    high-voltage tower line labelled `高壓輸電：電流小，損失少` → `變電所降壓` → a house. Inside the
    house: three appliances on parallel branches, labels `電器並聯`, `無熔絲開關`, and a third wire
    on a socket `接地線`.
41. **phy-magfield** — title `磁場與磁力線`. A bar magnet labelled `N` and `S` with curved field
    lines from N around to S (arrowheads pointing away from N), five small compass needles along
    the lines pointing along them. Notes `磁力線由 N 極出發，回到 S 極`, `兩極附近磁力線最密`.
42. **phy-electromag** — title `電流的磁效應`. Left: a vertical straight wire with an up arrow
    `電流`, around it circular field lines with arrows counterclockwise seen from above (draw as
    ellipses), labels `大拇指：電流方向`, `四指彎曲：磁場方向`. Right: a coil (solenoid) with
    current arrows, the right end labelled `N`, left `S`, labels `四指：電流方向`, `大拇指：N 極`,
    caption `放入鐵心＝電磁鐵`.
43. **phy-motor** — title `電流與磁場的交互作用`. Left: three perpendicular arrows from one point
    labelled `大拇指：電流`, `四指：磁場`, `掌心：受力方向`, caption `右手開掌定則`. Right: a simple
    DC motor — two magnet blocks `N` and `S`, a rectangular coil between them, a split ring
    `換向器`, two `電刷`, a battery; caption `電能→動能`.
44. **phy-induction** — title `電磁感應`. Three small panels each with a coil connected to a meter
    (needle): `磁鐵插入` needle to the right; `磁鐵拔出` needle to the left; `磁鐵靜止` needle in the
    middle with `沒有電流`. Strip `磁場變化愈快，感應電流愈大；發電機：動能→電能`.
