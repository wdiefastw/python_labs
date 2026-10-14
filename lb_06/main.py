import tkinter as tk
import student_utils

def form_report():
    value = count_entry.get().strip()
    
    if not value.isdecimal():
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, "Помилка: Введіть ціле число від 1 до 20")
        return
        
    count = int(value)
    if count < 1 or count > 20:
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, "Помилка: Кількість має бути в діапазоні 1–20")
        return
        
    students = ["Anna", "Ivan", "Olha"]
    report_lines = []
    
    #
    for student in students:
        grades = student_utils.generate_grades(count)
        avg = student_utils.average_grade(grades)
        level = student_utils.get_level(avg)
        
        line = f"{student}: {grades} → {round(avg, 2)} → {level}"
        report_lines.append(line)
        
    full_report = "\n".join(report_lines)
    
    print("\n--- Сформований звіт ---")
    print(full_report)
    
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, full_report)

window = tk.Tk()
window.title("Статистика учнів")
window.geometry("500x350")

tk.Label(window, text="Введіть кількість оцінок (1–20):").pack(pady=5)

count_entry = tk.Entry(window, width=15)
count_entry.pack(pady=5)

tk.Button(window, text="Сформувати звіт", command=form_report).pack(pady=10)

text_widget = tk.Text(window, height=10, width=55)
text_widget.pack(pady=10)

window.mainloop()
