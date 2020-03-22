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

def wenben():
    global word
    for i in text1:
        i=i.replace(',','')
        i=i.replace('.','')
        i=i.replace('!','')
        i=i.strip()
        x=i.split(' ')
        word.extend(x)
    return word

t=len(wenben())

def f(): 
    k=str('全文字数为:'+str(t)+'词')
    tkinter.messagebox.showinfo(title='字数统计',message=k)

tc=['a','is','to','do','am','are','than','it','the','an','that','be','in','on'\
    ,'at','so','by','this','these','and','but','of','for','he','two']
s=[]#去掉停用词后的词，用于词频统计
for i in word:
    if i not in tc:
        s.append(i)

def b(x):
	key0={}
	key0=key0.fromkeys(x)
	word1=list(key0.keys())
	for i in word1:
		key0[i]=x.count(i)
	return key0

def c():
    global s
    C=b(s)
    tkinter.messagebox.showinfo(title='词频统计',message=C)
    
def d(x):
	key1={}
	key1=sorted(x.items(),key=lambda d:d[1],reverse=True)
	key1=dict(key1)
	return key1
