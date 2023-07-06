import json
import tkinter as tk
from tkinter import messagebox

class DictionaryApp:
    def __init__(self):
        self.dictionary = self.load_dictionary()
        self.window = tk.Tk()
        self.window.title("Dictionary App")
        self.home_frame = None
        self.current_frame = None
        self.create_home_frame()

    def load_dictionary(self):
        try:
            with open('dictionary.json') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_dictionary(self):
        with open('dictionary.json', 'w') as file:
            json.dump(self.dictionary, file)

    def create_home_frame(self):
        self.home_frame = tk.Frame(self.window)
        self.home_frame.pack(pady=10)
        add_button = tk.Button(self.home_frame, text="Add Word", command=self.create_add_frame)
        add_button.pack(pady=10)
        search_button = tk.Button(self.home_frame, text="Search Word", command=self.create_search_frame)
        search_button.pack(pady=10)
        list_button = tk.Button(self.home_frame, text="List Words", command=self.create_list_frame)
        list_button.pack(pady=10)
        save_button = tk.Button(self.home_frame, text="Save & Exit", command=self.save_and_exit)
        save_button.pack(pady=10)

    def create_add_frame(self):
        self.home_frame.pack_forget()
        self.current_frame = tk.Frame(self.window)
        self.current_frame.pack(pady=10)
        word_label = tk.Label(self.current_frame, text="Word:")
        word_label.grid(row=0, column=0)
        word_entry = tk.Entry(self.current_frame)
        word_entry.grid(row=0, column=1)
        meaning_label = tk.Label(self.current_frame, text="Meaning:")
        meaning_label.grid(row=1, column=0)
        meaning_entry = tk.Entry(self.current_frame)
        meaning_entry.grid(row=1, column=1)
        add_button = tk.Button(self.current_frame, text="Add Word", command=lambda: self.add_word(word_entry.get(), meaning_entry.get()))
        add_button.grid(row=2, column=0, columnspan=2)
        back_button = tk.Button(self.current_frame, text="Back", command=self.go_back)
        back_button.grid(row=3, column=0, columnspan=2)

    def create_search_frame(self):
        self.home_frame.pack_forget()
        self.current_frame = tk.Frame(self.window)
        self.current_frame.pack(pady=10)
        search_label = tk.Label(self.current_frame, text="Search Word:")
        search_label.grid(row=0, column=0)
        search_entry = tk.Entry(self.current_frame)
        search_entry.grid(row=0, column=1)
        search_button = tk.Button(self.current_frame, text="Search", command=lambda: self.search_word(search_entry.get()))
        search_button.grid(row=1, column=0, columnspan=2)
        back_button = tk.Button(self.current_frame, text="Back", command=self.go_back)
        back_button.grid(row=2, column=0, columnspan=2)

    def create_list_frame(self):
        self.home_frame.pack_forget()
        self.current_frame = tk.Frame(self.window)
        self.current_frame.pack(pady=10)
        list_box = tk.Listbox(self.current_frame)
        list_box.pack(pady=10)
        for word in self.dictionary:
            list_box.insert(tk.END, word)
        back_button = tk.Button(self.current_frame, text="Back", command=self.go_back)
        back_button.pack(pady=10)

    def go_back(self):
        self.current_frame.pack_forget()
        self.home_frame.pack()

    def add_word(self, word, meaning):
        self.dictionary[word] = meaning
        messagebox.showinfo("Success", "Word added successfully!")

    def search_word(self, word):
        if word in self.dictionary:
            messagebox.showinfo("Meaning", self.dictionary[word])
        else:
            messagebox.showinfo("Word not found", "Word not found in the dictionary.")

    def save_and_exit(self):
        self.save_dictionary()
        messagebox.showinfo("Dictionary saved", "Dictionary saved successfully. Exiting...")
        self.window.quit()

    def run(self):
        self.window.mainloop()
        self.save_dictionary()

if __name__ == "__main__":
    app = DictionaryApp()
    app.run()
