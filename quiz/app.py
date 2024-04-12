# Quiz app using Python and Tkinter
# Create only for educational purpose
# date: 2024-4-11
# Created by @ostadsgo

import tkinter as tk
from tkinter import ttk

import questions


class QuizFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.question_index = 0
        self.score_board = []
        self.user_choice = tk.IntVar()

        self.question_lable = ttk.Label(self)
        self.opt_frame = ttk.Frame(self)
        self.next_button = ttk.Button(self, text="Next")
        self.prev_button = ttk.Button(self, text="Prev")
        self.next_button.grid(row=5, column=1, sticky="e")
        self.prev_button.grid(row=5, column=0, sticky="w")
        
        self.opt_frame.grid(row=1, column=0)

        self.next_button.config(command=self.next_question)
        # self.prev_button.config(command=self.prev_question)
        # self.check_prev()

    def check_prev(self):
        """hide prev button if question_index is 1
        in this case there is no previous question."""

        if self.question_index <= 0:
            self.prev_button.grid_forget()
        else:
            self.prev_button.grid(row=5, column=0, sticky="w")

    def get_quiz(self):
        quiz = questions.all_questions[self.question_index]
        question = quiz.get("question")
        options = quiz.get("options")

        return question, options

    def create_question(self, text):
        self.question_label = ttk.Label(
            self, text=text, font=("Noto Sans", 16, "normal")
        )
        self.question_label.grid(row=0, column=0)

    def create_options(self, options):
        for row_index, option in enumerate(options, 1):
            ttk.Radiobutton(
                self.opt_frame, text=option, value=row_index, variable=self.user_choice
            ).grid(row=row_index, column=0, sticky="w")

    def check_answer(self):
        user_answer = self.user_choice.get()
        correct_answer = questions.all_questions[self.question_index].get("answer")
        if user_answer == correct_answer:
            self.score_board.append(f"question {self.question_index}: correct")
        else:
            self.score_board.append(f"question {self.question_index}: incorrect")

        # Rest radio button
        self.user_choice.set(0)

    # Next question
    def next_question(self):
        self.check_prev()
        question, options = self.get_quiz()

        # create question and options
        self.create_question(question)
        self.create_options(options)
        self.check_answer()

        # if reach last question.
        if self.question_index == len(questions.all_questions) - 1:
            self.next_button.config(text="Show result", command=self.show_result)
            return

        self.question_index += 1

    # Previous question function
    def prev_question(self):
        self.check_prev()
        self.question_index -= 1
        question, options = self.get_quiz()

        # question text
        self.question_label = ttk.Label(
            self, text=question, font=("Noto Sans", 16, "normal")
        ).grid(row=0, column=0)

        # question options
        opt_frame = ttk.Frame(self)
        opt_frame.grid(row=1, column=0, stick="wsen")
        for opt in options:
            ttk.Radiobutton(opt_frame, text=opt).pack(fill="both", expand=True)

    def show_result(self):
        print(self.score_board)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz App")
        quiz = QuizFrame(self)
        quiz.pack(expand=True, fill="both")
        quiz.next_question()


if __name__ == "__main__":
    app = App()
    app.mainloop()
