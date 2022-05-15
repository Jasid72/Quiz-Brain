class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.scorce = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if correct_answer.lower() == user_answer.lower():
            self.scorce +=1
            print("This is Right.")
        else:
            print("That's Wrong!")
        print(f"This is Correct Answer: {correct_answer}")
        print(f"Your Scorce is : {self.scorce}/{self.question_number}")