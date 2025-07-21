from app import operator

question_prompts = [
    "What color are apples?\n(a)Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    operator(question_prompts[0], "a"),
    operator(question_prompts[1], "c"),
    operator(question_prompts[2], "b")
]

def run(question):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score} / {str(len(questions))} corrects")


run(questions)