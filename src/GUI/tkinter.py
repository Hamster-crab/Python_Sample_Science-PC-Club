# tkinterはウィンドウにテキストを表示するコードです
# サンプルコード

import tkinter as tk

root = tk.Tk()
root.geometry("680x450")

label = tk.Label(text="ルービックキューブ")
label["font"] = ("ゴシック",35)

label.pack()

root.mainloop()