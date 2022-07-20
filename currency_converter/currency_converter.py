import tkinter as tk
from tkinter import ttk
import requests
import os
from dotenv import load_dotenv
load_dotenv()

class CurrencyConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        api_key = os.getenv('API_KEY')
        self.currencies = []
        self.data = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/codes").json()
        for currency in self.data['supported_codes']:
            self.currencies.append(currency[0] + " - " + currency[1])

        self.data = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
        self.rates = self.data['rates']
        self.updated_date = self.data['date']
        
        self.title("Currency Converter")
        self.geometry("250x400")
        self.resizable(False, False)

        self.amount_label = self.display_label("Amount")
        self.amount_entry = self.display_amount_entry()
        self.from_label = self.display_label("FROM")
        self.from_currency_list = self.display_currency_list(self.currencies, 146) #default USD
        self.to_label = self.display_label("TO")
        self.to_currency_list = self.display_currency_list(self.currencies, 12) #default BDT
        self.to_currency_label = self.display_label("BDT")
        self.converted_amount_entry = self.display_converted_amount_entry()
        self.date_label = self.display_label(f"Rates on {self.updated_date}")
        self.convert_btn = self.display_button("Convert", self.convert_currency)

        self.from_currency_list.bind('<<ComboboxSelected>>', lambda event: self.from_currency_changed(event))

    def display_label(self, text):
        label = ttk.Label(self, text=text, font=('Arial', 14, 'bold'))
        label.pack(padx=10, pady=10)
        return label

    def display_amount_entry(self):
        text_entry = ttk.Entry(self, justify='right', font=('Arial', 20, 'bold'))
        text_entry.pack(fill='x', padx=10)
        return text_entry

    def display_currency_list(self, values, default_value_index = 0):
        currency_list = ttk.Combobox(
            self,
            font=('Arial', 16, 'bold'),
        )
        currency_list['values'] = values
        currency_list['state'] = 'readonly'
        currency_list.current(default_value_index)
        currency_list.pack(fill='x', padx=10)
        return currency_list

    def display_converted_amount_entry(self):
        text_entry = ttk.Entry(self, justify='right', font=('Arial', 20, 'bold'))
        text_entry['state'] = 'readonly'
        text_entry.pack(fill='x', padx=10)
        return text_entry

    def display_button(self, text, command):
        btn = ttk.Button(
            self, 
            text=text, 
            command=command
        )
        btn.pack(fill='x', padx=10)
        return btn
    
    def from_currency_changed(self, event):
        currency = self.from_currency_list.get()
        self.data = requests.get(f"https://api.exchangerate-api.com/v4/latest/{currency[0:3]}").json()
        self.rates = self.data['rates']
    
    def convert_currency(self):
        try:
            amount = self.amount_entry.get()
            from_currency = self.from_currency_list.get()
            to_currency = self.to_currency_list.get()
            self.to_currency_label['text'] = to_currency
            self.converted_amount_entry['state'] = 'normal'
            self.converted_amount_entry.delete(0, tk.END)
            self.converted_amount_entry.insert(0, float(amount) * self.rates[to_currency[0:3]])
            self.converted_amount_entry['state'] = 'readonly'
        except:
            print('Error!')

if __name__ == "__main__":
    currency_converter = CurrencyConverter()
    currency_converter.mainloop()