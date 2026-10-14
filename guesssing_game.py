import random

questions = [
    ("whats the capital of france?", "Paris"),
    ("who's the GOAT in football?", "Ronaldo"),
    ("who is the richest man on earth", "Elon Musk"),
    ("whats the hardest substance on earth", "Diamond"),
    ("best phone brand? ", "Samsung"),
    ]
random.shuffle(questions)
score = 0

for question, correct_answer in questions:
    collected_answer = input(question + ": ").strip()
    if collected_answer == "":
        print("youve skipped that one")
        continue
    if collected_answer.lower() == "quit":
        print("youve quit!")
        break
    if collected_answer.lower() == correct_answer.lower():
        print("thats correct!")
        score += 1
    else:
        print(f"as expected from you, wrong again tsk tsk tsk, the answer was {correct_answer}")
print(f"final score is {score} out of {len(questions)}")