#资料:
# http://www.wb86.com/post/330.html

# https://tkdocs.com/tutorial/text.html

#2022-01-28,22点58
# 现在技术难点已经完全攻破.
#现在解释如下. 道理就是把文字片段的背景色进行修改.(点击界面下面的标注1---5),消除标签点击第一个标注为空按钮
#======这里面我们就标注为B-tag1,I-tag1,E-tag1......B-tag5,....B-tag5即可
#得到BIO文件之后,用户只需要根据自己定好的替换自己需要的标签即可.比如B-PRODUCT...
#解释一下为什么用背景色来区分各个标签.因为我们有时候要标注空格比如尼古拉斯 凯奇.
# 这个名字之间带个空格,那么我们空格也要标注为I-PERSON才行.用前景色无法把空格染色!所以我们用背景色技巧!






from tkinter import *
#=============第一层是text
import tkinter
root = Tk()
# frame = Frame (root, relief=RAISED, borderwidth=20)

text = Text(root, width=100,height=20,font=('宋体',15),wrap = 'none')
text.insert('1.0', '贴入你要处理的文字 中文 English 都行\n贴入你要处理的文字')



#====滚动条竖直:
scroll = tkinter.Scrollbar()
# 放到窗口的右侧, 填充Y竖直方向
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)



#滚动条横向
s2 = Scrollbar(root, orient = HORIZONTAL)
s2.pack(side = BOTTOM, fill = X)

s2.config(command = text.xview)
text.config(xscrollcommand=s2.set)
print( text.get('1.0', 'end'))
text.pack()
# frame.pack()



#第二层是frame 来放按钮的.
frame = Frame (root, relief=RAISED, borderwidth=2)
frame.pack (side=TOP, fill=BOTH, ipadx=5, ipady=5, expand=1)
colorlist=['white','red','yellow','Blue','Cyan','Lime']
def helloCallBack(color):
   print(1111111111111)
   try:
       print(SEL_FIRST,SEL_LAST)
       print(text.index("sel.first"),text.index("sel.last"))
       text.tag_config(color,  background=color)  # 再为标签进行设置
       #===============注意要先删除其他的标签.
       for i in colorlist:
           text.tag_remove( i,text.index("sel.first"), text.index("sel.last"))  # =======变色
       if color !='white':#======white实际上是不进行背景色标注!这样效果最好!!!!!!a trick
            text.tag_add(color, text.index("sel.first"),text.index("sel.last")) #=======变色
       # print(text.tag_ranges(color))


       # print(11111111111)
   except:
       pass
#https://blog.csdn.net/wjciayf/article/details/79261005  颜色表
c0='black'
c1='red'
c2='yellow'
c3='Blue'
c4='Cyan'
c5='Lime'

b=tkinter.Button(frame, text ="标注为空", command = lambda :helloCallBack(colorlist[0]))
b.grid(row=0,column=1,padx=10)

b=tkinter.Button(frame, text ="标注1", command = lambda :helloCallBack(colorlist[1]))
b.grid(row=0,column=2,padx=10)
b=tkinter.Button(frame, text ="标注2", command = lambda :helloCallBack(colorlist[2]))
b.grid(row=0,column=3,padx=10)
b=tkinter.Button(frame, text ="标注3", command = lambda :helloCallBack(colorlist[3]))
b.grid(row=0,column=4,padx=10)
b=tkinter.Button(frame, text ="标注4", command = lambda :helloCallBack(colorlist[4]))
b.grid(row=0,column=5,padx=10)
b=tkinter.Button(frame, text ="标注5", command = lambda :helloCallBack(colorlist[5]))
b.grid(row=0,column=6,padx=10)





def save():
        print("获取文本")
        result = text.get("1.0", "end")  # 获取文本输入框的内容
        for i in colorlist:
            aaa=text.tag_ranges(i)###=得到的aaa标里面每2个表示开头结尾索引.
            print(aaa,i)
        #=======下面都是简单的字符串处理而已
        yuanwen=result.split('\n')
        jieguo=[list('O'*len(i)) for i in yuanwen]
        #=====根据颜色标注即可:
        for dex,i in enumerate(colorlist):
            aaa = text.tag_ranges(i)  ###=得到的aaa标里面每2个表示开头结尾索引.
            for j in range(len(aaa)//2):
                a11= int(aaa[2*j].string.split('.')[0])#首航
                a12= int(aaa[2*j].string.split('.')[1])#首列
                a21= int(aaa[2*j+1].string.split('.')[0])#尾行
                a22= int(aaa[2*j+1].string.split('.')[1])# 尾列
                if a11!=a21:
                    print("bugle !!!!","索引在",a11,a12,a21,a22)
                else:
                    if a22-a12==1:#标注S!
                        jieguo[a11-1][a12]="S-biaoqian"+str(dex)
                    else:
                        jieguo[a11-1][a12:a22]=["B-biaoqian"+str(dex)]+["I-biaoqian"+str(dex)]*(a22-a12-2)+["E-biaoqian"+str(dex)]
        print(jieguo,111111111111111111111111111111111111111111111111111111)
        jieguo=[' '.join(i)+'\n' for i in jieguo]
        print(jieguo)
        with open('output.bio','w') as f:
            f.writelines(jieguo)

















b=tkinter.Button(frame, text ="保存文件为BIO", command = save)
b.grid(row=0,column=7,padx=10)





# b=tkinter.Button(root, text ="标注2", command = helloCallBack(c2))
# b.pack()
# b=tkinter.Button(root, text ="标注3", command = helloCallBack(c3))
# b.pack()
# b=tkinter.Button(root, text ="标注4", command = helloCallBack(c4))
# b.pack()
# b=tkinter.Button(root, text ="标注5", command = helloCallBack(c5))


# text.tag_add('highlightline', '5.0', '6.0')
#
# text.tag_configure('highlightline', background='yellow', font='TkFixedFont', relief='raised')
# text.insert('end','ffffffffff','highlightline')
try:
    print(text.get(SEL_FIRST,SEL_LAST))
except:
    pass













root.mainloop()