from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class EmployeeDetail:
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
        title_lbl = Label(bg_img, text="EMPLOYEE MANAGMENT SYSTEM", font=("times new roman", 30, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #main frame
        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=("time new roman",15))
        Left_frame.place(x=10,y=10,width=660,height=580)

        left_img = Image.open(r'C:\Users\aakanksha bhadsale\Desktop\FaceReconition\images\employee.jfif')
        left_img =left_img.resize((660,130),Image.Resampling.LANCZOS)
        self.photoleft=ImageTk.PhotoImage(left_img)

        bg_img = Label(Left_frame,image=self.photoleft)
        bg_img.place(x=0,y=0,width=660,height=130)

        # Current course
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course",font=("time new roman",15))
        current_course_frame.place(x=5,y=135,width=720,height=150)

        dep_label = Label(current_course_frame,font=("time new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo = ttk.Combobox(current_course_frame,font=("time new roman",12,"bold"),state="readonly")
        dep_combo["values"]= ("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)


        #right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=("time new roman",15))
        Right_frame.place(x=680,y=10,width=660,height=580)


if __name__ == '__main__':
    root =Tk()
    obj = EmployeeDetail(root)
    root.mainloop()