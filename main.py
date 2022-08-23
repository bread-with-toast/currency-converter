import tkinter
import customtkinter
from currency_converter import CurrencyConverter

root = customtkinter.CTk()
root.geometry("350x350")
converter = CurrencyConverter()
root.set_appearance_mode("dark")

def functionality():
    try:
        if currency2Option.get() == "USD":
            result.configure(text=f"${converter.convert(float(value.get()), currency1Option.get(), currency2Option.get())}", text_color="white")
        elif currency2Option.get() == "EUR":
            result.configure(text=f"€{converter.convert(float(value.get()), currency1Option.get(), currency2Option.get())}", text_color="white")
        else:
            result.configure(text=f"£{converter.convert(float(value.get()), currency1Option.get(), currency2Option.get())}", text_color="white")
    except:
        result.configure(text=f"Could Not Process Your Input", text_color="#ff695e")

frame = customtkinter.CTkFrame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

currency1Option = customtkinter.StringVar(value="USD")
currency2Option = customtkinter.StringVar(value="EUR")

customtkinter.CTkLabel(frame, text="Currency Converter", text_font=("JetBrains Mono", 18)).pack(pady=20)
value = customtkinter.CTkEntry(frame, placeholder_text="First Value", text_font=("JetBrains Mono", 10))
value.pack()

currency1 = customtkinter.CTkComboBox(frame, values=["USD", "EUR", "GBP"], text_font=("JetBrains Mono", 10), variable=currency1Option)
currency1.pack(pady=10)

currency2 = customtkinter.CTkComboBox(frame, values=["USD", "EUR", "GBP"], text_font=("JetBrains Mono", 10), variable=currency2Option)
currency2.pack()

customtkinter.CTkButton(frame, text="Convert Currency", text_font=("JetBrains Mono", 10), fg_color="#f2a8ff", hover_color="#8c5396", text_color="black", command=functionality).pack(pady=20)

result = customtkinter.CTkLabel(frame, text="Result: £0", text_font=("JetBrains Mono", 12))
result.pack()

root.mainloop()