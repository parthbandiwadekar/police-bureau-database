from tkinter import *
from tkinter import ttk   #ttk is for adding style
from PIL import Image, ImageTk 
import mysql.connector
from tkinter import messagebox
import cv2#photo
from PIL import Image, ImageTk#photo
import io




class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('POLICE BUREAU DATABASE')
        self.root.configure(bg="black")
        self.photo_data=None
        
        

        #variables

        self.var_case_id=StringVar()
        self.var_criminal_name=StringVar()
        self.var_criminal_no=StringVar()
        self.var_arrest_date=StringVar()
        self.var_address=StringVar()
        self.var_occupation=StringVar()
        self.var_crime=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_age=StringVar()
        self.var_birthmark=StringVar()
        self.var_gender=StringVar()
        self.var_photo_data = StringVar()
        
        
        

        lbl_title=Label(self.root, text="POLICE  BUREAU  DATABASE", font=("Dutch801 XBd BT", 40,"bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=1540, height=70)

        



        #LOGO
        img_logo=Image.open("images/policelogofinal.png")
        img_logo=img_logo.resize((60, 60), Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=150, y=5, width=60, height=60)  #logoleftside

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=1320, y=5, width=60, height=60)  #logorightside

        #OUTER FRAME
        Main_frame=Frame(self.root, bd=2, relief=RIDGE, bg="grey")
        Main_frame.place(x=10, y=200, width=1512, height=570)

        img1=Image.open("images/policelogofinal.png")
        img1=img1.resize((175, 175), Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(image=self.photo1)
        self.img_1.place(x=695, y=70, width=135, height=130)




        #CRIMINAL FRAME
        upper_frame=LabelFrame(Main_frame, bd=2, relief=RIDGE, text="CRIMINAL INFORMATION", font=("times new roman", 15,"bold","underline"), bg="grey" ,fg="gold")
        upper_frame.place(x=10, y=10, width=1488, height=230 )

        #LABELS
        
        #case id
        caseid=Label(upper_frame, text="CASE ID:", font=("times new roman", 13, "bold"), bg="grey")
        caseid.grid(row=0, column=0,padx=10, pady=3, sticky=W)

        caseentry=ttk.Entry(upper_frame, textvariable=self.var_case_id ,width=22,font=("times new roman", 13,"bold"))
        caseentry.grid(row=0, column=1,padx=10, pady=3, sticky=W)


        #criminal name
        criminalname=Label(upper_frame, text="CRIMINAL NAME :", font=("times new roman",13,"bold"),bg="grey")
        criminalname.grid(row=1, column=0,padx=10, pady=3, sticky=W)

        criminalentry=ttk.Entry(upper_frame,textvariable=self.var_criminal_name ,width=22, font=("times new roman", 13, "bold"))
        criminalentry.grid(row=1, column=1, padx=10,pady=3, sticky=W)

        #criminal no.
        criminalno=Label(upper_frame, text="CRIMINAL NO. :", font=("times new roman",13,"bold"),bg="grey")
        criminalno.grid(row=2, column=0, padx=10,pady=3, sticky=W)

        criminalno=ttk.Entry(upper_frame,textvariable=self.var_criminal_no ,width=22, font=("times new roman", 13, "bold"))
        criminalno.grid(row=2, column=1, padx=10,pady=3, sticky=W)


        #arrest date
        arrestdate=Label(upper_frame, text="ARREST DATE :", font=("times new roman",13,"bold"),bg="grey")
        arrestdate.grid(row=3, column=0,padx=10, pady=3, sticky=W)

        arrestdate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date ,width=22, font=("times new roman", 13, "bold"))
        arrestdate.grid(row=3, column=1,padx=10, pady=3, sticky=W)

        #address
        address=Label(upper_frame, text="ADDRESS :", font=("times new roman",13,"bold"),bg="grey")
        address.grid(row=4, column=0,padx=10, pady=3, sticky=W)

        address=ttk.Entry(upper_frame,textvariable=self.var_address ,width=22, font=("times new roman", 13, "bold"))
        address.grid(row=4, column=1,padx=10, pady=3, sticky=W)

        #occupation
        occupation=Label(upper_frame, text="OCCUPATION :", font=("times new roman",13,"bold"),bg="grey")
        occupation.grid(row=5, column=0,padx=10, pady=3, sticky=W)

        occupation=ttk.Entry(upper_frame,textvariable=self.var_occupation ,width=22, font=("times new roman", 13, "bold"))
        occupation.grid(row=5, column=1,padx=10, pady=3, sticky=W)

        
        #crime
        crime=Label(upper_frame, text="CRIME :", font=("times new roman",13,"bold"),bg="grey")
        crime.grid(row=0, column=2, padx=10,pady=3, sticky=W)

        crime=ttk.Entry(upper_frame,textvariable=self.var_crime ,width=22, font=("times new roman", 13, "bold"))
        crime.grid(row=0, column=3, padx=10,pady=3, sticky=W)

        #date of crime
        dateofcrime=Label(upper_frame, text="DATE OF CRIME :", font=("times new roman",13,"bold"),bg="grey")
        dateofcrime.grid(row=1, column=2, padx=10,pady=3, sticky=W)

        dateofcrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime ,width=22, font=("times new roman", 13, "bold"))
        dateofcrime.grid(row=1, column=3, padx=10,pady=3, sticky=W)

        #age
        age=Label(upper_frame, text="AGE :", font=("times new roman",13,"bold"),bg="grey")
        age.grid(row=2, column=2, padx=10,pady=3, sticky=W)

        age=ttk.Entry(upper_frame,textvariable=self.var_age ,width=22, font=("times new roman", 13, "bold"))
        age.grid(row=2, column=3, padx=10,pady=3, sticky=W)

        #birth mark
        birthmark=Label(upper_frame,text="BIRTHMARK :", font=("times new roman",13,"bold"),bg="grey")
        birthmark.grid(row=3, column=2, padx=10,pady=3, sticky=W)

        birthmark=ttk.Entry(upper_frame,textvariable=self.var_birthmark  ,width=22, font=("times new roman", 13, "bold"))
        birthmark.grid(row=3, column=3, padx=10,pady=3, sticky=W)


        #gender
        
        gender=Label(upper_frame, text="GENDER :", font=("times new roman",13,"bold"),bg="grey")
        gender.grid(row=4, column=2, padx=10,pady=3, sticky=W)

        gender1=Radiobutton(upper_frame, variable=self.var_gender,width=7, text="MALE", value="MALE", font=("times new roman", 9, "bold"))
        gender1.grid(row=4, column=3, padx=10,pady=5, sticky=W)
        


        gender2=Radiobutton(upper_frame,variable=self.var_gender ,width=7, text="FEMALE", value="FEMALE", font=("times new roman", 9, "bold"))
        gender2.grid(row=4, column=3, padx=10,pady=5, sticky=E)


        gender3=Radiobutton(upper_frame,variable=self.var_gender ,width=7, text="OTHER", value="OTHER", font=("times new roman", 9, "bold"))
        gender3.grid(row=5, column=3, padx=10,pady=3, sticky=S)
        


        #button frame

        buttonframe=LabelFrame(upper_frame, bd=2, relief=RIDGE, font=("times new roman", 15,"bold","underline"), bg="gold" ,fg="gold")
        buttonframe.place(x=1290, y=5, width=180, height=185 )

        #buttons
        #save button
        btn_save=Button(buttonframe, command=self.add_data , text="SAVE", font=("times new roman", 13,"bold" ), width=15 ,bg="blue", fg="white")
        btn_save.grid(row=0, column=0, padx=5, pady=5, sticky=N)

        #update
        btn_update=Button(buttonframe, command=self.update_data , text="UPDATE", font=("times new roman", 13,"bold" ), width=15 ,bg="blue", fg="white")
        btn_update.grid(row=1, column=0, padx=5, pady=5, sticky=N)

        #clear
        btn_clear=Button(buttonframe, command=self.clear_data , text="CLEAR", font=("times new roman", 13,"bold" ), width=15 ,bg="blue", fg="white")
        btn_clear.grid(row=2, column=0, padx=5, pady=5, sticky=N)

        #delete
        btn_delete=Button(buttonframe, text="DELETE", command=self.delete_data,font=("times new roman", 13,"bold" ), width=15 ,bg="blue", fg="white")
        btn_delete.grid(row=3, column=0, padx=5, pady=5, sticky=N)


        #PHOTO
        btn_capture_photo = Button(upper_frame, command=self.capture_photo, text="CAPTURE PHOTO", font=("times new roman", 13, "bold"), width=15, bg="blue", fg="white")
        btn_capture_photo.grid(row=3, column=5, padx=200, pady=3, sticky=S)

        self.img_captured = Label(image=self.photo_logo, bg="black")
        self.img_captured.place(x=850, y=240, width=160, height=190)  # Display captured photo


        
        







        #LOWER FRAME
        lower_frame=LabelFrame(Main_frame, bd=2, relief=RIDGE,  text="CRIMINAL INFORMATION TABLE", font=("times new roman", 15,"bold","underline", ), bg="grey" ,fg="gold")
        lower_frame.place(x=10, y=260, width=1488, height=280)

        #INNER LOWER FRAME
        innerlower_frame=LabelFrame(Main_frame, bd=2, relief=RIDGE,  text="SEARCH RECORDS", font=("times new roman", 10,"bold","underline", ), bg="grey" ,fg="black")
        innerlower_frame.place(x=20, y=285, width=1467, height=70)

        search_by=Label(innerlower_frame,text="SEARCH BY:", font=("times new roman", 11, "bold"), bg="grey", fg="black")
        search_by.grid(row=0, column=0, padx=5, sticky=W)

        #combo box inside innerlower frame

        self.var_com_search=StringVar()

        combo_search_box=ttk.Combobox(innerlower_frame ,textvariable=self.var_com_search ,font=("times new roman", 10, "bold"), width=18, state="read")         #"read" so that u can only read and select and not type
        combo_search_box["value"]=( "CASE ID", "CRIMINAL NO.")
        combo_search_box.current=(NONE)
        combo_search_box.grid(row=0, column=1, padx=5, sticky=W)


        self.var_search=StringVar()
        
        search_bar=ttk.Entry(innerlower_frame ,textvariable=self.var_search ,width=22, font=("times new roman", 13, "bold"))
        search_bar.grid(row=0, column=2, padx=10,pady=3, sticky=W)

        #search button
        btn_search=Button(innerlower_frame, command=self.search_data , text="SEARCH", font=("times new roman", 13,"bold" ), width=15 ,bg="blue", fg="white")
        btn_search.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        #show all button
        btn_showall=Button(innerlower_frame, command=self.fetch_data , text="SHOW ALL", font=("times new roman", 13,"bold" ), width=15 ,bg="blue", fg="white")
        btn_showall.grid(row=0, column=4, padx=5, pady=5, sticky=W)

        #frame in inner lowframe

        table_frame=Frame(lower_frame, bd=2, relief=RIDGE)
        table_frame.place(x=8, y=80, width=1467, height=165 )

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame, column=("1","2","3","4","5","6","7","8","9","10","11","12"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        #table sections 
        self.criminal_table = ttk.Treeview(table_frame, column=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # Bind the event to self.criminal_table
        self.criminal_table.bind("<ButtonRelease-1>", self.view_selected_photo)

        self.criminal_table.heading("1", text="Case Id")
        self.criminal_table.heading("2", text="Criminal Name")
        self.criminal_table.heading("3", text="Criminal No.")
        self.criminal_table.heading("4", text="Arrest Date")
        self.criminal_table.heading("5", text="Addresss")
        self.criminal_table.heading("6", text="Occupation")
        self.criminal_table.heading("7", text="Crime")
        self.criminal_table.heading("8", text="Date Of Crime")
        self.criminal_table.heading("9", text="Age")
        self.criminal_table.heading("10", text="Birth Mark")
        self.criminal_table.heading("11", text="Gender")
        self.criminal_table.heading("12", text="Photo")
        


        self.criminal_table["show"]="headings"

        self.criminal_table.column("1", width=100)
        self.criminal_table.column("2", width=100)
        self.criminal_table.column("3", width=100)
        self.criminal_table.column("4", width=100)
        self.criminal_table.column("5", width=100)
        self.criminal_table.column("6", width=100)
        self.criminal_table.column("7", width=100)
        self.criminal_table.column("8", width=100)
        self.criminal_table.column("9", width=100)
        self.criminal_table.column("10", width=100)
        self.criminal_table.column("11", width=100)
        self.criminal_table.column("12", width=100)
        
        

        self.criminal_table.pack(fill=BOTH, expand=1)

        self.criminal_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data() ###########################################################################


    
    #ADD FUNCTION

    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root) #parent self root is given because the message box doesnt go in any other window 
        else:
            try:
                connect=mysql.connector.connect(host="localhost", username="root", password="parthu0509", database="police_bureau_database")
                my_cursor=connect.cursor()

                # Check if a record with the same case ID exists
                my_cursor.execute("SELECT * FROM criminal WHERE case_id=%s", (self.var_case_id.get(),))
                existing_record = my_cursor.fetchone()

                if existing_record:
                # Update the existing record
                    my_cursor.execute("UPDATE criminal SET criminal_name=%s, criminal_no=%s, arrest_date=%s, address=%s, occupation=%s, crime=%s, date_of_crime=%s, age=%s, birthmark=%s, gender=%s, photo=%s WHERE case_id=%s",
                                  (self.var_criminal_name.get(), self.var_criminal_no.get(), self.var_arrest_date.get(), self.var_address.get(),
                                   self.var_occupation.get(), self.var_crime.get(), self.var_date_of_crime.get(), self.var_age.get(),
                                   self.var_birthmark.get(), self.var_gender.get(), self.photo_data, self.var_case_id.get()))

                else:
                    my_cursor.execute("INSERT INTO criminal VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                              (self.var_case_id.get(), self.var_criminal_name.get(), self.var_criminal_no.get(),
                               self.var_arrest_date.get(), self.var_address.get(), self.var_occupation.get(),
                               self.var_crime.get(), self.var_date_of_crime.get(), self.var_age.get(),
                               self.var_birthmark.get(), self.var_gender.get(),self.photo_data  ))
                connect.commit()
                self.fetch_data()
                self.clear_data()
                connect.close()
                messagebox.showinfo("SUCCESS", "CRIMINAL RECORD HAS BEEN ADDED")
            
            except Exception as es:
                messagebox.showerror("Error", f"Due To{str(es)}")



    #fetch data
    def fetch_data(self):
        try:
            connect = mysql.connector.connect(host="localhost", username="root", password="parthu0509", database="police_bureau_database")
            my_cursor = connect.cursor()
            my_cursor.execute("SELECT case_id, criminal_name, criminal_no, arrest_date, address, occupation, crime, date_of_crime, age, birthmark, gender, photo FROM criminal")
            data = my_cursor.fetchall()
            if data:
                self.criminal_table.delete(*self.criminal_table.get_children())
                for row in data:
                    self.criminal_table.insert("", END, values=row[:-1] + ("View Photo",) )  # Exclude the last element (photo)
            connect.commit()
            connect.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error fetching data: {str(es)}")
                
            
    

    #get cursor

    def get_cursor(self, event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content["values"]

        if data and data[-1] == 'View Photo':
            self.view_selected_photo(event)
        else:

            self.var_case_id.set(data[0])
            self.var_criminal_name.set(data[1])
            self.var_criminal_no.set(data[2])
            self.var_arrest_date.set(data[3])
            self.var_address.set(data[4])
            self.var_occupation.set(data[5])
            self.var_crime.set(data[6])
            self.var_date_of_crime.set(data[7])
            self.var_age.set(data[8])
            self.var_birthmark.set(data[9])
            self.var_gender.set(data[10])
            self.view_photo(data[11])  # Display the photo

            # Display the stored photo
            if data[11]:
                self.view_photo(data[11])
            else:
                self.img_captured.config(image=self.photo_logo)

    #update button function

    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror("Error", "All Fields Are Required")
 
        else:
            try:
                update=messagebox.askyesno("Update", "Are you sure you want to update this criminal record")
                if update>0:
                    connect=mysql.connector.connect(host="localhost", username="root", password="parthu0509", database="police_bureau_database")
                    my_cursor=connect.cursor()

                    if self.photo_data is not None:  # Check if a new photo was captured
                        my_cursor.execute("UPDATE criminal SET criminal_name=%s, criminal_no=%s, arrest_date=%s, address=%s, occupation=%s, crime=%s, date_of_crime=%s, age=%s, birthmark=%s, gender=%s, photo=%s WHERE case_id=%s",
                                      (self.var_criminal_name.get(), self.var_criminal_no.get(), self.var_arrest_date.get(), self.var_address.get(),
                                       self.var_occupation.get(), self.var_crime.get(), self.var_date_of_crime.get(), self.var_age.get(),
                                       self.var_birthmark.get(), self.var_gender.get(), self.photo_data, self.var_case_id.get()))
                        
                        
                        
                        
                        
                        
                        
                    else:    
                        
                        my_cursor.execute("Update criminal set criminal_name=%s, criminal_no=%s, arrest_date=%s, address=%s, occupation=%s, crime=%s, date_of_crime=%s, age=%s, birthmark=%s, gender=%s, WHERE case_id=%s", (

                                                                                                                                                                                                                            
                                                                                                                                                                                                                            self.var_criminal_name.get(),
                                                                                                                                                                                                                            self.var_criminal_no.get(),
                                                                                                                                                                                                                            self.var_arrest_date.get(),
                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                            self.var_occupation.get(),
                                                                                                                                                                                                                            self.var_crime.get(),
                                                                                                                                                                                                                            self.var_date_of_crime.get(),
                                                                                                                                                                                                                            self.var_age.get(),
                                                                                                                                                                                                                            self.var_birthmark.get(),
                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                            self.var_case_id.get(),
                                                                                                                                                                                                                            
                                                                                                                                                                                                                            

                
                
                                                                                                                                                                                                                            ))
                    
                
                    connect.commit()
                    self.fetch_data()
                    self.clear_data()
                    connect.close() 
                    messagebox.showinfo("Success", "Criminal record has been successfully updated")
            
                else:
                    if not update:
                        return    
            
            except Exception as es:
                messagebox.showerror("ERROR", f"Due To{str(es)}")


    #delete button function
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                delete=messagebox.askyesno("Delete", "Are you sure you want to Delete this criminal record ?")
                if delete>0:
                    connect=mysql.connector.connect(host="localhost", username="root", password="parthu0509", database="police_bureau_database")
                    my_cursor=connect.cursor()

                    sql="delete from criminal where case_id=%s"
                    value=(self.var_case_id.get(), )   #if comma not given error will show
                    my_cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                connect.commit()
                self.fetch_data()
                self.clear_data()
                connect.close()
                messagebox.showinfo("Success", "Criminal record has been successfully Deleted")
            except Exception as es:
                messagebox.showerror("ERROR", f"Due To{str(es)}")



    #clear button function
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_name.set("")
        self.var_criminal_no.set("")
        self.var_arrest_date.set("")
        self.var_address.set("")
        self.var_occupation.set("")
        self.var_crime.set("")
        self.var_date_of_crime.set("")
        self.var_age.set("")
        self.var_birthmark.set("")
        self.var_gender.set("")
        self.photo_data = None  # Reset the photo data to None
        self.img_captured.config(image=self.photo_logo)  # Reset the displayed photo


    #search section functon

    def search_data(self): 
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                connect=mysql.connector.connect(host="localhost", username="root",password="parthu0509", database="police_bureau_database")
                my_cursor=connect.cursor()
                if self.var_com_search.get() == "CASE ID":
                    my_cursor.execute("SELECT * FROM criminal WHERE case_id = %s", (self.var_search.get(),))

                elif self.var_com_search.get() == "CRIMINAL NO.":
                    my_cursor.execute("SELECT * FROM criminal WHERE criminal_no = %s", (self.var_search.get(),))

                else:
                    my_cursor.execute("SELECT * FROM criminal WHERE " + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
                
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                connect.commit()
                connect.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}') 

    #PHOTO
    def capture_photo(self):
        try:
            cap = cv2.VideoCapture(0)  # Open the default camera (index 0)
            ret, frame = cap.read()    # Read a frame from the camera
            
            if ret:
                photo_path = "captured_photo.png"
                cv2.imwrite(photo_path, frame)  # Save the captured frame as an image
                self.display_captured_photo(photo_path)  # Display the captured photo
                
                # Open the saved photo and store its binary data in the variable
                with open(photo_path, "rb") as photo_file:
                    self.photo_data = photo_file.read()
                
                

                cap.release()  # Release the camera
            else:
                messagebox.showerror("Error", "Failed to capture photo.")
        except Exception as es:
            messagebox.showerror("Error", f"Error capturing photo: {str(es)}")

    def display_captured_photo(self, photo_path):
        img_captured = Image.open(photo_path)
        img_captured = img_captured.resize((150, 175), Image.ANTIALIAS)
        self.photo_captured = ImageTk.PhotoImage(img_captured)
        self.img_captured.config(image=self.photo_captured)

        with open(photo_path, "rb") as photo_file:
            photo_data = photo_file.read()
            self.var_photo_data.set(photo_data)  # Store the photo data in the variable

    def view_photo(self, photo_data):
        img = Image.open(io.BytesIO(photo_data))
        img = img.resize((100, 100), Image.ANTIALIAS)  # Resize the image
        img = ImageTk.PhotoImage(img)
        

    # Create a label to display the image
        photo_label = Label(image=img)
        photo_label.image = img
        photo_label.grid(row=1, column=12)  # Adjust row and column as needed
        
    

    def view_selected_photo(self, event):
        selected_item = self.criminal_table.selection()[0]
        item_values = self.criminal_table.item(selected_item)["values"]
        photo_data = item_values[-1]
        

        if photo_data:
            self.view_photo(photo_data)


    def save_photo_to_database(self, photo_path):
        try:
            with open(photo_path, "rb") as photo_file:
                photo_data = photo_file.read()

            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="parthu0509",
                database="police_bureau_database"
            )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO criminal (criminal_name, photo) VALUES (%s, %s)",
                           ("Unknown", photo_data))
            connection.commit()
            connection.close()
            print("Photo saved to database.")
        except Exception as e:
            print("Error:", e)







                    

                    

    



        







    



if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()