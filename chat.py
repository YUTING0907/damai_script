'''
import openai

# 输入你的 api_key
chat_gpt_key = 'XXXXXXX'
# 将 Key 进行传入
openai.api_key = chat_gpt_key

def completion(prompt):
    response = openai.Completion.create(
        # text-davinci-003 是指它的模型
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None
    )
    message = response.choices[0].text
    return message

print(completion(input("在这里输入你想对chatgpt说的话，然后它就会给出答案：")))
'''

import openai

import os, sys
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *


class AppUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('My ChatGPT vx:yhd13950307060')
        self.master.geometry('900x500')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Tftitle.TLabelframe', font=('黑体', 12))
        self.style.configure('Tftitle.TLabelframe.Label', font=('黑体', 12))

        self.ftitle = LabelFrame(self.top, text='', style='Tftitle.TLabelframe')
        self.ftitle.place(relx=0.008, rely=0.017, relwidth=0.982, relheight=0.998)

        self.stext = Text(self.ftitle, font=('黑体', 12), wrap=NONE, )
        self.stext.place(relx=0.017, rely=0.036, relwidth=0.957, relheight=0.412)

        # 垂直滚动条
        self.VScroll1 = Scrollbar(self.stext, orient='vertical')
        self.VScroll1.pack(side=RIGHT, fill=Y)
        self.VScroll1.config(command=self.stext.yview)
        self.stext.config(yscrollcommand=self.VScroll1.set)
        # 水平滚动条
        self.stextxscroll = Scrollbar(self.stext, orient=HORIZONTAL)
        self.stextxscroll.pack(side=BOTTOM, fill=X)
        self.stextxscroll.config(command=self.stext.xview)
        self.stext.config(xscrollcommand=self.stextxscroll.set)

        self.totext = Text(self.ftitle, font=('黑体', 12), wrap=NONE)
        self.totext.place(relx=0.017, rely=0.552, relwidth=0.957, relheight=0.412)

        self.VScroll2 = Scrollbar(self.totext, orient='vertical')
        self.VScroll2.pack(side=RIGHT, fill=Y)
        # 将滚动条与文本框关联
        self.VScroll2.config(command=self.totext.yview)
        self.totext.config(yscrollcommand=self.VScroll2.set)
        # 水平滚动条
        self.totextxscroll = Scrollbar(self.totext, orient=HORIZONTAL)
        self.totextxscroll.pack(side=BOTTOM, fill=X)
        self.totextxscroll.config(command=self.totext.xview)
        self.totext.config(xscrollcommand=self.totextxscroll.set)

        menubar = Menu(self.top, tearoff=False)  # 创建一个菜单
        self.style.configure('Tcleartext.TButton', font=('黑体', 12))
        self.cleartext = Button(self.ftitle, text='清空', command=self.cleartext_Cmd, style='Tcleartext.TButton')
        self.cleartext.place(relx=0.239, rely=0.463, relwidth=0.086, relheight=0.073)

        self.style.configure('Taddyh.TButton', font=('黑体', 12))
        self.addyh = Button(self.ftitle, text='查询', command=self.addyh_Cmd,
                            style='Taddyh.TButton')
        self.addyh.place(relx=0.512, rely=0.463, relwidth=0.2, relheight=0.073)


class App(AppUI):
    def __init__(self, master=None):
        AppUI.__init__(self, master)

    def cleartext_Cmd(self, event=None):
        self.stext.delete(1.0, "end")
        self.totext.delete(1.0, "end")

    def addyh_Cmd(self, event=None):
        cookiestext = self.stext.get(1.0, "end")
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=cookiestext,
            max_tokens=1024,
            n=1,
            temperature=0.5,
        )
        answer = (response["choices"][0]["text"]).split(".")
        for i in answer:
            self.totext.insert(1.0, i)

            self.totext.update()


if __name__ == "__main__":
    # 输入你的 api_key
    chat_gpt_key = 'xxxx'
    # 将 Key 进行传入
    openai.api_key = chat_gpt_key
    top = Tk()
    App(top).mainloop()
