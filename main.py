import tkinter as tk

def calculate_grade():
    total = 0
    for entry in entry_fields:
    
        result = int(entry.get())
        total += result
    average = int(total / len(subjects))

    if 0 <= average <= 40:
        grade_label.config(text=f"Average:{average} Grade: F")
    elif 41 <= average <= 60:
        grade_label.config(text=f"Average:{average} Grade: D")
    elif 61 <= average <= 70:
        grade_label.config(text=f"Average:{average} Grade: C")
    elif 71 <= average <= 80:
        grade_label.config(text=f"Average:{average} Grade: B")
    elif 81 <= average <= 90:
        grade_label.config(text=f"Average:{average} Grade: A")
    elif 91 <= average <= 100:
        grade_label.config(text=f"Average:{average} Grade: A+")


root = tk.Tk()
root.title("GPA Calculator")

subjects = ["Bangla", "English", "Math", "Science"]


entry_fields = []
for subject in subjects:
    label = tk.Label(root, text=f"Enter Number for {subject} subject:")
    label.pack()
    entry = tk.Entry(root, width=10)
    entry.pack()
    entry_fields.append(entry)


calculate_button = tk.Button(root, text="Calculate GPA", command=calculate_grade)
calculate_button.pack()



grade_label = tk.Label(root, text="")
grade_label.pack()
root.mainloop()
