import PIL as p
from PIL import ImageTk
from tkinter import filedialog
import cv2
from pathlib import Path
from tkinter import *
import pandas as pd
import real_face_reco
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def scan_image():
    global path
    videoCaptureObject = cv2.VideoCapture(1)
    result = True
    while (result):
        ret, frame = videoCaptureObject.read()
        txt="Press q for capture image"
        cv2.putText(frame,txt,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)

        cv2.imshow("Scan Image",frame)
        path="./employ_img/"+id.get()+".jpg"
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            cv2.imwrite(path, frame)
            break

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def submit():
    image=path
    id_val=id.get()
    name_val = name.get()
    email_val = email.get()
    new_row=pd.Series([id_val,name_val,email_val,image])
    df=pd.DataFrame([new_row])
    df.to_csv('./data/employData.csv', mode='a', header=False,index=False)

    print("The Id is : " + id_val)
    print("The Name is : " + name_val)
    print("The Email is : " + email_val)

    name.set("")
    email.set("")
    id.set("")

def button_4_fnc():
    videoCaptureObject = cv2.VideoCapture(1)
    result = True
    while (result):
        ret, frame = videoCaptureObject.read()
        txt="Press q for capture image"
        cv2.putText(frame,txt,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
        cv2.imshow("Scan Image", frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            break
    print(frame.shape)
    txt_name=real_face_reco.find_img(frame)

    updateData(id=txt_name,set_im=frame)

def updateData(name=None,id=None,email=None,set_im=None):
    df=pd.read_csv("./data/employData.csv")
    df['ID'].astype(str)
    var =df.loc[df['ID'].isin([id])]
    print(var)
    name=var["NAME"].values[0]
    email=var["EMAIL"].values[0]
    out_name.set(name)
    out_id.set(id)
    out_email.set(email)
    path=f"{(var['IMAGE'].values[0])}"
    set_im=cv2.imread(path)
    set_img(set_im)

def button_5_fnc():
    global res_img
    global  image_1,panelB
    path=filedialog.askopenfilename()
    if len(path)>0:
        image=cv2.imread(path)
        txt_name = real_face_reco.find_img(image)
        updateData(id=txt_name,set_im=image)


def set_img(image):
    global res_img
    global image_1, panelB
    image = cv2.resize(image, (500, 468))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = p.Image.fromarray(image)

    image = ImageTk.PhotoImage(image)
    res_img = image
    canvas.create_image(
        996.0,
        790.0,
        image=res_img
    )


def button_3_fncn():
    global path
    path = filedialog.askopenfilename()
    print(path)
    img=cv2.imread(path)
    path="./employ_img/"+id.get()+".jpg"
    if len(path)>0:


        cv2.imwrite(path,img)







def appendDFToCSV_void(df, csvFilePath, sep=","):
    import os
    if not os.path.isfile(csvFilePath):
        df.to_csv(csvFilePath, mode='a', index=False, sep=sep)
    elif len(df.columns) != len(pd.read_csv(csvFilePath, nrows=1, sep=sep).columns):
        raise Exception("Columns do not match!! Dataframe has " + str(len(df.columns)) + " columns. CSV file has " + str(len(pd.read_csv(csvFilePath, nrows=1, sep=sep).columns)) + " columns.")
    elif not (df.columns == pd.read_csv(csvFilePath, nrows=1, sep=sep).columns).all():
        raise Exception("Columns and column order of dataframe and csv file do not match!!")
    else:
        df.to_csv(csvFilePath, mode='a', index=False, sep=sep, header=False)



window = Tk()

window.geometry("1860x1024")
window.configure(bg = "#FFFCB7")


name=StringVar()
email=StringVar()
id=StringVar()
out_id=StringVar()
out_name=StringVar()
out_email=StringVar()

canvas = Canvas(
    window,
    bg = "#FFFCB7",
    height = 1024,
    width = 1860,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    1.1368683772161603e-13,
    0.0,
    720.0000000000001,
    1024.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    13.0,
    31.0,
    anchor="nw",
    text="Pandoras Box",
    fill="#F63333",
    font=("Roboto Bold", 50 * -1),
    width=718.0
)

canvas.create_text(
    33.0,
    195.0,
    anchor="nw",
    text="Register:",
    fill="#000",
    font=("Roboto Bold", 50 * -1),
    width=233.0
)

canvas.create_text(
    1043.0,
    16.0,
    anchor="nw",
    text="Show Me Everything:",
    fill="#000",
    font=("Roboto Bold", 50 * -1),
    width=664.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png")
)
entry_bg_1 = canvas.create_image(
    270.5,
    366.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable = id, font=('calibre',15,'bold'),fg="#000000"
)
entry_1.place(
    x=53.0,
    y=322.0,
    width=435.0,
    height=87.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png")
)
entry_bg_2 = canvas.create_image(
    1602.5,
    761.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable = out_email, font=('calibre',15,'bold'),fg="#000000"
)
entry_2.place(
    x=1385.0,
    y=717.0,
    width=435.0,
    height=87.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png")
)
entry_bg_3 = canvas.create_image(
    1612.5,
    949.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable = out_id, font=('calibre',15,'bold'),fg="#000000"
)
entry_3.place(
    x=1395.0,
    y=905.0,
    width=435.0,
    height=87.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png")
)
entry_bg_4 = canvas.create_image(
    1602.5,
    600.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable = out_name, font=('calibre',15,'bold'),fg="#000000"
)
entry_4.place(
    x=1385.0,
    y=556.0,
    width=435.0,
    height=87.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png")
)
entry_bg_5 = canvas.create_image(
    270.5,
    654.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable = email, font=('calibre',15,'bold'),fg="#000000"
)
entry_5.place(
    x=53.0,
    y=609.5,
    width=435.0,
    height=87.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png")
)
entry_bg_6 = canvas.create_image(
    270.5,
    511.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable = name, font=('calibre',15,'bold'),fg="#000000"
)
entry_6.place(
    x=53.0,
    y=467.0,
    width=435.0,
    height=87.0
)

canvas.create_text(
    34.0,
    281.0,
    anchor="nw",
    text="Enter ID:",
    fill="#000",
    font=("Roboto Bold", 25 * -1),
    width=126.0
)

canvas.create_text(
    1544.0,
    486.0,
    anchor="nw",
    text="Name",
    fill="#000",
    font=("Roboto Bold", 35 * -1),
    width=138.0
)

canvas.create_text(
    1544.0,
    671.0,
    anchor="nw",
    text="Email",
    fill="#000",
    font=("Roboto Bold", 35 * -1),
    width=138.0
)

canvas.create_text(
    1544.0,
    837.0,
    anchor="nw",
    text="Id No",
    fill="#000",
    font=("Roboto Bold", 35 * -1),
    width=138.0
)

canvas.create_text(
    33.0,
    429.0,
    anchor="nw",
    text="Enter Name:",
    fill="#000",
    font=("Roboto Bold", 25 * -1),
    width=163.0
)

canvas.create_text(
    34.0,
    574.0,
    anchor="nw",
    text="Enter Email:",
    fill="#000",
    font=("Roboto Bold", 25 * -1),
    width=189.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=scan_image,
    relief="flat"
)
button_1.place(
    x=34.0,
    y=762.0,
    width=280.0,
    height=65.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=submit,
    relief="flat"
)
button_2.place(
    x=220.0,
    y=891.0,
    width=280.0,
    height=65.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=button_3_fncn,
    relief="flat"
)
button_3.place(
    x=401.0,
    y=762.0,
    width=280.0,
    height=65.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=button_4_fnc,
    relief="flat"
)
button_4.place(
    x=731.0,
    y=166.0,
    width=471.0,
    height=114.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=button_5_fnc,
    relief="flat"
)
button_5.place(
    x=1379.0,
    y=166.0,
    width=471.0,
    height=114.0
)

canvas.create_text(
    763.0,
    313.0,
    anchor="nw",
    text="Employ Details:",
    fill="#000",
    font=("Roboto Bold", 40 * -1),
    width=315.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    996.0,
    790.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    996.0,
    518.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()