'use strict';
// All mathematical panels follow version 2, Theorem 1 and Proposition 2.
// The square is manuscript Corollary 5; the ten-grid count is Lemma 3.
// Only the separate negation in the final scene is marked with formal evidence.
function heading(en, zh) {
  txt(en, 960, 210, {size: 44, fam: F.disp, w: 700, align: 'center', c: C.white});
  txt(zh, 960, 268, {size: 32, fam: F.zh, align: 'center', c: C.cyan});
}
function label(s, x, y, size = 36, c = C.white, a = 1) {
  txt(s, x, y, {size, fam: F.math, align: 'center', c, a});
}
function equalityBars(a) {
  panel(260, 350, 620, 390, a, C.argued, 'MINIMUM FAILURES');
  panel(1040, 350, 620, 390, a, C.argued, 'SHARED LINES');
  label('12', 570, 535, 140, C.white, a);
  label('15', 1350, 535, 140, C.white, a);
  for (let j=0;j<12;j++) line(320+j*43, 635, 320+j*43, 690, C.cyan, a, 16);
  for (let j=0;j<15;j++) line(1100+j*35, 635, 1100+j*35, 690, C.mag, a, 12);
  label('<', 960, 535, 90, C.white, a);
}
SCENES.question = S => {
  badgeQ(S, [[0, null, 'argued']]);
  heading('WHY TWELVE IS NOT FIFTEEN', '为什么 12 不等于 15');
  equalityBars(at(S, 1, 0.7));
  label('75 lines · 31 points', 960, 825, 38, C.cyan, at(S,1,0.7));
};
SCENES.parity = S => {
  badgeQ(S, [[0, null, 'argued']]);
  heading('ONE ASSIGNMENT CANNOT SATISFY EVERY RULE', '同一个赋值不能满足全部规则');
  panel(180, 315, 790, 505, 1, C.cyan, 'MERMIN–PERES SQUARE');
  const a = at(S,0,0.7), names = ['XII','IXI','XXI','IZI','ZII','ZZI','XZI','ZXI','YYI'];
  for(let j=0;j<3;j++) {
    line(320,430+j*125,820,430+j*125,C.cyan,a,4);
    line(320+j*250,430,320+j*250,680,j===2?C.mag:C.cyan,a,4);
  }
  names.forEach((n,i)=>chip(320+(i%3)*250,430+Math.floor(i/3)*125,138,66,n,C.white,a,31));
  for(let j=0;j<3;j++) label('+', 900,440+j*125,34,C.cyan,a);
  ['+','+','−'].forEach((n,j)=>label(n,320+j*250,770,42,j===2?C.mag:C.cyan,a));
  panel(1050,315,660,505,1,C.argued,'COUNTING TEN GRIDS');
  label('Each point appears twice',1380,405,32,C.white,at(S,1,0.6));
  label('(+1) = (−1) ?',1380,490,50,C.mag,at(S,1,0.6));
  const c = at(S,2,0.6);
  for(let j=0;j<10;j++)chip(1160+(j%5)*108,590+Math.floor(j/5)*80,76,52,String(j+1),C.cyan,c,24);
  label('4k ≥ 10  →  k ≥ 3',1380,775,40,C.white,c);
};
SCENES.lifts = S => {
  badgeQ(S, [[0, null, 'argued']]);
  heading('ONE BASE LINE HAS FOUR SIGN-PRESERVING LIFTS', '每条底层线有四种同号提升');
  const a=at(S,0,0.7);
  panel(555,315,810,170,a,C.cyan,'A NEGATIVE BASE LINE');
  label('XX     ZZ     YY',960,405,58,C.white,a);
  const b=at(S,1,0.7);
  const triples=['XXI  ZZI  YYI','XXI  ZZZ  YYZ','XXZ  ZZI  YYZ','XXZ  ZZZ  YYI'];
  triples.forEach((s,i)=>{
    const x=75+i*455;
    arrow(960,485,x+202,550,C.cyan,b,3);
    panel(x,555,405,145,b,C.argued,'LIFT '+(i+1));
    label(s,x+202,635,31,C.white,b);
    label('−',x+202,685,33,C.mag,b);
  });
  label('15 pole lines + 4 × 15 lifts = 75 lines',960,765,38,C.white,b);
  label('3 base failures × 4 = 12 failures',960,815,37,C.cyan,at(S,2,0.6));
};
SCENES.sections = S => {
  badgeQ(S, [[0, null, 'argued']]);
  heading('COUNT EVERY FAILED LINE EQUALLY OFTEN', '每条错线都以相同重数被计数');
  const a=at(S,0,0.7);
  panel(140,320,800,505,a,C.cyan,'SIXTEEN LINEAR SECTIONS');
  for(let i=0;i<16;i++){
    const x=255+(i%4)*185,y=420+Math.floor(i/4)*108;
    panel(x-70,y-38,140,78,a,C.cyan);
    label('≥3',x,y+15,35,C.white,at(S,1,0.5));
  }
  panel(1020,320,750,505,1,C.argued,'INCIDENCE COUNT');
  label('16 × 3 = 48',1395,445,64,C.white,at(S,1,0.6));
  label('each non-pole line × 4',1395,555,35,C.cyan,at(S,2,0.6));
  label('N ≥ 48 / 4 = 12',1395,685,59,C.white,at(S,2,0.6));
  label('pole lines: counted zero times',1395,780,30,C.dim,at(S,2,0.6));
};
SCENES.intersection = S => {
  badgeQ(S, [[0, null, 'argued']]);
  heading('A DIFFERENT COUNT FORCES FIFTEEN', '另一种计数强迫交集为十五');
  const a=at(S,0,0.6);
  panel(130,320,800,500,a,C.cyan,'TWO POSSIBLE LINE PROFILES');
  const xs=[280,510,740];
  [460,670].forEach(y=>line(235,y,785,y,C.cyan,a,5));
  xs.forEach(x=>chip(x,460,85,66,'in',C.cyan,a,26));
  xs.forEach((x,i)=>chip(x,670,100,66,i===1?'in':'out',i===1?C.cyan:C.dim,a,26));
  label('3 points inside',530,555,34,C.white,a);
  label('1 point inside',530,770,34,C.white,a);
  panel(1020,320,750,500,1,C.argued,'POINT–LINE INCIDENCES');
  label('31 × 3 = 93',1395,435,58,C.white,at(S,1,0.6));
  label('93 = 3k + (63 − k)',1395,555,44,C.white,at(S,2,0.6));
  label('k = 15',1395,700,88,C.mag,at(S,2,0.6));
  label('degree = 12',1395,780,38,C.cyan,at(S,2,0.6));
};
SCENES.scope = S => {
  badgeQ(S, [[0, null, 'argued'], [1, 'negation', 'lean'], [2, null, 'argued']]);
  heading('THE UNIVERSAL EQUALITY IS FALSE', '普遍交集等式为假');
  panel(260,335,1400,460,1,C.cyan,'WHAT IS ESTABLISHED');
  label('An upper bound need not be exact',960,440,48,C.white,at(S,0,0.6));
  label('Formal conclusion: universal equality is false',960,540,42,C.white,at(S,1,0.6));
  label('Exact counts: manuscript written proofs',960,625,38,C.argued,at(S,1,0.6));
  label('Which hypotheses restore equality?',960,730,42,C.cyan,at(S,2,0.6));
  label('Haobo Ma · Wenlin Zhang | Version 2',960,818,28,C.dim,at(S,2,0.6));
};
FILM.poster = () => {
  background(42,TL.scenes[0],0,4);
  heading('WHY TWELVE IS NOT FIFTEEN', '为什么 12 不等于 15');
  equalityBars(1);
  label('75 lines · a contextuality counterexample',960,825,37,C.cyan);
  label('Haobo Ma · Wenlin Zhang',960,900,32,C.white);
  label('Version 2 · DOI:10.5281/zenodo.23904468',960,964,26,C.dim);
};
