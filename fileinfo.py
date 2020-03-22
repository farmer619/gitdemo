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
l1=[]
l2=[]
def m(x):
    i=0
    for x,y in x.items():
        if i<6:
            l1.append('{}'.format(x))
            l2.append('{}'.format(y))
            i+=1
m(d(b(s)))

l3=[]
for i in range(len(l2)):
    l3.append(int(l2[i]))  


mpl.rcParams['font.sans-serif'] = ['SimHei']
def e():
    global l1
    global l2
    f = Figure(figsize = (5,4), dpi=100)
    m = f.add_subplot(111)
    m.bar(l1,l3,width=1,facecolor='black',edgecolor='white',label='词频最高')
    canvas=FigureCanvasTkAgg(f,master=tk1)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=tkinter.YES)


tk.Button(tk1,text='字数统计',command=f).pack()
tk.Button(tk1,text='查看词频',command=c).pack()
tk.Button(tk1,text='查看原文',command=a).pack()
tk.Button(tk1,text='词频统计表',command=e).pack()


tk1.mainloop()
