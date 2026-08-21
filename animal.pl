% Facts
has_hair(tiger).
gives_milk(tiger).
% Rule
mammal(X) :- has_hair(X), gives_milk(X).