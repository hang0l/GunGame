import tkinter as tk
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)

KOLICH = 1
NEW_GAME = 0

def quant():
    a = tk.Toplevel()
    a.geometry('+300+300')
    a.overrideredirect(True)
    e = tk.Entry(a)
    e.pack()
    def get():
        global KOLICH, NEW_GAME
        NEW_GAME = 1
        try:
            KOLICH = int(e.get())
        except:
            tk.mb.showerror('Ошибка', 'Введите число')
    tk.Button(a, text = 'OK', command = get).pack()
    tk.Button(a, text = 'Закрыть', command = a.destroy).pack()


menu_quant_of_targets = tk.Menu(root, tearoff = 0)
menu_quant_of_targets.add_command(label = 'Количество мишеней', command = quant)
root.config(menu = menu_quant_of_targets)
