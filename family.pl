% Facts
parent(john, mary).
parent(mary, susan).
parent(john, mike).
% Rules
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
% Query
% ?- grandparent(john, susan).