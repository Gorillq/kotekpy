from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import filedialog
import qrcode
import cv2


root = Tk()
root.geometry('220x60')
root.title('QR')
root.resizable(False, False)

def select():
    A1 = simpledialog.askstring("input", "Stwórz", parent=root)
    if A1 is not NONE:
        f = open(r"myqr.txt", 'w')
        f.writelines(A1)
        with open (r"myqr.txt") as f:
            data = f.read()
            img = qrcode.make(data)
            img.save(r"kot.png")
        pass
    
def save_decode():
    filename = filedialog.askopenfilename()
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    g=open(r"youqr.txt" , "w")
    if vertices_array is not NONE:
        g.writelines(data)
        toptb = Toplevel(root)
        toptb.geometry('230x50')
        toptb.title('Done')
        toptb.resizable(False, False)
        msg = "You can check your QRdata at path/youqr.txt"
        K1 = Text(toptb, height=40, width=30)
        K1.pack(expand=True)
        K1.insert("end", msg)
        K1.config(state='disabled')
        pass
    else:
        g.writelines("Error 404")
        pass

def destroy():
    root.destroy()

def nic():
    return

def manual():
    topm = Toplevel(root)
    topm.geometry('210x110')
    topm.title("Manual")
    topm.resizable(False, False)
    msg = "Welk to my first tkinter file. Here you could make your own QRcode or decode current one. Have fun."
    K2 = Text(topm)
    K2.pack(expand=True)
    K2.insert("end", msg)
    K2.config(state='disabled')
    pass

mainframe = ttk.Frame(root, padding="6 6 18 18")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
B1 = ttk.Button(mainframe, command=save_decode, width=10, text='Decode')
B1.grid(column=1, row=1, sticky=N)
B2 = ttk.Button(mainframe, command=select, width=10, text ="Create")
B2.grid(column=2, row=1, sticky=N)
B3 = ttk.Button(mainframe, command=destroy, width=10, text="Quit")
B3.grid(column=3, row=1, sticky=N)
# B4 = ttk.Button(mainframe, command=destroy, width = 10, text="Quit")
# B4.grid(column=2, row=3, sticky=S)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Readme", command=manual)
filemenu.add_separator()
filemenu.add_command(label="Terminate", command=root.quit)
menubar.add_cascade(label="Menu", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
        
        
    