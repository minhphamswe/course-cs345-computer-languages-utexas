/* Bell's Theorem - num(disagree1) + num(disagree2) >= num(disagree3)
*
* If see 0 30 60
* a_strategy: { P, P, P }
* b_strategy: { A, P, P }
* c_strategy: { P, A, P }
* d_strategy: { P, P, A }
*/
disagree1(N) :- b_strategy(N), data(N,0,30).
disagree1(N) :- b_strategy(N), data(N,30,0).
disagree1(N) :- c_strategy(N), data(N,0,30).
disagree1(N) :- c_strategy(N), data(N,30,0).
disagree2(N) :- d_strategy(N), data(N,30,60).
disagree2(N) :- d_strategy(N), data(N,60,30).
disagree2(N) :- c_strategy(N), data(N,30,60).
disagree2(N) :- c_strategy(N), data(N,60,30).
disagree3(N) :- b_strategy(N), data(N,0,60).
disagree3(N) :- b_strategy(N), data(N,60,0).
disagree3(N) :- d_strategy(N), data(N,0,60).
disagree3(N) :- d_strategy(N), data(N,60,0).
/*
*data(1,0,0).
*data(2,0,30).
*data(3,0,60).
*data(4,30,0).
*data(5,30,30).
* This doesn't seem to work unfortunately
*discontiguous(b_strategy).
*discontiguous(c_strategy).
*discontiguous(d_strategy).
* so the following are in sorted order
* instead of number order of the arguments.
*/
b_strategy(1).
b_strategy(4).
c_strategy(5).
c_strategy(2).
d_strategy(3).
