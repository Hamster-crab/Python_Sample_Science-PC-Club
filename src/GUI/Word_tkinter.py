# 文字を出力させるサンプルコード

import tkinter as tk

root = tk.Tk()
root.geometry("680x450")

label = tk.Label(text="ルービックキューブ")
label["font"] = ("ゴシック",35)

label.pack()

root.mainloop()
