import tkinter as tk
from random import choice

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("угадай фрукт!")
        
        self.word_to_guess = choice(['яблоко', 'груша', 'апельсин', 'банан', 'киви'])
        self.guess_word = ['_'] * len(self.word_to_guess)
        self.attempts_left = 6
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.label_word = tk.Label(self.master, text=' '.join(self.guess_word), font=('Helvetica', 16))
        self.label_word.pack(pady=10)

        self.label_attempts = tk.Label(self.master, text=f'Попыток осталось: {self.attempts_left}', font=('Helvetica', 12))
        self.label_attempts.pack()

        self.label_score = tk.Label(self.master, text=f'Баллы: {self.score}', font=('Helvetica', 12))
        self.label_score.pack()

        self.entry_letter = tk.Entry(self.master, width=5, font=('Helvetica', 12))
        self.entry_letter.pack(pady=10)

        self.button_guess = tk.Button(self.master, text='Угадать', command=self.guess_letter)
        self.button_guess.pack()

    def guess_letter(self):
        letter = self.entry_letter.get().lower()
        self.entry_letter.delete(0, tk.END)

        if letter.isalpha() and len(letter) == 1:
            if letter in self.word_to_guess:
                for i in range(len(self.word_to_guess)):
                    if self.word_to_guess[i] == letter:
                        self.guess_word[i] = letter
                self.label_word.config(text=' '.join(self.guess_word))
                self.score += 1
                self.label_score.config(text=f'Баллы: {self.score}')
            else:
                self.attempts_left -= 1
                self.label_attempts.config(text=f'Попыток осталось: {self.attempts_left}')

            if '_' not in self.guess_word:
                self.end_game("Поздравляем! Вы угадали слово.")
            elif self.attempts_left == 0:
                self.end_game("Игра окончена. Вы проиграли. Правильное слово: " + self.word_to_guess)
        else:
            self.label_attempts.config(text='Введите одну букву.')

    def end_game(self, message):
        self.label_attempts.config(text=message)
        self.button_guess.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()

