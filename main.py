from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_system:
    def  __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # set Image1 
        img = Image.open(r'C:\Users\aakanksha bhadsale\Desktop\FaceReconition\images\faceScan.jpeg')
        img =img.resize((700,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=700,height=130)

        # set Image2
        img1 = Image.open(r'C:\Users\aakanksha bhadsale\Desktop\FaceReconition\images\faceScan.jpeg')
        img1 =img1.resize((700,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img = Label(self.root,image=self.photoimg1)
        bg_img.place(x=700,y=0,width=700,height=130)

        # Background Image 
        img_bg = Image.open(r'C:\Users\aakanksha bhadsale\Desktop\FaceReconition\images\bg1.jpg')
        img_bg =img_bg.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg_bg=ImageTk.PhotoImage(img_bg)

        bg_img = Label(self.root,image=self.photoimg_bg)
        bg_img.place(x=0,y=130,width=1530,height=710)

        # Create and place the title label
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Student button 
        img4 = Image.open(r'C:\Users\aakanksha bhadsale\Desktop\FaceReconition\images\person.png')
        img4 =img4.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Student details", cursor="hand2",font=("times new roman", 20, "bold"), bg="blue", fg="white")
        b1_1.place(x=200,y=250,width=180,height=40)
        
        # Face Detection button
        img5 = Image.open(r'C:\Users\aakanksha bhadsale\Desktop\FaceReconition\images\FaceDetect.jfif')
        img5 =img5.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=420,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Face detection", cursor="hand2",font=("times new roman", 20, "bold"), bg="blue", fg="white")
        b1_1.place(x=420,y=250,width=180,height=40)

        # Attendance button
        img6 = Image.open(r'C:\Users\aakanksha bhadsale\Desktop\FaceReconition\images\attendance3.png')
        img6 =img6.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=640,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Attendance", cursor="hand2",font=("times new roman", 20, "bold"), bg="blue", fg="white")
        b1_1.place(x=640,y=250,width=180,height=40)

        # Help desk button
        img7 = Image.open(r'C:\Users\aakanksha bhadsale\Desktop\FaceReconition\images\help.png')
        img7 =img7.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=860,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Help Desk", cursor="hand2",font=("times new roman", 20, "bold"), bg="blue", fg="white")
        b1_1.place(x=860,y=250,width=180,height=40)

        # Build button
        img8 = Image.open(r'C:\Users\aakanksha bhadsale\Desktop\FaceReconition\images\build.png')
        img8 =img8.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Build", cursor="hand2",font=("times new roman", 20, "bold"), bg="blue", fg="white")
        b1_1.place(x=200,y=500,width=180,height=40)

        # Photo button
        img9 = Image.open(r'C:\Users\aakanksha bhadsale\Desktop\FaceReconition\images\cam.png')
        img9 =img9.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=420,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Build", cursor="hand2",font=("times new roman", 20, "bold"), bg="blue", fg="white")
        b1_1.place(x=420,y=500,width=180,height=40)

        # Devloper button
        img10 = Image.open(r'C:\Users\aakanksha bhadsale\Desktop\FaceReconition\images\dev.png')
        img10 =img10.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=640,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Build", cursor="hand2",font=("times new roman", 20, "bold"), bg="blue", fg="white")
        b1_1.place(x=640,y=500,width=180,height=40)
        
        # logout button
        img11 = Image.open(r'C:\Users\aakanksha bhadsale\Desktop\FaceReconition\images\logout1.png')
        img11 =img11.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=860,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="logout", cursor="hand2",font=("times new roman", 20, "bold"), bg="blue", fg="white")
        b1_1.place(x=860,y=500,width=180,height=40)


if __name__ == '__main__':
    root =Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()



    