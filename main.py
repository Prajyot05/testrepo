import tkinter as tk


def replace_words():
    with open(file="A:/temp/av8trix spnosor drafts/sent/draft balsa.docx",mode ="r",) as file:
        text = file.read()
    modified_text = text.replace(old_company, new_company)
    with open(file = f"A:/temp/av8trix spnosor drafts/sent/New folder/{new_company}", mode ="w",) as file:
        file.write(modified_text)


root = tk.Tk()
root.title("Word Replacer")

# File Path
# file_path_label = tk.Label(root, text="File Path:")
# file_path_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
#
# file_path_entry = tk.Entry(root, width=40)
# file_path_entry.grid(row=0, column=1, padx=10, pady=10)

# browse_button = tk.Button(root, text="Browse", command=browse_file)
# browse_button.grid(row=0, column=2, padx=10, pady=10)

# Old Word
old_word_label = tk.Label(root, text="Old Word:")
old_word_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

old_word_entry = tk.Entry(root, width=40)
old_word_entry.grid(row=1, column=1, padx=10, pady=10)

# New Word
new_word_label = tk.Label(root, text="New Word:")
new_word_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

new_word_entry = tk.Entry(root, width=40)
new_word_entry.grid(row=2, column=1, padx=10, pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3, pady=10)

old_company = old_word_entry.get()
new_company = new_word_entry.get()

# Replace Button
replace_button = tk.Button(root, text="Replace Words", command=replace_words)
replace_button.grid(row=4, column=0, columnspan=3, pady=10)

# Run the Tkinter event loop


root.mainloop()