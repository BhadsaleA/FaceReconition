from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import mysql.connector

os.chdir(r'C:\Users\aakanksha bhadsale\Desktop\FaceReconition')

class EmployeeDetail:
    def  __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ========= VARIABLE ============
        self.var_department = StringVar()
        self.var_empType = StringVar()
        self.var_designation = StringVar()
        self.var_emp_id = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_bod = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_pincode = StringVar()
        self.var_join_date = StringVar()
        self.var_manager = StringVar() 
        self.var_radio1 = StringVar()        

        # set Image1 
        img = Image.open(r'images\faceScan.jpeg')
        img =img.resize((800,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=800,height=130)

        # set Image2
        img1 = Image.open(r'images\faceScan.jpeg')
        img1 =img1.resize((800,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img = Label(self.root,image=self.photoimg1)
        bg_img.place(x=800,y=0,width=800,height=130)

        # Background Image 
        img_bg = Image.open(r'images\bg1.jpg')
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
        Left_frame.place(x=20,y=10,width=700,height=580)

        left_img = Image.open(r'images\employee.jfif')
        left_img =left_img.resize((687,100),Image.Resampling.LANCZOS)
        self.photoleft=ImageTk.PhotoImage(left_img)

        bg_img = Label(Left_frame,image=self.photoleft)
        bg_img.place(x=5,y=0,width=686,height=100)

        # Current Detail
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Department",font=("time new roman",15))
        current_course_frame.place(x=5,y=105,width=686,height=115)

        dep_label = Label(current_course_frame,text="Department:",bg="white",font=("time new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=8)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_department,font=("time new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]= ("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        # Employee Type
        dep_label = Label(current_course_frame,text="Employee Type:",bg="white",font=("time new roman",12,"bold"))
        dep_label.grid(row=0,column=2,padx=8)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_empType,font=("time new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]= ("Select Empoyee type","Intern","Employee","HR","Manager")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Designation
        dep_label = Label(current_course_frame,text="Designation:",bg="white",font=("time new roman",12,"bold"))
        dep_label.grid(row=1,column=0,padx=8)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_designation,font=("time new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]= ("Select Designation","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Employee Detail Frame
        emp_detail_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Employee Information",font=("time new roman",15))
        emp_detail_frame.place(x=5,y=225,width=686,height=230)

        #emp_id
        emp_id = Label(emp_detail_frame,text="EmployeeID:",bg="white",font=("time new roman",12,"bold"))
        emp_id.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        emp_id_entry=ttk.Entry(emp_detail_frame,textvariable=self.var_emp_id,width=20,font=("times new roman",13,"bold"))
        emp_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #emp_name
        emp_name = Label(emp_detail_frame,text="Name:",bg="white",font=("time new roman",12,"bold"))
        emp_name.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        emp_name_entry=ttk.Entry(emp_detail_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        emp_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #emp_gender
        emp_gender = Label(emp_detail_frame,text="Gender:",bg="white",font=("time new roman",12,"bold"))
        emp_gender.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        emp_gender = ttk.Combobox(emp_detail_frame,textvariable=self.var_gender,width=18,font=("time new roman",12,"bold"),state="readonly")
        emp_gender["values"]= ("Select Gender","Female","Male","Other")
        emp_gender.current(0)
        emp_gender.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #emp_bod
        emp_BOD = Label(emp_detail_frame,text="Birth Date:",bg="white",font=("time new roman",12,"bold"))
        emp_BOD.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        emp_BOD_entry=ttk.Entry(emp_detail_frame,textvariable=self.var_bod,width=20,font=("times new roman",13,"bold"))
        emp_BOD_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #emp_email
        emp_email = Label(emp_detail_frame,text="Email:",bg="white",font=("time new roman",12,"bold"))
        emp_email.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        emp_email_entry=ttk.Entry(emp_detail_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        emp_email_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #emp_mobile
        emp_mobileNo = Label(emp_detail_frame,text="Contact NO:",bg="white",font=("time new roman",12,"bold"))
        emp_mobileNo.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        emp_mobileNo_entry=ttk.Entry(emp_detail_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        emp_mobileNo_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #emp_address
        emp_address = Label(emp_detail_frame,text="Adress:",bg="white",font=("time new roman",12,"bold"))
        emp_address.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        emp_address_entry=ttk.Entry(emp_detail_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        emp_address_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #emp_pincode
        emp_pincode = Label(emp_detail_frame,text="PinCode:",bg="white",font=("time new roman",12,"bold"))
        emp_pincode.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        emp_pincode_entry=ttk.Entry(emp_detail_frame,textvariable=self.var_pincode,width=20,font=("times new roman",13,"bold"))
        emp_pincode_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #emp_joining_date
        emp_joiningDate = Label(emp_detail_frame,text="Joining Date:",bg="white",font=("time new roman",12,"bold"))
        emp_joiningDate.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        emp_joiningDate_entry=ttk.Entry(emp_detail_frame,textvariable=self.var_join_date,width=20,font=("times new roman",13,"bold"))
        emp_joiningDate_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #emp_manager
        emp_manager = Label(emp_detail_frame,text="Manager:",bg="white",font=("time new roman",12,"bold"))
        emp_manager.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        emp_manager_entry=ttk.Entry(emp_detail_frame,textvariable=self.var_manager,width=20,font=("times new roman",13,"bold"))
        emp_manager_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)                

        #Radio Button
        radiobtn1=ttk.Radiobutton(emp_detail_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(emp_detail_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #button frame
        btn_frame =Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=455,width=686,height=38)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("time new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=16,font=("time new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        delete_btn=Button(btn_frame,text="Delete",width=16,font=("time new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=3)

        reset_btn=Button(btn_frame,text="Reset",width=16,font=("time new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=4)

        #btn2 frame
        btn_frame1 =Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=495,width=686,height=38)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=34,font=("time new roman",13,"bold"),bg="light blue",fg="white")
        take_photo_btn.grid(row=0,column=1)

        update_photo_btn=Button(btn_frame1,text="Update Photo",width=34,font=("time new roman",13,"bold"),bg="light blue",fg="white")
        update_photo_btn.grid(row=0,column=2)

        #right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=("time new roman",15))
        Right_frame.place(x=750,y=10,width=700,height=580)

        Right_img = Image.open(r'images\employee.jfif')
        Right_img =Right_img.resize((687,100),Image.Resampling.LANCZOS)
        self.photoright=ImageTk.PhotoImage(Right_img)

        bg_img = Label(Right_frame,image=self.photoright)
        bg_img.place(x=5,y=0,width=686,height=100)

        # =========Search Style ============

        Search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("time new roman",15))
        Search_frame.place(x=5,y=105,width=686,height=70)

        search_label = Label(Search_frame,text="Search By:",bg="red",font=("time new roman",12,"bold"))
        search_label.grid(row=0,column=0,padx=8)

        search_combo = ttk.Combobox(Search_frame,font=("time new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]= ("Select","Employee_Id","Contact No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("time new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=1,pady=10,sticky=W)

        search_button=Button(Search_frame,text="Search",width=12,font=("time new roman",12,"bold"),bg="sky blue")
        search_button.grid(row=0,column=3,padx=2)

        searchAll_button=Button(Search_frame,text="Search All",width=12,font=("time new roman",12,"bold"),bg="sky blue")
        searchAll_button.grid(row=0,column=4,padx=4)

        # ============== Table Frame ===========

        table_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=180,width=686,height=370)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("department","emp_type","EMP_ID","name","gender","dob","email","address","pincode","joining date","manager","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("department",text="Department")
        self.student_table.heading("emp_type",text="EmployeeType")
        self.student_table.heading("EMP_ID",text="EmployeeID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("pincode",text="Pincode")
        self.student_table.heading("joining date",text="Joining Date")
        self.student_table.heading("manager",text="Manager")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("department",width=100)
        self.student_table.column("emp_type",width=100)
        self.student_table.column("EMP_ID",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("pincode",width=100)
        self.student_table.column("joining date",width=100)
        self.student_table.column("manager",width=100)
        self.student_table.column("photo",width=115)
        

        self.student_table.pack(fill=BOTH,expand=1)
    # ==================== Data function ==============================

    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_name.get() == "" or self.var_emp_id.get() == "":
            messagebox.showerror("Error","Fields are required",parent =self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognition")
                my_cursor = conn.cursor()
                query = "INSERT INTO emp (emp_id,emp_name,gender,bod,email,phone,address,joining_date,pincode,department,emptype,designation,manager,photo_sample) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = ( self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_bod.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_join_date.get(),
                        self.var_pincode.get(),
                        self.var_department.get(),
                        self.var_empType.get(),
                        self.var_designation.get(),
                        self.var_manager.get(),
                        self.var_radio1.get()
                        )
                my_cursor.execute(query,val)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Employee has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


if __name__ == '__main__':
    root =Tk()
    obj = EmployeeDetail(root)
    root.mainloop()