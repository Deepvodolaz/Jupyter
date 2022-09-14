import tkinter as tk
import requests
import xmltodict

window=tk.Tk()
window.geometry("800x650")
window.title("Программа просмотра курсов валют")

# Создание текстового вывода с прокруткой
output_text = st(height = 25, width = 70)
output_text.grid(row=3, column=1, padx=10, pady=10, sticky="w")


url = "http://www.cbr.ru/scripts/XML_daily.asp"
response = requests.get(url)
data = xmltodict.parse(response.content)
# ~ print (data)

my_array =[]
for item in data['ValCurs']['Valute']:
    my_set = [item['CharCode'], item['Name'], item['Value']]
    my_array.append(my_set)
    print(my_set)
    

window.mainloop()
