import re
import tkinter as tk
import random
import string


def check_strength(event=None):
    pwd = entry.get()

    if not pwd:
        lbl_result.config(text="Type your password...", fg="#00E5FF")
        return

    if len(pwd) < 8 or not re.search(r"\d", pwd) or not re.search(r"[A-Za-z]", pwd):
        lbl_result.config(text="Weak: Need 8+ chars, letters & numbers", fg="#FF1744")
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd):
        lbl_result.config(text="Medium: Add a special character (!@#)", fg="#FFEA00")
    else:
        lbl_result.config(text="Strong: Password is fully secure! 🔥", fg="#00E676")


def toggle_eye():
    entry.config(show="" if show_var.get() else "*")


def gen_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    new_pwd = "".join(random.choice(chars) for _ in range(12))

    entry.delete(0, tk.END)
    entry.insert(0, new_pwd)
    check_strength()


def on_enter(e):
    btn_gen["background"] = "#FF79C6"


def on_leave(e):
    btn_gen["background"] = "#BD93F9"


app = tk.Tk()
app.title("Neon Password Pro")
app.geometry("450x420")
app.configure(bg="#1E1E2F")

tk.Label(
    app,
    text="✨ Password Analyzer ✨",
    font=("Segoe UI", 20, "bold"),
    bg="#1E1E2F",
    fg="#FF79C6",
).pack(pady=(30, 20))

entry = tk.Entry(
    app,
    font=("Consolas", 15),
    width=24,
    show="*",
    bg="#282A36",
    fg="#F8F8F2",
    insertbackground="white",
    bd=0,
    justify="center",
)
entry.pack(ipady=12, pady=10)
entry.bind("<KeyRelease>", check_strength)

show_var = tk.BooleanVar()
chk = tk.Checkbutton(
    app,
    text="👁️ Show Password",
    variable=show_var,
    command=toggle_eye,
    bg="#1E1E2F",
    fg="#8BE9FD",
    selectcolor="#282A36",
    activebackground="#1E1E2F",
    activeforeground="#8BE9FD",
    font=("Segoe UI", 10, "bold"),
    bd=0,
)
chk.pack(pady=10)

btn_gen = tk.Button(
    app,
    text="🎲 Generate Strong Password",
    font=("Segoe UI", 12, "bold"),
    bg="#BD93F9",
    fg="#282A36",
    activebackground="#FF79C6",
    activeforeground="white",
    bd=0,
    cursor="hand2",
    command=gen_password,
)
btn_gen.pack(ipady=10, ipadx=20, pady=25)

btn_gen.bind("<Enter>", on_enter)
btn_gen.bind("<Leave>", on_leave)

lbl_result = tk.Label(
    app,
    text="Type your password...",
    font=("Segoe UI", 12, "bold"),
    bg="#1E1E2F",
    fg="#00E5FF",
)
lbl_result.pack(pady=10)

if __name__ == "__main__":
    app.mainloop()
