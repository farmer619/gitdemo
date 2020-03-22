#菜鸡fkme的python大作业
#是根本用不了的文本编辑器哦
#一起来试试吧！
import tkinter as tk
import tkinter.messagebox
from pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

tk1=tk.Tk()
tk1.title('fkme的简单文本编辑器')
tk1.geometry('600x400') 

file=open('words example.txt')
text=file.read()
def a():
    tkinter.messagebox.showinfo(title='原文显示',message=text)
text0=text.lower()
text1=text0.split()
word=[]
word1=[]