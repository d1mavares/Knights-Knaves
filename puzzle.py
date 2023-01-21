from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# you are either knight or knave
 # but not both
knowledge0 = And(
        Or(AKnight,AKnave),
        Not(And(AKnight,AKnave))
        )
# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0.add(Implication(AKnight,And(AKnave,AKnight)))
knowledge0.add(Implication(AKnave,Not(And(AKnave,AKnight))))

# Puzzle 1

knowledge1 = And(
        Or(AKnight,AKnave),
        Not(And(AKnight,AKnave)),
        Or(BKnight,BKnave),
        Not(And(BKnight,BKnave))
        )
# A says "We are both knaves."
knowledge1.add(Implication(AKnight,And(AKnave,BKnave)))
knowledge1.add(Implication(AKnave,Not(And(AKnave,BKnave))))
# B says nothing.

# Puzzle 2
knowledge2 = And(
        Or(AKnight,AKnave),
        Not(And(AKnight,AKnave)),
        Or(BKnight,BKnave),
        Not(And(BKnight,BKnave))
)
# A says "We are the same kind."
knowledge2.add(Implication(AKnight,Or(And(AKnight,BKnight),And(AKnave,BKnave))))
knowledge2.add(Implication(AKnave,Or(And(AKnight,BKnave),And(AKnave,BKnight))))
# B says "We are of different kinds."
knowledge2.add(Implication(BKnight,Or(And(AKnight,BKnave),And(AKnave,BKnight))))
knowledge2.add(Implication(BKnave,Or(And(AKnight,BKnight),And(AKnave,BKnave))))
# Puzzle 3
knowledge3 = And(
        Or(AKnight,AKnave),
        Not(And(AKnight,AKnave)),
        Or(BKnight,BKnave),
        Not(And(BKnight,BKnave)),
        Or(CKnight,CKnave),
        Not(And(CKnight,CKnave)),
)

# A says either "I am a knight." or "I am a knave.", but you don't know which.
knowledge3.add(Implication(AKnight,Or(AKnight,AKnave)))
knowledge3.add(Implication(AKnave,Not(Or(AKnight,AKnave))))

# B says "C is a knave."
knowledge3.add(Implication(BKnight,CKnave))
knowledge3.add(Implication(BKnave,CKnight))

# C says "A is a knight."
knowledge3.add(Implication(CKnight,AKnight))
knowledge3.add(Implication(CKnave,CKnave))

# B says "A said 'I am a knave'."
knowledge3.add(Implication(BKnight,Or(And(AKnight,BKnave),And(AKnave,BKnight))))
# If BKnight => If AKnight => BKnave
#            => If AKnave => BKnight
# If BKnave, then A didn't say that, which mean that said otherwise or nothing. No knowledge from this

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
