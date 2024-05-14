import asyncio
import tkinter as tk
import tkinter.font as tkFont

import rt95


class App(tk.Tk):
    VFO1_TXT = "---> VFO 1 <---"
    VFO1_FREQ = "144.000"
    VFO1RX_TXT = ""
    VFO1TX_TXT = ""
    VFO2_TXT = "VFO 2"
    VFO2_FREQ = "144.000"
    VFO2RX_TXT = ""
    VFO2TX_TXT = ""

    def close(self):
        for task in self.tasks:
            task.cancel()
        self.loop.stop()
        self.destroy()

    async def updater(self, interval=1 / 30):
        while True:
            if self.tty.RX_A:
                self.VFO1RX_TXT = "RX"
            else:
                self.VFO1RX_TXT = ""
            if self.tty.RX_B:
                self.VFO2RX_TXT = "RX"
            else:
                self.VFO2RX_TXT = ""
            if self.tty.TX_A:
                self.VFO1TX_TXT = "TX"
            else:
                self.VFO1TX_TXT = ""
            if self.tty.TX_B:
                self.VFO2TX_TXT = "TX"
            else:
                self.VFO2TX_TXT = ""
            if self.tty.VFO == 'A':
                self.VFO1_TXT = "---> VFO 1 <---"
                self.VFO2_TXT = "VFO 2"
            else:
                self.VFO1_TXT = "VFO 1"
                self.VFO2_TXT = "---> VFO 2 <---"

            self.update()
            await asyncio.sleep(interval)

    def __init__(self, async_loop, com_device="/dev/ttyUSB0", freq="144.520"):
        super().__init__()
        self.VFO1_FREQ = freq
        self.VFO2_FREQ = freq

        # setting title
        self.title("RT95")
        self.protocol("WM_DELETE_WINDOW", self.close)

        self.tty = rt95.RT95(com_device)

        self.loop = async_loop
        self.tasks = []
        self.tasks.append(loop.create_task(self.tty.main_loop()))
        self.tasks.append(loop.create_task(self.updater()))

        # -------------Build Window-----------------------------
        # setting window size
        width = 200
        height = 310
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        lblVFO1 = tk.Label(self)
        lblVFO1["bg"] = "#393d49"
        ft = tkFont.Font(family='Times', size=26)
        lblVFO1["font"] = ft
        lblVFO1["fg"] = "#90ee90"
        lblVFO1["justify"] = "right"
        lblVFO1["text"] = self.VFO1_FREQ
        lblVFO1.place(x=0, y=20, width=200, height=40)

        lblVFO2 = tk.Label(self)
        lblVFO2["bg"] = "#393d49"
        ft = tkFont.Font(family='Times', size=26)
        lblVFO2["font"] = ft
        lblVFO2["fg"] = "#90ee90"
        lblVFO2["justify"] = "right"
        lblVFO2["text"] = self.VFO2_FREQ
        lblVFO2.place(x=0, y=80, width=200, height=40)

        btnKEY1 = tk.Button(self)
        btnKEY1["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times', size=22)
        btnKEY1["font"] = ft
        btnKEY1["fg"] = "#000000"
        btnKEY1["justify"] = "center"
        btnKEY1["text"] = "1"
        btnKEY1.place(x=0, y=120, width=40, height=40)
        btnKEY1["command"] = self.btnKEY1_command

        btnKEY2 = tk.Button(self)
        btnKEY2["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times', size=22)
        btnKEY2["font"] = ft
        btnKEY2["fg"] = "#000000"
        btnKEY2["justify"] = "center"
        btnKEY2["text"] = "2"
        btnKEY2.place(x=40, y=120, width=40, height=40)
        btnKEY2["command"] = self.btnKEY2_command

        btnKEY3 = tk.Button(self)
        btnKEY3["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times', size=22)
        btnKEY3["font"] = ft
        btnKEY3["fg"] = "#000000"
        btnKEY3["justify"] = "center"
        btnKEY3["text"] = "3"
        btnKEY3.place(x=80, y=120, width=40, height=40)
        btnKEY3["command"] = self.btnKEY3_command

        btnKEY4 = tk.Button(self)
        btnKEY4["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times', size=22)
        btnKEY4["font"] = ft
        btnKEY4["fg"] = "#000000"
        btnKEY4["justify"] = "center"
        btnKEY4["text"] = "4"
        btnKEY4.place(x=0, y=160, width=40, height=40)
        btnKEY4["command"] = self.btnKEY4_command

        btnKEY5 = tk.Button(self)
        btnKEY5["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times', size=22)
        btnKEY5["font"] = ft
        btnKEY5["fg"] = "#000000"
        btnKEY5["justify"] = "center"
        btnKEY5["text"] = "5"
        btnKEY5.place(x=40, y=160, width=40, height=40)
        btnKEY5["command"] = self.btnKEY5_command

        btnKEY6 = tk.Button(self)
        btnKEY6["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times', size=22)
        btnKEY6["font"] = ft
        btnKEY6["fg"] = "#000000"
        btnKEY6["justify"] = "center"
        btnKEY6["text"] = "6"
        btnKEY6.place(x=80, y=160, width=40, height=40)
        btnKEY6["command"] = self.btnKEY6_command

        btnKEY7 = tk.Button(self)
        btnKEY7["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times', size=22)
        btnKEY7["font"] = ft
        btnKEY7["fg"] = "#000000"
        btnKEY7["justify"] = "center"
        btnKEY7["text"] = "7"
        btnKEY7.place(x=0, y=200, width=40, height=40)
        btnKEY7["command"] = self.btnKEY7_command

        btnKEY8 = tk.Button(self)
        btnKEY8["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times', size=22)
        btnKEY8["font"] = ft
        btnKEY8["fg"] = "#000000"
        btnKEY8["justify"] = "center"
        btnKEY8["text"] = "8"
        btnKEY8.place(x=40, y=200, width=40, height=40)
        btnKEY8["command"] = self.btnKEY8_command

        btnKEY9 = tk.Button(self)
        btnKEY9["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times', size=22)
        btnKEY9["font"] = ft
        btnKEY9["fg"] = "#000000"
        btnKEY9["justify"] = "center"
        btnKEY9["text"] = "9"
        btnKEY9.place(x=80, y=200, width=40, height=40)
        btnKEY9["command"] = self.btnKEY9_command

        btnKEYstar = tk.Button(self)
        btnKEYstar["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times', size=22)
        btnKEYstar["font"] = ft
        btnKEYstar["fg"] = "#000000"
        btnKEYstar["justify"] = "center"
        btnKEYstar["text"] = "*"
        btnKEYstar.place(x=0, y=240, width=40, height=40)
        btnKEYstar["command"] = self.btnKEYstar_command

        btnKEY0 = tk.Button(self)
        btnKEY0["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times', size=22)
        btnKEY0["font"] = ft
        btnKEY0["fg"] = "#000000"
        btnKEY0["justify"] = "center"
        btnKEY0["text"] = "0"
        btnKEY0.place(x=40, y=240, width=40, height=40)
        btnKEY0["command"] = self.btnKEY0_command

        btnKEYpound = tk.Button(self)
        btnKEYpound["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times', size=22)
        btnKEYpound["font"] = ft
        btnKEYpound["fg"] = "#000000"
        btnKEYpound["justify"] = "center"
        btnKEYpound["text"] = "#"
        btnKEYpound.place(x=80, y=240, width=40, height=40)
        btnKEYpound["command"] = self.btnKEYpound_command

        btnUSER1 = tk.Button(self)
        btnUSER1["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=14)
        btnUSER1["font"] = ft
        btnUSER1["fg"] = "#000000"
        btnUSER1["justify"] = "center"
        btnUSER1["text"] = "User 1"
        btnUSER1.place(x=120, y=120, width=80, height=30)
        btnUSER1["command"] = self.btnUSER1_command

        btnUSER2 = tk.Button(self)
        btnUSER2["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=14)
        btnUSER2["font"] = ft
        btnUSER2["fg"] = "#000000"
        btnUSER2["justify"] = "center"
        btnUSER2["text"] = "User 2"
        btnUSER2.place(x=120, y=150, width=80, height=30)
        btnUSER2["command"] = self.btnUSER2_command

        btnUSER3 = tk.Button(self)
        btnUSER3["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=14)
        btnUSER3["font"] = ft
        btnUSER3["fg"] = "#000000"
        btnUSER3["justify"] = "center"
        btnUSER3["text"] = "User 3"
        btnUSER3.place(x=120, y=180, width=80, height=30)
        btnUSER3["command"] = self.btnUSER3_command

        btnUSER4 = tk.Button(self)
        btnUSER4["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=14)
        btnUSER4["font"] = ft
        btnUSER4["fg"] = "#000000"
        btnUSER4["justify"] = "center"
        btnUSER4["text"] = "User 4"
        btnUSER4.place(x=120, y=210, width=80, height=30)
        btnUSER4["command"] = self.btnUSER4_command

        btnAB = tk.Button(self)
        btnAB["bg"] = "#ff5722"
        ft = tkFont.Font(family='Times', size=30)
        btnAB["font"] = ft
        btnAB["fg"] = "#000000"
        btnAB["justify"] = "center"
        btnAB["text"] = "A/B"
        btnAB.place(x=120, y=240, width=80, height=40)
        btnAB["command"] = self.btnAB_command

        lblVFO1RX = tk.Label(self)
        ft = tkFont.Font(family='Times', size=12)
        lblVFO1RX["bg"] = "#393d49"
        lblVFO1RX["font"] = ft
        lblVFO1RX["fg"] = "#cc0000"
        lblVFO1RX["justify"] = "center"
        lblVFO1RX["text"] = self.VFO1RX_TXT
        lblVFO1RX.place(x=0, y=20, width=32, height=20)

        lblVFO1TX = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        lblVFO1TX["bg"] = "#393d49"
        lblVFO1TX["font"] = ft
        lblVFO1TX["fg"] = "#90ee90"
        lblVFO1TX["justify"] = "center"
        lblVFO1TX["text"] = self.VFO1TX_TXT
        lblVFO1TX.place(x=0, y=40, width=32, height=20)

        lblVFO2RX = tk.Label(self)
        ft = tkFont.Font(family='Times', size=12)
        lblVFO2RX["bg"] = "#393d49"
        lblVFO2RX["font"] = ft
        lblVFO2RX["fg"] = "#cc0000"
        lblVFO2RX["justify"] = "center"
        lblVFO2RX["text"] = self.VFO2RX_TXT
        lblVFO2RX.place(x=0, y=80, width=32, height=20)

        lblVFO2TX = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        lblVFO2TX["bg"] = "#393d49"
        lblVFO2TX["font"] = ft
        lblVFO2TX["fg"] = "#90ee90"
        lblVFO2TX["justify"] = "center"
        lblVFO2TX["text"] = self.VFO2TX_TXT
        lblVFO2TX.place(x=0, y=100, width=32, height=20)

        lblVFO1name = tk.Label(self)
        lblVFO1name["bg"] = "#393d49"
        ft = tkFont.Font(family='Times', size=12)
        lblVFO1name["font"] = ft
        lblVFO1name["fg"] = "#ffffff"
        lblVFO1name["justify"] = "center"
        lblVFO1name["text"] = self.VFO1_TXT
        lblVFO1name.place(x=0, y=0, width=200, height=20)

        lblVFO2name = tk.Label(self)
        lblVFO2name["bg"] = "#393d49"
        ft = tkFont.Font(family='Times', size=12)
        lblVFO2name["font"] = ft
        lblVFO2name["fg"] = "#ffffff"
        lblVFO2name["justify"] = "center"
        lblVFO2name["text"] = self.VFO2_TXT
        lblVFO2name.place(x=0, y=60, width=200, height=20)

        btnTX = tk.Button(self)
        btnTX["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times', size=10)
        btnTX["font"] = ft
        btnTX["fg"] = "#000000"
        btnTX["justify"] = "center"
        btnTX["text"] = "Transmit"
        btnTX.place(x=0, y=280, width=200, height=35)
        btnTX["command"] = self.btnTX_command

    def btnKEY1_command(self):
        self.tty.send_single("1")

    def btnKEY2_command(self):
        self.tty.send_single("2")

    def btnKEY3_command(self):
        self.tty.send_single("3")

    def btnKEY4_command(self):
        self.tty.send_single("4")

    def btnKEY5_command(self):
        self.tty.send_single("5")

    def btnKEY6_command(self):
        self.tty.send_single("6")

    def btnKEY7_command(self):
        self.tty.send_single("7")

    def btnKEY8_command(self):
        self.tty.send_single("8")

    def btnKEY9_command(self):
        self.tty.send_single("9")

    def btnKEYstar_command(self):
        self.tty.send_single("*")

    def btnKEY0_command(self):
        self.tty.send_single("0")

    def btnKEYpound_command(self):
        self.tty.send_single("#")

    def btnUSER1_command(self):
        self.tty.send_single("User1")

    def btnUSER2_command(self):
        self.tty.send_single("User2")

    def btnUSER3_command(self):
        self.tty.send_single("User3")

    def btnUSER4_command(self):
        self.tty.send_single("User4")

    def btnAB_command(self):
        self.tty.send_single("AB")

    def btnTX_command(self):
        self.tty.setRTS(not self.tty.isRTS)


if __name__ == "__main__":
    import argparse
    # create a parser
    parser = argparse.ArgumentParser()
    # -----------Parser Arguments -----------------------
    # Without a '-' it is a must have
    # parser.add_argument('keypresses', help='A string of keypresses', type=str)
    # With a '-' it is optional
    parser.add_argument('-d', '--device', help='Set the device. Default is "/dev/ttyUSB0"',
                        type=str, default='/dev/ttyUSB0')
    parser.add_argument('-1', '--vfo1', help='Set the starting frequency for VFO 1. Default is "144.000"',
                        type=str, default='144.000')
    parser.add_argument('-2', '--vfo2', help='Set the starting frequency for VFO 2. Default is "435.000"',
                        type=str, default='435.000')
    # -------------- End Arguments -----------------------
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    app = App(loop, com_device=args.device, freq=args.freq)
    loop.run_forever()
    loop.close()
