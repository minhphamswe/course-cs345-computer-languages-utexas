spot(0..7).

%
%married is symmetric
married(P,P1):-married(P1,P), person(P;P1).



%
%two places at a table are opposite
opposite(S,S+4):-spot(S;S+4).

%
%opposite is symmetric 
opposite(S1,S2):-opposite(S2,S1), spot(S1;S2).


%%%%% GENERATE %%%%%
%%
%% Mr and Mrs Astor, Mr and Mrs Blake, Mr and Mrs Crane, 
%% and Mr and Mrs Davis were seated around a circular table. 
%%

%
%every person is assigned a spot
1{place(P,S): spot(S)}1:-person(P).



%%%%% TEST %%%%%

%
% two people cannot occupy the same spot
:-place(P1,S), place(P2,S), P1!=P2, spot(S), person(P1;P2).

%% 
%% Mrs Astor was insulted by Mr Blake, who sat
%% next to her on her left. 
%% 
% Mr Blake sat next to Mrs Astor on her left. 
:-place(mrsAstor,S), not place(mrBlake,S+1), spot(S).

%% 
%% Mr Blake was insulted by Mrs Crane, who sat opposite
%% him across the center of the table. 
%%
:-place(mrBlake,S1), not place(mrsCrane,S2), opposite(S1,S2), spot(S1;S2).

%%
%% Mrs Crane was insulted by the hostess, who
%% was the only person to sit next to each one of a married couple. 
%%
% The hostess, Mrs. Davis, was to sit next to each 
% one of a married couple
:-place(P1,1), place(P2,7), not married(P1,P2), person(P1;P2).  

% The hostess, Mrs. Davis, was *the only person* to sit next to each 
% one of a married couple
:-place(P1,S), place(P2,S+2), married(P1,P2), person(P1;P2), spot(S;S+2).  

:-place(P1,0), place(P2,6), married(P1,P2), person(P1;P2).


%% 
%% The hostess was insulted by the only person to sit next to each 
%% one of two men. 
%%
% The hostess was insulted by the person to sit next to each 
% one of two men. 
insult(P):-place(P,S), place(P1,S-1), place(P2,S+1), 
		male(P1), male(P2),person(P), spot(S).

% There was only one person to sit next to each 
% one of two men. (or in other words to insult mrsDavis
:- insult(P), insult(P1), P!=P1, person(P;P1).


%%
%% Mrs. Davis is the hostess and she is seated at place 0.
%%
place(mrsDavis,0).

%#hide.
%#show insult(P).
%% uncomment to see where everyone is sitting
% #show place(X,Y).

%male(mrAstor;mrBlake;mrCrane;mrDavis). %male(mrAstor). male(mrBlake). ...

%person(mrAstor;mrsAstor;mrBlake;mrsBlake;mrCrane;mrsCrane;mrDavis;mrsDavis).

%married(mrAstor,mrsAstor).
%married(mrBlake,mrsBlake).
%married(mrCrane,mrsCrane).
%married(mrDavis,mrsDavis).

