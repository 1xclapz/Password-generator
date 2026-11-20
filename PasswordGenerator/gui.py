import customtkinter as ctk
from Password import generate_password

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class PasswordApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("420x360")
        self.resizable(False, False)

        # Title
        ctk.CTkLabel(self, text="Password Generator",
                     font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(20, 10))

        # Password display
        self.password_entry = ctk.CTkEntry(self, width=340, height=40,
                                           font=ctk.CTkFont(size=16), justify="center")
        self.password_entry.pack(pady=10)

        # Length slider
        self.length_label = ctk.CTkLabel(self, text="Length: 16")
        self.length_label.pack()
        self.length_slider = ctk.CTkSlider(self, from_=6, to=40, number_of_steps=34,
                                           command=self.on_slide)
        self.length_slider.set(16)
        self.length_slider.pack(pady=5, padx=40, fill="x")

        # Options
        self.digits_box = ctk.CTkCheckBox(self, text="Include numbers")
        self.digits_box.select()
        self.digits_box.pack(pady=5)

        self.symbols_box = ctk.CTkCheckBox(self, text="Include symbols")
        self.symbols_box.select()
        self.symbols_box.pack(pady=5)

        # Buttons
        button_row = ctk.CTkFrame(self, fg_color="transparent")
        button_row.pack(pady=15)
        ctk.CTkButton(button_row, text="Generate", command=self.make_password).pack(side="left", padx=5)
        self.copy_button = ctk.CTkButton(button_row, text="Copy", command=self.copy_password)
        self.copy_button.pack(side="left", padx=5)

        self.make_password()

    def on_slide(self, value):
        self.length_label.configure(text=f"Length: {int(value)}")

    def make_password(self):
        password = generate_password(
            int(self.length_slider.get()),
            use_digits=self.digits_box.get() == 1,
            use_symbols=self.symbols_box.get() == 1,
        )
        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, password)
        self.copy_button.configure(text="Copy")

    def copy_password(self):
        self.clipboard_clear()
        self.clipboard_append(self.password_entry.get())
        self.copy_button.configure(text="Copied!")


if __name__ == "__main__":
    app = PasswordApp()
    app.mainloop()