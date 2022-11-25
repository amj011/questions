animal(dog)  :- is_true("Are they the loyal of the all animals"), is_true("does it bark").
animal(cat)  :- is_true("has fur"), is_true("says meow").
animal(tiger) :- is_true("Does the animal eat meat"), is_true("does it roar").
animal(duck) :- is_true("has feathers"), is_true("says quack").
animal(flatworms) :- is_true("Is the animal live mostly in soil"), is_true("Does animal has flat body").


is_true(Q) :-
        format("~s?\n", [Q]),
        read(yes).