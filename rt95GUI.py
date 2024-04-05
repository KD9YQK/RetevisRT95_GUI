import tkinter as tk
import tkinter.font as tkFont

class App:
    cur_freq = "144.520"
    entryText = None
    btnTX = None

    def clear(self):
        self.cur_freq = "144.520"
        self.entryText.set("144.520")

    def freq_shift(self, num):
        split = self.cur_freq.split('.')
        new = split[0][1:]
        new += split[1][:1]
        new += "."
        new += split[1][1:]
        new += str(num)
        return new

    def press(self, num):
        self.cur_freq = self.freq_shift(num)
        self.entryText.set(self.cur_freq)

    def __init__(self, root):
        #setting title
        root.title("Retevis RT95")
        #setting window size
        self.entryText = tk.StringVar()
        width=264
        height=332
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        entryFreq=tk.Entry(root)
        entryFreq["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        entryFreq["font"] = ft
        entryFreq["fg"] = "#333333"
        entryFreq["justify"] = "center"
        entryFreq["textvariable"] = self.entryText
        entryFreq.place(x=24,y=10,width=87,height=30)
        self.entryText.set(self.cur_freq)

        btnClear=tk.Button(root)
        btnClear["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=8)
        btnClear["font"] = ft
        btnClear["fg"] = "#000000"
        btnClear["justify"] = "center"
        btnClear["text"] = "Clear"
        btnClear.place(x=128,y=15,width=40,height=20)
        btnClear["command"] = self.btnClear_command

        btn1=tk.Button(root)
        btn1["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=22)
        btn1["font"] = ft
        btn1["fg"] = "#000000"
        btn1["justify"] = "center"
        btn1["text"] = "1"
        btn1.place(x=10,y=90,width=48,height=48)
        btn1["command"] = self.btn1_command

        btn2=tk.Button(root)
        btn2["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=22)
        btn2["font"] = ft
        btn2["fg"] = "#000000"
        btn2["justify"] = "center"
        btn2["text"] = "2"
        btn2.place(x=70,y=90,width=48,height=48)
        btn2["command"] = self.btn2_command

        btn3=tk.Button(root)
        btn3["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=22)
        btn3["font"] = ft
        btn3["fg"] = "#000000"
        btn3["justify"] = "center"
        btn3["text"] = "3"
        btn3.place(x=130,y=90,width=48,height=48)
        btn3["command"] = self.btn3_command

        self.btnTX=tk.Button(root)
        self.btnTX["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=16)
        self.btnTX["font"] = ft
        self.btnTX["fg"] = "#000000"
        self.btnTX["justify"] = "center"
        self.btnTX["text"] = "Transmit"
        self.btnTX.place(x=10,y=50,width=168,height=30)
        self.btnTX["command"] = self.btnTX_command

        btn4=tk.Button(root)
        btn4["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=22)
        btn4["font"] = ft
        btn4["fg"] = "#000000"
        btn4["justify"] = "center"
        btn4["text"] = "4"
        btn4.place(x=10,y=150,width=48,height=48)
        btn4["command"] = self.btn4_command

        btn5=tk.Button(root)
        btn5["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=22)
        btn5["font"] = ft
        btn5["fg"] = "#000000"
        btn5["justify"] = "center"
        btn5["text"] = "5"
        btn5.place(x=70,y=150,width=48,height=48)
        btn5["command"] = self.btn5_command

        btn6=tk.Button(root)
        btn6["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=22)
        btn6["font"] = ft
        btn6["fg"] = "#000000"
        btn6["justify"] = "center"
        btn6["text"] = "6"
        btn6.place(x=130,y=150,width=48,height=48)
        btn6["command"] = self.btn6_command

        btn7=tk.Button(root)
        btn7["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=22)
        btn7["font"] = ft
        btn7["fg"] = "#000000"
        btn7["justify"] = "center"
        btn7["text"] = "7"
        btn7.place(x=10,y=210,width=48,height=48)
        btn7["command"] = self.btn7_command

        btn8=tk.Button(root)
        btn8["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=22)
        btn8["font"] = ft
        btn8["fg"] = "#000000"
        btn8["justify"] = "center"
        btn8["text"] = "8"
        btn8.place(x=70,y=210,width=48,height=48)
        btn8["command"] = self.btn8_command

        btn9=tk.Button(root)
        btn9["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=22)
        btn9["font"] = ft
        btn9["fg"] = "#000000"
        btn9["justify"] = "center"
        btn9["text"] = "9"
        btn9.place(x=130,y=210,width=48,height=48)
        btn9["command"] = self.btn9_command

        btnStar=tk.Button(root)
        btnStar["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=22)
        btnStar["font"] = ft
        btnStar["fg"] = "#000000"
        btnStar["justify"] = "center"
        btnStar["text"] = "*"
        btnStar.place(x=10,y=270,width=48,height=48)
        btnStar["command"] = self.btnStar_command

        btn0=tk.Button(root)
        btn0["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=22)
        btn0["font"] = ft
        btn0["fg"] = "#000000"
        btn0["justify"] = "center"
        btn0["text"] = "0"
        btn0.place(x=70,y=270,width=48,height=48)
        btn0["command"] = self.btn0_command

        btnPound=tk.Button(root)
        btnPound["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=22)
        btnPound["font"] = ft
        btnPound["fg"] = "#000000"
        btnPound["justify"] = "center"
        btnPound["text"] = "#"
        btnPound.place(x=130,y=270,width=48,height=48)
        btnPound["command"] = self.btnPound_command

        btnUser1=tk.Button(root)
        btnUser1["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=12)
        btnUser1["font"] = ft
        btnUser1["fg"] = "#000000"
        btnUser1["justify"] = "center"
        btnUser1["text"] = "User 1"
        btnUser1.place(x=190,y=90,width=64,height=48)
        btnUser1["command"] = self.btnUser1_command

        btnUser2=tk.Button(root)
        btnUser2["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=12)
        btnUser2["font"] = ft
        btnUser2["fg"] = "#000000"
        btnUser2["justify"] = "center"
        btnUser2["text"] = "User 2"
        btnUser2.place(x=190,y=150,width=64,height=48)
        btnUser2["command"] = self.btnUser2_command

        btnUser3=tk.Button(root)
        btnUser3["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=12)
        btnUser3["font"] = ft
        btnUser3["fg"] = "#000000"
        btnUser3["justify"] = "center"
        btnUser3["text"] = "User 3"
        btnUser3.place(x=190,y=210,width=64,height=48)
        btnUser3["command"] = self.btnUser3_command

        btnUser4=tk.Button(root)
        btnUser4["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=12)
        btnUser4["font"] = ft
        btnUser4["fg"] = "#000000"
        btnUser4["justify"] = "center"
        btnUser4["text"] = "User 4"
        btnUser4.place(x=190,y=270,width=64,height=48)
        btnUser4["command"] = self.btnUser4_command

        btnAB=tk.Button(root)
        btnAB["bg"] = "#ff5722"
        ft = tkFont.Font(family='Times',size=22)
        btnAB["font"] = ft
        btnAB["fg"] = "#000000"
        btnAB["justify"] = "center"
        btnAB["text"] = "A / B"
        btnAB.place(x=190,y=10,width=64,height=64)
        btnAB["command"] = self.btnAB_command

    def btnClear_command(self):
        self.clear()


    def btn1_command(self):
        self.press('1')


    def btn2_command(self):
        self.press('2')


    def btn3_command(self):
        self.press('3')


    def btnTX_command(self):
        print("TX Pressed")
        if self.btnTX["bg"] == "#90ee90":
            self.btnTX["bg"] = "#ff5722"
        else:
            self.btnTX["bg"] = "#90ee90"


    def btn4_command(self):
        self.press('4')


    def btn5_command(self):
        self.press('5')


    def btn6_command(self):
        self.press('6')


    def btn7_command(self):
        self.press('7')


    def btn8_command(self):
        self.press('8')


    def btn9_command(self):
        self.press('9')


    def btnStar_command(self):
        print("* Pressed")


    def btn0_command(self):
        self.press('0')


    def btnPound_command(self):
        print("# Pressed")


    def btnUser1_command(self):
        print("User1 Pressed")


    def btnUser2_command(self):
        print("User2 Pressed")


    def btnUser3_command(self):
        print("User3 Pressed")


    def btnUser4_command(self):
        print("User4 Pressed")


    def btnAB_command(self):
        print("AB Pressed")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
