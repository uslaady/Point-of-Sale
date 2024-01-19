from tkinter import*
import math,random,os
from tkinter import messagebox
from datetime import datetime
import os
import re
import tkinter as tk
from PIL import ImageTk
from PIL import Image
from tkinter import ttk
import pymysql

import threading
from threading import Thread 

##############################################
from tkinter import filedialog
import pandas as pd
from collections import defaultdict
############################################## 
import xlsxwriter
import csv
from openpyxl import Workbook


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Newly added
#This function will happen once there is a quit!
def login_quit():
	ask=messagebox.askyesno("Quitting Application","Are you sure to proceed with Quitting! \nGoodbye!")
	if ask==True:
		master.destroy()

def change_password():
	#Interface for change password
	
	global ChangePasswordRegUserID
	global ChangePasswordOldPassword
	global ChangePasswordNewPassword1
	global ChangePasswordNewPassword2
	
	ChangePasswordRegUserID=StringVar()
	ChangePasswordOldPassword=StringVar()
	ChangePasswordNewPassword1=StringVar()
	ChangePasswordNewPassword2=StringVar()

	global bg_color
	bg_color="DarkGray"
	global ChangePassword
	ChangePassword = tk.Toplevel(master)
	ChangePassword.title("Change Password")
	ChangePassword.wm_iconbitmap('icon.ico')
	ChangePassword.focus()
	ChangePasswordList = tk.Label(ChangePassword, text = "Change Your Password",bd=5,relief=GROOVE,font=("Arial",15,"bold"),bg="DarkGray",fg="DarkGreen")
	ChangePasswordList.pack(side=TOP,fill=X)
	ChangePassword.geometry("350x285+545+325")
	ChangePasswordList.pack()	

	#=======================ChangePassword detail frame
	ChangePasswordNow=LabelFrame(ChangePassword,bd=10,relief=GROOVE,text="User-Password",font=("Arial",15,"bold"),fg="DarkRed",bg=bg_color)
	ChangePasswordNow.place(x=0,y=40,relwidth=1,height=190)
	
	#Label for ChangePasswordRegUserID
	ChangePasswordRegUserID_lbl=Label(ChangePasswordNow,text="UserName       ",bg=bg_color,fg="black",font=("Arial",15,"bold")).grid(row=0,column=0,padx=1,pady=2)
	global ChangePasswordRegUserID_txt
	ChangePasswordRegUserID_txt=Entry(ChangePasswordNow,width=16,textvariable=ChangePasswordRegUserID,fg="black",font="arial 12 bold",bd=3,relief=SUNKEN)
	ChangePasswordRegUserID_txt.grid(row=0,column=1,pady=2,padx=2)
	ChangePasswordRegUserID_txt.focus()
	
	#Label for ChangePasswordOldPassword
	ChangePasswordOldPassword_lbl=Label(ChangePasswordNow,text="Old Password ",bg=bg_color,fg="red",font=("Arial",15,"bold")).grid(row=1,column=0,padx=5,pady=2)
	global ChangePasswordOldPassword_txt
	ChangePasswordOldPassword_txt=Entry(ChangePasswordNow,show="*",width=16,textvariable=ChangePasswordOldPassword,fg="red",font="arial 12 bold",bd=3,relief=SUNKEN)
	ChangePasswordOldPassword_txt.grid(row=1,column=1,pady=2,padx=2)
	ChangePasswordOldPassword_txt.focus()
	
	
	#Label for ChangePasswordNewPassword1
	ChangePasswordNewPassword1_lbl=Label(ChangePasswordNow,text="New Password",bg=bg_color,fg="green",font=("Arial",15,"bold")).grid(row=2,column=0,padx=5,pady=2)
	global ChangePasswordNewPassword1_txt
	ChangePasswordNewPassword1_txt=Entry(ChangePasswordNow,show="*",width=16,textvariable=ChangePasswordNewPassword1,fg="green",font="arial 12 bold",bd=3,relief=SUNKEN)
	ChangePasswordNewPassword1_txt.grid(row=2,column=1,pady=2,padx=2)
	ChangePasswordNewPassword1_txt.focus()

	#Label for ChangePasswordNewPassword2
	ChangePasswordNewPassword2_lbl=Label(ChangePasswordNow,text="New Password",bg=bg_color,fg="green",font=("Arial",15,"bold")).grid(row=3,column=0,padx=5,pady=2)
	global ChangePasswordNewPassword2_txt
	ChangePasswordNewPassword2_txt=Entry(ChangePasswordNow,show="*",width=16,textvariable=ChangePasswordNewPassword2,fg="green",font="arial 12 bold",bd=3,relief=SUNKEN)
	ChangePasswordNewPassword2_txt.grid(row=3,column=1,pady=2,padx=2)
	ChangePasswordNewPassword2_txt.focus()
	
	
	#=======================Control frame
	btn_ChangePasswordFrame=LabelFrame(ChangePassword,bd=8,relief=RIDGE,bg=bg_color)
	btn_ChangePasswordFrame.place(x=0,y=228,relwidth=1,height=54)
	
	#Adding buttons to perform different actions
	#Different commands will be added to this buttons to perform actions upon click
	#The add_staff function will be added to Addbtn: command=self.add_staff (test it, confirm data in DB)
	Change=Button(btn_ChangePasswordFrame,text="Change",width=10,command=ChangePasswordFunction,fg="Blue",font=("Arial",12,"bold")).grid(row=0,column=0,padx=2,pady=3)
	
	#The clear function will be added to Clearbtn: command=self.clear to enable clear the visible data
	Clearbtn=Button(btn_ChangePasswordFrame,text="Clear",width=9,command=Clear_ChangePassword,fg="Black",font=("Arial",12,"bold")).grid(row=0,column=1,padx=2,pady=3)
	
	#The clear function will be added to Clearbtn: command=self.clear to enable clear the visible data
	Closebtn=Button(btn_ChangePasswordFrame,text="Close",width=10,command=Close_ChangePassword,fg="Black",font=("Arial",12,"bold")).grid(row=0,column=2,padx=2,pady=3)

	ChangePasswordList.pack()

	#Lovely Code that will ensure Child Window remains active and Root remains inactive until Child is Closed 
	#After Clicking on Register Unit the new Window to Register Unit must be fully used and closed before using main interface
	ChangePassword.transient(master)
	ChangePassword.grab_set()
	master.wait_window(ChangePassword)
	
def Close_ChangePassword():
	ChangePassword.destroy()
	
def Clear_ChangePassword():
	ChangePasswordRegUserID.set("")
	ChangePasswordOldPassword.set("")
	ChangePasswordNewPassword1.set("")
	ChangePasswordNewPassword2.set("")

def ChangePasswordFunction():
	global ChangeCurrentUserID
	global ChangeCurrentPassword
	
	ChangeCurrentUserID = StringVar()
	ChangeCurrentPassword = StringVar()
	
	#Connection to the Database
	con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
	cur=con.cursor()
	#cur.execute("select * from register WHERE UserID = '" + ery2.get() + "' AND Password = '" + ery3.get() + "'")
	cur.execute("select * from register WHERE UserID = '" + ChangePasswordRegUserID.get() + "'")
	rows=cur.fetchall()
	populated=rows
	#print(populated)
	#For each record on the Database Record assign Price to each variables
	#for records in a as normal sales price
	for x in populated:
		ChangeCurrentUserID = x[0]
		ChangeCurrentPassword = x[1]
	
	#Condition to check if password provided exist
	if ChangePasswordRegUserID.get()=="":
		messagebox.showerror("Invalid Action","Your UserID is compulsory.")
	elif ChangePasswordOldPassword.get()=="":
		messagebox.showerror("Invalid Action","Your Old Password is compulsory.")
	elif ChangePasswordNewPassword1.get()=="":
		messagebox.showerror("Invalid Action","Your New Password 1 is compulsory.")
	elif ChangePasswordNewPassword2.get()=="":
		messagebox.showerror("Invalid Action","Your New Password 2 is compulsory.")
	elif ChangePasswordRegUserID.get() == ChangeCurrentUserID:
		if ChangePasswordOldPassword.get() == ChangeCurrentPassword: 
			if ChangePasswordNewPassword1.get() == ChangePasswordNewPassword2.get():
				#Connect to DB and Update the Password field of Register Table
				con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
				cur=con.cursor()
				cur.execute("update register set Password=%s where UserID=%s",(
															ChangePasswordNewPassword1.get(),
															ChangePasswordRegUserID.get()
															))
				con.commit()
				con.close()
				#Message box to indicate successfully changed
				messagebox.showinfo('Successfully Changed!',"Password Change was successful!\nProceed to Login with New Password")	
				#Clear Change Password
				Clear_ChangePassword()
				#Close Change Password
				Close_ChangePassword()
			else:
				messagebox.showerror("New Password Mismatch","Your New Password(s) does not match.")	
		else:
			messagebox.showerror("Invalid Old Password","Your Old Password is incorrect.")		
	else:
		messagebox.showerror("Invalid UserID","Your UserID does not exist.")
	
#This function will happen once the login is valid
def user_valid():
	global v, n
	v=ery2.get()
	n=ery3.get()
	global root
	
	#NEW OPERATION for Variables Globalized
	global CurrentUserID
	global CurrentPassword
	global CurrentFullName
	global CurrentPhone
	global CurrentRegVehicleNo
	global CurrentRedAddress
	global CurrentCategory
	global CurrentRegDateCreated
	
	CurrentUserID = StringVar()
	CurrentPassword = StringVar()
	CurrentFullName = StringVar()
	CurrentPhone = StringVar()
	CurrentRegVehicleNo = StringVar()
	CurrentRedAddress = StringVar()
	CurrentCategory = StringVar()
	CurrentRegDateCreated = StringVar()
	
	#Connection to the Database
	con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
	cur=con.cursor()
	#cur.execute("select * from register WHERE UserID = '" + ery2.get() + "' AND Password = '" + ery3.get() + "'")
	#Using User ID to check the Available Record in the Table: Register
	cur.execute("select * from register WHERE UserID = '" + ery2.get() + "'")
	rows=cur.fetchall()
	populated=rows
	#print(populated)
	for x in populated:
		CurrentUserID = x[0]
		CurrentPassword = x[1]
		CurrentFullName = x[2]
		CurrentPhone = x[3]
		CurrentRedAddress = x[4]
		CurrentCategory = x[5]
		CurrentRegVehicleNo = x[6]
		CurrentRegDateCreated = x[7]
	
	try:
		#if v.lower()=="admin" and n=="P@55#0rd" or v.lower()=="user" and n=="P@55w0rd" :      
		if v.lower()==CurrentUserID and n==CurrentPassword:
			#Exit the login dialog
			master.destroy()
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

			class Bill_App:
				def __init__(self,root):
					#Holder for record to be saved to Excel 
					mydata=[]
					driverdata=[]
					packagerdata=[]
					operaterdata=[]
					
					self.root=root
					#Title of the Application
					self.root.title("Kwambal Water @2020"+"   Active User: "+str(v))
					self.root.wm_iconbitmap('icon.ico')
					
					#This code enables the app to open in a maximized state
					root.state('zoomed')
					
					#I used the code below to ensure the app zooms to any system in use resolution
					width, height = root.winfo_screenwidth(), root.winfo_screenheight()
					root.geometry('%dx%d+0+0' % (width,height))
					
					#Assigning a Background Color to a Variable bg_color
					#bg_color="#074463"
					global bg_color
					bg_color="DarkGray"
					#The heading of the application
					#Text, Border, Style, Font Type, Size, Style, Background and Foreground Colors
					title=Label(self.root,text="Kwambal Water",bd=12,relief=GROOVE,font=("arial black",35,"bold"),bg="DarkGray",fg="DarkGreen")
					title.pack(side=TOP,fill=X)
					
					
					#To Know active running Function
					global RunningFunction
					RunningFunction=0
					
					#=======================All Variables
					#Grocery Items Variables
					self.BottleDispenser=IntVar()
					self.BigBottleWater=IntVar()
					self.SmallBottleWater=IntVar()
					self.SachetPureWater=IntVar()
					#Total Operation Menu Variables
					self.TotalBottleDispenser=StringVar()
					self.TotalBigBottleWater=StringVar()
					self.TotalSmallBottleWater=StringVar()
					self.TotalSachetPureWater=StringVar()
					self.TotalPayable=StringVar()
					#Customer Variables
					self.CName=StringVar()
					self.CPhone=StringVar() 
					self.BillNo=StringVar()
					self.TotalInventory=StringVar()
					self.SearchedSumation=StringVar()
					self.FromDateNormal=StringVar()
					self.ToDateNormal=StringVar()
					
					#New Bill Code Starting With YYMMDD
					yy=str(datetime.now()).split(' ')[0]
					yy=str((yy[2:]).replace('-',''))
					#print(yy)
					
					#Newly added line of x Datetime splited at the dot using index [1] as microsecond
					x=str(datetime.now()).split('.')[1]+str("N")
					
					randbillno=random.randint(10000,99999)
					#self.BillNo.set(str(randbillno))
					
					#Newly added line appending the microsecond to BillNo for uniqueness
					self.BillNo.set(yy+str(randbillno)+x)
					
					#-#self.SearchBill=StringVar()
					self.Total_Bill=StringVar()
					self.CurrentTime=StringVar()
					self.search_by=StringVar()
					self.search_txt=StringVar()
					#self.dateTimeObj=datetime.now()
					
					#=======================Customer detail frame
					F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("Arial",15,"bold"),fg="DarkRed",bg=bg_color)
					F1.place(x=0,y=92,relwidth=1)
					
					#Label for Customer Name, same background, black text
					cname_lbl=Label(F1,text="Name",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=2,pady=2)
					#Text field to Enter the Customer Name, SUNKEN
					global cname_txt
					cname_txt=Entry(F1,width=15,textvariable=self.CName,font="arial 13",bd=3,relief=SUNKEN)
					cname_txt.grid(row=0,column=1,pady=2,padx=2)
					cname_txt.focus()
					
					#Label for Customer Phone, same background, black text
					cphone_lbl=Label(F1,text="Mobile",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=2,pady=2)
					#Text field to Enter the Customer Phone, SUNKEN
					cphone_txt=Entry(F1,width=11,textvariable=self.CPhone,font="arial 13",bd=3,relief=SUNKEN).grid(row=0,column=3,pady=2,padx=2)
					
					#Label for Customer Bill, same background, black text
					cbill_lbl=Label(F1,text=" Bill No.",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=2,pady=2)
					#Text field to Enter the Customer BillNo, SUNKEN
					global cbill_txt
					cbill_txt=Entry(F1,width=18,textvariable=self.BillNo,font="arial 14",bd=3,relief=SUNKEN)
					cbill_txt.grid(row=0,column=5,pady=2,padx=2)
					cbill_txt.configure(state='disabled')
					
					global bill_btn
					#Button to Search Bill
					bill_btn=Button(F1,text="Find",command=self.Find_bill,width=6,bd=3,font="arial 12 bold")
					bill_btn.grid(row=0,column=6,padx=2,pady=2)
					bill_btn['state']='disabled'
					
					global FetchAllDB_btn
					#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ TRYING TO DO SOMETHING ON UPDATING PRICE
					#Removed button to add to DB by one self, automated adding into Generate Bill so line below for Add to DB button deactivated
					#AddtoDB_btn=Button(F1,text="Add to DB",command=self.Add_bills,width=10,bd=3,bg=bg_color,fg="DarkRed",font="arial 12 bold").grid(row=0,column=9,padx=2,pady=2)
					FetchAllDB_btn=Button(F1,text="Show ALL",command=self.fetch_data_all,width=10,bd=3,bg=bg_color,fg="DarkRed",font="arial 12 bold")
					FetchAllDB_btn.grid(row=0,column=9,padx=2,pady=2)
					FetchAllDB_btn['state']='disabled'
					
					#NEWLY to Search DB
					#ComboBox for Text area select kind of data to search
					combo_search=ttk.Combobox(F1,textvariable=self.search_by,width=12,font=("Arial",15,"normal"))
					#All variables for search
					combo_search['values']=("BillNo","Amount","DateStamp","Name","Phone","EnteredBy","UpdatedBy")
					#Position of combo box
					combo_search.grid(row=0,column=10,padx=2,pady=2)
					
					#Text Space to Type Data for Search
					#Addition of textvariable=self.search_txt
					txt_search=Entry(F1,textvariable=self.search_txt,width=25,bg="LightGray",fg="DarkBlue",font=("Arial",15,"normal"),bd=5,relief=GROOVE)
					txt_search.grid(row=0,column=11,pady=2,padx=2,sticky="w")
					
					#Button to Search DB
					#This button works with the Combo Search and Search text above
					#They must comply
					Search_btn=Button(F1,text="Search DB",command=self.search_data,width=10,bd=3,font="arial 12 bold").grid(row=0,column=13,padx=2,pady=2)
					
					#=======================Item Frame
					F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery Items",font=("Arial",15,"bold"),fg="DarkRed",bg=bg_color)
					F2.place(x=0,y=165,width=400,height=420)
					
					#Dispenser Bottle
					dbwater_lbl=Label(F2,text="Dispenser Bottle",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
					dbwater_txt=Entry(F2,width=10,textvariable=self.BottleDispenser,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
					
					#BIG Bottle water
					bbwater_lbl=Label(F2,text="BIG Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
					bbwater_txt=Entry(F2,width=10,textvariable=self.BigBottleWater,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
					
					#Small Bottle water
					sbwater_lbl=Label(F2,text="Small Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
					sbwater_txt=Entry(F2,width=10,textvariable=self.SmallBottleWater,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
					
					#Sachet Pure water
					spwater_lbl=Label(F2,text="Sachet Pure Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
					spwater_txt=Entry(F2,width=10,textvariable=self.SachetPureWater,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
					
					#=======================Bill Frame
					F3=LabelFrame(self.root,bd=10,relief=GROOVE)
					F3.place(x=405,y=165,width=340,height=415) 
					bill_title=Label(F3,text="Bills",font="arial 15 bold",bd=5,relief=GROOVE).pack(fill=X)
					scroll_y=Scrollbar(F3,orient=VERTICAL)
					self.txtarea=Text(F3,yscrollcommand=scroll_y.set)
					scroll_y.pack(side=RIGHT,fill=Y)
					scroll_y.config(command=self.txtarea.yview)
					self.txtarea.pack(fill=BOTH,expand=1)
					
					#=======================Side Frame
					Table_Frame=LabelFrame(self.root,bd=10,relief=RIDGE,bg=bg_color)
					Table_Frame.place(x=750,y=165,width=685,height=415)
					
					#DISPLAY FOR ALL BILL ENTRY
					scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
					scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
					#Format for the required column headings that will be displayed
					self.Bill_table=ttk.Treeview(Table_Frame,columns=("BillNo","Dispenser","BigBottle","SmallBottle","SachetWater","CostDispenser","CostBigBottle","CostSmallBottle","CostSachetWater","Amount","DateStamp","Name","Phone","EnteredBy","PreviousTotal","UpdatedBy","UpdatedDate",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
					
					#Scroll bar direction and configuration
					scroll_x.pack(side=BOTTOM,fill=X)
					scroll_y.pack(side=RIGHT,fill=Y)
					scroll_x.config(command=self.Bill_table.xview)
					scroll_y.config(command=self.Bill_table.yview)		
					
					#Connecting each heading to a column of the exisiting fields
					self.Bill_table.heading("BillNo",text="BillNo")
					self.Bill_table.heading("Dispenser",text="Dispenser")
					self.Bill_table.heading("BigBottle",text="BigBottle")
					self.Bill_table.heading("SmallBottle",text="SmallBottle")
					self.Bill_table.heading("SachetWater",text="SachetWater")
					self.Bill_table.heading("CostDispenser",text="CostDispenser")
					self.Bill_table.heading("CostBigBottle",text="CostBigBottle")
					self.Bill_table.heading("CostSmallBottle",text="CostSmallBottle")
					self.Bill_table.heading("CostSachetWater",text="CostSachetWater")
					self.Bill_table.heading("Amount",text="Amount")
					self.Bill_table.heading("DateStamp",text="DateStamp")
					self.Bill_table.heading("Name",text="Name")
					self.Bill_table.heading("Phone",text="Phone")
					self.Bill_table.heading("EnteredBy",text="EnteredBy")
					self.Bill_table.heading("PreviousTotal",text="PreviousTotal")
					self.Bill_table.heading("UpdatedBy",text="UpdatedBy")
					self.Bill_table.heading("UpdatedDate",text="UpdatedDate")
					#Enable heading of tables to show
					self.Bill_table['show']='headings'
					
					#Set column width for each field in the table
					self.Bill_table.column("BillNo",width=120)
					self.Bill_table.column("Dispenser", anchor="center", width=80)
					self.Bill_table.column("BigBottle", anchor="center", width=80)
					self.Bill_table.column("SmallBottle", anchor="center", width=80)
					self.Bill_table.column("SachetWater", anchor="center", width=80)
					self.Bill_table.column("CostDispenser", anchor="center", width=80)
					self.Bill_table.column("CostBigBottle", anchor="center", width=80)
					self.Bill_table.column("CostSmallBottle", anchor="center", width=100)
					self.Bill_table.column("CostSachetWater", anchor="center", width=100)
					#anchor="e" simply means align to east i.e. right align
					self.Bill_table.column("Amount", anchor="e", width=100)
					self.Bill_table.column("DateStamp",width=150)
					self.Bill_table.column("Name",width=120)
					self.Bill_table.column("Phone", anchor="center", width=120)
					self.Bill_table.column("EnteredBy", anchor="center", width=120)
					self.Bill_table.column("PreviousTotal", anchor="center", width=120)
					self.Bill_table.column("UpdatedBy", anchor="center", width=120)
					self.Bill_table.column("UpdatedDate", anchor="center", width=120)
					#To expand the table  
					self.Bill_table.pack(fill=BOTH,expand=1)
					#Enable selection of items in the Bill_table
					self.Bill_table.bind("<ButtonRelease-1>",self.get_cursor)
				
				
									
					#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ printing button in side frame
					#print_btn=Button(F33,command=self.Print_bill,text="Print",bg=bg_color,fg="blue",bd=3,pady=30,width=10,font="ArialBold 15 bold").grid(row=0,column=0,padx=5,pady=5)
					
					
					#=======================Total Operation and Button Frame
					F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Operation Menu",font=("Arial",15,"bold"),fg="DarkRed",bg=bg_color)
					F4.place(x=0,y=585,relwidth=1,height=170)
					#Total Cost of Dispenser Label and Text Area, ReadOnly
					t1_lbl=Label(F4,text="Total Dispenser Bottle",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=1,sticky="w")	
					t1_txt=Entry(F4,width=17,textvariable=self.TotalBottleDispenser,font="arial 10 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=1,padx=10,pady=1)

					#Total Cost of BIG Bottle Water Label and Text Area, ReadOnly
					t2_lbl=Label(F4,text="Total BIG Bottle Water",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=1,sticky="w")	
					t2_txt=Entry(F4,width=17,textvariable=self.TotalBigBottleWater,font="arial 10 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=1,column=1,padx=10,pady=1)

					#Total Cost of Small Bottle Water Label and Text Area, ReadOnly
					t3_lbl=Label(F4,text="Total Small Bottle Water",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=1,sticky="w")	
					t3_txt=Entry(F4,width=17,textvariable=self.TotalSmallBottleWater,font="arial 10 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=2,column=1,padx=10,pady=1)

					#Total Cost of Sachet Pure Water Label and Text Area, ReadOnly
					t4_lbl=Label(F4,text="Total Sachet Pure Water",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=1,sticky="w")	
					t4_txt=Entry(F4,width=17,textvariable=self.TotalSachetPureWater,font="arial 10 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=3,column=1,padx=10,pady=1)		
					
					#=======================Control Button Frame
					btn_F=Frame(F4,bd=3,relief=GROOVE)
					btn_F.place(x=395,width=340,height=120)
					
					#Buttons
					global total_btn
					total_btn=Button(btn_F,command=self.total,text="Total",bg=bg_color,fg="blue",bd=3,pady=5,width=13,font="ArialBold 15 bold")
					total_btn.grid(row=0,column=0,padx=2,pady=2)
					total_btn['state']='normal'
					#Function Bill_Area added to the Generate Button
					
					#Global the variable of the button to enable use in all DB
					global gbill_btn
					#Seperate each of the assignment to enable modification of specific one, ['state'] which is 'normal' or 'disabled'
					gbill_btn=Button(btn_F,text="Generate Bill",command=self.Add_bills,bg=bg_color,fg="green",bd=3,pady=5,width=13,font="ArialBold 15 bold")
					gbill_btn.grid(row=1,column=0,padx=2,pady=2)
					#Enabling the Generate Button to be normal from initial startup
					gbill_btn['state']='normal'
					
					clear_btn=Button(btn_F,text="Clear",command=self.Clear_data,bg=bg_color,fg="black",bd=3,pady=5,width=12,font="ArialBold 15 bold").grid(row=0,column=1,padx=2,pady=2)
					#exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg=bg_color,fg="red",bd=3,pady=5,width=12,font="ArialBold 15 bold").grid(row=1,column=1,padx=2,pady=2)
					print_btn=Button(btn_F,text="Print Bill",command=self.Print_bill,bg=bg_color,fg="red",bd=3,pady=5,width=12,font="ArialBold 15 bold").grid(row=1,column=1,padx=2,pady=2)
							
					#This function runs automatically to display message in Bill Area
					#self.Welcome_bill()
					self.ClearWelcome_bill()
					
					#Automatically focus cursor in search space when search criteria is chosen
					self.AutoFocusSearch()
					
					#=======================Bottom Frame
					F5=LabelFrame(self.root,bd=10,relief=GROOVE,bg=bg_color)
					F5.place(x=0,y=755,relwidth=1,height=80)
					
					#Total Cost of Dispenser Label and Text Area, ReadOnly
					t5_lbl=Label(F5,text="***Total Payable    ",bg=bg_color,fg="DarkRed",font=("times new roman",18,"bold")).grid(row=0,column=1,padx=10,pady=1,sticky="w")	
					t5_txt=Entry(F5,width=12,textvariable=self.TotalPayable,fg="DarkRed",font="ArialBold 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=2,padx=10,pady=1)
							
					#Time Frame:
					CurrentTime_txt=Entry(F5,width=30,textvariable=self.CurrentTime,fg="black",font="ArialBold 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=4,padx=10,pady=1)
					
					
					global UpdateUnitPrice_btn		
					#New Button to Open New Page for Unit Price Updating
					UpdateUnitPrice_btn=Button(F5,text="Update Price",command=self.createNewWindow,bg=bg_color,fg="blue",bd=3,pady=5,width=12,font="ArialBold 10 bold")
					UpdateUnitPrice_btn.grid(row=0,column=5,padx=2,pady=2)
					UpdateUnitPrice_btn['state']='disabled'

					global DriverUnit_btn
					#New Button to Open New Page for Driver Unit
					DriverUnit_btn=Button(F5,text="Driver",command=self.createDriverUnit,bg=bg_color,fg="blue",bd=3,pady=5,width=8,font="ArialBold 10 bold")
					DriverUnit_btn.grid(row=0,column=6,padx=2,pady=2)
					DriverUnit_btn['state']='disabled'
					
					global OperateUnit_btn
					#New Button to Open New Page for Package Unit
					OperateUnit_btn=Button(F5,text="Operator",command=self.createOperateUnit,bg=bg_color,fg="blue",bd=3,pady=5,width=8,font="ArialBold 10 bold")
					OperateUnit_btn.grid(row=0,column=7,padx=2,pady=2)
					OperateUnit_btn['state']='disabled'
										
					global PackageUnit_btn
					#New Button to Open New Page for Package Unit
					PackageUnit_btn=Button(F5,text="Packager",command=self.createPackageUnit,bg=bg_color,fg="blue",bd=3,pady=5,width=8,font="ArialBold 10 bold")
					PackageUnit_btn.grid(row=0,column=8,padx=2,pady=2)
					PackageUnit_btn['state']='disabled'
					
					global SaveToExcel_btn
					#New Button to Open New Page for Package Unit
					SaveToExcel_btn=Button(F5,text="SaveToExcel",command=self.SaveCurrentTableItem,bg=bg_color,fg="DarkGreen",bd=3,pady=5,width=11,font="ArialBold 10 bold")
					SaveToExcel_btn.grid(row=0,column=9,padx=2,pady=2)
					SaveToExcel_btn['state']='disabled'
					
					global AllDBToExcel_btn
					#New Button to Open New Page for Package Unit
					AllDBToExcel_btn=Button(F5,text="AllDBToExcel",command=self.SaveToCSVandExcel,bg=bg_color,fg="DarkGreen",bd=3,pady=5,width=11,font="ArialBold 10 bold")
					AllDBToExcel_btn.grid(row=0,column=11,padx=2,pady=2)
					AllDBToExcel_btn['state']='disabled'
					
					global ManageUser_btn
					#New Button to Open New Page for Package Unit
					ManageUser_btn=Button(F5,text="Manage Users",command=self.CreateManageUser,bg=bg_color,fg="Black",bd=3,pady=5,width=12,font="ArialBold 10 bold")
					ManageUser_btn.grid(row=0,column=12,padx=2,pady=2)
					ManageUser_btn['state']='disabled'
				
					#======================= 2nd bottom right Control Button Frame
					btn_F2=Frame(F4,bd=3,relief=GROOVE)
					btn_F2.place(x=740,width=675,height=55)
					
					t6_lbl=Label(btn_F2,text="Sub-Total",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=1,sticky="w")	
					t6_txt=Entry(btn_F2,width=18,textvariable=self.SearchedSumation,fg="red",font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=1,padx=10,pady=1)
					
					t7_lbl=Label(btn_F2,text="TOTAL",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=10,pady=1,sticky="w")	
					t7_txt=Entry(btn_F2,width=19,textvariable=self.TotalInventory,fg="red",font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=3,padx=10,pady=1)
					
					
					btn_F22=Frame(F4,bd=3,relief=GROOVE)
					btn_F22.place(x=740,y=60,width=338,height=60)
					
					global UpdateRecord_btn
					#This button will automatically Update selected record on DB and the Text File and Generate Bills Simultaneously
					UpdateRecord_btn=Button(btn_F22,text="Update Record",command=self.UpdateDB_data,bg=bg_color,fg="blue",bd=3,pady=5,width=13,font="ArialBold 14 bold")
					UpdateRecord_btn.grid(row=0,column=0,padx=2,pady=2)
					UpdateRecord_btn['state']='disabled'
					
					global DeleteRecord_btn
					#This button will delete the record on the DB and also that of the text file
					DeleteRecord_btn=Button(btn_F22,text="Delete Record",command=self.DeleteDBandText_data,bg=bg_color,fg="red",bd=3,pady=5,width=12,font="ArialBold 14 bold")
					DeleteRecord_btn.grid(row=0,column=1,padx=2,pady=2)
					DeleteRecord_btn['state']='disabled'
					
					#REPORT SECTION
					btn_F222=Frame(F4,bd=3,relief=GROOVE)
					btn_F222.place(x=1083,y=60,width=333,height=60)
					
					t5_lbl=Label(btn_F222,text="*****REPORT****",bg=bg_color,fg="DarkRed",font=("times new roman",10,"bold")).grid(row=0,column=0,padx=4,pady=0,sticky="w")
					
					global fromtextnormal
					fromlabel=Label(btn_F222,text="From: ",bg=bg_color,fg="black",font=("times new roman",12,"bold")).grid(row=0,column=1,padx=15,pady=0,sticky="w")
					fromtextnormal=Entry(btn_F222,width=11,textvariable=self.FromDateNormal,fg="black",font="ArialBold 12 bold",bd=3,relief=SUNKEN,state='normal')
					fromtextnormal.grid(row=0,column=2,padx=1,pady=0)
					#fromtextnormal.focus()
					
					global totextnormal
					tolabel=Label(btn_F222,text="To:::::",bg=bg_color,fg="black",font=("times new roman",12,"bold")).grid(row=1,column=1,padx=15,pady=0,sticky="w")
					totextnormal=Entry(btn_F222,width=11,textvariable=self.ToDateNormal,fg="black",font="ArialBold 12 bold",bd=3,relief=SUNKEN,state='normal')
					totextnormal.grid(row=1,column=2,padx=1,pady=0)
					#totextnormal.focus()
					
					global ReportNormal_btn
					#This button will generate report
					ReportNormal_btn=Button(btn_F222,text="Generate Report",command=self.GenerateReport_Normal,bg=bg_color,fg="Green",bd=3,pady=0,width=14,font="ArialBold 10 bold")
					ReportNormal_btn.grid(row=1,column=0,padx=2,pady=0)
					ReportNormal_btn['state']='disabled'
					
					#NEWLY ADDED to Search
					#self.DBTOTAL()
					
					#Function to Clear data and input dd/mm/yyyy into FROM and TO of REPORT
					self.ResetFromTo()
					
					#This function will constantly fetch the DB data and it has the self.DBTOTAL() function inside it
					self.fetch_data()
					
					self.user_type()
					
					#Display All DB DISABLED so the ADMIN will click on DISPLAY ALL HIM/HERSELF to see ALL
					#-#self.fetch_data_all()
				
					#Default folder to save all bills in txt files
					global directory
					directory="C:/Bills/"
				
				#Function to enable Admin more privileges
				def user_type(self):
					if CurrentCategory == 'Super-Admin':
						#self.fetch_data_all()
						DeleteRecord_btn['state']='normal'
						UpdateRecord_btn['state']='normal'
						SaveToExcel_btn['state']='normal'
						AllDBToExcel_btn['state']='normal'
						UpdateUnitPrice_btn['state']='normal'
						FetchAllDB_btn['state']='normal'
						ManageUser_btn['state']='normal'
						ReportNormal_btn['state']='normal'
						bill_btn['state']='normal'
						DriverUnit_btn['state']='normal'
						PackageUnit_btn['state']='normal'
						OperateUnit_btn['state']='normal'
					elif CurrentCategory == 'Admin':
						UpdateRecord_btn['state']='normal'
						UpdateUnitPrice_btn['state']='normal'
						FetchAllDB_btn['state']='normal'
						DriverUnit_btn['state']='normal'
						PackageUnit_btn['state']='normal'
						OperateUnit_btn['state']='normal'
				
				def CreateManageUser(self):
					global RegUserID
					global RegPassword
					global RegName
					global RegPhone
					global RegVehicleNo
					global RegAddress
					global RegCategory
					global RegDateCreated
					global RegSearch_by
					global RegSearch_txt
					
					RegUserID=StringVar()
					RegPassword=StringVar()
					RegName=StringVar()
					RegPhone=StringVar()
					RegVehicleNo=StringVar()
					RegAddress=StringVar()
					RegCategory=StringVar()
					RegDateCreated=StringVar()
					RegSearch_by=StringVar()
					RegSearch_txt=StringVar()
				
					global Register
					Register = tk.Toplevel(root)
					Register.title("All Personnel")
					Register.focus()
					RegisterList = tk.Label(Register, text = "Personnel Role Management",bd=5,relief=GROOVE,font=("arial black",15,"bold"),bg="DarkGray",fg="DarkGreen")
					RegisterList.pack(side=TOP,fill=X)
					Register.geometry("750x455+350+170")
					RegisterList.pack()
					

					#=======================Personnel detail frame
					Personnel=LabelFrame(Register,bd=10,relief=GROOVE,text="Personnel Details",font=("Arial",15,"bold"),fg="DarkRed",bg=bg_color)
					Personnel.place(x=0,y=32,relwidth=1,height=215)
					
					#RegCategory 
					global combo_RegCategory
					RegCategory_lbl=Label(Personnel,text="Category ",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=5,pady=2)	
					combo_RegCategory=ttk.Combobox(Personnel,textvariable=RegCategory,width=25,font="arial 11 bold",state='readonly')
					combo_RegCategory['values']=("Super-Admin","Admin","Employee","Driver","Operator","Packager")
					combo_RegCategory.bind('<<ComboboxSelected>>', self.getPlateNo)
					combo_RegCategory.grid(row=0,column=1,padx=5,pady=2)
					combo_RegCategory.focus()
					combo_RegCategory['state']='normal'
					
					#Label for RegVehicleNo
					RegPlateNo_lbl=Label(Personnel,text="Vehicle No.",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=25,pady=2)
					global RegVehicleNo_txt
					RegVehicleNo_txt=Entry(Personnel,width=24,textvariable=RegVehicleNo,font="arial 12 bold",bd=3,relief=SUNKEN,state='readonly')
					RegVehicleNo_txt.grid(row=0,column=3,pady=2,padx=2)
					RegVehicleNo_txt.focus()
					
					#Label for RegUserID
					RegUserID_lbl=Label(Personnel,text="UserName",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=5,pady=2)
					global RegUserID_txt
					RegUserID_txt=Entry(Personnel,width=24,textvariable=RegUserID,fg="blue",font="arial 12 bold",bd=3,relief=SUNKEN)
					RegUserID_txt.grid(row=1,column=1,pady=2,padx=2)
					RegUserID_txt.focus()
					
					#Label for RegPassword
					RegPassword_lbl=Label(Personnel,text="Password",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=1,column=2,padx=25,pady=2)
					global RegPassword_txt
					RegPassword_txt=Entry(Personnel,show="*",width=24,textvariable=RegPassword,fg="red",font="arial 12 bold",bd=3,relief=SUNKEN,state='normal')
					RegPassword_txt.grid(row=1,column=3,pady=2,padx=2)
					RegPassword_txt.focus()
					
					#Label for RegName
					RegName_lbl=Label(Personnel,text="FullName ",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=5,pady=2)
					global RegName_txt
					RegName_txt=Entry(Personnel,width=24,textvariable=RegName,font="arial 12 bold",bd=3,relief=SUNKEN)
					RegName_txt.grid(row=2,column=1,pady=2,padx=2)
					RegName_txt.focus()
					
					#Label for RegPhone
					RegPhone_lbl=Label(Personnel,text="Mobile No.",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=2,column=2,padx=25,pady=2)
					global RegPhone_txt
					RegPhone_txt=Entry(Personnel,width=24,textvariable=RegPhone,font="arial 12 bold",bd=3,relief=SUNKEN)
					RegPhone_txt.grid(row=2,column=3,pady=2,padx=2)
					RegPhone_txt.focus()
					
					#Label for RegAddress
					RegAddress_lbl=Label(Personnel,text="Address ",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=5,pady=2)
					global RegAddress_txt
					RegAddress_txt=Entry(Personnel,width=67,textvariable=RegAddress,font="arial 12 bold",bd=3,relief=SUNKEN)
					RegAddress_txt.grid(row=3,column=1,columnspan=3,pady=2,padx=2)
					RegAddress_txt.focus()
					
					#Label for RegDateCreated
					RegDateCreated_lbl=Label(Personnel,text="DateStamp",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=4,column=0,padx=5,pady=2)
					global RegDateCreated_txt
					RegDateCreated_txt=Entry(Personnel,width=24,textvariable=RegDateCreated,fg="green",font="arial 12 bold",bd=3,relief=SUNKEN,state='readonly')
					RegDateCreated_txt.grid(row=4,column=1,pady=2,padx=2)
					RegDateCreated_txt.focus()

					#=======================Control frame
					btn_Frame=LabelFrame(Register,bd=8,relief=RIDGE,bg=bg_color)
					btn_Frame.place(x=0,y=247,relwidth=1,height=55)
					
					#Adding buttons to perform different actions
					#Different commands will be added to this buttons to perform actions upon click
					#The add_staff function will be added to Addbtn: command=self.add_staff (test it, confirm data in DB)
					Addbtn=Button(btn_Frame,text="Add",width=7,command=self.Add_RegRecord,fg="Blue",font=("Arial",12,"bold")).grid(row=0,column=0,padx=4,pady=3)
					
					#The update function will be added here to Updatebtn: command=self.update_data
					Updatebtn=Button(btn_Frame,text="Update",width=7,command=self.Update_RegDB,fg="Green",font=("Arial",12,"bold")).grid(row=0,column=1,padx=4,pady=3)
					
					global Deletebtn
					#The delete function will be added here to Deletebtn: command=self.delete_data 
					Deletebtn=Button(btn_Frame,text="Delete",width=7,command=self.Delete_RegData,fg="Red",font=("Arial",12,"bold"))
					Deletebtn.grid(row=0,column=2,padx=4,pady=3)
					Deletebtn['state']='normal'
					
					#The clear function will be added to Clearbtn: command=self.clear to enable clear the visible data
					Clearbtn=Button(btn_Frame,text="Clear",width=7,command=self.Clear_RegData,fg="Black",font=("Arial",12,"bold")).grid(row=0,column=3,padx=4,pady=3)
					
					
					#NEWLY to Search DB
					#ComboBox for Text area select kind of data to search
					combo_Search_By=ttk.Combobox(btn_Frame,textvariable=RegSearch_by,width=8,font=("Arial",15,"normal"))
					#All variables for search
					combo_Search_By['values']=("UserID","Password","FullName","MobileNo","Address","Category","VehicleNo","DateStamp")
					#Position of combo box
					combo_Search_By.grid(row=0,column=4,padx=2,pady=2)
					
					#Text Space to Type Data for Search
					#Addition of textvariable=self.search_txt
					txt_Search_Txt=Entry(btn_Frame,textvariable=RegSearch_txt,width=13,bg="LightGray",fg="DarkBlue",font=("Arial",15,"normal"),bd=5,relief=GROOVE)
					txt_Search_Txt.grid(row=0,column=5,pady=2,padx=2,sticky="w")
					
					#Button to Search DB
					#This button works with the Combo Search and Search text above
					#They must comply
					Search_btn=Button(btn_Frame,text="Search DB",command=self.RegSearch_data,width=9,bd=3,font="arial 12 bold").grid(row=0,column=6,padx=2,pady=2)		
								
					#=======================Personnel Table
					PersonnelTable_Frame=LabelFrame(Register,bd=10,relief=RIDGE,bg=bg_color)
					PersonnelTable_Frame.place(x=0,y=302,relwidth=1,height=150)
				
					#=======================DISPLAY FOR ALL REGISTERED PERSONNEL
					scroll_x=Scrollbar(PersonnelTable_Frame,orient=HORIZONTAL)
					scroll_y=Scrollbar(PersonnelTable_Frame,orient=VERTICAL)
					#Format for the required column headings that will be displayed
					global PersonnelBill_table
					PersonnelBill_table=ttk.Treeview(PersonnelTable_Frame,columns=("UserID","Password","FullName","MobileNo","Address","Category","VehicleNo","DateStamp"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
					
					#Scroll bar direction and configuration
					scroll_x.pack(side=BOTTOM,fill=X)
					scroll_y.pack(side=RIGHT,fill=Y)
					scroll_x.config(command=PersonnelBill_table.xview)
					scroll_y.config(command=PersonnelBill_table.yview)		
					
					#Connecting each heading to a column of the existing fields
					PersonnelBill_table.heading("UserID",text="UserID")
					PersonnelBill_table.heading("Password",text="Password")
					PersonnelBill_table.heading("FullName",text="FullName")
					PersonnelBill_table.heading("MobileNo",text="MobileNo")
					PersonnelBill_table.heading("Address",text="Address")
					PersonnelBill_table.heading("Category",text="Category")
					PersonnelBill_table.heading("VehicleNo",text="VehicleNo")
					PersonnelBill_table.heading("DateStamp",text="DateStamp")
					
					
					#Enable heading of tables to show
					PersonnelBill_table['show']='headings'
					
					#Set column width for each field in the table
					PersonnelBill_table.column("UserID",width=90)
					PersonnelBill_table.column("Password", anchor="center", width=10)
					PersonnelBill_table.column("FullName",width=80)
					PersonnelBill_table.column("MobileNo", anchor="center", width=80)
					PersonnelBill_table.column("Address",width=80)
					PersonnelBill_table.column("Category", anchor="center", width=100)
					PersonnelBill_table.column("VehicleNo", anchor="center", width=100)
					PersonnelBill_table.column("DateStamp",width=100)

					#To expand the table  
					PersonnelBill_table.pack(fill=BOTH,expand=1)
					#Enable selection of items in the Bill_table
					PersonnelBill_table.bind("<ButtonRelease-1>",self.PersonnelBillget_cursor)
					
					#To avoid application hanging to lack of DB connection
					try:
						#Fetch all data from DB
						self.RegisterFetchDB_data()
					except pymysql.err.OperationalError:
						#Friendly message to connect DB and restart app
						messagebox.showerror("Database Connection Error","Connect the Database and Restart Application")
						exit()
					
					RegisterList.pack()
					
					#Lovely Code that will ensure Child Window remains active and Root remains inactive until Child is Closed 
					#After Clicking on Register Unit the new Window to Register Unit must be fully used and closed before using main interface
					Register.transient(root)
					Register.grab_set()
					root.wait_window(Register)
				
				def getPlateNo(self, event):
					#Enable the Vehicle Plate Number field if Category is Driver
					if RegCategory.get()=="Driver":
						RegVehicleNo_txt.config(state=NORMAL)
						RegPassword_txt.config(state=DISABLED)
					elif RegCategory.get()=="Operator" or RegCategory.get()=="Packager":
						RegVehicleNo_txt.config(state=DISABLED)
						RegPassword_txt.config(state=DISABLED)
					else:
						RegVehicleNo.set("")
						RegVehicleNo_txt.config(state=DISABLED)
						RegPassword_txt.config(state=NORMAL)
				
				def RegSearch_data(self):
					try:
						#If one or both of the criteria is/are empty
						if RegSearch_by.get()=="" or RegSearch_txt.get()=="":
							messagebox.showerror("Search Error","Select Search by and \nType correct keyword")
						else:
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("select * from register where "+str(RegSearch_by.get())+" LIKE '%"+str(RegSearch_txt.get())+"%'")
							rows=cur.fetchall()
							if len(rows)!=0:
								PersonnelBill_table.delete(*PersonnelBill_table.get_children())
								for row in rows:
									PersonnelBill_table.insert('',END,values=row)
								con.commit()
							con.close()
							#Auto focus the last record from the records returned after search (highlight the first row automatically)
							child_id = PersonnelBill_table.get_children()[-1]
							cursor_row=PersonnelBill_table.focus(child_id)
							PersonnelBill_table.selection_set(child_id)
							self.PersonnelBillget_cursor(cursor_row)
					except:
						pass
						
				def PersonnelBillget_cursor(self,ev):
					try:
						cursor_row=PersonnelBill_table.focus()
						contents=PersonnelBill_table.item(cursor_row)
						row=contents['values']
						RegUserID.set(row[0])
						RegPassword.set(row[1])
						RegName.set(row[2])
						RegPhone.set(row[3])
						RegAddress.set(row[4])
						RegCategory.set(row[5])
						RegVehicleNo.set(row[6])
						RegDateCreated.set(row[7])
					except IndexError:
						pass
					#Disable Deleting of Super-Admin
					#Disable Changing of Super-Admin Role
					if RegCategory.get()=="Super-Admin":
						Deletebtn['state']='disabled'
						combo_RegCategory['state']='disabled'
					else:
						Deletebtn['state']='normal'
						combo_RegCategory['state']='normal'
					
					#Disable and Enable the Password Field
					if RegCategory.get()=="Driver" or RegCategory.get()=="Operator" or RegCategory.get()=="Packager":
						RegPassword_txt.config(state=DISABLED)
					else:
						RegPassword_txt.config(state=NORMAL)
					
					#Disable and Enable the VehicleNo Field
					if RegCategory.get()=="Driver":
						RegVehicleNo_txt.config(state=NORMAL)
					else:
						RegVehicleNo_txt.config(state=DISABLED)
				
				#Function to Modifying the format for DatePrepare and DatePaid
				def mynice_date(self):
					todaydate = datetime.now()                    
					lastpart=str(datetime.now()).split(' ')[1]
					new_today_date = todaydate.strftime("%d/%m/%Y")
					global today_date                    
					today_date = new_today_date+" "+lastpart                    
					return today_date
				
				def Add_RegRecord(self):
					try:
						if RegCategory.get() == "":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nCategory is mandatory!")
							RegCategory_txt.focus()
						
						elif RegCategory.get() == "Driver" and RegVehicleNo.get()=="":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nVechile Number is mandatory!")
							RegVehicleNo_txt.focus()
						
						elif RegUserID.get()=="":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nUserId is mandatory!")
							RegUserID_txt.focus()
							
						elif RegPassword_txt.config(state=NORMAL) == True:
							messagebox.showerror("Add Data Error","Kindly make valid entry\nPassword is mandatory!")
							RegPassword_txt.focus()
							
						elif RegName.get()=="":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nFull Name is mandatory!")
							RegName_txt.focus()
							
						elif RegPhone.get()=="":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nPhone Number is mandatory!")
							RegPhone_txt.focus()
							
						else:
							ask=messagebox.askyesno("Add New Personnel","Do you really want to ADD this record?")
							if ask==True:
								#Capture the DateTIme Created
								self.mynice_date()
								##y=str(datetime.now())
								RegDateCreated.set(today_date)
								con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
								cur=con.cursor()
								cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",(RegUserID.get(),
																								RegPassword.get(),
																								RegName.get(),
																								RegPhone.get(),
																								RegAddress.get(),
																								RegCategory.get(),
																								RegVehicleNo.get(),
																								RegDateCreated.get()
																								))
						
								con.commit()
								#Function of fetch_data is called here
								self.RegisterFetchDB_data()
								messagebox.showinfo('Successfully Added!',"Record of " +RegUserID.get()+ " was successfully added")
								self.Clear_RegData()
								con.close()
								
					except pymysql.err.IntegrityError:
						messagebox.showerror("Duplicate Error","UserID already exist")
							
				def Update_RegDB(self):
					
					if RegCategory.get() == "":
						messagebox.showerror("Add Data Error","Kindly make valid entry\nCategory is mandatory!")
						RegCategory_txt.focus()
					
					elif RegCategory.get() == "Driver" and RegVehicleNo.get()=="":
						messagebox.showerror("Add Data Error","Kindly make valid entry\nVechile Number is mandatory!")
						RegVehicleNo_txt.focus()
					
					elif RegUserID.get()=="":
						messagebox.showerror("Add Data Error","Kindly make valid entry\nUserId is mandatory!")
						RegUserID_txt.focus()
						
					elif RegPassword_txt.config(state=NORMAL) == True:
						messagebox.showerror("Add Data Error","Kindly make valid entry\nPassword is mandatory!")
						RegPassword_txt.focus()
						
					elif RegName.get()=="":
						messagebox.showerror("Add Data Error","Kindly make valid entry\nFull Name is mandatory!")
						RegName_txt.focus()
						
					elif RegPhone.get()=="":
						messagebox.showerror("Add Data Error","Kindly make valid entry\nPhone Number is mandatory!")
						RegPhone_txt.focus()	

					else:
						ask=messagebox.askyesno("Update Record","Are you sure to proceed with update!")
						if ask==True:
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("update register set Password=%s,FullName=%s,MobileNo=%s,Address=%s,Category=%s,VehicleNo=%s,DateStamp=%s where UserID=%s",(
																																				RegPassword.get(),
																																				RegName.get(),
																																				RegPhone.get(),
																																				RegAddress.get(),
																																				RegCategory.get(),
																																				RegVehicleNo.get(),
																																				RegDateCreated.get(),
																																				RegUserID.get()
																																				))
							con.commit()

							#NEWLY To auto focus the selection Balanced is performed on any selected Record
							#Using variable xx and yy to get the current fucos and index of the focus iid
							#This is done before the fetching of Database from DB to the TreeView
							xx=PersonnelBill_table.focus()
							yy=PersonnelBill_table.index(xx)
							#print(yy)				
							
							#Function of fetch_data is called here
							self.RegisterFetchDB_data()

							#NEWLY To auto focus the selection Balanced selected Record
							child_id = PersonnelBill_table.get_children()[yy]
							cursor_row=PersonnelBill_table.focus(child_id)
							PersonnelBill_table.selection_set(child_id)
							messagebox.showinfo('Successfully Update!',"Record of " +RegUserID.get()+ " was successfully updated")
							self.Clear_RegData()
							con.close()	
					
				def RegisterFetchDB_data(self):
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					#Sorting the data fetched to display in descending order of DateStamp
					cur.execute("select * from register order by Category, DateStamp DESC")
					rows=cur.fetchall()
					if len(rows)!=0:
						PersonnelBill_table.delete(*PersonnelBill_table.get_children())
						for row in rows:
							PersonnelBill_table.insert('',END,values=row)
						con.commit()
					con.close()
					
				
				def Delete_RegData(self):
					#This function delete current selected record
					ask=messagebox.askyesno("Deleting Record","Are you sure to proceed with delete! \nYou cannot undo this action")
					if ask==True:
						con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
						cur=con.cursor()
						cur.execute("delete from register where UserID=%s",RegUserID.get())
						con.commit()
						con.close()
						#Function of fetch_data is called here
						self.RegisterFetchDB_data()
						#Function to clear the data from interface after Delete from DB
						self.Clear_RegData()
					
				def Clear_RegData(self):
					RegUserID.set("")
					RegPassword.set("")
					RegName.set("")
					RegPhone.set("")
					RegAddress.set("")
					RegCategory.set("")
					RegVehicleNo.set("")
					RegDateCreated.set("")
					RegSearch_by.set("")
					RegSearch_txt.set("")
					
					RegUserID_txt.focus()
					
					#Clear highlight of selected record
					PersonnelBill_table.selection_set()
					
					#Function of fetch_data is called here
					self.RegisterFetchDB_data()
					
					#Enable the Category Field
					combo_RegCategory['state']='normal'
					RegVehicleNo_txt['state']='normal'
					RegPassword_txt['state']='normal'
					
				#New Function to Create new window for Driver Unit
				def createDriverUnit(self):
					
					#Assign 1 to variable RunningFunction
					RunningFunction=1
					
					global GivenTotal
					global ReturnedTotal
					global DamagedTotal
					global SoldTotal
					
					global GivenDBPrice
					global GivenBBWPrice
					global GivenSBWPrice
					global GivenSPWPrice
					
					global ReturnedDBPrice
					global ReturnedBBWPrice
					global ReturnedSBWPrice
					global ReturnedSPWPrice
					
					global DamagedDBPrice
					global DamagedBBWPrice
					global DamagedSBWPrice
					global DamagedSPWPrice
					
					global SoldDBPrice
					global SoldBBWPrice
					global SoldSBWPrice
					global SoldSPWPrice
					
					global DriverName
					global DriverPhone
					global DriverPlateNumber
					global DriverBillNumber
					global DriverIssuedDateStamp
					global DriverBalancedDateStamp
					
					global DriverSearch
					global DriverSearch_Txt
					global DriverSearchedSumation
					global DriverTotalInventory
					
					global FromDriverReport
					global ToDriverReport
					
					DriverName=StringVar()
					DriverPhone=StringVar()
					DriverPlateNumber=StringVar()
					
					DriverBillNumber=StringVar()
					
					GivenDBPrice=IntVar()
					GivenBBWPrice=IntVar()
					GivenSBWPrice=IntVar()
					GivenSPWPrice=IntVar()
					GivenTotal=StringVar()
					
					ReturnedDBPrice=IntVar()
					ReturnedBBWPrice=IntVar()
					ReturnedSBWPrice=IntVar()
					ReturnedSPWPrice=IntVar()
					ReturnedTotal=StringVar()
					
					DamagedDBPrice=IntVar()
					DamagedBBWPrice=IntVar()
					DamagedSBWPrice=IntVar()
					DamagedSPWPrice=IntVar()
					DamagedTotal=StringVar()
					
					SoldDBPrice=IntVar()
					SoldBBWPrice=IntVar()
					SoldSBWPrice=IntVar()
					SoldSPWPrice=IntVar()
					SoldTotal=StringVar()
								
					DriverIssuedDateStamp=StringVar()
					DriverBalancedDateStamp=StringVar()
					
					
					DriverSearchedSumation=IntVar()
					DriverTotalInventory=IntVar()
					#Search related
					DriverSearch=StringVar()
					DriverSearch_Txt=StringVar()
					
					FromDriverReport=StringVar()
					ToDriverReport=StringVar()
					
					DriverUnit = tk.Toplevel(root)
					DriverUnit.wm_iconbitmap('icon.ico')
					
					DriverUnit.state('zoomed')
					#Size of the new window
					width, height = DriverUnit.winfo_screenwidth(), DriverUnit.winfo_screenheight()
					DriverUnit.geometry('%dx%d+0+0' % (width,height))
					DriverList = tk.Label(DriverUnit, text = "Driver Unit",bd=5,relief=GROOVE,font=("arial black",15,"bold"),bg="DarkGray",fg="DarkGreen")
					DriverList.pack(side=TOP,fill=X)
					DriverUnit.focus()
					
					#=======================Driver detail frame
					Driver=LabelFrame(DriverUnit,bd=10,relief=GROOVE,text="Driver Details",font=("Arial",15,"bold"),fg="DarkRed",bg=bg_color)
					Driver.place(x=0,y=32,relwidth=1,height=70)
					
					#Label for Driver Name, same background, black text
					##DriverName_lbl=Label(Driver,text="Name",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=5,pady=2)
					#Driver Name
					##global DriverName_txt
					##DriverName_txt=Entry(Driver,width=30,textvariable=DriverName,font="arial 13",bd=3,relief=SUNKEN)
					##DriverName_txt.grid(row=0,column=1,pady=2,padx=2)
					##DriverName_txt.focus()
					
					#DriverName 
					global DriverName_txt
					DriverName_lbl=Label(Driver,text="Name",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=5,pady=2)	
					DriverName_txt=ttk.Combobox(Driver,textvariable=DriverName,width=28,font="arial 11 bold",state='readonly')
					DriverName_txt['values']= self.RegisteredDriver_input()
					DriverName_txt.bind('<<ComboboxSelected>>', self.autoFullDriver)
					DriverName_txt.grid(row=0,column=1,padx=2,pady=2)
					DriverName_txt.focus()
					#DriverName_txt['state']='normal'
					
					
					#Label for Driver Phone, same background, black text
					DriverPhone_lbl=Label(Driver,text="Phone No.",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=8,pady=2)
					#Text field to Enter the Driver Phone, SUNKEN
					DriverPhone_txt=Entry(Driver,width=18,textvariable=DriverPhone,font="arial 13",bd=3,relief=SUNKEN,state='readonly')
					DriverPhone_txt.grid(row=0,column=3,pady=2,padx=2)
					
					#Label for Driver Phone, same background, black text
					DriverPlateNumber_lbl=Label(Driver,text="Plate No.",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=8,pady=2)
					#Text field to Enter the Driver Phone, SUNKEN
					DriverPlateNumber_txt=Entry(Driver,width=15,textvariable=DriverPlateNumber,font="arial 13",bd=3,relief=SUNKEN,state='readonly')
					DriverPlateNumber_txt.grid(row=0,column=5,pady=2,padx=2)
					
					#Label for Driver Phone, same background, black text
					DriverBillNumber_lbl=Label(Driver,text="BillNo.",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=6,padx=8,pady=2)
					#Text field to Enter the Driver Phone, SUNKEN
					DriverBillNumber_txt=Entry(Driver,width=18,textvariable=DriverBillNumber,fg="DarkRed",font=("arial",12,"bold"),bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=7,pady=2,padx=2)
					
					#Label for Driver Phone, same background, black text
					DriverIssuedDateStamp_lbl=Label(Driver,text="IssueDate",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=8,padx=8,pady=2)
					#Text field to Enter the Driver Phone, SUNKEN
					DriverIssuedDateStamp_txt=Entry(Driver,width=25,textvariable=DriverIssuedDateStamp,fg="DarkRed",font=("arial",11,"bold"),bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=9,pady=2,padx=2)
							
					#=======================Given Driver Item Frame
					GivenDriverItemFrame=LabelFrame(DriverUnit,bd=10,relief=GROOVE,text="Grocery Items GIVEN",font=("Arial",15,"bold"),fg="Black",bg=bg_color)
					GivenDriverItemFrame.place(x=5,y=100,width=350,height=200)
					

					#Driver Dispenser Bottle
					global GivenDriverdbwater_txt
					GivenDriverdbwater_lbl=Label(GivenDriverItemFrame,text="Dispenser Bottle",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=5,sticky="w")
					GivenDriverdbwater_txt=Entry(GivenDriverItemFrame,width=8,textvariable=GivenDBPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN)
					GivenDriverdbwater_txt.grid(row=0,column=1,padx=10,pady=5)
					GivenDriverdbwater_txt.focus()
					
					#Driver BIG Bottle water
					GivenDriverbbwater_lbl=Label(GivenDriverItemFrame,text="BIG Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=5,sticky="w")
					GivenDriverbbwater_txt=Entry(GivenDriverItemFrame,width=8,textvariable=GivenBBWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN)
					GivenDriverbbwater_txt.grid(row=1,column=1,padx=10,pady=5)
					
					#Driver Small Bottle water
					GivenDriversbwater_lbl=Label(GivenDriverItemFrame,text="Small Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=5,sticky="w")
					GivenDriversbwater_txt=Entry(GivenDriverItemFrame,width=8,textvariable=GivenSBWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)
					
					#Driver Sachet Pure water
					GivenDriverspwater_lbl=Label(GivenDriverItemFrame,text="Sachet Pure Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=5,sticky="w")
					GivenDriverspwater_txt=Entry(GivenDriverItemFrame,width=8,textvariable=GivenSPWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)
					
					#=======================Returned Driver Item Frame
					ReturnedDriverItemFrame=LabelFrame(DriverUnit,bd=10,relief=GROOVE,text="Grocery Items RETURNED",font=("Arial",15,"bold"),fg="Blue",bg=bg_color)
					ReturnedDriverItemFrame.place(x=365,y=100,width=350,height=200)
				
					#Driver Dispenser Bottle
					ReturnedDriverdbwater_lbl=Label(ReturnedDriverItemFrame,text="Dispenser Bottle",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=5,sticky="w")
					ReturnedDriverdbwater_txt=Entry(ReturnedDriverItemFrame,width=8,textvariable=ReturnedDBPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
					
					#Driver BIG Bottle water
					ReturnedDriverbbwater_lbl=Label(ReturnedDriverItemFrame,text="BIG Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=5,sticky="w")
					ReturnedDriverbbwater_txt=Entry(ReturnedDriverItemFrame,width=8,textvariable=ReturnedBBWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)
					
					#Driver Small Bottle water
					ReturnedDriversbwater_lbl=Label(ReturnedDriverItemFrame,text="Small Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=5,sticky="w")
					ReturnedDriversbwater_txt=Entry(ReturnedDriverItemFrame,width=8,textvariable=ReturnedSBWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)
					
					#Driver Sachet Pure water
					ReturnedDriverspwater_lbl=Label(ReturnedDriverItemFrame,text="Sachet Pure Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=5,sticky="w")
					ReturnedDriverspwater_txt=Entry(ReturnedDriverItemFrame,width=8,textvariable=ReturnedSPWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)
					
				
					#=======================Damaged Driver Item Frame
					DamagedDriverItemFrame=LabelFrame(DriverUnit,bd=10,relief=GROOVE,text="Grocery Items DAMAGED",font=("Arial",15,"bold"),fg="Red",bg=bg_color)
					DamagedDriverItemFrame.place(x=725,y=100,width=350,height=200)
				
					#Driver Dispenser Bottle
					DamagedDriverdbwater_lbl=Label(DamagedDriverItemFrame,text="Dispenser Bottle",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=5,sticky="w")
					DamagedDriverdbwater_txt=Entry(DamagedDriverItemFrame,width=8,textvariable=DamagedDBPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
					
					#Driver BIG Bottle water
					DamagedDriverbbwater_lbl=Label(DamagedDriverItemFrame,text="BIG Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=5,sticky="w")
					DamagedDriverbbwater_txt=Entry(DamagedDriverItemFrame,width=8,textvariable=DamagedBBWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)
					
					#Driver Small Bottle water
					DamagedDriversbwater_lbl=Label(DamagedDriverItemFrame,text="Small Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=5,sticky="w")
					DamagedDriversbwater_txt=Entry(DamagedDriverItemFrame,width=8,textvariable=DamagedSBWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)
					
					#Driver Sachet Pure water
					DamagedDriverspwater_lbl=Label(DamagedDriverItemFrame,text="Sachet Pure Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=5,sticky="w")
					DamagedDriverspwater_txt=Entry(DamagedDriverItemFrame,width=8,textvariable=DamagedSPWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)
					
				
					#=======================Sold Driver Item Frame
					SoldDriverItemFrame=LabelFrame(DriverUnit,bd=10,relief=GROOVE,text="Grocery Items SOLD",font=("Arial",15,"bold"),fg="Green",bg=bg_color)
					SoldDriverItemFrame.place(x=1085,y=100,width=350,height=200)
				
					#Driver Dispenser Bottle
					SoldDriverdbwater_lbl=Label(SoldDriverItemFrame,text="Dispenser Bottle",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=5,sticky="w")
					SoldDriverdbwater_txt=Entry(SoldDriverItemFrame,width=8,textvariable=SoldDBPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=1,padx=10,pady=5)
					
					#Driver BIG Bottle water
					SoldDriverbbwater_lbl=Label(SoldDriverItemFrame,text="BIG Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=5,sticky="w")
					SoldDriverbbwater_txt=Entry(SoldDriverItemFrame,width=8,textvariable=SoldBBWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN,state='readonly').grid(row=1,column=1,padx=10,pady=5)
					
					#Driver Small Bottle water
					SoldDriversbwater_lbl=Label(SoldDriverItemFrame,text="Small Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=5,sticky="w")
					SoldDriversbwater_txt=Entry(SoldDriverItemFrame,width=8,textvariable=SoldSBWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN,state='readonly').grid(row=2,column=1,padx=10,pady=5)
					
					#Driver Sachet Pure water
					SoldDriverspwater_lbl=Label(SoldDriverItemFrame,text="Sachet Pure Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=5,sticky="w")
					SoldDriverspwater_txt=Entry(SoldDriverItemFrame,width=8,textvariable=SoldSPWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN,state='readonly').grid(row=3,column=1,padx=10,pady=5)
					
					
					#=======================Driver Given Total Holder
					DriverGivenTotalFrame=LabelFrame(DriverUnit,bd=5,relief=SUNKEN,bg=bg_color)
					DriverGivenTotalFrame.place(x=5,y=300,width=350,height=45)
					
					GivenTotal_lbl=Label(DriverGivenTotalFrame,text="Given Total",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=25,pady=1,sticky="w")	
					GivenTotal_txt=Entry(DriverGivenTotalFrame,width=12,fg="black",textvariable=GivenTotal,font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=1,padx=2,pady=1,sticky="w")
					
					
					#=======================Driver Returned Total Holder
					DriverReturnedTotalFrame=LabelFrame(DriverUnit,bd=5,relief=SUNKEN,bg=bg_color)
					DriverReturnedTotalFrame.place(x=365,y=300,width=350,height=45)
					
					ReturnedTotal_lbl=Label(DriverReturnedTotalFrame,text="Returned Total",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=10,pady=1,sticky="w")	
					ReturnedTotal_txt=Entry(DriverReturnedTotalFrame,width=12,fg="blue",textvariable=ReturnedTotal,font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=3,padx=2,pady=1,sticky="w")
					
					
					#=======================Driver Damaged Total Holder
					DriverDamagedTotalFrame=LabelFrame(DriverUnit,bd=5,relief=SUNKEN,bg=bg_color)
					DriverDamagedTotalFrame.place(x=725,y=300,width=350,height=45)
					
					DamagedTotal_lbl=Label(DriverDamagedTotalFrame,text="Damaged Total",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=10,pady=1,sticky="w")	
					DamageTotal_txt=Entry(DriverDamagedTotalFrame,width=12,fg="red",textvariable=DamagedTotal,font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=5,padx=2,pady=1,sticky="w")

					
					#=======================Driver Sold Total Holder
					DriverSoldTotalFrame=LabelFrame(DriverUnit,bd=5,relief=SUNKEN,bg=bg_color)
					DriverSoldTotalFrame.place(x=1085,y=300,width=350,height=45)
					
					SoldTotal_lbl=Label(DriverSoldTotalFrame,text="Sold Total",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=6,padx=32,pady=1,sticky="w")	
					SoldTotal_txt=Entry(DriverSoldTotalFrame,width=12,fg="green",textvariable=SoldTotal,font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=7,padx=2,pady=1,sticky="w")
					
					
					#=======================Driver Total/Add/Print, Update and Clear Button Holder
					DriverButtonFrame=LabelFrame(DriverUnit,bd=5,relief=SUNKEN,bg=bg_color)
					DriverButtonFrame.place(x=0,y=345,relwidth=1,height=50)
					
					global AddDriver_btn
					#Button to Total/Add/Print Driver Record
					AddDriver_btn=Button(DriverButtonFrame,text="Total/Add",bg=bg_color,fg="Green",command=self.DriverAdd_bills,bd=3,pady=5,width=12,font="ArialBold 10 bold")
					AddDriver_btn.grid(row=0,column=0,padx=3,pady=2)
					AddDriver_btn['state']='normal'
					
					global UpdateDriver_btn
					#Button to Update Driver Record
					UpdateDriver_btn=Button(DriverButtonFrame,text="Update",bg=bg_color,fg="Blue",command=self.UpdateDriverDB_data,bd=3,pady=5,width=12,font="ArialBold 10 bold")
					UpdateDriver_btn.grid(row=0,column=1,padx=4,pady=2)
					UpdateDriver_btn['state']='normal'
					
					#Button to Clear Screen
					ClearDriver_btn=Button(DriverButtonFrame,text="Clear",bg=bg_color,fg="Red",command=self.DriverClear_data,bd=3,pady=5,width=12,font="ArialBold 10 bold").grid(row=0,column=2,padx=4,pady=2)
					
					
					#=======================Driver Print Bill
					PrintDriver_btn=Button(DriverButtonFrame,text="Print Bill",command=self.DriverPrint_bill,width=10,bd=3,bg=bg_color,fg="DarkRed",font="arial 12 bold").grid(row=0,column=3,padx=10,pady=2)
					
					global DriverCombo_search
					#Driver Search DB
					#ComboBox for Driver Text area select kind of data to search
					DriverCombo_search=ttk.Combobox(DriverButtonFrame,textvariable=DriverSearch,width=12,font=("Arial",15,"normal"))
					#All Driver variables for search
					DriverCombo_search['values']=("BillNo","Amount","RAmount","DAmount","SAmount","DateStamp","Name","PlateNo","Phone","NewDateStamp","EnteredBy","PreviousTotal","UpdatedBy","UpdatedDate")
					#Position of Driver combo box
					DriverCombo_search.grid(row=0,column=4,padx=4,pady=2)
					
					#Text Space to Type Data for Search
					#Addition of textvariable=self.search_txt
					DriverTxt_search=Entry(DriverButtonFrame,textvariable=DriverSearch_Txt,width=25,bg="LightGray",fg="DarkBlue",font=("Arial",15,"normal"),bd=5,relief=GROOVE)
					DriverTxt_search.grid(row=0,column=5,pady=2,padx=4,sticky="w")
					
					#Button to Search DriverDB
					#This button works with the Combo Search and Search text above
					#They must comply
					DriverSearch_btn=Button(DriverButtonFrame,text="Search DB",command=self.DriverSearch_data,width=13,bd=3,font="arial 12 bold").grid(row=0,column=6,padx=4,pady=2)
					
					global BalanceDriver_btn
					#Button to Balance/Add/Print Driver Record
					BalanceDriver_btn=Button(DriverButtonFrame,text="Balance",width=9,bd=3,bg=bg_color,fg="Green",command=self.UpdateDriverReturnedDamagedSoldDB_data,font="ArialBold 12 bold")
					BalanceDriver_btn.grid(row=0,column=7,padx=4,pady=2)
					BalanceDriver_btn['state']='normal'
					
					global SavetoExcelDriver_btn
					#Button to Update Driver Return, Damage and Sold
					SavetoExcelDriver_btn=Button(DriverButtonFrame,text="To-Excel",command=self.DriverSaveCurrentTableItem,width=9,bd=3,bg=bg_color,fg="Blue",font="ArialBold 12 bold")
					SavetoExcelDriver_btn.grid(row=0,column=8,padx=4,pady=2)
					SavetoExcelDriver_btn['state']='disable'
					
					global DeleteDriver_btn
					#Button to Delete entry from DATABASE
					DeleteDriver_btn=Button(DriverButtonFrame,text="Delete",width=10,bd=3,bg=bg_color,fg="Red",command=self.DeleteDriverData,font="ArialBold 12 bold")
					DeleteDriver_btn.grid(row=0,column=9,padx=4,pady=2)
					DeleteDriver_btn['state']='disable'
					
					#=======================Driver Bill Frame
					DriverBill=LabelFrame(DriverUnit,bd=10,relief=GROOVE)
					DriverBill.place(x=5,y=395,width=345,height=380) 
					DriverBill_title=Label(DriverBill,text="Bills",font="arial 15 bold",bd=5,relief=GROOVE).pack(fill=X)
					scroll_y=Scrollbar(DriverBill,orient=VERTICAL)
					global DriverTxtarea
					DriverTxtarea=Text(DriverBill,yscrollcommand=scroll_y.set)
					scroll_y.pack(side=RIGHT,fill=Y)
					scroll_y.config(command=DriverTxtarea.yview)
					DriverTxtarea.pack(fill=BOTH,expand=1)

					#=======================Driver Table Side Frame
					DriverTable_Frame=LabelFrame(DriverUnit,bd=10,relief=RIDGE,bg=bg_color)
					DriverTable_Frame.place(x=350,y=395,width=1080,height=380)
					
					#=======================DISPLAY FOR ALL DRIVER BILL ENTRY
					scroll_x=Scrollbar(DriverTable_Frame,orient=HORIZONTAL)
					scroll_y=Scrollbar(DriverTable_Frame,orient=VERTICAL)
					#Format for the required column headings that will be displayed
					global DriverBill_table
					DriverBill_table=ttk.Treeview(DriverTable_Frame,columns=("BillNo","Dispenser","BigBottle","SmallBottle","SachetWater","CostDispenser","CostBigBottle","CostSmallBottle","CostSachetWater","Amount","DateStamp","Name","PlateNo","Phone","NewDateStamp","RDispenser","RBigBottle","RSmallBottle","RSachetWater","RAmount","DDispenser","DBigBottle","DSmallBottle","DSachetWater","DAmount","SDispenser","SBigBottle","SSmallBottle","SSachetWater","SAmount","EnteredBy","PreviousTotal","UpdatedBy","UpdatedDate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
					
					#Scroll bar direction and configuration
					scroll_x.pack(side=BOTTOM,fill=X)
					scroll_y.pack(side=RIGHT,fill=Y)
					scroll_x.config(command=DriverBill_table.xview)
					scroll_y.config(command=DriverBill_table.yview)		
					
					#Connecting each heading to a column of the existing fields
					DriverBill_table.heading("BillNo",text="BillNo")
					DriverBill_table.heading("Dispenser",text="Dispenser")
					DriverBill_table.heading("BigBottle",text="BigBottle")
					DriverBill_table.heading("SmallBottle",text="SmallBottle")
					DriverBill_table.heading("SachetWater",text="SachetWater")
					
					DriverBill_table.heading("CostDispenser",text="CostDispenser")
					DriverBill_table.heading("CostBigBottle",text="CostBigBottle")
					DriverBill_table.heading("CostSmallBottle",text="CostSmallBottle")
					DriverBill_table.heading("CostSachetWater",text="CostSachetWater")
					
					DriverBill_table.heading("Amount",text="Amount")
					DriverBill_table.heading("DateStamp",text="DateStamp")
					DriverBill_table.heading("Name",text="Name")
					DriverBill_table.heading("PlateNo",text="PlateNo")
					DriverBill_table.heading("Phone",text="Phone")
					#Returned
					DriverBill_table.heading("NewDateStamp",text="NewDateStamp")
					DriverBill_table.heading("RDispenser",text="RDispenser")
					DriverBill_table.heading("RBigBottle",text="RBigBottle")
					DriverBill_table.heading("RSmallBottle",text="RSmallBottle")
					DriverBill_table.heading("RSachetWater",text="RSachetWater")
					DriverBill_table.heading("RAmount",text="RAmount")
					#Damaged
					DriverBill_table.heading("DDispenser",text="DDispenser")
					DriverBill_table.heading("DBigBottle",text="DBigBottle")
					DriverBill_table.heading("DSmallBottle",text="DSmallBottle")
					DriverBill_table.heading("DSachetWater",text="DSachetWater")
					DriverBill_table.heading("DAmount",text="DAmount")
					#Sold
					DriverBill_table.heading("SDispenser",text="SDispenser")
					DriverBill_table.heading("SBigBottle",text="SBigBottle")
					DriverBill_table.heading("SSmallBottle",text="SSmallBottle")
					DriverBill_table.heading("SSachetWater",text="SSachetWater")
					DriverBill_table.heading("SAmount",text="SAmount")
					DriverBill_table.heading("EnteredBy",text="EnteredBy")
					DriverBill_table.heading("PreviousTotal",text="PreviousTotal")
					DriverBill_table.heading("UpdatedBy",text="UpdatedBy")
					DriverBill_table.heading("UpdatedDate",text="UpdatedDate")
					
					#Enable heading of tables to show
					DriverBill_table['show']='headings'
					
					#Set column width for each field in the table
					DriverBill_table.column("BillNo",width=120)
					DriverBill_table.column("Dispenser", anchor="center", width=80)
					DriverBill_table.column("BigBottle", anchor="center", width=80)
					DriverBill_table.column("SmallBottle", anchor="center", width=80)
					DriverBill_table.column("SachetWater", anchor="center", width=80)
					#Cost
					DriverBill_table.column("CostDispenser", anchor="center", width=100)
					DriverBill_table.column("CostBigBottle", anchor="center", width=100)
					DriverBill_table.column("CostSmallBottle", anchor="center", width=100)
					DriverBill_table.column("CostSachetWater", anchor="center", width=100)
					
					DriverBill_table.column("Amount", anchor="e", width=100)
					DriverBill_table.column("DateStamp",width=150)
					DriverBill_table.column("Name",width=120)
					DriverBill_table.column("PlateNo",width=120)
					DriverBill_table.column("Phone",width=120)
					#Returned
					DriverBill_table.column("NewDateStamp",width=150)
					DriverBill_table.column("RDispenser", anchor="center", width=80)
					DriverBill_table.column("RBigBottle", anchor="center", width=80)
					DriverBill_table.column("RSmallBottle", anchor="center", width=80)
					DriverBill_table.column("RSachetWater", anchor="center", width=80)
					DriverBill_table.column("RAmount", anchor="e", width=100)
					#Damaged
					DriverBill_table.column("DDispenser", anchor="center", width=80)
					DriverBill_table.column("DBigBottle", anchor="center", width=80)
					DriverBill_table.column("DSmallBottle", anchor="center", width=80)
					DriverBill_table.column("DSachetWater", anchor="center", width=80)
					DriverBill_table.column("DAmount", anchor="e", width=100)
					#Sold
					DriverBill_table.column("SDispenser", anchor="center", width=80)
					DriverBill_table.column("SBigBottle", anchor="center", width=80)
					DriverBill_table.column("SSmallBottle", anchor="center", width=80)
					DriverBill_table.column("SSachetWater", anchor="center", width=80)
					DriverBill_table.column("SAmount", anchor="e", width=100)
					DriverBill_table.column("EnteredBy", anchor="center", width=150)
					DriverBill_table.column("PreviousTotal", anchor="center", width=150)
					DriverBill_table.column("UpdatedBy", anchor="center", width=150)
					DriverBill_table.column("UpdatedDate", anchor="center", width=150)
					
					#To expand the table  
					DriverBill_table.pack(fill=BOTH,expand=1)
					#Enable selection of items in the Bill_table
					DriverBill_table.bind("<ButtonRelease-1>",self.DriverBillget_cursor)
					
					
					#=======================Driver Bottom Frame
					DriverBottomFrame=LabelFrame(DriverUnit,bd=5,relief=GROOVE,bg=bg_color)
					DriverBottomFrame.place(x=0,y=780,relwidth=1,height=50)
					
					#Label for Driver Phone, same background, black text
					DriverIssuedDateStamp_lbl=Label(DriverBottomFrame,text="Bal. Date",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=8,pady=2)
					#Text field to Enter the Driver Phone, SUNKEN
					DriverIssuedDateStamp_txt=Entry(DriverBottomFrame,width=25,textvariable=DriverBalancedDateStamp,fg="DarkRed",font=("arial",11,"bold"),bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=1,pady=2,padx=2)
									
					DriverAmountSelected_lbl=Label(DriverBottomFrame,text="Sub-Total",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=2,pady=1,sticky="w")	
					DriverAmountSelected_txt=Entry(DriverBottomFrame,width=18,textvariable=DriverSearchedSumation,fg="red",font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=3,padx=2,pady=1)
					
					DriverTotalInventory_lbl=Label(DriverBottomFrame,text="TOTAL",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=2,pady=1,sticky="w")	
					DriverTotalInventory_txt=Entry(DriverBottomFrame,width=19,textvariable=DriverTotalInventory,fg="red",font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=5,padx=2,pady=1)
					
					global GenerateReportDriverFrom_txt
					GenerateReportDriverFrom_lbl=Label(DriverBottomFrame,text="From:",bg=bg_color,fg="Black",font=("times new roman",12,"bold")).grid(row=0,column=6,padx=17,pady=1,sticky="w")	
					GenerateReportDriverFrom_txt=Entry(DriverBottomFrame,width=10,textvariable=FromDriverReport,fg="Black",font="arial 12 bold",bd=3,relief=SUNKEN)
					GenerateReportDriverFrom_txt.grid(row=0,column=7,padx=2,pady=1)
					
					global GenerateReportDriverTo_txt
					GenerateReportDriverTo_lbl=Label(DriverBottomFrame,text="To:::",bg=bg_color,fg="Black",font=("times new roman",12,"bold")).grid(row=0,column=8,padx=2,pady=1,sticky="w")	
					GenerateReportDriverTo_txt=Entry(DriverBottomFrame,width=10,textvariable=ToDriverReport,fg="Black",font="arial 12 bold",bd=3,relief=SUNKEN)
					GenerateReportDriverTo_txt.grid(row=0,column=9,padx=2,pady=1)	
					
					global GenerateReportDriver_btn
					GenerateReportDriver_btn=Button(DriverBottomFrame,text="Generate Report",width=15,bd=3,bg=bg_color,fg="Green",command=self.GenerateReport_Driver,font="ArialBold 10 bold")
					GenerateReportDriver_btn.grid(row=0,column=10,padx=4,pady=2)
					GenerateReportDriver_btn['state']='disable'
					
					self.DriverWelcome_bill()
					
					
					#Automatically focus cursor in the search txt once there is a selection of Search_by
					self.DriverAutoFocusSearch()
					
					#Automatically Clear Screen
					self.DriverClear_data()
					
					global DriverDirectory
					DriverDirectory="C:/DriverBills/"
					
					#Function to Fetch all data from Driver Table
					self.DriverFetchDB_data()
					
					DriverList.pack()
					
					#Lovely Code that will ensure Child Window remains active and Root remains inactive until Child is Closed 
					#After Clicking on Driver Unit the new Window to Driver Unit must be fully used and closed before using main interface
					DriverUnit.transient(root)
					DriverUnit.grab_set()
					root.wait_window(DriverUnit)
				
				#Generate REPORT Normal Sales
				def GenerateReport_Driver(self):
					try:
						#If one or both of the criteria is/are empty
						if FromDriverReport.get()=="" or ToDriverReport.get()=="":
							messagebox.showerror("Report Error","Date From: and Date To: \nAre compulsory")
							
						elif FromDriverReport.get()=="dd/mm/yyyy" or len((str(FromDriverReport.get()).split('/')[2]))!=4 or int((str(FromDriverReport.get()).split('/')[1]))>12:
							messagebox.showerror("Data Error","Date FROM must be in dd/mm/yyyy format")
							GenerateReportDriverFrom_txt.focus()
						
						elif ToDriverReport.get()=="dd/mm/yyyy" or len((str(ToDriverReport.get()).split('/')[2]))!=4 or int((str(ToDriverReport.get()).split('/')[1]))>12:
							messagebox.showerror("Data Error","Date TO must be in dd/mm/yyyy format")
							GenerateReportDriverTo_txt.focus()
							
						else:
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("select * from driverbills where DateStamp BETWEEN '"+str(FromDriverReport.get())+" 00:00:00.000000' AND '"+str(ToDriverReport.get())+" 99:99:99.999999'")
							DriverBill_table.delete(*DriverBill_table.get_children())
							rows=cur.fetchall()
							if len(rows)<1:
								con.close()
								messagebox.showinfo('No Data!',"No record was captured within date range")
							elif len(rows)>=1:
								DriverBill_table.delete(*DriverBill_table.get_children())
								for row in rows:
									DriverBill_table.insert('',END,values=row)
								con.commit()
								con.close()
								#Auto focus the last record from the records returned after search
								child_id = DriverBill_table.get_children()[-1]
								cursor_row = DriverBill_table.focus(child_id)
								DriverBill_table.selection_set(child_id)
								self.DriverBillget_cursor(cursor_row)
								
								#Calling a function to do Sub-Total Sum all items displayed in table after every search performed
								self.DriverSearchedSum()
								
								#SAVE but ask use first
								savereport=messagebox.askyesno("Driver Report","Report Successfully Retrieved \nDo you want to Save this Report?")
								if savereport>0:
									self.DriverSaveCurrentTableItem()
								else:
									pass
							
					except ValueError:
						messagebox.showerror("Data Report Error","Invalid data entry")
				
				#Automatically Fill Driver Details after FullName Selection
				def autoFullDriver(self, event):
					#Connection to the Database
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					
					#Getting the exact MobileNo of the Fullname
					cur.execute("select MobileNo FROM register WHERE FullName = '"+DriverName.get()+"'")
					row=cur.fetchall()
					DriverPhone.set(row[0])
					
					#Getting the exact VehicleNo of the Fullname
					cur.execute("select VehicleNo FROM register WHERE FullName = '"+DriverName.get()+"'")
					row=cur.fetchall()
					for rows in row:
						#print(rows[0])
						DriverPlateNumber.set(rows[0])
					
					GivenDriverdbwater_txt.focus()
				
				#Function to connect to DB and populate Data in a Column as the Drop Down Values another Combobox
				def RegisteredDriver_input(self):
					#Connection to the Database
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					#cur.execute("select * from register WHERE UserID = '" + ery2.get() + "' AND Password = '" + ery3.get() + "'")
					cur.execute("select FullName FROM register WHERE Category = 'Driver'")
					data=[]
					
					for row in cur.fetchall():
						data.append(row[0])
					return data
					
				def DisableAddTotalUpdateBalanceDriver(self):
					#Automatically disable the Add/Total and Update Buttons
					if CurrentCategory == 'Super-Admin' or CurrentCategory == 'Admin':
						AddDriver_btn['state']='disabled'
						#UpdateDriver_btn['state']='normal'
					else:
						AddDriver_btn['state']='disabled'
						UpdateDriver_btn['state']='disabled'
					
					if CurrentCategory == 'Super-Admin':
						SavetoExcelDriver_btn['state']='normal'
						DeleteDriver_btn['state']='normal'
						GenerateReportDriver_btn['state']='normal'
					
					#if condition to disable Balance Button
					if SoldTotal.get()!="N0.00":
						BalanceDriver_btn['state']='disabled'
						if CurrentCategory != 'Super-Admin':
							UpdateDriver_btn['state']='disabled'
						if CurrentCategory == 'Super-Admin':
							BalanceDriver_btn['state']='normal'
					else:
						BalanceDriver_btn['state']='normal'
						
						
				def DriverSaveCurrentTableItem(self):
					#Empty list for each column in the treeview
					column1_list = []
					column2_list = []
					column3_list = []
					column4_list = []
					column5_list = []
					column6_list = []
					column7_list = []
					column8_list = []
					column9_list = []
					column10_list = []
					column11_list = []
					column12_list = []
					column13_list = []
					column14_list = []
					column15_list = []
					column16_list = []
					column17_list = []
					column18_list = []
					column19_list = []
					column20_list = []
					column21_list = []
					column22_list = []
					column23_list = []
					column24_list = []
					column25_list = []
					column26_list = []
					column27_list = []
					column28_list = []
					column29_list = []
					column30_list = []
					column31_list = []
					column32_list = []
					column33_list = []
					column34_list = []
					
					#running through the lines of the treeview in a "for" function, append to each column list the value of the column in each line
					for child in DriverBill_table.get_children():
						column1_list.append(DriverBill_table.item(child)["values"][0]) 
						column2_list.append(DriverBill_table.item(child)["values"][1]) 
						column3_list.append(DriverBill_table.item(child)["values"][2]) 
						column4_list.append(DriverBill_table.item(child)["values"][3]) 
						column5_list.append(DriverBill_table.item(child)["values"][4]) 
						column6_list.append(DriverBill_table.item(child)["values"][5]) 
						column7_list.append(DriverBill_table.item(child)["values"][6]) 
						column8_list.append(DriverBill_table.item(child)["values"][7]) 
						column9_list.append(DriverBill_table.item(child)["values"][8]) 
						column10_list.append(DriverBill_table.item(child)["values"][9]) 
						column11_list.append(DriverBill_table.item(child)["values"][10]) 
						column12_list.append(DriverBill_table.item(child)["values"][11]) 
						column13_list.append(DriverBill_table.item(child)["values"][12]) 
						column14_list.append(DriverBill_table.item(child)["values"][13]) 
						column15_list.append(DriverBill_table.item(child)["values"][14]) 
						column16_list.append(DriverBill_table.item(child)["values"][15]) 
						column17_list.append(DriverBill_table.item(child)["values"][16]) 
						column18_list.append(DriverBill_table.item(child)["values"][17]) 
						column19_list.append(DriverBill_table.item(child)["values"][18]) 
						column20_list.append(DriverBill_table.item(child)["values"][19]) 
						column21_list.append(DriverBill_table.item(child)["values"][20]) 
						column22_list.append(DriverBill_table.item(child)["values"][21]) 
						column23_list.append(DriverBill_table.item(child)["values"][22]) 
						column24_list.append(DriverBill_table.item(child)["values"][23]) 
						column25_list.append(DriverBill_table.item(child)["values"][24]) 
						column26_list.append(DriverBill_table.item(child)["values"][25])
						column27_list.append(DriverBill_table.item(child)["values"][26])
						column28_list.append(DriverBill_table.item(child)["values"][27])
						column29_list.append(DriverBill_table.item(child)["values"][28])
						column30_list.append(DriverBill_table.item(child)["values"][29])
						column31_list.append(DriverBill_table.item(child)["values"][30])
						column32_list.append(DriverBill_table.item(child)["values"][31])
						column33_list.append(DriverBill_table.item(child)["values"][32])
						column34_list.append(DriverBill_table.item(child)["values"][33])
						
					
					#create a dictionary from all the lists, using the header as the key and lists are the values as a list
					Driverfull_treeview_data_dict = {'BillNo': column1_list, 'Dispenser': column2_list, 'BigBottle': column3_list, 'SmallBottle': column4_list, 'SachetWater': column5_list, 'CostDispenser': column6_list, 'CostBigBottle': column7_list,
												'CostSmallBottle': column8_list, 'CostSachetWater': column9_list, 'Amount': column10_list, 'DateStamp': column11_list, 'Name': column12_list, 'PlateNo': column13_list, 'Phone': column14_list,
												'NewDateStamp': column15_list, 'RDispenser': column16_list, 'RBigBottle': column17_list, 'RSmallBottle': column18_list, 'RSachetWater': column19_list, 'RAmount': column20_list, 'DDispenser': column21_list,
												'DBigBottle': column22_list, 'DSmallBottle': column23_list, 'DSachetWater': column24_list, 'DAmount': column25_list, 'SDispenser': column26_list, 'SBigBottle': column27_list, 'SSmallBottle': column28_list,
												'SSachetWater': column29_list, 'SAmount' : column30_list, 'EnteredBy' : column31_list, 'PreviousTotal' : column32_list, 'UpdatedBy' : column33_list, 'UpdatedDate' : column34_list}
												
					#Create a dataframe from the dictionary
					Drivertreeview_df = pd.DataFrame.from_dict(Driverfull_treeview_data_dict)
					
					#print(Drivertreeview_df)
					if len(driverdata) < 1:
						messagebox.showerror("No Data","No data available to export")
						return False
					try:
						filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Save to Excel',defaultextension='.xlsx',filetypes=[("Excel file", "*.xlsx")])
						Drivertreeview_df.to_excel(filename, engine='xlsxwriter',index= False)
						messagebox.showinfo("Data Exported","Your data has been exported to "+os.path.basename(filename)+" successfully.")
					except:
						pass

				
				def DriverPrint_bill(self):
					##Check if the Bill No. is blank string then it Prints using the Bill No. in the text area
					if DriverBillNumber.get()!="":
						self.DriverSaveBill()
						#Opens the main file using the Bill No.
						fin = open("C:/DriverBills/"+str(DriverBillNumber.get())+".txt","rt")
						#Create another temporary file mainly for printing format
						fout = open("C:/DriverBills/printout.txt","wt")
						#Condition statement for each line in the file main fin
						for line in fin:
							#If the line startswith Items then just print it like that
							if line.startswith(" Items"):
								fout.write(line)
							#Else try to replace double tabs \t\t on any other lines with single tab \t
							else:
								#print(line.rstrip().replace("\t\t","\t"))
								fout.write(line.replace("\t\t","\t"))
						#Close the files
						fin.close()
						fout.close()
						os.startfile("C:/DriverBills/printout.txt","print")
					##Else it will automatically PRINT using the Bill No. in the Search
					else:
						messagebox.showerror("Print Error","Kindly select a Bill to print")
				
				#Total of all items in general given to all drivers to display below screen
				def DriverDBTOTAL(self):
					#Using a try and catch error incase when the Database is wiped
					#Opening the app will automatically want to Calculate all Total Inventory
					try:
						#Amount=float(Amount.repalce("N","").replace(",",""))
						con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
						cur=con.cursor()
						cur.execute("SELECT sum(Amount) AS totalsum FROM driverbills")
						result=cur.fetchall()
						for i in result:
							#print(i[0])
							DriverTotalInventory.set("N"+str("{:0,.2f}".format(i[0])))
						con.commit()
					except TypeError:
						pass
				
				
				def DriverSearchedSum(self):
					#Variable Stubtotal is used as accumulator set at 0.00 float
					Stubtotal = 0.00
					#For Every child of the table
					for child in DriverBill_table.get_children():
						#Accumulate the sum of each item displayed
						Stubtotal += float(DriverBill_table.item(child,'values')[9])
					#Transferring the sum above into the Sub-total text holder
					DriverSearchedSumation.set("N"+str("{:0,.2f}".format(Stubtotal)))
					#print(Stubtotal)

				def DriverAutoFocusSearch(self):
					if DriverSearch.get()!="":
						DriverTxt_search.focus()
				
				#This function will search using the search_by and search_txt to populate the data from DB to Table
				def DriverSearch_data(self):
					##try:
					#If one or both of the criteria is/are empty
					if DriverSearch.get()=="" or DriverSearch_Txt.get()=="":
						messagebox.showerror("Search Error","Select Search by and \nType correct keyword")
					else:
						con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
						cur=con.cursor()
						if cur.execute("select * from driverbills where "+str(DriverSearch.get())+" LIKE '%"+str(DriverSearch_Txt.get())+"%'"):
							rows=cur.fetchall()
							if len(rows)!=0:
								DriverBill_table.delete(*DriverBill_table.get_children())
								for row in rows:
									DriverBill_table.insert('',END,values=row)
								con.commit()
							con.close()
							#Auto focus the last record from the records returned after search
							child_id = DriverBill_table.get_children()[-1]
							cursor_row = DriverBill_table.focus(child_id)
							DriverBill_table.selection_set(child_id)
							self.DriverBillget_cursor(cursor_row)
							
							#Calling a function to do Sub-Total Sum all items displayed in table after every search performed
							self.DriverSearchedSum()
							#NEWLY
							#self.DisableGenBill()
						else:
							messagebox.showerror("Data Search Error","You have made an invalid data search\n"+DriverSearch_Txt.get()+" does not exist.")
							#Then automatically show all records from DB
							self.DriverFetchDB_data()
							#clear screen
							self.DriverClear_data()
							
					##except ValueError:
						##messagebox.showerror("Data Search Error","You have made an invalid data search")		
				
				
				#Update Driver Given Records
				def UpdateDriverDB_data(self):
					if DriverBillNumber.get()=="" or GivenTotal.get()=="":
						messagebox.showerror("Update Error","Select record from table\n and Insert valid data")
					else:
						self.DriverGivenTotal()
						DriverTotalPayable=GivenTotal.get().replace("N","").replace(",","")
						ask=messagebox.askyesno("Update Record","Are you sure to proceed with update!")
						if ask==True:
							self.mynice_date()
							updatedate=today_date
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("update driverbills set Dispenser=%s,BigBottle=%s,SmallBottle=%s,SachetWater=%s,CostDispenser=%s,CostBigBottle=%s,CostSmallBottle=%s,CostSachetWater=%s,Amount=%s,DateStamp=%s,Name=%s,PlateNo=%s,Phone=%s,PreviousTotal=%s,UpdatedBy=%s,UpdatedDate=%s where BillNo=%s",(
																																																											GivenDBPrice.get(),
																																																											GivenBBWPrice.get(),
																																																											GivenSBWPrice.get(),
																																																											GivenSPWPrice.get(),
																																																											DriverDBP,
																																																											DriverBBWP,
																																																											DriverSBWP,
																																																											DriverSPWP,
																																																											DriverTotalPayable,
																																																											DriverIssuedDateStamp.get(),
																																																											DriverName.get(),
																																																											DriverPlateNumber.get(),
																																																											DriverPhone.get(),
																																																											PreviousDriverAmount,
																																																											v,
																																																											updatedate,
																																																											DriverBillNumber.get()
																																																											))
							con.commit()

							#NEWLY To auto focus the selection Balanced is performed on any selected Record
							#Using variable xx and yy to get the current fucos and index of the focus iid
							#This is done before the fetching of Database from DB to the TreeView
							xx=DriverBill_table.focus()
							yy=DriverBill_table.index(xx)
							#print(yy)				
							
							#Function of fetch_data is called here
							self.DriverFetchDB_data()

							#NEWLY To auto focus the selection Balanced selected Record
							child_id = DriverBill_table.get_children()[yy]
							cursor_row=DriverBill_table.focus(child_id)
							DriverBill_table.selection_set(child_id)
							
							#NEWLY ADDED
							#Display current values in the Bill Text area depending on Given Only and Returned/Damaged/Sold
							if SoldTotal.get()=="N0.00":
								self.DriverAddBill_area()
							else:
								self.DriverReturnedDamagedSoldUpdate()				
							
							#After fetching the data then save the text file too
							#Save Driver Bill to Text
							self.DriverSaveBill()			
							
							UpdateDriver_btn['state']='disabled'
							
							#self.UpdateBill_area()
							#self.UpdateText_bill()
							con.close()	
				
				
				#Update Driver Returned, Damaged and Sold Records
				def UpdateDriverReturnedDamagedSoldDB_data(self):
					if DriverBillNumber.get()=="" or GivenTotal.get()=="":
						messagebox.showerror("Update Error","Select record from table\n and Insert valid data")
					else:
						ask=messagebox.askyesno("Update Record","Are you sure to proceed with balance update!\nYou cannot undo this action!")
						if ask==True:		
							self.DriverGivenTotal()
							
							#Recalculate the Returned, Damaged and Sold
							self.DriverReturnedDamagedSoldTotal()
							
							DriverReturnedTotal=ReturnedTotal.get().replace("N","").replace(",","")
							DriverDamagedTotal=DamagedTotal.get().replace("N","").replace(",","")
							DriverSoldTotal=SoldTotal.get().replace("N","").replace(",","")
							
							#Newly added line appending the microsecond to BillNo for uniqueness
							#x=str(datetime.now()).split('.')[1]
							#randbillno=random.randint(10000,99999)
							#DriverBillNumber.set(str(randbillno)+x)
							#Capture the Date Issued
							self.mynice_date()
							##y=str(datetime.now())
							DriverBalancedDateStamp.set(today_date)	
						
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("update driverbills set NewDateStamp=%s,RDispenser=%s,RBigBottle=%s,RSmallBottle=%s,RSachetWater=%s,RAmount=%s,DDispenser=%s,DBigBottle=%s,DSmallBottle=%s,DSachetWater=%s,DAmount=%s,SDispenser=%s,SBigBottle=%s,SSmallBottle=%s,SSachetWater=%s,SAmount=%s where BillNo=%s",(
																																																																						DriverBalancedDateStamp.get(),
																																																																						ReturnedDBPrice.get(),
																																																																						ReturnedBBWPrice.get(),
																																																																						ReturnedSBWPrice.get(),
																																																																						ReturnedSPWPrice.get(),
																																																																						DriverReturnedTotal,
																																																																						DamagedDBPrice.get(),
																																																																						DamagedBBWPrice.get(),
																																																																						DamagedSBWPrice.get(),
																																																																						DamagedSPWPrice.get(),
																																																																						DriverDamagedTotal,
																																																																						SoldDBPrice.get(),
																																																																						SoldBBWPrice.get(),
																																																																						SoldSBWPrice.get(),
																																																																						SoldSPWPrice.get(),
																																																																						DriverSoldTotal,
																																																																						DriverBillNumber.get()
																																																																						))
							con.commit()
							
							#NEWLY To auto focus the selection Balanced is performed on any selected Record
							#Using variable xx and yy to get the current fucos and index of the focus iid
							#This is done before the fetching of Database from DB to the TreeView
							xx=DriverBill_table.focus()
							yy=DriverBill_table.index(xx)
							#print(yy)
							
							#Function of fetch_data is called here
							self.DriverFetchDB_data()
							
							#Auto focus the first record from the records returned after New Addition
							#child_id = DriverBill_table.get_children([DriverBillNumber.get()])
							#cursor_row=DriverBill_table.focus(child_id)
							
							#NEWLY To auto focus the selection Balanced selected Record
							child_id = DriverBill_table.get_children()[yy]
							cursor_row=DriverBill_table.focus(child_id)
							DriverBill_table.selection_set(child_id)
							#DriverBill_table.selection_set(yy)				
							
							
							#After fetching the data then save the text file too
							#self.UpdateBill_area()
							#self.UpdateText_bill()
							self.DriverReturnedDamagedSoldUpdate()
							
							#Save Driver Bill to Text
							self.DriverSaveBill()
							
							con.close()
				
				
				
				
				#Delete Driver record from DB 	
				def DeleteDriverData(self):
					ask=messagebox.askyesno("Deleting Record","Are you sure to proceed with delete! \nYou cannot undo this action")
					if ask==True:
						con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
						cur=con.cursor()
						cur.execute("delete from driverbills where BillNo=%s",DriverBillNumber.get())
						con.commit()
						con.close()
						#Clear Screen
						self.DriverClear_data()
						#Function of fetch_data is called here
						self.DriverFetchDB_data()	
				
				
				def DriverCompute_Add(self):
					self.DriverAdd_bills()
					#self.UpdateDriverDB_data()
					self.DriverAddBill_area()
				
				
				#NEW Function to focus cursor, when any record on the table is clicked it should display all the info therein
				def DriverBillget_cursor(self,ev):
					##try:
					#self.DriverClear_data()					
					try:
						cursor_row=DriverBill_table.focus()
						contents=DriverBill_table.item(cursor_row)
						row=contents['values']
						DriverBillNumber.set(row[0])
						GivenDBPrice.set(row[1])
						GivenBBWPrice.set(row[2])
						GivenSBWPrice.set(row[3])
						GivenSPWPrice.set(row[4])
						GivenTotal.set("N"+str("{:0,.2f}".format(float(row[9]))))
						
						global PreviousDriverAmount
						PreviousDriverAmount=(row[9])
						
						DriverIssuedDateStamp.set(row[10])
						DriverName.set(row[11])
						DriverPlateNumber.set(row[12])
						DriverPhone.set(row[13])
						DriverBalancedDateStamp.set(row[14])
						
						ReturnedDBPrice.set(row[15])
						ReturnedBBWPrice.set(row[16])
						ReturnedSBWPrice.set(row[17])
						ReturnedSPWPrice.set(row[18])
						
						#ReturnedTotal.set(row[19])
						ReturnedTotal.set("N"+str("{:0,.2f}".format(float(row[19]))))
						
						DamagedDBPrice.set(row[20])
						DamagedBBWPrice.set(row[21])
						DamagedSBWPrice.set(row[22])
						DamagedSPWPrice.set(row[23])
						
						#DamagedTotal.set(row[24])
						DamagedTotal.set("N"+str("{:0,.2f}".format(float(row[24]))))
						
						SoldDBPrice.set(row[25])
						SoldBBWPrice.set(row[26])
						SoldSBWPrice.set(row[27])
						SoldSPWPrice.set(row[28])
						
						#SoldTotal.set(row[29])
						SoldTotal.set("N"+str("{:0,.2f}".format(float(row[29]))))
					
					except:
						pass
						
					#NEWLY ADDED
					#Display current values in the Bill Text area depending on Given Only and Returned/Damaged/Sold
					if SoldTotal.get()=="N0.00":
						self.DriverAddBill_area()
					else:
						self.DriverReturnedDamagedSoldUpdate()
					
					
					#This code disable Update Record Button once it has been previously Updated 1ce
					if CurrentCategory == 'Super-Admin':
						UpdateDriver_btn['state']='normal'
					elif CurrentCategory == 'Admin':
						if (row[31]) != "":
							UpdateDriver_btn['state']='disabled'
						else:
							UpdateDriver_btn['state']='normal'
					
					
					
					#Disable Add/Total, Update and Balance Buttons
					self.DisableAddTotalUpdateBalanceDriver()
					
					#Cost per items * Qty of Items
					#self.TotalBottleDispenser.set(str("{:0,.2f}".format(float(row[1])*float(row[5]))))
					#self.TotalBigBottleWater.set(str("{:0,.2f}".format(float(row[2])*float(row[6]))))
					#self.TotalSmallBottleWater.set(str("{:0,.2f}".format(float(row[3])*float(row[7]))))
					#self.TotalSachetPureWater.set(str("{:0,.2f}".format(float(row[4])*float(row[8]))))
					
					
					#NEWLY ADDED to automatically find the bill of any selected item from the textarea
					#self.Find_bill()
					#self.total()
					#Function to disable the Generate Bill needed here to avoid duplicate saving
					#self.DisableGenBill()
					##except:
						##pass
				
				#NEW Function to fetch Price data
				def DriverFetchDB_data(self):
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					#Sorting the data fetched to display in descending order of DateStamp
					cur.execute("select * from driverbills order by DateStamp DESC")
					rows=cur.fetchall()
					if len(rows)!=0:
						DriverBill_table.delete(*DriverBill_table.get_children())
						for row in rows:
							DriverBill_table.insert('',END,values=row)
						con.commit()
					self.DriverDBTOTAL()
					con.close()
				
					#NEW function to add info of Driver to DB
				def DriverAdd_bills(self):
					#try:
					ask=messagebox.askyesno("Add Driver Record","Do you really want to ADD this record?")
					if ask==True:
						#if self.TotalPayable.get()=="" and self.BillNo.get()=="" and self.CurrentTime.get()=="":
						#Newly added line appending the microsecond to BillNo for uniqueness
						
						#New Bill Code Starting With YYMMDD
						yy=str(datetime.now()).split(' ')[0]
						yy=str((yy[2:]).replace('-',''))
						#print(yy)
							
						x=str(datetime.now()).split('.')[1]+str("D")
						randbillno=random.randint(10000,99999)
						DriverBillNumber.set(yy+str(randbillno)+x)
						
						#Capture the Date Issued
						self.mynice_date()
						##y=str(datetime.now())
						DriverIssuedDateStamp.set(today_date)
						
						#Call Functions to perform Total Given by acquiring price multiplier DBPrice, BBWPrice, SBWPrice and SPWPrice
						self.DriverGivenTotal()
						#self.PriceMultiplier()
					
						#Remove Naira sign and comma from all TOTALs
						TotalPayable=GivenTotal.get().replace("N","").replace(",","")
						ReturnedTotalCash=ReturnedTotal.get().replace("N","").replace(",","")
						DamagedTotalCash=DamagedTotal.get().replace("N","").replace(",","")
						SoldTotalCash=SoldTotal.get().replace("N","").replace(",","")
						
						#TotalPayable=float(TotalPayable)
						#print(TotalPayable)
						
						if DriverName.get()=="":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nDriver Name is mandatory")
							self.DriverClear_data()
						elif TotalPayable=="" or TotalPayable=="0.00":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nBillNo. and TotalBill are mandatory")
							self.DriverClear_data()
						else:
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("insert into driverbills values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(DriverBillNumber.get(),
																																				GivenDBPrice.get(),
																																				GivenBBWPrice.get(),
																																				GivenSBWPrice.get(),
																																				GivenSPWPrice.get(),
																																				DriverDBP,
																																				DriverBBWP,
																																				DriverSBWP,
																																				DriverSPWP,
																																				TotalPayable,
																																				DriverIssuedDateStamp.get(),
																																				DriverName.get(),
																																				DriverPlateNumber.get(),
																																				DriverPhone.get(),
																																				
																																				DriverBalancedDateStamp.get(),	
																																				ReturnedDBPrice.get(),
																																				ReturnedBBWPrice.get(),
																																				ReturnedSBWPrice.get(),
																																				ReturnedSPWPrice.get(),
																																				ReturnedTotalCash,
																																				
																																				DamagedDBPrice.get(),
																																				DamagedBBWPrice.get(),
																																				DamagedSBWPrice.get(),
																																				DamagedSPWPrice.get(),
																																				DamagedTotalCash,
																																				
																																				SoldDBPrice.get(),
																																				SoldBBWPrice.get(),
																																				SoldSBWPrice.get(),
																																				SoldSPWPrice.get(),
																																				SoldTotalCash,
																																				v,
																																				"",
																																				"",
																																				""
																																				))

							#Function of fetch_data is called here	
							con.commit()
							
							#NEWEST
							self.DriverFetchDB_data()
							
							#Function to clear the data after adding it to DB
							#self.Clear_data()
							con.close()
							#Driver Bill Text Area
							self.DriverAddBill_area()
							#Save Driver Bill to Text
							self.DriverSaveBill()
							
							#NEWEST Auto Highlight the record that was added in the Driver Table TreeView
							#Auto focus the first record from the records returned after New Addition
							child_id = DriverBill_table.get_children()[0]
							cursor_row=DriverBill_table.focus(child_id)
							DriverBill_table.selection_set(child_id)
							self.DriverBillget_cursor(cursor_row)
							
							#Message box to indicate successfully added
							messagebox.showinfo('Successfully added!',"The record has been captured")
							
							AddDriver_btn['state']='disabled'
					else:
						pass
					#except Exception:
						#messagebox.showerror("Add Data Error","There is a duplicate entry")

				#Function to Save Driver Bill as Text File
				#I have to global DriverDirectory as C:/DriverBills at the header of Driver Section
				def DriverSaveBill(self):
					#op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
					#if op>0:
					driverbill_data=DriverTxtarea.get('1.0',END)
					#print(driverbill_data)
					if not os.path.exists(DriverDirectory):
						os.makedirs(DriverDirectory)
					f1=open("C:/DriverBills/"+str(DriverBillNumber.get())+".txt","w")
					f1.write(driverbill_data)
					f1.close()
				
				#NEW Function to fetch data
				def Driverfetch_data(self):
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					cur.execute("select * from driverbills order by DateStamp DESC")		
					rows=cur.fetchall()
					
					##NEWLY
					global driverdata
					driverdata=rows
					
					if len(rows)!=0:
						DriverBill_table.delete(*DriverBill_table.get_children())
						for row in rows:
							DriverBill_table.insert('',END,values=row)
						con.commit()
					con.close()
				
				#DRIVER FUNCTIONS COMPUTE GIVEN TOTALS
				def DriverGivenTotal(self):
					try:
						#Run function to Recapture the Current Price data from the DB as Variables and use as Multiplier
						self.PriceMultiplier()
						
						#This will automatically sum values in Currency of 2 decimal places		
						#Added a N for Naira sign, must be: self.TotalPayable.get().replace("N","").replace(",","") when calculating
						#GIVEN TOTAL
						GivenTotal.set("N"+str("{:0,.2f}".format(
															float((str("{:0,.2f}".format(float(GivenDBPrice.get()*float(DriverDBP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(GivenBBWPrice.get()*float(DriverBBWP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(GivenSBWPrice.get()*float(DriverSBWP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(GivenSPWPrice.get()*float(DriverSPWP))))).replace(",",""))
															)))
						#self.DriverWelcome_bill()
							
					except TclError:
						#Display this message
						messagebox.showerror("Data Error","You have made an invalid \ndata entry")
						#Clear the content of all totals and reset the Bill Section
				
				#DRIVER FUNCTIONS to COMPUTE RETURNED, DAMAGED AND SOLD TOTALS
				def DriverReturnedDamagedSoldTotal(self):
					try:
						#Run function to Recapture the Current Price data from the DB as Variables and use as Multiplier
						self.PriceMultiplier()

						#RETURNED TOTAL
						ReturnedTotal.set("N"+str("{:0,.2f}".format(
															float((str("{:0,.2f}".format(float(ReturnedDBPrice.get()*float(DriverDBP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(ReturnedBBWPrice.get()*float(DriverBBWP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(ReturnedSBWPrice.get()*float(DriverSBWP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(ReturnedSPWPrice.get()*float(DriverSPWP))))).replace(",",""))
															)))
						#DAMAGED TOTAL
						DamagedTotal.set("N"+str("{:0,.2f}".format(
															float((str("{:0,.2f}".format(float(DamagedDBPrice.get()*float(DriverDBP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(DamagedBBWPrice.get()*float(DriverBBWP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(DamagedSBWPrice.get()*float(DriverSBWP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(DamagedSPWPrice.get()*float(DriverSPWP))))).replace(",",""))
															)))
						
						#Computation for SOLD GROCERIES
						SoldDBPrice.set(GivenDBPrice.get()-(ReturnedDBPrice.get()+DamagedDBPrice.get()))
						SoldBBWPrice.set(GivenBBWPrice.get()-(ReturnedBBWPrice.get()+DamagedBBWPrice.get()))
						SoldSBWPrice.set(GivenSBWPrice.get()-(ReturnedSBWPrice.get()+DamagedSBWPrice.get()))
						SoldSPWPrice.set(GivenSPWPrice.get()-(ReturnedSPWPrice.get()+DamagedSPWPrice.get()))

						#SOLD TOTAL
						SoldTotal.set("N"+str("{:0,.2f}".format(
															float((str("{:0,.2f}".format(float(SoldDBPrice.get()*float(DriverDBP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(SoldBBWPrice.get()*float(DriverBBWP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(SoldSBWPrice.get()*float(DriverSBWP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(SoldSPWPrice.get()*float(DriverSPWP))))).replace(",",""))
															)))
						#*#*#*Disabled for the moment									
						##self.DriverReturnedDamagedSoldUpdate()
						
						#Update the Values in the Returned, Damaged and Sold Sections into Existing DB Record
						#self.UpdateDriverReturnedDamagedSoldDB_data()
							
					except TclError:
						#Display this message
						messagebox.showerror("Data Error","You have made an invalid \ndata entry")
						#Clear the content of all totals and reset the Bill Section

				#Updating the DriverBill with Returned, Damaged and Sold Record
				def DriverReturnedDamagedSoldUpdate(self):
					
					##self.PriceMultiplier()
					
					#VITAL CODE to get Starting Point of where to delete in the DriverTxtArea
					#Assigned the Content of DriverTxtArea to a Variable lines
					##lines=DriverTxtarea.get('1.0',END).splitlines()
					#Initialize variable count as 0
					#count=0
					#Each line in lines
					##for line in lines:
						#check if line is equal to variable of specific line
						##if line != ' ------- Kindly Drive Safely -------':
							#increment count if condition is okay
							##count = count + 1
						#Get out of the count
						##else:
							##break
					#Count is converted to float +3 lines down
					##start=(float(count+3))
					#start=(float(15.0))
					
					#I need to count the lines in the DriverTxtarea where the line '------- Kindly Drive Safely -------' appears
					#Assign the count to a variable start as float and use it in the code below
					#Delete lines from specific location to the end in the DriverTxtarea so that when Balance is clicked it overwrite previous
					#DriverTxtarea.delete(start,END)
					
					self.DriverAddBill_area()
					DriverTxtarea.config(state=NORMAL)
					#RETURNED Items Captured into Driver Bill
					DriverTxtarea.insert(END,f"\n \t{self.Time_get()}")
					DriverTxtarea.insert(END,f"\n ---------- ITEMS RETURNED ---------")
					if ReturnedDBPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 18.5 Litre\t\t{ReturnedDBPrice.get()}\t{(str('{:0,.2f}'.format(float(ReturnedDBPrice.get()*float(DriverDBP)))))}")
					#Condition if Qty of Big Bottle Water is not NIL
					if ReturnedBBWPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 75cl Bottle \t\t{ReturnedBBWPrice.get()}\t{(str('{:0,.2f}'.format(float(ReturnedBBWPrice.get()*float(DriverBBWP)))))}")
					#Condition if Qty of Small Bottle Water is not NIL
					if ReturnedSBWPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 55cl Bottle \t\t{ReturnedSBWPrice.get()}\t{(str('{:0,.2f}'.format(float(ReturnedSBWPrice.get()*float(DriverSBWP)))))}")
					#Condition if Qty of Sachet Pure Water is not NIL
					if ReturnedSPWPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 55cl Sachet \t\t{ReturnedSPWPrice.get()}\t{(str('{:0,.2f}'.format(float(ReturnedSPWPrice.get()*float(DriverSPWP)))))}")	
					DriverTxtarea.insert(END,f"\n -----------------------------------")
					#Total Bill
					DriverTxtarea.insert(END,f"\n TOTAL BILL :\t\t\t{ReturnedTotal.get()}")
					#DriverTxtarea.insert(END,f"\n -----------------------------------")
					DriverTxtarea.insert(END,f"\n ===================================")
					
					#DAMAGED Items Captured into Driver Bill
					DriverTxtarea.insert(END,f"\n ---------- ITEMS DAMAGED ----------")
					if DamagedDBPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 18.5 Litre\t\t{DamagedDBPrice.get()}\t{(str('{:0,.2f}'.format(float(DamagedDBPrice.get()*float(DriverDBP)))))}")
					#Condition if Qty of Big Bottle Water is not NIL
					if DamagedBBWPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 75cl Bottle \t\t{DamagedBBWPrice.get()}\t{(str('{:0,.2f}'.format(float(DamagedBBWPrice.get()*float(DriverBBWP)))))}")
					#Condition if Qty of Small Bottle Water is not NIL
					if DamagedSBWPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 55cl Bottle \t\t{DamagedSBWPrice.get()}\t{(str('{:0,.2f}'.format(float(DamagedSBWPrice.get()*float(DriverSBWP)))))}")
					#Condition if Qty of Sachet Pure Water is not NIL
					if DamagedSPWPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 55cl Sachet \t\t{DamagedSPWPrice.get()}\t{(str('{:0,.2f}'.format(float(DamagedSPWPrice.get()*float(DriverSPWP)))))}")	
					DriverTxtarea.insert(END,f"\n -----------------------------------")
					#Total Bill
					DriverTxtarea.insert(END,f"\n TOTAL BILL :\t\t\t{DamagedTotal.get()}")
					#DriverTxtarea.insert(END,f"\n -----------------------------------")
					DriverTxtarea.insert(END,f"\n ===================================")
					
					#SOLD Items Captured into Driver Bill
					DriverTxtarea.insert(END,f"\n ----------- ITEMS SOLD -----------")
					if SoldDBPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 18.5 Litre\t\t{SoldDBPrice.get()}\t{(str('{:0,.2f}'.format(float(SoldDBPrice.get()*float(DriverDBP)))))}")
					#Condition if Qty of Big Bottle Water is not NIL
					if SoldBBWPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 75cl Bottle \t\t{SoldBBWPrice.get()}\t{(str('{:0,.2f}'.format(float(SoldBBWPrice.get()*float(DriverBBWP)))))}")
					#Condition if Qty of Small Bottle Water is not NIL
					if SoldSBWPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 55cl Bottle \t\t{SoldSBWPrice.get()}\t{(str('{:0,.2f}'.format(float(SoldSBWPrice.get()*float(DriverSBWP)))))}")
					#Condition if Qty of Sachet Pure Water is not NIL
					if SoldSPWPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 55cl Sachet \t\t{SoldSPWPrice.get()}\t{(str('{:0,.2f}'.format(float(SoldSPWPrice.get()*float(DriverSPWP)))))}")	
					DriverTxtarea.insert(END,f"\n -----------------------------------")
					#Total Bill
					DriverTxtarea.insert(END,f"\n TOTAL BILL :\t\t\t{SoldTotal.get()}")
					#DriverTxtarea.insert(END,f"\n -----------------------------------")
					DriverTxtarea.insert(END,f"\n ===================================")
					
					DriverTxtarea.config(state=DISABLED)		
						
				
				#Function to display text in the Bill Area
				#Welcome Message constant displaying
				def DriverWelcome_bill(self):
					DriverTxtarea.config(state=NORMAL)
					DriverTxtarea.delete('1.0',END)
					#The use of \t for tab to indent location of he welcome message
					DriverTxtarea.insert(END,"    Welcome to Kwambal Table Water")
					#Capture Company Address
					DriverTxtarea.insert(END,f"\n    Plot 9 No.64 Opp. Trailer Park\n Pompomari Bypass M/guri, Borno State")
					#Calling the function to display timeframe at exact point of generating Bill
					DriverTxtarea.insert(END,f"\n \t{self.Time_get()}")
					#Adding more text with ability to capture Driver details
					#Modified the Bill Number here to half of Bill Number of Customer
					#DriverTxtarea.insert(END,f"\n Bill Number   : {int(int(self.BillNo.get())/2)}")
					DriverTxtarea.insert(END,f"\n Bill Number   : {DriverBillNumber.get()}")
					DriverTxtarea.insert(END,f"\n Driver's Name : {DriverName.get()}")
					DriverTxtarea.insert(END,f"\n Phone Number  : {DriverPhone.get()}")
					DriverTxtarea.insert(END,f"\n Plate Number  : {DriverPlateNumber.get()}")
					DriverTxtarea.insert(END,f"\n ----------- ITEMS GIVEN -----------")
					DriverTxtarea.insert(END,f"\n ===================================")
					DriverTxtarea.insert(END,f"\n Items\t\tQTY\tPrice")
					DriverTxtarea.insert(END,f"\n ===================================")
					DriverTxtarea.config(state=DISABLED)
				
				#Updating the Text_Bill also requires Updating Generate Bill
				#But we do not need new features just needed the Qty and the amount
				def DriverAddBill_area(self):
					DriverTxtarea.config(state=NORMAL)
					self.PriceMultiplier()
					self.DriverGivenTotal()
					#Enabling the txtarea to allow modification
					#self.Welcome_bill()
					#Condition if Qty of Bottle Dispenser is not NIL
					#Enable display of item name, qty and subtotal cost of any item whose Qty order is above 0
					self.UpdateDriverWelcome_bill()
					if GivenDBPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 18.5 Litre\t\t{GivenDBPrice.get()}\t{(str('{:0,.2f}'.format(float(GivenDBPrice.get()*float(DriverDBP)))))}")
					#Condition if Qty of Big Bottle Water is not NIL
					if GivenBBWPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 75cl Bottle \t\t{GivenBBWPrice.get()}\t{(str('{:0,.2f}'.format(float(GivenBBWPrice.get()*float(DriverBBWP)))))}")
					#Condition if Qty of Small Bottle Water is not NIL
					if GivenSBWPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 55cl Bottle \t\t{GivenSBWPrice.get()}\t{(str('{:0,.2f}'.format(float(GivenSBWPrice.get()*float(DriverSBWP)))))}")
					#Condition if Qty of Sachet Pure Water is not NIL
					if GivenSPWPrice.get()!=0:
						DriverTxtarea.insert(END,f"\n 55cl Sachet \t\t{GivenSPWPrice.get()}\t{(str('{:0,.2f}'.format(float(GivenSPWPrice.get()*float(DriverSPWP)))))}")	
					DriverTxtarea.insert(END,f"\n -----------------------------------")
					#Total Bill
					DriverTxtarea.insert(END,f"\n TOTAL BILL :\t\t\t{GivenTotal.get()}")
					#DriverTxtarea.insert(END,f"\n -----------------------------------")
					DriverTxtarea.insert(END,f"\n ------- Kindly Drive Safely -------")
					DriverTxtarea.insert(END,f"\n -----------------------------------")
					DriverTxtarea.config(state=DISABLED)
					
					#After generating and saving bill, there is need to disable the txtarea from been modified
				
				#Function to display text in the Bill Area
				#Welcome Message constant displaying
				def UpdateDriverWelcome_bill(self):
					DriverTxtarea.config(state=NORMAL)
					DriverTxtarea.delete('1.0',END)
					#The use of \t for tab to indent location of he welcome message
					DriverTxtarea.insert(END,"    Welcome to Kwambal Table Water")
					#Capture Company Address
					DriverTxtarea.insert(END,f"\n    Plot 9 No.64 Opp. Trailer Park\n Pompomari Bypass M/guri, Borno State")
					#Calling the function to display timeframe at exact point of generating Bill
					#DriverTxtarea.insert(END,f"\n \t{self.Time_get()}")
					DriverTxtarea.insert(END,f"\n \t{DriverIssuedDateStamp.get()}")
					#Adding more text with ability to capture Driver details
					#Modified the Bill Number here to half of Bill Number of Customer
					#DriverTxtarea.insert(END,f"\n Bill Number   : {int(int(self.BillNo.get())/2)}")
					DriverTxtarea.insert(END,f"\n Bill Number   : {DriverBillNumber.get()}")
					DriverTxtarea.insert(END,f"\n Driver's Name : {DriverName.get()}")
					DriverTxtarea.insert(END,f"\n Phone Number  : {DriverPhone.get()}")
					DriverTxtarea.insert(END,f"\n Plate Number  : {DriverPlateNumber.get()}")
					DriverTxtarea.insert(END,f"\n ----------- ITEMS GIVEN -----------")
					DriverTxtarea.insert(END,f"\n ===================================")
					DriverTxtarea.insert(END,f"\n Items\t\tQTY\tPrice")
					DriverTxtarea.insert(END,f"\n ===================================")
				
				def DriverClear_data(self):
					#clear=messagebox.askyesno("Clear Data","Do you really want to Clear Screen?")
					#if clear>0:
					#Enabling the txtarea to allow modification
					DriverTxtarea.config(state=NORMAL)
					#Clear Driver Data
					DriverName.set("")
					DriverPhone.set("")
					DriverPlateNumber.set("")
					#Clear Given Items Variables
					GivenDBPrice.set("0")
					GivenBBWPrice.set("0")
					GivenSBWPrice.set("0")
					GivenSPWPrice.set("0")
					#Clear Total Operation Menu Variables
					GivenTotal.set("")
					
					#Clear Returned Items Variables
					ReturnedDBPrice.set("0")
					ReturnedBBWPrice.set("0")
					ReturnedSBWPrice.set("0")
					ReturnedSPWPrice.set("0")
					#Clear Total Operation Menu Variables
					ReturnedTotal.set("N0.00")
					
					#Clear Damaged Items Variables
					DamagedDBPrice.set("0")
					DamagedBBWPrice.set("0")
					DamagedSBWPrice.set("0")
					DamagedSPWPrice.set("0")
					#Clear Total Operation Menu Variables
					DamagedTotal.set("N0.00")
					
					#Clear Sold Items Variables
					SoldDBPrice.set("0")
					SoldBBWPrice.set("0")
					SoldSBWPrice.set("0")
					SoldSPWPrice.set("0")
					#Clear Total Operation Menu Variables
					SoldTotal.set("N0.00")
					
					DriverBillNumber.set("")
					DriverIssuedDateStamp.set("")
					DriverBalancedDateStamp.set("")
					
					#BillNo. to change
					##self.BillNo=StringVar("")
					##randbillno=random.randint(1000,9999)
					#X is the miscrosecond last part of datetime
					##x=str(datetime.now()).split('.')[1]
					##self.BillNo.set(str(randbillno))
					#Newly added line of x is the microsecond
					##self.BillNo.set(str(randbillno)+x)
					
					self.DriverClearWelcome_bill()
					self.Driverfetch_data()
					
					DriverSearchedSumation.set("")
					#DriverTotalInventory.set("")
					
					#Clear Search Criteria and Text
					DriverSearch.set("")
					DriverSearch_Txt.set("")
					
					FromDriverReport.set("dd/mm/yyyy")
					ToDriverReport.set("dd/mm/yyyy")
					
					#To enable the Generate Bill again
					#self.EnableGenBill()
					#Re-enable the BillNo field so that search can be performed from that section too
					#cbill_txt.configure(state='normal')
					#Automatically focus the cursor in the Driver Name section
					DriverName_txt.focus()
					DriverTxtarea.config(state=DISABLED)
					
					UpdateDriver_btn['state']='normal'
					
					BalanceDriver_btn['state']='normal'
					
					#DriverBill_table.selection_clear()
					DriverBill_table.selection_set()
					
					AddDriver_btn['state']='normal'
				
				def DriverClearWelcome_bill(self):
					DriverTxtarea.delete('1.0',END)
					#The use of \t for tab to indent location of he welcome message
					DriverTxtarea.insert(END,"    Welcome to Kwambal Table Water")
					#Capture Company Address
					DriverTxtarea.insert(END,f"\n    Plot 9 No.64 Opp. Trailer Park\n Pompomari Bypass M/guri, Borno State\n")
					#Adding more text with ability to capture Customer details
					DriverTxtarea.insert(END,"\n Bill Number   :")
					DriverTxtarea.insert(END,f"\n Driver's Name : {DriverName.get()}")
					DriverTxtarea.insert(END,f"\n Phone Number  : {DriverPhone.get()}")
					DriverTxtarea.insert(END,f"\n Plate Number  : {DriverPlateNumber.get()}")
					DriverTxtarea.insert(END,f"\n ----------- ITEMS GIVEN -----------")
					DriverTxtarea.insert(END,f"\n ===================================")
					DriverTxtarea.insert(END,f"\n Items\t\tQTY\tPrice")
					DriverTxtarea.insert(END,f"\n ===================================")
				
				
				
				
				#New Function to Create new window for Operate Unit
				def createOperateUnit(self):	
					
					#Assign 2 to variable RunningFunction
					RunningFunction=2
							
					global DBOperated
					global BBWOperated
					global SBWOperated
					global SPWOperated
					global OperatedTotal
					
					global OperaterName
					global OperaterPhone
					global OperaterAddress
					global OperaterBillNumber
					
					global OperaterIssuedDateStamp
					
					global OperaterSearch
					global OperaterSearch_Txt
					
					global OperaterSearchedSumation
					global OperaterTotalInventory
					
					global FromOperaterReport
					global ToOperaterReport
					
					global OperaterPriceType
					
					#Operater Details
					OperaterName=StringVar()
					OperaterPhone=StringVar()
					OperaterAddress=StringVar()
					OperaterBillNumber=StringVar()
					
					#Quantity Operated
					DBOperated=IntVar()
					BBWOperated=IntVar()
					SBWOperated=IntVar()
					SPWOperated=IntVar()
					OperatedTotal=StringVar()
					
					#OperaterDate
					OperaterIssuedDateStamp=StringVar()
					
					#Summation
					OperaterSearchedSumation=IntVar()
					OperaterTotalInventory=IntVar()
					
					#Operater Search related
					OperaterSearch=StringVar()
					OperaterSearch_Txt=StringVar()
					
					FromOperaterReport=StringVar()
					ToOperaterReport=StringVar()
					
					#Operater Price Type
					OperaterPriceType=StringVar()
					
					OperateUnit = tk.Toplevel(root)
					OperateUnit.wm_iconbitmap('icon.ico')
					
					OperateUnit.state('zoomed')
					#Size of the new window
					width, height = OperateUnit.winfo_screenwidth(), OperateUnit.winfo_screenheight()
					OperateUnit.geometry('%dx%d+0+0' % (width,height))
					OperateList = tk.Label(OperateUnit, text = "Operator Unit",bd=5,relief=GROOVE,font=("arial black",15,"bold"),bg="DarkGray",fg="DarkGreen")
					OperateList.pack(side=TOP,fill=X)
					OperateUnit.focus()
					
					#=======================Operate detail frame
					Operater=LabelFrame(OperateUnit,bd=10,relief=GROOVE,text="Operator Details",font=("Arial",15,"bold"),fg="DarkRed",bg=bg_color)
					Operater.place(x=0,y=40,relwidth=1,height=80)
					
					#Label for Operater Name, same background, black text
					##DriverName_lbl=Label(Operater,text="Name",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=5,pady=2)
					#Operater Name
					##global OperaterName_txt
					##OperaterName_txt=Entry(Operater,width=29,textvariable=OperaterName,font="arial 13",bd=3,relief=SUNKEN)
					##OperaterName_txt.grid(row=0,column=1,pady=2,padx=2)
					##OperaterName_txt.focus()
					
					#Label for Operater Name, same background, black text
					global OperaterName_txt
					OperaterName_lbl=Label(Operater,text="Name",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=5,pady=2)	
					OperaterName_txt=ttk.Combobox(Operater,textvariable=OperaterName,width=28,font="arial 11 bold",state='readonly')
					#This will make the Combobox connect with the function to populate itself with the DB row data
					OperaterName_txt['values']= self.RegisteredOperater_input()
					OperaterName_txt.bind('<<ComboboxSelected>>', self.autoFullOperater)
					OperaterName_txt.grid(row=0,column=1,padx=2,pady=2)
					OperaterName_txt.focus()
					#OperaterName_txt['state']='normal'
					
					
					#Label for Operater Phone, same background, black text
					OperaterPhone_lbl=Label(Operater,text="Phone No.",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=8,pady=2)
					#Text field to Enter the Operater Phone, SUNKEN
					OperaterPhone_txt=Entry(Operater,width=18,textvariable=OperaterPhone,font="arial 13",bd=3,relief=SUNKEN,state='readonly')
					OperaterPhone_txt.grid(row=0,column=3,pady=2,padx=2)
					
					#Label for Operater Phone, same background, black text
					OperaterAddress_lbl=Label(Operater,text="Address",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=8,pady=2)
					#Text field to Enter the Operater Phone, SUNKEN
					OperaterAddress_txt=Entry(Operater,width=15,textvariable=OperaterAddress,font="arial 13",bd=3,relief=SUNKEN,state='readonly')
					OperaterAddress_txt.grid(row=0,column=5,pady=2,padx=2)
					
					#Label for Operater Phone, same background, black text
					OperaterBillNumber_lbl=Label(Operater,text="BillNo.",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=6,padx=8,pady=2)
					#Text field to Enter the Operater Phone, SUNKEN
					OperaterBillNumber_txt=Entry(Operater,width=18,textvariable=OperaterBillNumber,fg="DarkRed",font=("arial",12,"bold"),bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=7,pady=2,padx=2)
					
					#Label for Operater Phone, same background, black text
					OperaterIssuedDateStamp_lbl=Label(Operater,text="IssueDate",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=8,padx=8,pady=2)
					#Text field to Enter the Operater Phone, SUNKEN
					OperaterIssuedDateStamp_txt=Entry(Operater,width=26,textvariable=OperaterIssuedDateStamp,fg="DarkRed",font=("arial",11,"bold"),bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=9,pady=2,padx=2)
					
					
					#=======================Operater Quantity Frame
					OperaterQtyItemFrame=LabelFrame(OperateUnit,bd=10,relief=GROOVE,text="Operated Quantity",font=("Arial",15,"bold"),fg="DarkRed",bg=bg_color)
					OperaterQtyItemFrame.place(x=5,y=105,width=350,height=200)

					#Driver Dispenser Bottle
					global Operaterdbwater_txt
					Operaterdbwater_lbl=Label(OperaterQtyItemFrame,text="Dispenser Bottle",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=5,sticky="w")
					Operaterdbwater_txt=Entry(OperaterQtyItemFrame,width=8,textvariable=DBOperated,font=("arial",15,"bold"),bd=3,relief=SUNKEN)
					Operaterdbwater_txt.grid(row=0,column=1,padx=10,pady=5)
					Operaterdbwater_txt.focus()
					
					#Driver BIG Bottle water
					Operaterbbwater_lbl=Label(OperaterQtyItemFrame,text="BIG Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=5,sticky="w")
					Operaterbbwater_txt=Entry(OperaterQtyItemFrame,width=8,textvariable=BBWOperated,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)
					
					#Driver Small Bottle water
					Operatersbwater_lbl=Label(OperaterQtyItemFrame,text="Small Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=5,sticky="w")
					Operatersbwater_txt=Entry(OperaterQtyItemFrame,width=8,textvariable=SBWOperated,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)
					
					#Driver Sachet Pure water
					Operaterspwater_lbl=Label(OperaterQtyItemFrame,text="Sachet Pure Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=5,sticky="w")
					Operaterspwater_txt=Entry(OperaterQtyItemFrame,width=8,textvariable=SPWOperated,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)
					
					
					#=======================Operater Total Holder
					OperateTotalFrame=LabelFrame(OperateUnit,bd=5,relief=SUNKEN,bg=bg_color)
					OperateTotalFrame.place(x=5,y=300,width=350,height=45)
					
					PacakagedTotal_lbl=Label(OperateTotalFrame,text="Operated Total",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=8,pady=1,sticky="w")	
					PacakagedTotal_txt=Entry(OperateTotalFrame,width=12,fg="black",textvariable=OperatedTotal,font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=1,padx=2,pady=1,sticky="w")
					
					#=======================Operater Total/Add/Print, Update and Clear Button Holder
					OperaterButtonFrame1=LabelFrame(OperateUnit,bd=5,relief=SUNKEN,bg=bg_color)
					OperaterButtonFrame1.place(x=0,y=345,width=350,height=50)
					
					global AddOperater_btn
					#Button to Total/Add/Print Operater Record
					AddOperater_btn=Button(OperaterButtonFrame1,text="Total/Add",command=self.OperaterCompute_Add,bg=bg_color,fg="Green",bd=3,pady=5,width=12,font="ArialBold 10 bold")
					AddOperater_btn.grid(row=0,column=0,padx=3,pady=2)
					AddOperater_btn['state']='normal'
					
					global UpdateOperater_btn
					#Button to Update Operater Record
					UpdateOperater_btn=Button(OperaterButtonFrame1,text="Update",command=self.UpdateOperaterDB_data,bg=bg_color,fg="Blue",bd=3,pady=5,width=12,font="ArialBold 10 bold")
					UpdateOperater_btn.grid(row=0,column=1,padx=4,pady=2)
					UpdateOperater_btn['state']='disabled'
				
					#Button to Clear Screen
					ClearOperater_btn=Button(OperaterButtonFrame1,text="Clear",command=self.OperaterClear_data,bg=bg_color,fg="Red",bd=3,pady=5,width=12,font="ArialBold 10 bold").grid(row=0,column=2,padx=4,pady=2)
					
					
					#=======================Print, Search, Export and Delete Buttons
					OperaterButtonFrame2=LabelFrame(OperateUnit,bd=5,relief=SUNKEN,bg=bg_color)
					OperaterButtonFrame2.place(x=355,y=120,relwidth=1,height=50)
					
					#Operater Print Bill
					PrintOperater_btn=Button(OperaterButtonFrame2,text="Print Bill",command=self.OperaterPrint_bill,width=10,bd=3,bg=bg_color,fg="DarkRed",font="arial 12 bold").grid(row=0,column=3,padx=2,pady=2)
					
					global OperaterCombo_search
					#Operater Search DB
					#ComboBox for Operater Text area select kind of data to search
					OperaterCombo_search=ttk.Combobox(OperaterButtonFrame2,textvariable=OperaterSearch,width=14,font=("Arial",15,"normal"))
					#All Operater variables for search
					OperaterCombo_search['values']=("BillNo","Amount","PriceType","DateStamp","Name","Address","Phone","NewDateStamp","EnteredBy","PreviousTotal","UpdatedBy","UpdatedDate")
					#Position of Operater combo box
					OperaterCombo_search.grid(row=0,column=4,padx=4,pady=2)
					
					#Text Space to Type Data for Search
					#Addition of textvariable=self.search_txt
					OperaterTxt_search=Entry(OperaterButtonFrame2,textvariable=OperaterSearch_Txt,width=28,bg="LightGray",fg="DarkBlue",font=("Arial",15,"normal"),bd=5,relief=GROOVE)
					OperaterTxt_search.grid(row=0,column=5,pady=2,padx=4,sticky="w")
					
					#Button to Search OperaterDB
					#This button works with the Combo Search and Search text above
					#They must comply
					OperaterSearch_btn=Button(OperaterButtonFrame2,text="Search DB",command=self.OperaterSearch_data,width=13,bd=3,font="arial 12 bold").grid(row=0,column=6,padx=4,pady=2)
					
					#Button to Balance/Add/Print Operater Record
					#AddOperater_btn=Button(OperaterButtonFrame2,text="Balance",width=10,bd=3,bg=bg_color,fg="Green",font="ArialBold 12 bold").grid(row=0,column=7,padx=4,pady=2)
					#command=self.UpdateOperaterReturnedDamagedSoldDB_data
					
					global ExportOperater_btn
					#Button to Update Operater Return, Damage and Sold
					ExportOperater_btn=Button(OperaterButtonFrame2,text="Export-Excel",command=self.OperaterSaveCurrentTableItem,width=16,bd=3,bg=bg_color,fg="Blue",font="ArialBold 12 bold")
					ExportOperater_btn.grid(row=0,column=8,padx=4,pady=2)
					ExportOperater_btn['state']='disable'
					
					global DeleteOperater_btn
					#Button to Delete entry from DATABASE
					DeleteOperater_btn=Button(OperaterButtonFrame2,text="Delete",command=self.DeleteOperaterData,width=10,bd=3,bg=bg_color,fg="Red",font="ArialBold 12 bold")
					DeleteOperater_btn.grid(row=0,column=9,padx=4,pady=2)
					DeleteOperater_btn['state']='disable'
					
					#=======================Operater Bill Frame
					OperaterBill=LabelFrame(OperateUnit,bd=10,relief=GROOVE)
					OperaterBill.place(x=5,y=395,width=345,height=380) 
					OperaterBill_title=Label(OperaterBill,text="Bills",font="arial 15 bold",bd=5,relief=GROOVE).pack(fill=X)
				
					scroll_y=Scrollbar(OperaterBill,orient=VERTICAL)
					global OperaterTxtarea
					OperaterTxtarea=Text(OperaterBill,yscrollcommand=scroll_y.set)
					scroll_y.pack(side=RIGHT,fill=Y)
					scroll_y.config(command=OperaterTxtarea.yview)
					OperaterTxtarea.pack(fill=BOTH,expand=1)
					
					#NEWLY ADDED to ensure multiplier prices for DAY and NIGHT differs
					global OperaterPriceType_txt
					OperaterBillx=LabelFrame(OperateUnit,bd=5,relief=GROOVE)
					OperaterBillx.place(x=13,y=402,width=104,height=40)
					#OperaterPriceType_lbl=Label(OperaterBillx,text="DUTY",bg=bg_color,fg="black",font=("times new roman",10,"bold")).grid(row=0,column=0,padx=5,pady=2)	
					OperaterPriceType_txt=ttk.Combobox(OperaterBillx,textvariable=OperaterPriceType,width=8,font="arial 11 bold",state='readonly')
					OperaterPriceType_txt['values']=("DAY","NIGHT")
					OperaterPriceType_txt.grid(row=0,column=0,padx=2,pady=2)
					OperaterPriceType_txt['state']="normal"
					
					#=======================Operater Table Side Frame
					OperaterTable_Frame=LabelFrame(OperateUnit,bd=10,relief=RIDGE,bg=bg_color)
					OperaterTable_Frame.place(x=350,y=170,width=1085,height=600)
					
					#=======================DISPLAY FOR ALL Operater BILL ENTRY
					scroll_x=Scrollbar(OperaterTable_Frame,orient=HORIZONTAL)
					scroll_y=Scrollbar(OperaterTable_Frame,orient=VERTICAL)
					#Format for the required column headings that will be displayed
					global OperaterBill_table
					OperaterBill_table=ttk.Treeview(OperaterTable_Frame,columns=("BillNo","Dispenser","BigBottle","SmallBottle","SachetWater","CostDispenser","CostBigBottle","CostSmallBottle","CostSachetWater","Amount","PriceType","DateStamp","Name","Address","Phone","EnteredBy","PreviousTotal","UpdatedBy","UpdatedDate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
					
					#Scroll bar direction and configuration
					scroll_x.pack(side=BOTTOM,fill=X)
					scroll_y.pack(side=RIGHT,fill=Y)
					scroll_x.config(command=OperaterBill_table.xview)
					scroll_y.config(command=OperaterBill_table.yview)		
					
					#Connecting each heading to a column of the existing fields
					OperaterBill_table.heading("BillNo",text="BillNo")
					OperaterBill_table.heading("Dispenser",text="Dispenser")
					OperaterBill_table.heading("BigBottle",text="BigBottle")
					OperaterBill_table.heading("SmallBottle",text="SmallBottle")
					OperaterBill_table.heading("SachetWater",text="SachetWater")
					
					OperaterBill_table.heading("CostDispenser",text="CostDispenser")
					OperaterBill_table.heading("CostBigBottle",text="CostBigBottle")
					OperaterBill_table.heading("CostSmallBottle",text="CostSmallBottle")
					OperaterBill_table.heading("CostSachetWater",text="CostSachetWater")
					
					OperaterBill_table.heading("Amount",text="Amount")
					OperaterBill_table.heading("PriceType",text="PriceType")
					OperaterBill_table.heading("DateStamp",text="DateStamp")
					OperaterBill_table.heading("Name",text="Name")
					OperaterBill_table.heading("Address",text="Address")
					OperaterBill_table.heading("Phone",text="Phone")
					OperaterBill_table.heading("EnteredBy",text="EnteredBy")
					OperaterBill_table.heading("PreviousTotal",text="PreviousTotal")
					OperaterBill_table.heading("UpdatedBy",text="UpdatedBy")
					OperaterBill_table.heading("UpdatedDate",text="UpdatedDate")
					
					#Enable heading of tables to show
					OperaterBill_table['show']='headings'
					
					#Set column width for each field in the table
					OperaterBill_table.column("BillNo",width=120)
					OperaterBill_table.column("Dispenser", anchor="center", width=80)
					OperaterBill_table.column("BigBottle", anchor="center", width=80)
					OperaterBill_table.column("SmallBottle", anchor="center", width=80)
					OperaterBill_table.column("SachetWater", anchor="center", width=80)
					#Cost
					OperaterBill_table.column("CostDispenser", anchor="center", width=100)
					OperaterBill_table.column("CostBigBottle", anchor="center", width=100)
					OperaterBill_table.column("CostSmallBottle", anchor="center", width=100)
					OperaterBill_table.column("CostSachetWater", anchor="center", width=100)
					
					OperaterBill_table.column("Amount", anchor="e", width=100)
					OperaterBill_table.column("PriceType", anchor="e", width=100)
					OperaterBill_table.column("DateStamp",width=150)
					OperaterBill_table.column("Name",width=120)
					OperaterBill_table.column("Address",width=120)
					OperaterBill_table.column("Phone",width=120)
					OperaterBill_table.column("EnteredBy", anchor="center", width=120)
					OperaterBill_table.column("PreviousTotal", anchor="center", width=120)
					OperaterBill_table.column("UpdatedBy", anchor="center", width=120)
					OperaterBill_table.column("UpdatedDate", anchor="center", width=120)

					#To expand the table  
					OperaterBill_table.pack(fill=BOTH,expand=1)
					#Enable selection of items in the Bill_table
					OperaterBill_table.bind("<ButtonRelease-1>",self.OperaterBillget_cursor)
					
					
					#=======================Operater Bottom Frame
					OperaterBottomFrame=LabelFrame(OperateUnit,bd=5,relief=GROOVE,bg=bg_color)
					OperaterBottomFrame.place(x=0,y=780,relwidth=1,height=80)
					
					OperaterAmountSelected_lbl=Label(OperaterBottomFrame,text="Sub-Total",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=10,pady=1,sticky="w")	
					OperaterAmountSelected_txt=Entry(OperaterBottomFrame,width=18,textvariable=OperaterSearchedSumation,fg="red",font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=3,padx=10,pady=1)
					
					OperaterTotalInventory_lbl=Label(OperaterBottomFrame,text="TOTAL",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=10,pady=1,sticky="w")	
					OperaterTotalInventory_txt=Entry(OperaterBottomFrame,width=19,textvariable=OperaterTotalInventory,fg="red",font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=5,padx=10,pady=1)
					
					global GenerateReportOperaterFrom_txt
					GenerateReportOperaterFrom_lbl=Label(OperaterBottomFrame,text="From:",bg=bg_color,fg="Black",font=("times new roman",12,"bold")).grid(row=0,column=6,padx=17,pady=1,sticky="w")	
					GenerateReportOperaterFrom_txt=Entry(OperaterBottomFrame,width=10,textvariable=FromOperaterReport,fg="Black",font="arial 12 bold",bd=3,relief=SUNKEN)
					GenerateReportOperaterFrom_txt.grid(row=0,column=7,padx=2,pady=1)
					
					global GenerateReportDriverTo_txt
					GenerateReportOperaterTo_lbl=Label(OperaterBottomFrame,text="To:::",bg=bg_color,fg="Black",font=("times new roman",12,"bold")).grid(row=0,column=8,padx=2,pady=1,sticky="w")	
					GenerateReportOperaterTo_txt=Entry(OperaterBottomFrame,width=10,textvariable=ToOperaterReport,fg="Black",font="arial 12 bold",bd=3,relief=SUNKEN)
					GenerateReportOperaterTo_txt.grid(row=0,column=9,padx=2,pady=1)	
					
					global GenerateReportOperater_btn
					GenerateReportOperater_btn=Button(OperaterBottomFrame,text="Generate Report",width=15,bd=3,bg=bg_color,fg="Green",command=self.GenerateReport_Operater,font="ArialBold 10 bold")
					GenerateReportOperater_btn.grid(row=0,column=10,padx=4,pady=2)
					GenerateReportOperater_btn['state']='disable'
					
					#Automatically Clear Screen
					self.OperaterClear_data()
					
					#Automatically focus cursor in the search txt once there is a selection of Search_by
					self.OperaterAutoFocusSearch()
					
					global OperaterDirectory
					OperaterDirectory="C:/OperaterBills/"
					
					#Function to Fetch all data from Driver Table
					self.OperaterFetchDB_data()
					
					#Welcome Screen Bill
					self.OperaterWelcome_bill()
					
					self.Operateruser_type()
					
					OperateList.pack()
					#Lovely Code that will ensure Child Window remains active and Root remains inactive until Child is Closed 
					#After Clicking on Operater Unit the new Window to Operater Unit must be fully used and closed before using main interface
					OperateUnit.transient(root)
					OperateUnit.grab_set()
					root.wait_window(OperateUnit)
				
				def DisableAddTotalUpdateBalanceOperater(self):
					#Automatically disable the Add/Total and Update Buttons
					if CurrentCategory == 'Super-Admin':
						AddOperater_btn['state']='disabled'
						UpdateOperater_btn['state']='normal'
					else:
						AddOperater_btn['state']='disabled'
						#UpdateOperater_btn['state']='disabled'
					if CurrentCategory == 'Super-Admin':
						ExportOperater_btn['state']='normal'
						DeleteOperater_btn['state']='normal'
						GenerateReportOperater_btn['state']='normal'
					
				def Operateruser_type(self):
					if CurrentCategory == 'Super-Admin':
						DeleteOperater_btn['state']='normal'
				
				
				#Generate REPORT Normal Sales
				def GenerateReport_Operater(self):
					try:
						#If one or both of the criteria is/are empty
						if FromOperaterReport.get()=="" or ToOperaterReport.get()=="":
							messagebox.showerror("Report Error","Date From: and Date To: \nAre compulsory")
							
						elif FromOperaterReport.get()=="dd/mm/yyyy" or len((str(FromOperaterReport.get()).split('/')[2]))!=4 or int((str(FromOperaterReport.get()).split('/')[1]))>12:
							messagebox.showerror("Data Error","Date FROM must be in dd/mm/yyyy format")
							GenerateReportOperaterFrom_txt.focus()
						
						elif ToOperaterReport.get()=="dd/mm/yyyy" or len((str(ToOperaterReport.get()).split('/')[2]))!=4 or int((str(ToOperaterReport.get()).split('/')[1]))>12:
							messagebox.showerror("Data Error","Date TO must be in dd/mm/yyyy format")
							GenerateReportOperaterTo_txt.focus()
							
						else:
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("select * from operaterbills where DateStamp BETWEEN '"+str(FromOperaterReport.get())+" 00:00:00.000000' AND '"+str(ToOperaterReport.get())+" 99:99:99.999999'")
							OperaterBill_table.delete(*OperaterBill_table.get_children())
							rows=cur.fetchall()
							if len(rows)<1:
								con.close()
								messagebox.showinfo('No Data!',"No record was captured within date range")
							elif len(rows)>=1:
								OperaterBill_table.delete(*OperaterBill_table.get_children())
								for row in rows:
									OperaterBill_table.insert('',END,values=row)
								con.commit()
								con.close()
								#Auto focus the last record from the records returned after search
								child_id = OperaterBill_table.get_children()[-1]
								cursor_row = OperaterBill_table.focus(child_id)
								OperaterBill_table.selection_set(child_id)
								self.OperaterBillget_cursor(cursor_row)
								
								#Calling a function to do Sub-Total Sum all items displayed in table after every search performed
								self.OperaterSearchedSum()
								
								#SAVE but ask use first
								savereport=messagebox.askyesno("Driver Report","Report Successfully Retrieved \nDo you want to Save this Report?")
								if savereport>0:
									self.OperaterSaveCurrentTableItem()
								else:
									pass
							
					except ValueError:
						messagebox.showerror("Data Report Error","Invalid data entry")

				
				#Automatically Fill Operater Details after FullName Selection
				def autoFullOperater(self, event):
					#Connection to the Database
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					
					#Getting the exact MobileNo of the Fullname
					cur.execute("select MobileNo FROM register WHERE FullName = '"+OperaterName.get()+"'")
					row=cur.fetchall()
					OperaterPhone.set(row[0])
					
					#Getting the exact VehicleNo of the Fullname
					cur.execute("select Address FROM register WHERE FullName = '"+OperaterName.get()+"'")
					row=cur.fetchall()
					for rows in row:
						#print(rows[0])
						OperaterAddress.set(str(rows[0]))
					
					Operaterdbwater_txt.focus()
				
				#Function to connect to DB and populate Data in a Column as the Drop Down Values another Combobox
				def RegisteredOperater_input(self):
					#Connection to the Database
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					#cur.execute("select * from register WHERE UserID = '" + ery2.get() + "' AND Password = '" + ery3.get() + "'")
					cur.execute("select FullName FROM register WHERE Category = 'Operator'")
					data=[]
					
					for row in cur.fetchall():
						data.append(row[0])
					return data
				
				#Print Bill for Operater
				def OperaterPrint_bill(self):
					##Check if the Bill No. is blank string then it Prints using the Bill No. in the text area
					if OperaterBillNumber.get()!="":
						self.OperaterSaveBill()
						#Opens the main file using the Bill No.
						fin = open("C:/OperaterBills/"+str(OperaterBillNumber.get())+".txt","rt")
						#Create another temporary file mainly for printing format
						fout = open("C:/OperaterBills/printout.txt","wt")
						#Condition statement for each line in the file main fin
						for line in fin:
							#If the line startswith Items then just print it like that
							if line.startswith(" Items"):
								fout.write(line)
							#Else try to replace double tabs \t\t on any other lines with single tab \t
							else:
								#print(line.rstrip().replace("\t\t","\t"))
								fout.write(line.replace("\t\t","\t"))
						#Close the files
						fin.close()
						fout.close()
						os.startfile("C:/OperaterBills/printout.txt","print")
					##Else it will automatically PRINT using the Bill No. in the Search
					else:
						messagebox.showerror("Print Error","Kindly select a Bill to print")	
				
				#Function to Save Operater Bill as Text File
				#I have to global OperaterDirectory as C:/operaterbills at the header of Operater Section
				def OperaterSaveBill(self):
					#op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
					#if op>0:
					Operaterbill_data=OperaterTxtarea.get('1.0',END)
					if not os.path.exists(OperaterDirectory):
						os.makedirs(OperaterDirectory)
					f1=open("C:/OperaterBills/"+str(OperaterBillNumber.get())+".txt","w")
					f1.write(Operaterbill_data)
					f1.close()
				
				def OperaterSaveCurrentTableItem(self):
					#Empty list for each column in the treeview
					column1_list = []
					column2_list = []
					column3_list = []
					column4_list = []
					column5_list = []
					column6_list = []
					column7_list = []
					column8_list = []
					column9_list = []
					column10_list = []
					column11_list = []
					column12_list = []
					column13_list = []
					column14_list = []
					column15_list = []
					column16_list = []
					column17_list = []
					column18_list = []
					column19_list = []
					
					
					#running through the lines of the treeview in a "for" function, append to each column list the value of the column in each line
					for child in OperaterBill_table.get_children():
						column1_list.append(OperaterBill_table.item(child)["values"][0]) 
						column2_list.append(OperaterBill_table.item(child)["values"][1]) 
						column3_list.append(OperaterBill_table.item(child)["values"][2]) 
						column4_list.append(OperaterBill_table.item(child)["values"][3]) 
						column5_list.append(OperaterBill_table.item(child)["values"][4]) 
						column6_list.append(OperaterBill_table.item(child)["values"][5]) 
						column7_list.append(OperaterBill_table.item(child)["values"][6]) 
						column8_list.append(OperaterBill_table.item(child)["values"][7]) 
						column9_list.append(OperaterBill_table.item(child)["values"][8]) 
						column10_list.append(OperaterBill_table.item(child)["values"][9]) 
						column11_list.append(OperaterBill_table.item(child)["values"][10]) 
						column12_list.append(OperaterBill_table.item(child)["values"][11]) 
						column13_list.append(OperaterBill_table.item(child)["values"][12]) 
						column14_list.append(OperaterBill_table.item(child)["values"][13]) 
						column15_list.append(OperaterBill_table.item(child)["values"][14]) 
						column16_list.append(OperaterBill_table.item(child)["values"][15]) 
						column17_list.append(OperaterBill_table.item(child)["values"][16]) 
						column18_list.append(OperaterBill_table.item(child)["values"][17]) 
						column19_list.append(OperaterBill_table.item(child)["values"][18])
					
					#create a dictionary from all the lists, using the header as the key and lists are the values as a list
					Operaterfull_treeview_data_dict = {'BillNo': column1_list, 'Dispenser': column2_list, 'BigBottle': column3_list, 'SmallBottle': column4_list, 'SachetWater': column5_list, 'CostDispenser': column6_list, 'CostBigBottle': column7_list,
												'CostSmallBottle': column8_list, 'CostSachetWater': column9_list, 'Amount': column10_list, 'PriceType': column11_list, 'DateStamp': column12_list, 'Name': column13_list, 'Address': column14_list,
												'Phone': column15_list, 'EnteredBy': column16_list, 'PreviousTotal': column17_list, 'UpdatedBy': column18_list, 'UpdatedDate': column19_list}
												
					#Create a dataframe from the dictionary
					Operatertreeview_df = pd.DataFrame.from_dict(Operaterfull_treeview_data_dict)
					
					#print(Operatertreeview_df)
					if len(operaterdata) < 1:
						messagebox.showerror("No Data","No data available to export")
						return False
					try:
						filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Save to Excel',defaultextension='.xlsx',filetypes=[("Excel file", "*.xlsx")])
						Operatertreeview_df.to_excel(filename, engine='xlsxwriter',index= False)
						messagebox.showinfo("Data Exported","Your data has been exported to "+os.path.basename(filename)+" successfully.")
					except:
						pass
				
				
				
				def OperaterCompute_Add(self):
					self.OperaterAdd_bills()
					#self.UpdateOperaterDB_data()
					self.OperaterAddBill_area()
				
				#Function to display text in the Bill Area with Welcome Message constant displaying
				def OperaterWelcome_bill(self):
					OperaterTxtarea.config(state=NORMAL)
					OperaterTxtarea.delete('1.0',END)
					#The use of \t for tab to indent location of he welcome message
					OperaterTxtarea.insert(END,"    Welcome to Kwambal Table Water")
					#Capture Company Address
					OperaterTxtarea.insert(END,f"\n    Plot 9 No.64 Opp. Trailer Park\n Pompomari Bypass M/guri, Borno State")
					OperaterTxtarea.insert(END,f"\n \t{self.Time_get()}")
					if OperaterPriceType_txt.get()==('DAY'):
						OperaterTxtarea.insert(END,f"\n {OperaterPriceType.get()} Bill No.    : {OperaterBillNumber.get()}")
					else:
						OperaterTxtarea.insert(END,f"\n {OperaterPriceType.get()} Bill No.  : {OperaterBillNumber.get()}")
					OperaterTxtarea.insert(END,f"\n Operator's Name : {OperaterName.get()}")
					OperaterTxtarea.insert(END,f"\n Phone Number    : {OperaterPhone.get()}")
					OperaterTxtarea.insert(END,f"\n Address         : {OperaterAddress.get()}")
					OperaterTxtarea.insert(END,f"\n ---------- PACKAGING COST ---------")
					OperaterTxtarea.insert(END,f"\n ===================================")
					OperaterTxtarea.insert(END,f"\n Items\t\tQTY\tPrice")
					OperaterTxtarea.insert(END,f"\n ===================================")
					OperaterTxtarea.config(state=DISABLED)
				
				
				#Updating the Text_Bill also requires Updating Generate Bill
				#But we do not need new features just needed the Qty and the amount
				def OperaterAddBill_area(self):
					OperaterTxtarea.config(state=NORMAL)
					self.OperatorPriceMultiplier()
					self.OperaterGivenTotal()
					#Enabling the txtarea to allow modification
					#self.Welcome_bill()
					#Condition if Qty of Bottle Dispenser is not NIL
					#Enable display of item name, qty and subtotal cost of any item whose Qty order is above 0
					self.UpdateOperaterWelcome_bill()
					if DBOperated.get()!=0:
						OperaterTxtarea.insert(END,f"\n 18.5 Litre\t\t{DBOperated.get()}\t{(str('{:0,.2f}'.format(float(DBOperated.get()*float(OperateDBP)))))}")
					#Condition if Qty of Big Bottle Water is not NIL
					if BBWOperated.get()!=0:
						OperaterTxtarea.insert(END,f"\n 75cl Bottle \t\t{BBWOperated.get()}\t{(str('{:0,.2f}'.format(float(BBWOperated.get()*float(OperateBBWP)))))}")
					#Condition if Qty of Small Bottle Water is not NIL
					if SBWOperated.get()!=0:
						OperaterTxtarea.insert(END,f"\n 55cl Bottle \t\t{SBWOperated.get()}\t{(str('{:0,.2f}'.format(float(SBWOperated.get()*float(OperateSBWP)))))}")
					#Condition if Qty of Sachet Pure Water is not NIL
					if SPWOperated.get()!=0:
						OperaterTxtarea.insert(END,f"\n 55cl Sachet \t\t{SPWOperated.get()}\t{(str('{:0,.2f}'.format(float(SPWOperated.get()*float(OperateSPWP)))))}")	
					OperaterTxtarea.insert(END,f"\n -----------------------------------")
					#Total Bill
					OperaterTxtarea.insert(END,f"\n TOTAL BILL :\t\t\t{OperatedTotal.get()}")
					#OperaterTxtarea.insert(END,f"\n -----------------------------------")
					OperaterTxtarea.insert(END,f"\n ----- Be Honest, Brave & True -----")
					OperaterTxtarea.insert(END,f"\n -----------------------------------")
					OperaterTxtarea.config(state=DISABLED)
					
					#After generating and saving bill, there is need to disable the txtarea from been modified
				
				#Function to display text in the Bill Area
				#Welcome Message constant displaying
				def UpdateOperaterWelcome_bill(self):
					OperaterTxtarea.config(state=NORMAL)
					OperaterTxtarea.delete('1.0',END)
					#The use of \t for tab to indent location of he welcome message
					OperaterTxtarea.insert(END,"    Welcome to Kwambal Table Water")
					#Capture Company Address
					OperaterTxtarea.insert(END,f"\n    Plot 9 No.64 Opp. Trailer Park\n Pompomari Bypass M/guri, Borno State")
					OperaterTxtarea.insert(END,f"\n \t{OperaterIssuedDateStamp.get()}")
					if OperaterPriceType.get()==('DAY'):
						OperaterTxtarea.insert(END,f"\n {OperaterPriceType.get()} Bill No.    : {OperaterBillNumber.get()}")
					else:
						OperaterTxtarea.insert(END,f"\n {OperaterPriceType.get()} Bill No.  : {OperaterBillNumber.get()}")
					OperaterTxtarea.insert(END,f"\n Operator's Name : {OperaterName.get()}")
					OperaterTxtarea.insert(END,f"\n Phone Number    : {OperaterPhone.get()}")
					OperaterTxtarea.insert(END,f"\n Address         : {OperaterAddress.get()}")
					OperaterTxtarea.insert(END,f"\n ---------- PACKAGING COST ---------")
					OperaterTxtarea.insert(END,f"\n ===================================")
					OperaterTxtarea.insert(END,f"\n Items\t\tQTY\tPrice")
					OperaterTxtarea.insert(END,f"\n ===================================")
				
				#NEW Function to fetch data
				def Operaterfetch_data(self):
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					cur.execute("select * from operaterbills order by DateStamp DESC")		
					rows=cur.fetchall()
					
					##NEWLY
					global operaterdata
					operaterdata=rows
					
					if len(rows)!=0:
						OperaterBill_table.delete(*OperaterBill_table.get_children())
						for row in rows:
							OperaterBill_table.insert('',END,values=row)
						con.commit()
					con.close()
				
				#Summation of Searched Amount in Operater Record
				def OperaterSearchedSum(self):
					#Variable Stubtotal is used as accumulator set at 0.00 float
					Stubtotal = 0.00
					#For Every child of the table
					for child in OperaterBill_table.get_children():
						#Accumulate the sum of each item displayed
						Stubtotal += float(OperaterBill_table.item(child,'values')[9])
					#Transferring the sum above into the Sub-total text holder
					OperaterSearchedSumation.set("N"+str("{:0,.2f}".format(Stubtotal)))

				def OperaterAutoFocusSearch(self):
					if OperaterSearch.get()!="":
						OperaterTxt_search.focus()
				
				#This function will search using the search_by and search_txt to populate the data from DB to Table
				def OperaterSearch_data(self):
					##try:
					#If one or both of the criteria is/are empty
					if OperaterSearch.get()=="" or OperaterSearch_Txt.get()=="":
						messagebox.showerror("Search Error","Select Search by and \nType correct keyword")
					else:
						con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
						cur=con.cursor()
						if cur.execute("select * from operaterbills where "+str(OperaterSearch.get())+" LIKE '%"+str(OperaterSearch_Txt.get())+"%'"):
							rows=cur.fetchall()
							if len(rows)!=0:
								OperaterBill_table.delete(*OperaterBill_table.get_children())
								for row in rows:
									OperaterBill_table.insert('',END,values=row)
								con.commit()
							con.close()
							#Auto focus the last record from the records returned after search
							child_id = OperaterBill_table.get_children()[-1]
							cursor_row = OperaterBill_table.focus(child_id)
							OperaterBill_table.selection_set(child_id)
							self.OperaterBillget_cursor(cursor_row)
							
							#Calling a function to do Sub-Total Sum all items displayed in table after every search performed
							self.OperaterSearchedSum()
							#NEWLY
							#self.DisableGenBill()
						else:
							messagebox.showerror("Data Search Error","You have made an invalid data search\n"+OperaterSearch_Txt.get()+" does not exist.")
							#Then automatically show all records from DB
							self.OperaterFetchDB_data()
							#clear screen
							self.OperaterClear_data()
				
				
				#Delete Operater record from DB 	
				def DeleteOperaterData(self):
					ask=messagebox.askyesno("Deleting Record","Are you sure to proceed with delete! \nYou cannot undo this action")
					if ask==True:
						con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
						cur=con.cursor()
						cur.execute("delete from operaterbills where BillNo=%s",OperaterBillNumber.get())
						con.commit()
						con.close()
						#Clear Screen
						self.OperaterClear_data()
						#Function of fetch_data is called here
						self.OperaterFetchDB_data()	
				
				
				#Update Operater Given Records
				def UpdateOperaterDB_data(self):
					if OperaterBillNumber.get()=="" or OperatedTotal.get()=="":
						messagebox.showerror("Update Error","Select record from table\n and Insert valid data")
					else:
						self.OperaterGivenTotal()
						OperaterTotalPayable=OperatedTotal.get().replace("N","").replace(",","")
						ask=messagebox.askyesno("Update Record","Are you sure to proceed with update!")
						if ask==True:
							self.mynice_date()
							updatedate=today_date
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("update operaterbills set Dispenser=%s,BigBottle=%s,SmallBottle=%s,SachetWater=%s,CostDispenser=%s,CostBigBottle=%s,CostSmallBottle=%s,CostSachetWater=%s,Amount=%s,PriceType=%s,DateStamp=%s,Name=%s,Address=%s,Phone=%s,PreviousTotal=%s,UpdatedBy=%s,UpdatedDate=%s where BillNo=%s",(
																																																											DBOperated.get(),
																																																											BBWOperated.get(),
																																																											SBWOperated.get(),
																																																											SPWOperated.get(),
																																																											OperateDBP,
																																																											OperateBBWP,
																																																											OperateSBWP,
																																																											OperateSPWP,
																																																											OperaterTotalPayable,
																																																											OperaterPriceType.get(),
																																																											OperaterIssuedDateStamp.get(),
																																																											OperaterName.get(),
																																																											OperaterAddress.get(),
																																																											OperaterPhone.get(),
																																																											PreviousOperaterAmount,
																																																											v,
																																																											updatedate,
																																																											OperaterBillNumber.get()
																																																											))
							con.commit()

							#NEWLY To auto focus the selection Balanced is performed on any selected Record
							#Using variable xx and yy to get the current fucos and index of the focus iid
							#This is done before the fetching of Database from DB to the TreeView
							xx=OperaterBill_table.focus()
							yy=OperaterBill_table.index(xx)
							#print(yy)				
							
							#Function of fetch_data is called here
							self.OperaterFetchDB_data()
				
							#NEWLY To auto focus the selection Balanced selected Record
							child_id = OperaterBill_table.get_children()[yy]
							cursor_row=OperaterBill_table.focus(child_id)
							OperaterBill_table.selection_set(child_id)
							
							#NEWLY ADDED
							#Display current values in the Bill Text area depending
							self.OperaterAddBill_area()			
							
							#After fetching the data then save the text file too
							#Save Operater Bill to Text
							self.OperaterSaveBill()
							
							#Disable Update Button
							UpdateOperater_btn['state']='disabled'
						
							con.close()
				

			
				def OperaterBillget_cursor(self,ev):
					try:
						cursor_row=OperaterBill_table.focus()
						contents=OperaterBill_table.item(cursor_row)
						row=contents['values']
						OperaterBillNumber.set(row[0])
						DBOperated.set(row[1])
						BBWOperated.set(row[2])
						SBWOperated.set(row[3])
						SPWOperated.set(row[4])
						OperatedTotal.set("N"+str("{:0,.2f}".format(float(row[9]))))
						OperaterPriceType.set(row[10])
						OperaterIssuedDateStamp.set(row[11])
						OperaterName.set(row[12])
						OperaterAddress.set(row[13])
						OperaterPhone.set(row[14])
						
						global PreviousOperaterAmount
						PreviousOperaterAmount=(row[9])
						
						#This code disable Update Record Button once it has been previously Updated 1ce
						if CurrentCategory == 'Super-Admin':
							AddOperater_btn['state']='disabled'
							UpdateOperater_btn['state']='normal'
							OperaterPriceType_txt['state']='normal'
						elif CurrentCategory == 'Admin':
							if (row[16]) != "":
								AddOperater_btn['state']='disabled'
								UpdateOperater_btn['state']='disabled'
								OperaterPriceType_txt['state']='disabled'
							else:
								UpdateOperater_btn['state']='normal'
								OperaterPriceType_txt['state']='normal'
						
						
						self.OperaterAddBill_area()
						
						self.DisableAddTotalUpdateBalanceOperater()

					except:
						pass
				
				def OperaterAdd_bills(self):
					#try:
					ask=messagebox.askyesno("Add Operater Record","Do you really want to ADD this record?")
					if ask==True:
						#if self.TotalPayable.get()=="" and self.BillNo.get()=="" and self.CurrentTime.get()=="":
						#Newly added line appending the microsecond to BillNo for uniqueness
						
						#New Bill Code Starting With YYMMDD
						yy=str(datetime.now()).split(' ')[0]
						yy=str((yy[2:]).replace('-',''))
						#print(yy)
						
						x=str(datetime.now()).split('.')[1]+str("O")
						randbillno=random.randint(10000,99999)
						OperaterBillNumber.set(yy+str(randbillno)+x)
						
						self.mynice_date()
						#Capture the Date Issued
						##y=str(datetime.now())
						OperaterIssuedDateStamp.set(today_date)
						
						#Call Functions to perform Total Given by acquiring price multiplier DBPrice, BBWPrice, SBWPrice and SPWPrice
						self.OperaterGivenTotal()
						#self.PriceMultiplier()
					
						#Remove Naira sign and comma from all TOTALs
						TotalPayable=OperatedTotal.get().replace("N","").replace(",","")			
			
						#TotalPayable=float(TotalPayable)
						#print(TotalPayable)
						if OperaterName.get()=="":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nOperater Name is mandatory")
							self.OperaterClear_data()
						elif TotalPayable=="" or TotalPayable=="0.00":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nBillNo. and TotalBill are mandatory")
							self.OperaterClear_data()
						else:
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("insert into operaterbills values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(OperaterBillNumber.get(),
																														DBOperated.get(),
																														BBWOperated.get(),
																														SBWOperated.get(),
																														SPWOperated.get(),
																														OperateDBP,
																														OperateBBWP,
																														OperateSBWP,
																														OperateSPWP,
																														TotalPayable,
																														OperaterPriceType.get(),
																														OperaterIssuedDateStamp.get(),
																														OperaterName.get(),
																														OperaterAddress.get(),
																														OperaterPhone.get(),
																														v,
																														"",
																														"",
																														""
																														))

							#Function of fetch_data is called here	
							con.commit()
							
							#NEWEST
							self.OperaterFetchDB_data()
							
							con.close()
							
							#Operater Bill Text Area
							self.OperaterAddBill_area()
							
							#Save Operater Bill to Text
							self.OperaterSaveBill()
							
							#NEWEST Auto Highlight the record that was added in the Operater Table TreeView
							#Auto focus the first record from the records returned after New Addition
							child_id = OperaterBill_table.get_children()[0]
							cursor_row=OperaterBill_table.focus(child_id)
							OperaterBill_table.selection_set(child_id)
							self.OperaterBillget_cursor(cursor_row)
							
							#Message box to indicate successfully added
							messagebox.showinfo('Successfully added!',"The record has been captured")
					else:
						pass
				
				#Total of all items in general given to all drivers to display below screen
				def OperaterDBTOTAL(self):
					#Using a try and catch error incase when the Database is wiped
					#Opening the app will automatically want to Calculate all Total Inventory
					try:
						#Amount=float(Amount.repalce("N","").replace(",",""))
						con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
						cur=con.cursor()
						cur.execute("SELECT sum(Amount) AS totalsum FROM operaterbills")
						result=cur.fetchall()
						for i in result:
							#print(i[0])
							OperaterTotalInventory.set("N"+str("{:0,.2f}".format(i[0])))
						con.commit()
					except TypeError:
						pass
				
				#NEW Function to fetch Price data
				def OperaterFetchDB_data(self):
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					#Sorting the data fetched to display in descending order of DateStamp
					cur.execute("select * from operaterbills order by DateStamp DESC")
					rows=cur.fetchall()
					if len(rows)!=0:
						OperaterBill_table.delete(*OperaterBill_table.get_children())
						for row in rows:
							OperaterBill_table.insert('',END,values=row)
						con.commit()
					self.OperaterDBTOTAL()
					con.close()
				
				
				
				
				
				#OperateR FUNCTIONS COMPUTE GIVEN TOTALS
				def OperaterGivenTotal(self):
					try:
						#Run function to Recapture the Current Price data from the DB as Variables and use as Multiplier
						self.OperatorPriceMultiplier()
						
						#This will automatically sum values in Currency of 2 decimal places		
						#Added a N for Naira sign, must be: self.TotalPayable.get().replace("N","").replace(",","") when calculating
						#GIVEN TOTAL
						OperatedTotal.set("N"+str("{:0,.2f}".format(
															float((str("{:0,.2f}".format(float(DBOperated.get()*float(OperateDBP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(BBWOperated.get()*float(OperateBBWP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(SBWOperated.get()*float(OperateSBWP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(SPWOperated.get()*float(OperateSPWP))))).replace(",",""))
															)))
						#self.DriverWelcome_bill()
							
					except TclError:
						#Display this message
						messagebox.showerror("Data Error","You have made an invalid \ndata entry")
				
				
				
				def OperaterClear_data(self):
					##OperaterTxtarea.config(state=NORMAL)
					#Clear Operater Data
					OperaterName.set("")
					OperaterPhone.set("")
					OperaterAddress.set("")
					#Clear Item Variables
					DBOperated.set("0")
					BBWOperated.set("0")
					SBWOperated.set("0")
					SPWOperated.set("0")
					#Clear Total Operation Menu Variables
					OperatedTotal.set("N0.00")
					OperaterBillNumber.set("")
					OperaterIssuedDateStamp.set("")
					self.OperaterWelcome_bill()
					#self.OperaterClearWelcome_bill()
					self.Operaterfetch_data()
					OperaterSearchedSumation.set("")	
					OperaterSearch.set("")
					OperaterSearch_Txt.set("")	
					FromOperaterReport.set("dd/mm/yyyy")
					ToOperaterReport.set("dd/mm/yyyy")
					OperaterName_txt.focus()
					OperaterTxtarea.config(state=DISABLED)
					AddOperater_btn['state']='normal'
					UpdateOperater_btn['state']='normal'
					#OperaterBill_table.selection_clear()
					OperaterBill_table.selection_set()
					#Set OperaterPriceType as DAY at default opening or clear
					OperaterPriceType_txt['state']='normal'
					OperaterPriceType.set("DAY")
				
				
				
				
				
				
				
				
				
				#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
				#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
				#New Function to Create new window for Package Unit
				def createPackageUnit(self):	
					
					#Assign 2 to variable RunningFunction
					RunningFunction=2
							
					global DBPackaged
					global BBWPackaged
					global SBWPackaged
					global SPWPackaged
					global PackagedTotal
					
					global PackagerName
					global PackagerPhone
					global PackagerAddress
					global PackagerBillNumber
					
					global PackagerIssuedDateStamp
					
					global PackagerSearch
					global PackagerSearch_Txt
					
					global PackagerSearchedSumation
					global PackagerTotalInventory
					
					global FromPackagerReport
					global ToPackagerReport
					
					global PackagerPriceType
					
					#Packager Details
					PackagerName=StringVar()
					PackagerPhone=StringVar()
					PackagerAddress=StringVar()
					PackagerBillNumber=StringVar()
					
					#Quantity Packaged
					DBPackaged=IntVar()
					BBWPackaged=IntVar()
					SBWPackaged=IntVar()
					SPWPackaged=IntVar()
					PackagedTotal=StringVar()
					
					#PackagerDate
					PackagerIssuedDateStamp=StringVar()
					
					#Summation
					PackagerSearchedSumation=IntVar()
					PackagerTotalInventory=IntVar()
					
					#Packager Search related
					PackagerSearch=StringVar()
					PackagerSearch_Txt=StringVar()
					
					FromPackagerReport=StringVar()
					ToPackagerReport=StringVar()
					
					#Packager Price Type
					PackagerPriceType=StringVar()
					
					PackageUnit = tk.Toplevel(root)
					PackageUnit.wm_iconbitmap('icon.ico')
					
					PackageUnit.state('zoomed')
					#Size of the new window
					width, height = PackageUnit.winfo_screenwidth(), PackageUnit.winfo_screenheight()
					PackageUnit.geometry('%dx%d+0+0' % (width,height))
					PackageList = tk.Label(PackageUnit, text = "Package Unit",bd=5,relief=GROOVE,font=("arial black",15,"bold"),bg="DarkGray",fg="DarkGreen")
					PackageList.pack(side=TOP,fill=X)
					PackageUnit.focus()
					
					#=======================Package detail frame
					Packager=LabelFrame(PackageUnit,bd=10,relief=GROOVE,text="Packager Details",font=("Arial",15,"bold"),fg="DarkRed",bg=bg_color)
					Packager.place(x=0,y=40,relwidth=1,height=80)
					
					#Label for Packager Name, same background, black text
					##DriverName_lbl=Label(Packager,text="Name",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=5,pady=2)
					#Packager Name
					##global PackagerName_txt
					##PackagerName_txt=Entry(Packager,width=29,textvariable=PackagerName,font="arial 13",bd=3,relief=SUNKEN)
					##PackagerName_txt.grid(row=0,column=1,pady=2,padx=2)
					##PackagerName_txt.focus()
					
					#Label for Packager Name, same background, black text
					global PackagerName_txt
					PackagerName_lbl=Label(Packager,text="Name",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=5,pady=2)	
					PackagerName_txt=ttk.Combobox(Packager,textvariable=PackagerName,width=28,font="arial 11 bold",state='readonly')
					#This will make the Combobox connect with the function to populate itself with the DB row data
					PackagerName_txt['values']= self.RegisteredPackager_input()
					PackagerName_txt.bind('<<ComboboxSelected>>', self.autoFullPackager)
					PackagerName_txt.grid(row=0,column=1,padx=2,pady=2)
					PackagerName_txt.focus()
					#PackagerName_txt['state']='normal'
					
					
					#Label for Packager Phone, same background, black text
					PackagerPhone_lbl=Label(Packager,text="Phone No.",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=8,pady=2)
					#Text field to Enter the Packager Phone, SUNKEN
					PackagerPhone_txt=Entry(Packager,width=18,textvariable=PackagerPhone,font="arial 13",bd=3,relief=SUNKEN,state='readonly')
					PackagerPhone_txt.grid(row=0,column=3,pady=2,padx=2)
					
					#Label for Packager Phone, same background, black text
					PackagerAddress_lbl=Label(Packager,text="Address",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=8,pady=2)
					#Text field to Enter the Packager Phone, SUNKEN
					PackagerAddress_txt=Entry(Packager,width=15,textvariable=PackagerAddress,font="arial 13",bd=3,relief=SUNKEN,state='readonly')
					PackagerAddress_txt.grid(row=0,column=5,pady=2,padx=2)
					
					#Label for Packager Phone, same background, black text
					PackagerBillNumber_lbl=Label(Packager,text="BillNo.",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=6,padx=8,pady=2)
					#Text field to Enter the Packager Phone, SUNKEN
					PackagerBillNumber_txt=Entry(Packager,width=18,textvariable=PackagerBillNumber,fg="DarkRed",font=("arial",12,"bold"),bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=7,pady=2,padx=2)
					
					#Label for Packager Phone, same background, black text
					PackagerIssuedDateStamp_lbl=Label(Packager,text="IssueDate",bg=bg_color,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=8,padx=8,pady=2)
					#Text field to Enter the Packager Phone, SUNKEN
					PackagerIssuedDateStamp_txt=Entry(Packager,width=26,textvariable=PackagerIssuedDateStamp,fg="DarkRed",font=("arial",11,"bold"),bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=9,pady=2,padx=2)
					
					
					#=======================Packager Quantity Frame
					PackagerQtyItemFrame=LabelFrame(PackageUnit,bd=10,relief=GROOVE,text="Packaged Quantity",font=("Arial",15,"bold"),fg="DarkRed",bg=bg_color)
					PackagerQtyItemFrame.place(x=5,y=105,width=350,height=200)

					#Driver Dispenser Bottle
					global Packagerdbwater_txt
					Packagerdbwater_lbl=Label(PackagerQtyItemFrame,text="Dispenser Bottle",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=5,sticky="w")
					Packagerdbwater_txt=Entry(PackagerQtyItemFrame,width=8,textvariable=DBPackaged,font=("arial",15,"bold"),bd=3,relief=SUNKEN)
					Packagerdbwater_txt.grid(row=0,column=1,padx=10,pady=5)
					Packagerdbwater_txt.focus()
					
					#Driver BIG Bottle water
					Packagerbbwater_lbl=Label(PackagerQtyItemFrame,text="BIG Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=5,sticky="w")
					Packagerbbwater_txt=Entry(PackagerQtyItemFrame,width=8,textvariable=BBWPackaged,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)
					
					#Driver Small Bottle water
					Packagersbwater_lbl=Label(PackagerQtyItemFrame,text="Small Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=5,sticky="w")
					Packagersbwater_txt=Entry(PackagerQtyItemFrame,width=8,textvariable=SBWPackaged,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)
					
					#Driver Sachet Pure water
					Packagerspwater_lbl=Label(PackagerQtyItemFrame,text="Sachet Pure Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=5,sticky="w")
					Packagerspwater_txt=Entry(PackagerQtyItemFrame,width=8,textvariable=SPWPackaged,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)
					
					
					#=======================Packager Total Holder
					PackageTotalFrame=LabelFrame(PackageUnit,bd=5,relief=SUNKEN,bg=bg_color)
					PackageTotalFrame.place(x=5,y=300,width=350,height=45)
					
					PacakagedTotal_lbl=Label(PackageTotalFrame,text="Packaged Total",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=8,pady=1,sticky="w")	
					PacakagedTotal_txt=Entry(PackageTotalFrame,width=12,fg="black",textvariable=PackagedTotal,font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=1,padx=2,pady=1,sticky="w")
					
					#=======================Packager Total/Add/Print, Update and Clear Button Holder
					PackagerButtonFrame1=LabelFrame(PackageUnit,bd=5,relief=SUNKEN,bg=bg_color)
					PackagerButtonFrame1.place(x=0,y=345,width=350,height=50)
					
					global AddPackager_btn
					#Button to Total/Add/Print Packager Record
					AddPackager_btn=Button(PackagerButtonFrame1,text="Total/Add",command=self.PackagerCompute_Add,bg=bg_color,fg="Green",bd=3,pady=5,width=12,font="ArialBold 10 bold")
					AddPackager_btn.grid(row=0,column=0,padx=3,pady=2)
					AddPackager_btn['state']='normal'
					
					global UpdatePackager_btn
					#Button to Update Packager Record
					UpdatePackager_btn=Button(PackagerButtonFrame1,text="Update",command=self.UpdatePackagerDB_data,bg=bg_color,fg="Blue",bd=3,pady=5,width=12,font="ArialBold 10 bold")
					UpdatePackager_btn.grid(row=0,column=1,padx=4,pady=2)
					UpdatePackager_btn['state']='disabled'
				
					#Button to Clear Screen
					ClearPackager_btn=Button(PackagerButtonFrame1,text="Clear",command=self.PackagerClear_data,bg=bg_color,fg="Red",bd=3,pady=5,width=12,font="ArialBold 10 bold").grid(row=0,column=2,padx=4,pady=2)
					
					
					#=======================Print, Search, Export and Delete Buttons
					PackagerButtonFrame2=LabelFrame(PackageUnit,bd=5,relief=SUNKEN,bg=bg_color)
					PackagerButtonFrame2.place(x=355,y=120,relwidth=1,height=50)
					
					#Packager Print Bill
					PrintPackager_btn=Button(PackagerButtonFrame2,text="Print Bill",command=self.PackagerPrint_bill,width=10,bd=3,bg=bg_color,fg="DarkRed",font="arial 12 bold").grid(row=0,column=3,padx=2,pady=2)
					
					global PackagerCombo_search
					#Packager Search DB
					#ComboBox for Packager Text area select kind of data to search
					PackagerCombo_search=ttk.Combobox(PackagerButtonFrame2,textvariable=PackagerSearch,width=14,font=("Arial",15,"normal"))
					#All Packager variables for search
					PackagerCombo_search['values']=("BillNo","Amount","PriceType","DateStamp","Name","Address","Phone","NewDateStamp","EnteredBy","PreviousTotal","UpdatedBy","UpdatedDate")
					#Position of Packager combo box
					PackagerCombo_search.grid(row=0,column=4,padx=4,pady=2)
					
					#Text Space to Type Data for Search
					#Addition of textvariable=self.search_txt
					PackagerTxt_search=Entry(PackagerButtonFrame2,textvariable=PackagerSearch_Txt,width=28,bg="LightGray",fg="DarkBlue",font=("Arial",15,"normal"),bd=5,relief=GROOVE)
					PackagerTxt_search.grid(row=0,column=5,pady=2,padx=4,sticky="w")
					
					#Button to Search PackagerDB
					#This button works with the Combo Search and Search text above
					#They must comply
					PackagerSearch_btn=Button(PackagerButtonFrame2,text="Search DB",command=self.PackagerSearch_data,width=13,bd=3,font="arial 12 bold").grid(row=0,column=6,padx=4,pady=2)
					
					#Button to Balance/Add/Print Packager Record
					#AddPackager_btn=Button(PackagerButtonFrame2,text="Balance",width=10,bd=3,bg=bg_color,fg="Green",font="ArialBold 12 bold").grid(row=0,column=7,padx=4,pady=2)
					#command=self.UpdatePackagerReturnedDamagedSoldDB_data
					
					global ExportPackager_btn
					#Button to Update Packager Return, Damage and Sold
					ExportPackager_btn=Button(PackagerButtonFrame2,text="Export-Excel",command=self.PackagerSaveCurrentTableItem,width=16,bd=3,bg=bg_color,fg="Blue",font="ArialBold 12 bold")
					ExportPackager_btn.grid(row=0,column=8,padx=4,pady=2)
					ExportPackager_btn['state']='disable'
					
					global DeletePackager_btn
					#Button to Delete entry from DATABASE
					DeletePackager_btn=Button(PackagerButtonFrame2,text="Delete",command=self.DeletePackagerData,width=10,bd=3,bg=bg_color,fg="Red",font="ArialBold 12 bold")
					DeletePackager_btn.grid(row=0,column=9,padx=4,pady=2)
					DeletePackager_btn['state']='disable'
					
					#=======================Packager Bill Frame
					PackagerBill=LabelFrame(PackageUnit,bd=10,relief=GROOVE)
					PackagerBill.place(x=5,y=395,width=345,height=380) 
					PackagerBill_title=Label(PackagerBill,text="Bills",font="arial 15 bold",bd=5,relief=GROOVE).pack(fill=X)
				
					scroll_y=Scrollbar(PackagerBill,orient=VERTICAL)
					global PackagerTxtarea
					PackagerTxtarea=Text(PackagerBill,yscrollcommand=scroll_y.set)
					scroll_y.pack(side=RIGHT,fill=Y)
					scroll_y.config(command=PackagerTxtarea.yview)
					PackagerTxtarea.pack(fill=BOTH,expand=1)
					
					#NEWLY ADDED to ensure multiplier prices for DAY and NIGHT differs
					global PackagerPriceType_txt
					PackagerBillx=LabelFrame(PackageUnit,bd=5,relief=GROOVE)
					PackagerBillx.place(x=13,y=402,width=104,height=40)
					#PackagerPriceType_lbl=Label(PackagerBillx,text="DUTY",bg=bg_color,fg="black",font=("times new roman",10,"bold")).grid(row=0,column=0,padx=5,pady=2)	
					PackagerPriceType_txt=ttk.Combobox(PackagerBillx,textvariable=PackagerPriceType,width=8,font="arial 11 bold",state='readonly')
					PackagerPriceType_txt['values']=("DAY","NIGHT")
					PackagerPriceType_txt.grid(row=0,column=0,padx=2,pady=2)
					PackagerPriceType_txt['state']="normal"
					
					#=======================Packager Table Side Frame
					PackagerTable_Frame=LabelFrame(PackageUnit,bd=10,relief=RIDGE,bg=bg_color)
					PackagerTable_Frame.place(x=350,y=170,width=1085,height=600)
					
					#=======================DISPLAY FOR ALL Packager BILL ENTRY
					scroll_x=Scrollbar(PackagerTable_Frame,orient=HORIZONTAL)
					scroll_y=Scrollbar(PackagerTable_Frame,orient=VERTICAL)
					#Format for the required column headings that will be displayed
					global PackagerBill_table
					PackagerBill_table=ttk.Treeview(PackagerTable_Frame,columns=("BillNo","Dispenser","BigBottle","SmallBottle","SachetWater","CostDispenser","CostBigBottle","CostSmallBottle","CostSachetWater","Amount","PriceType","DateStamp","Name","Address","Phone","EnteredBy","PreviousTotal","UpdatedBy","UpdatedDate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
					
					#Scroll bar direction and configuration
					scroll_x.pack(side=BOTTOM,fill=X)
					scroll_y.pack(side=RIGHT,fill=Y)
					scroll_x.config(command=PackagerBill_table.xview)
					scroll_y.config(command=PackagerBill_table.yview)		
					
					#Connecting each heading to a column of the existing fields
					PackagerBill_table.heading("BillNo",text="BillNo")
					PackagerBill_table.heading("Dispenser",text="Dispenser")
					PackagerBill_table.heading("BigBottle",text="BigBottle")
					PackagerBill_table.heading("SmallBottle",text="SmallBottle")
					PackagerBill_table.heading("SachetWater",text="SachetWater")
					
					PackagerBill_table.heading("CostDispenser",text="CostDispenser")
					PackagerBill_table.heading("CostBigBottle",text="CostBigBottle")
					PackagerBill_table.heading("CostSmallBottle",text="CostSmallBottle")
					PackagerBill_table.heading("CostSachetWater",text="CostSachetWater")
					
					PackagerBill_table.heading("Amount",text="Amount")
					PackagerBill_table.heading("PriceType",text="PriceType")
					PackagerBill_table.heading("DateStamp",text="DateStamp")
					PackagerBill_table.heading("Name",text="Name")
					PackagerBill_table.heading("Address",text="Address")
					PackagerBill_table.heading("Phone",text="Phone")
					PackagerBill_table.heading("EnteredBy",text="EnteredBy")
					PackagerBill_table.heading("PreviousTotal",text="PreviousTotal")
					PackagerBill_table.heading("UpdatedBy",text="UpdatedBy")
					PackagerBill_table.heading("UpdatedDate",text="UpdatedDate")
					
					#Enable heading of tables to show
					PackagerBill_table['show']='headings'
					
					#Set column width for each field in the table
					PackagerBill_table.column("BillNo",width=120)
					PackagerBill_table.column("Dispenser", anchor="center", width=80)
					PackagerBill_table.column("BigBottle", anchor="center", width=80)
					PackagerBill_table.column("SmallBottle", anchor="center", width=80)
					PackagerBill_table.column("SachetWater", anchor="center", width=80)
					#Cost
					PackagerBill_table.column("CostDispenser", anchor="center", width=100)
					PackagerBill_table.column("CostBigBottle", anchor="center", width=100)
					PackagerBill_table.column("CostSmallBottle", anchor="center", width=100)
					PackagerBill_table.column("CostSachetWater", anchor="center", width=100)
					
					PackagerBill_table.column("Amount", anchor="e", width=100)
					PackagerBill_table.column("PriceType", anchor="e", width=100)
					PackagerBill_table.column("DateStamp",width=150)
					PackagerBill_table.column("Name",width=120)
					PackagerBill_table.column("Address",width=120)
					PackagerBill_table.column("Phone",width=120)
					PackagerBill_table.column("EnteredBy", anchor="center", width=120)
					PackagerBill_table.column("PreviousTotal", anchor="center", width=120)
					PackagerBill_table.column("UpdatedBy", anchor="center", width=120)
					PackagerBill_table.column("UpdatedDate", anchor="center", width=120)

					#To expand the table  
					PackagerBill_table.pack(fill=BOTH,expand=1)
					#Enable selection of items in the Bill_table
					PackagerBill_table.bind("<ButtonRelease-1>",self.PackagerBillget_cursor)
					
					
					#=======================Packager Bottom Frame
					PackagerBottomFrame=LabelFrame(PackageUnit,bd=5,relief=GROOVE,bg=bg_color)
					PackagerBottomFrame.place(x=0,y=780,relwidth=1,height=80)
					
					PackagerAmountSelected_lbl=Label(PackagerBottomFrame,text="Sub-Total",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=10,pady=1,sticky="w")	
					PackagerAmountSelected_txt=Entry(PackagerBottomFrame,width=18,textvariable=PackagerSearchedSumation,fg="red",font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=3,padx=10,pady=1)
					
					PackagerTotalInventory_lbl=Label(PackagerBottomFrame,text="TOTAL",bg=bg_color,fg="DarkRed",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=10,pady=1,sticky="w")	
					PackagerTotalInventory_txt=Entry(PackagerBottomFrame,width=19,textvariable=PackagerTotalInventory,fg="red",font="arial 15 bold",bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=5,padx=10,pady=1)
					
					global GenerateReportPackagerFrom_txt
					GenerateReportPackagerFrom_lbl=Label(PackagerBottomFrame,text="From:",bg=bg_color,fg="Black",font=("times new roman",12,"bold")).grid(row=0,column=6,padx=17,pady=1,sticky="w")	
					GenerateReportPackagerFrom_txt=Entry(PackagerBottomFrame,width=10,textvariable=FromPackagerReport,fg="Black",font="arial 12 bold",bd=3,relief=SUNKEN)
					GenerateReportPackagerFrom_txt.grid(row=0,column=7,padx=2,pady=1)
					
					global GenerateReportDriverTo_txt
					GenerateReportPackagerTo_lbl=Label(PackagerBottomFrame,text="To:::",bg=bg_color,fg="Black",font=("times new roman",12,"bold")).grid(row=0,column=8,padx=2,pady=1,sticky="w")	
					GenerateReportPackagerTo_txt=Entry(PackagerBottomFrame,width=10,textvariable=ToPackagerReport,fg="Black",font="arial 12 bold",bd=3,relief=SUNKEN)
					GenerateReportPackagerTo_txt.grid(row=0,column=9,padx=2,pady=1)	
					
					global GenerateReportPackager_btn
					GenerateReportPackager_btn=Button(PackagerBottomFrame,text="Generate Report",width=15,bd=3,bg=bg_color,fg="Green",command=self.GenerateReport_Packager,font="ArialBold 10 bold")
					GenerateReportPackager_btn.grid(row=0,column=10,padx=4,pady=2)
					GenerateReportPackager_btn['state']='disable'
					
					#Automatically Clear Screen
					self.PackagerClear_data()
					
					#Automatically focus cursor in the search txt once there is a selection of Search_by
					self.PackagerAutoFocusSearch()
					
					global PackagerDirectory
					PackagerDirectory="C:/PackagerBills/"
					
					#Function to Fetch all data from Driver Table
					self.PackagerFetchDB_data()
					
					#Welcome Screen Bill
					self.PackagerWelcome_bill()
					
					self.packageruser_type()
					
					PackageList.pack()
					#Lovely Code that will ensure Child Window remains active and Root remains inactive until Child is Closed 
					#After Clicking on Packager Unit the new Window to Packager Unit must be fully used and closed before using main interface
					PackageUnit.transient(root)
					PackageUnit.grab_set()
					root.wait_window(PackageUnit)
				
				def DisableAddTotalUpdateBalancePackager(self):
					#Automatically disable the Add/Total and Update Buttons
					if CurrentCategory == 'Super-Admin':
						AddPackager_btn['state']='disabled'
						UpdatePackager_btn['state']='normal'
					else:
						AddPackager_btn['state']='disabled'
						#UpdatePackager_btn['state']='disabled'
					if CurrentCategory == 'Super-Admin':
						ExportPackager_btn['state']='normal'
						DeletePackager_btn['state']='normal'
						GenerateReportPackager_btn['state']='normal'
					
				def packageruser_type(self):
					if CurrentCategory == 'Super-Admin':
						DeletePackager_btn['state']='normal'
				
				
				#Generate REPORT Normal Sales
				def GenerateReport_Packager(self):
					try:
						#If one or both of the criteria is/are empty
						if FromPackagerReport.get()=="" or ToPackagerReport.get()=="":
							messagebox.showerror("Report Error","Date From: and Date To: \nAre compulsory")
							
						elif FromPackagerReport.get()=="dd/mm/yyyy" or len((str(FromPackagerReport.get()).split('/')[2]))!=4 or int((str(FromPackagerReport.get()).split('/')[1]))>12:
							messagebox.showerror("Data Error","Date FROM must be in dd/mm/yyyy format")
							GenerateReportPackagerFrom_txt.focus()
						
						elif ToPackagerReport.get()=="dd/mm/yyyy" or len((str(ToPackagerReport.get()).split('/')[2]))!=4 or int((str(ToPackagerReport.get()).split('/')[1]))>12:
							messagebox.showerror("Data Error","Date TO must be in dd/mm/yyyy format")
							GenerateReportPackagerTo_txt.focus()
							
						else:
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("select * from packagerbills where DateStamp BETWEEN '"+str(FromPackagerReport.get())+" 00:00:00.000000' AND '"+str(ToPackagerReport.get())+" 99:99:99.999999'")
							PackagerBill_table.delete(*PackagerBill_table.get_children())
							rows=cur.fetchall()
							if len(rows)<1:
								con.close()
								messagebox.showinfo('No Data!',"No record was captured within date range")
							elif len(rows)>=1:
								PackagerBill_table.delete(*PackagerBill_table.get_children())
								for row in rows:
									PackagerBill_table.insert('',END,values=row)
								con.commit()
								con.close()
								#Auto focus the last record from the records returned after search
								child_id = PackagerBill_table.get_children()[-1]
								cursor_row = PackagerBill_table.focus(child_id)
								PackagerBill_table.selection_set(child_id)
								self.PackagerBillget_cursor(cursor_row)
								
								#Calling a function to do Sub-Total Sum all items displayed in table after every search performed
								self.PackagerSearchedSum()
								
								#SAVE but ask use first
								savereport=messagebox.askyesno("Driver Report","Report Successfully Retrieved \nDo you want to Save this Report?")
								if savereport>0:
									self.PackagerSaveCurrentTableItem()
								else:
									pass
							
					except ValueError:
						messagebox.showerror("Data Report Error","Invalid data entry")

				
				#Automatically Fill Packager Details after FullName Selection
				def autoFullPackager(self, event):
					#Connection to the Database
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					
					#Getting the exact MobileNo of the Fullname
					cur.execute("select MobileNo FROM register WHERE FullName = '"+PackagerName.get()+"'")
					row=cur.fetchall()
					PackagerPhone.set(row[0])
					
					#Getting the exact VehicleNo of the Fullname
					cur.execute("select Address FROM register WHERE FullName = '"+PackagerName.get()+"'")
					row=cur.fetchall()
					for rows in row:
						#print(rows[0])
						PackagerAddress.set(str(rows[0]))
					
					Packagerdbwater_txt.focus()
				
				#Function to connect to DB and populate Data in a Column as the Drop Down Values another Combobox
				def RegisteredPackager_input(self):
					#Connection to the Database
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					#cur.execute("select * from register WHERE UserID = '" + ery2.get() + "' AND Password = '" + ery3.get() + "'")
					cur.execute("select FullName FROM register WHERE Category = 'Packager'")
					data=[]
					
					for row in cur.fetchall():
						data.append(row[0])
					return data
				
				#Print Bill for Packager
				def PackagerPrint_bill(self):
					##Check if the Bill No. is blank string then it Prints using the Bill No. in the text area
					if PackagerBillNumber.get()!="":
						self.PackagerSaveBill()
						#Opens the main file using the Bill No.
						fin = open("C:/PackagerBills/"+str(PackagerBillNumber.get())+".txt","rt")
						#Create another temporary file mainly for printing format
						fout = open("C:/PackagerBills/printout.txt","wt")
						#Condition statement for each line in the file main fin
						for line in fin:
							#If the line startswith Items then just print it like that
							if line.startswith(" Items"):
								fout.write(line)
							#Else try to replace double tabs \t\t on any other lines with single tab \t
							else:
								#print(line.rstrip().replace("\t\t","\t"))
								fout.write(line.replace("\t\t","\t"))
						#Close the files
						fin.close()
						fout.close()
						os.startfile("C:/PackagerBills/printout.txt","print")
					##Else it will automatically PRINT using the Bill No. in the Search
					else:
						messagebox.showerror("Print Error","Kindly select a Bill to print")	
				
				#Function to Save Packager Bill as Text File
				#I have to global PackagerDirectory as C:/PackagerBills at the header of Packager Section
				def PackagerSaveBill(self):
					#op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
					#if op>0:
					packagerbill_data=PackagerTxtarea.get('1.0',END)
					if not os.path.exists(PackagerDirectory):
						os.makedirs(PackagerDirectory)
					f1=open("C:/PackagerBills/"+str(PackagerBillNumber.get())+".txt","w")
					f1.write(packagerbill_data)
					f1.close()
				
				def PackagerSaveCurrentTableItem(self):
					#Empty list for each column in the treeview
					column1_list = []
					column2_list = []
					column3_list = []
					column4_list = []
					column5_list = []
					column6_list = []
					column7_list = []
					column8_list = []
					column9_list = []
					column10_list = []
					column11_list = []
					column12_list = []
					column13_list = []
					column14_list = []
					column15_list = []
					column16_list = []
					column17_list = []
					column18_list = []
					column19_list = []
					
					
					#running through the lines of the treeview in a "for" function, append to each column list the value of the column in each line
					for child in PackagerBill_table.get_children():
						column1_list.append(PackagerBill_table.item(child)["values"][0]) 
						column2_list.append(PackagerBill_table.item(child)["values"][1]) 
						column3_list.append(PackagerBill_table.item(child)["values"][2]) 
						column4_list.append(PackagerBill_table.item(child)["values"][3]) 
						column5_list.append(PackagerBill_table.item(child)["values"][4]) 
						column6_list.append(PackagerBill_table.item(child)["values"][5]) 
						column7_list.append(PackagerBill_table.item(child)["values"][6]) 
						column8_list.append(PackagerBill_table.item(child)["values"][7]) 
						column9_list.append(PackagerBill_table.item(child)["values"][8]) 
						column10_list.append(PackagerBill_table.item(child)["values"][9]) 
						column11_list.append(PackagerBill_table.item(child)["values"][10]) 
						column12_list.append(PackagerBill_table.item(child)["values"][11]) 
						column13_list.append(PackagerBill_table.item(child)["values"][12]) 
						column14_list.append(PackagerBill_table.item(child)["values"][13])
						column15_list.append(PackagerBill_table.item(child)["values"][14])
						column16_list.append(PackagerBill_table.item(child)["values"][15])
						column17_list.append(PackagerBill_table.item(child)["values"][16])
						column18_list.append(PackagerBill_table.item(child)["values"][17])
						column19_list.append(PackagerBill_table.item(child)["values"][18])
					
					#create a dictionary from all the lists, using the header as the key and lists are the values as a list
					Packagerfull_treeview_data_dict = {'BillNo': column1_list, 'Dispenser': column2_list, 'BigBottle': column3_list, 'SmallBottle': column4_list, 'SachetWater': column5_list, 'CostDispenser': column6_list, 'CostBigBottle': column7_list,
												'CostSmallBottle': column8_list, 'CostSachetWater': column9_list, 'Amount': column10_list, 'PriceType': column11_list, 'DateStamp': column12_list, 'Name': column13_list, 'Address': column14_list,
												'Phone': column15_list, 'EnteredBy': column16_list, 'PreviousTotal': column17_list, 'UpdatedBy': column18_list, 'UpdatedDate': column19_list}
												
					#Create a dataframe from the dictionary
					Packagertreeview_df = pd.DataFrame.from_dict(Packagerfull_treeview_data_dict)
					
					#print(Packagertreeview_df)
					if len(packagerdata) < 1:
						messagebox.showerror("No Data","No data available to export")
						return False
					try:
						filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Save to Excel',defaultextension='.xlsx',filetypes=[("Excel file", "*.xlsx")])
						Packagertreeview_df.to_excel(filename, engine='xlsxwriter',index= False)
						messagebox.showinfo("Data Exported","Your data has been exported to "+os.path.basename(filename)+" successfully.")
					except:
						pass
				
				
				
				def PackagerCompute_Add(self):
					self.PackagerAdd_bills()
					#self.UpdatePackagerDB_data()
					self.PackagerAddBill_area()
				
				#Function to display text in the Bill Area with Welcome Message constant displaying
				def PackagerWelcome_bill(self):
					PackagerTxtarea.config(state=NORMAL)
					PackagerTxtarea.delete('1.0',END)
					#The use of \t for tab to indent location of he welcome message
					PackagerTxtarea.insert(END,"    Welcome to Kwambal Table Water")
					#Capture Company Address
					PackagerTxtarea.insert(END,f"\n    Plot 9 No.64 Opp. Trailer Park\n Pompomari Bypass M/guri, Borno State")
					PackagerTxtarea.insert(END,f"\n \t{self.Time_get()}")
					if PackagerPriceType_txt.get()==('DAY'):
						PackagerTxtarea.insert(END,f"\n {PackagerPriceType.get()} Bill No.    : {PackagerBillNumber.get()}")
					else:
						PackagerTxtarea.insert(END,f"\n {PackagerPriceType.get()} Bill No.  : {PackagerBillNumber.get()}")
					PackagerTxtarea.insert(END,f"\n Packager's Name : {PackagerName.get()}")
					PackagerTxtarea.insert(END,f"\n Phone Number    : {PackagerPhone.get()}")
					PackagerTxtarea.insert(END,f"\n Address         : {PackagerAddress.get()}")
					PackagerTxtarea.insert(END,f"\n ---------- PACKAGING COST ---------")
					PackagerTxtarea.insert(END,f"\n ===================================")
					PackagerTxtarea.insert(END,f"\n Items\t\tQTY\tPrice")
					PackagerTxtarea.insert(END,f"\n ===================================")
					PackagerTxtarea.config(state=DISABLED)
				
				
				#Updating the Text_Bill also requires Updating Generate Bill
				#But we do not need new features just needed the Qty and the amount
				def PackagerAddBill_area(self):
					PackagerTxtarea.config(state=NORMAL)
					self.PackagerPriceMultiplier()
					self.PackagerGivenTotal()
					#Enabling the txtarea to allow modification
					#self.Welcome_bill()
					#Condition if Qty of Bottle Dispenser is not NIL
					#Enable display of item name, qty and subtotal cost of any item whose Qty order is above 0
					self.UpdatePackagerWelcome_bill()
					if DBPackaged.get()!=0:
						PackagerTxtarea.insert(END,f"\n 18.5 Litre\t\t{DBPackaged.get()}\t{(str('{:0,.2f}'.format(float(DBPackaged.get()*float(PackageDBP)))))}")
					#Condition if Qty of Big Bottle Water is not NIL
					if BBWPackaged.get()!=0:
						PackagerTxtarea.insert(END,f"\n 75cl Bottle \t\t{BBWPackaged.get()}\t{(str('{:0,.2f}'.format(float(BBWPackaged.get()*float(PackageBBWP)))))}")
					#Condition if Qty of Small Bottle Water is not NIL
					if SBWPackaged.get()!=0:
						PackagerTxtarea.insert(END,f"\n 55cl Bottle \t\t{SBWPackaged.get()}\t{(str('{:0,.2f}'.format(float(SBWPackaged.get()*float(PackageSBWP)))))}")
					#Condition if Qty of Sachet Pure Water is not NIL
					if SPWPackaged.get()!=0:
						PackagerTxtarea.insert(END,f"\n 55cl Sachet \t\t{SPWPackaged.get()}\t{(str('{:0,.2f}'.format(float(SPWPackaged.get()*float(PackageSPWP)))))}")	
					PackagerTxtarea.insert(END,f"\n -----------------------------------")
					#Total Bill
					PackagerTxtarea.insert(END,f"\n TOTAL BILL :\t\t\t{PackagedTotal.get()}")
					#PackagerTxtarea.insert(END,f"\n -----------------------------------")
					PackagerTxtarea.insert(END,f"\n ----- Be Honest, Brave & True -----")
					PackagerTxtarea.insert(END,f"\n -----------------------------------")
					PackagerTxtarea.config(state=DISABLED)
					
					#After generating and saving bill, there is need to disable the txtarea from been modified
				
				#Function to display text in the Bill Area
				#Welcome Message constant displaying
				def UpdatePackagerWelcome_bill(self):
					PackagerTxtarea.config(state=NORMAL)
					PackagerTxtarea.delete('1.0',END)
					#The use of \t for tab to indent location of he welcome message
					PackagerTxtarea.insert(END,"    Welcome to Kwambal Table Water")
					#Capture Company Address
					PackagerTxtarea.insert(END,f"\n    Plot 9 No.64 Opp. Trailer Park\n Pompomari Bypass M/guri, Borno State")
					PackagerTxtarea.insert(END,f"\n \t{PackagerIssuedDateStamp.get()}")
					if PackagerPriceType.get()==('DAY'):
						PackagerTxtarea.insert(END,f"\n {PackagerPriceType.get()} Bill No.    : {PackagerBillNumber.get()}")
					else:
						PackagerTxtarea.insert(END,f"\n {PackagerPriceType.get()} Bill No.  : {PackagerBillNumber.get()}")
					PackagerTxtarea.insert(END,f"\n Packager's Name : {PackagerName.get()}")
					PackagerTxtarea.insert(END,f"\n Phone Number    : {PackagerPhone.get()}")
					PackagerTxtarea.insert(END,f"\n Address         : {PackagerAddress.get()}")
					PackagerTxtarea.insert(END,f"\n ---------- PACKAGING COST ---------")
					PackagerTxtarea.insert(END,f"\n ===================================")
					PackagerTxtarea.insert(END,f"\n Items\t\tQTY\tPrice")
					PackagerTxtarea.insert(END,f"\n ===================================")
				
				#NEW Function to fetch data
				def Packagerfetch_data(self):
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					cur.execute("select * from packagerbills order by DateStamp DESC")		
					rows=cur.fetchall()
					
					##NEWLY
					global packagerdata
					packagerdata=rows
					
					if len(rows)!=0:
						PackagerBill_table.delete(*PackagerBill_table.get_children())
						for row in rows:
							PackagerBill_table.insert('',END,values=row)
						con.commit()
					con.close()
				
				#Summation of Searched Amount in Packager Record
				def PackagerSearchedSum(self):
					#Variable Stubtotal is used as accumulator set at 0.00 float
					Stubtotal = 0.00
					#For Every child of the table
					for child in PackagerBill_table.get_children():
						#Accumulate the sum of each item displayed
						Stubtotal += float(PackagerBill_table.item(child,'values')[9])
					#Transferring the sum above into the Sub-total text holder
					PackagerSearchedSumation.set("N"+str("{:0,.2f}".format(Stubtotal)))

				def PackagerAutoFocusSearch(self):
					if PackagerSearch.get()!="":
						PackagerTxt_search.focus()
				
				#This function will search using the search_by and search_txt to populate the data from DB to Table
				def PackagerSearch_data(self):
					##try:
					#If one or both of the criteria is/are empty
					if PackagerSearch.get()=="" or PackagerSearch_Txt.get()=="":
						messagebox.showerror("Search Error","Select Search by and \nType correct keyword")
					else:
						con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
						cur=con.cursor()
						if cur.execute("select * from packagerbills where "+str(PackagerSearch.get())+" LIKE '%"+str(PackagerSearch_Txt.get())+"%'"):
							rows=cur.fetchall()
							if len(rows)!=0:
								PackagerBill_table.delete(*PackagerBill_table.get_children())
								for row in rows:
									PackagerBill_table.insert('',END,values=row)
								con.commit()
							con.close()
							#Auto focus the last record from the records returned after search
							child_id = PackagerBill_table.get_children()[-1]
							cursor_row = PackagerBill_table.focus(child_id)
							PackagerBill_table.selection_set(child_id)
							self.PackagerBillget_cursor(cursor_row)
							
							#Calling a function to do Sub-Total Sum all items displayed in table after every search performed
							self.PackagerSearchedSum()
							#NEWLY
							#self.DisableGenBill()
						else:
							messagebox.showerror("Data Search Error","You have made an invalid data search\n"+PackagerSearch_Txt.get()+" does not exist.")
							#Then automatically show all records from DB
							self.PackagerFetchDB_data()
							#clear screen
							self.PackagerClear_data()
				
				
				#Delete Packager record from DB 	
				def DeletePackagerData(self):
					ask=messagebox.askyesno("Deleting Record","Are you sure to proceed with delete! \nYou cannot undo this action")
					if ask==True:
						con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
						cur=con.cursor()
						cur.execute("delete from packagerbills where BillNo=%s",PackagerBillNumber.get())
						con.commit()
						con.close()
						#Clear Screen
						self.PackagerClear_data()
						#Function of fetch_data is called here
						self.PackagerFetchDB_data()	
				
				
				#Update Packager Given Records
				def UpdatePackagerDB_data(self):
					if PackagerBillNumber.get()=="" or PackagedTotal.get()=="":
						messagebox.showerror("Update Error","Select record from table\n and Insert valid data")
					else:
						self.PackagerGivenTotal()
						PackagerTotalPayable=PackagedTotal.get().replace("N","").replace(",","")
						ask=messagebox.askyesno("Update Record","Are you sure to proceed with update!")
						if ask==True:
							self.mynice_date()
							updatedate=today_date
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("update packagerbills set Dispenser=%s,BigBottle=%s,SmallBottle=%s,SachetWater=%s,CostDispenser=%s,CostBigBottle=%s,CostSmallBottle=%s,CostSachetWater=%s,Amount=%s,PriceType=%s,DateStamp=%s,Name=%s,Address=%s,Phone=%s,PreviousTotal=%s,UpdatedBy=%s,UpdatedDate=%s where BillNo=%s",(
																																																											DBPackaged.get(),
																																																											BBWPackaged.get(),
																																																											SBWPackaged.get(),
																																																											SPWPackaged.get(),
																																																											PackageDBP,
																																																											PackageBBWP,
																																																											PackageSBWP,
																																																											PackageSPWP,
																																																											PackagerTotalPayable,
																																																											PackagerPriceType.get(),
																																																											PackagerIssuedDateStamp.get(),
																																																											PackagerName.get(),
																																																											PackagerAddress.get(),
																																																											PackagerPhone.get(),
																																																											PreviousPackagerAmount,
																																																											v,
																																																											updatedate,
																																																											PackagerBillNumber.get()
																																																											))
							con.commit()

							#NEWLY To auto focus the selection Balanced is performed on any selected Record
							#Using variable xx and yy to get the current fucos and index of the focus iid
							#This is done before the fetching of Database from DB to the TreeView
							xx=PackagerBill_table.focus()
							yy=PackagerBill_table.index(xx)
							#print(yy)				
							
							#Function of fetch_data is called here
							self.PackagerFetchDB_data()
				
							#NEWLY To auto focus the selection Balanced selected Record
							child_id = PackagerBill_table.get_children()[yy]
							cursor_row=PackagerBill_table.focus(child_id)
							PackagerBill_table.selection_set(child_id)
							
							#NEWLY ADDED
							#Display current values in the Bill Text area depending
							self.PackagerAddBill_area()			
							
							#After fetching the data then save the text file too
							#Save Packager Bill to Text
							self.PackagerSaveBill()
							
							#Disable Update Button
							UpdatePackager_btn['state']='disabled'
						
							con.close()
				

			
				def PackagerBillget_cursor(self,ev):
					try:
						cursor_row=PackagerBill_table.focus()
						contents=PackagerBill_table.item(cursor_row)
						row=contents['values']
						PackagerBillNumber.set(row[0])
						DBPackaged.set(row[1])
						BBWPackaged.set(row[2])
						SBWPackaged.set(row[3])
						SPWPackaged.set(row[4])
						PackagedTotal.set("N"+str("{:0,.2f}".format(float(row[9]))))
						PackagerPriceType.set(row[10])
						PackagerIssuedDateStamp.set(row[11])
						PackagerName.set(row[12])
						PackagerAddress.set(row[13])
						PackagerPhone.set(row[14])
						
						global PreviousPackagerAmount
						PreviousPackagerAmount=(row[9])
						
						#This code disable Update Record Button once it has been previously Updated 1ce
						if CurrentCategory == 'Super-Admin':
							AddPackager_btn['state']='disabled'
							UpdatePackager_btn['state']='normal'
							PackagerPriceType_txt['state']='normal'
						elif CurrentCategory == 'Admin':
							if (row[16]) != "":
								AddPackager_btn['state']='disabled'
								UpdatePackager_btn['state']='disabled'
								PackagerPriceType_txt['state']='disabled'
							else:
								UpdatePackager_btn['state']='normal'
								PackagerPriceType_txt['state']='normal'
						
						
						self.PackagerAddBill_area()
						
						self.DisableAddTotalUpdateBalancePackager()

					except:
						pass
				
				def PackagerAdd_bills(self):
					#try:
					ask=messagebox.askyesno("Add Packager Record","Do you really want to ADD this record?")
					if ask==True:
						#if self.TotalPayable.get()=="" and self.BillNo.get()=="" and self.CurrentTime.get()=="":
						#Newly added line appending the microsecond to BillNo for uniqueness
						
						#New Bill Code Starting With YYMMDD
						yy=str(datetime.now()).split(' ')[0]
						yy=str((yy[2:]).replace('-',''))
						#print(yy)
						
						x=str(datetime.now()).split('.')[1]+str("P")
						randbillno=random.randint(10000,99999)
						PackagerBillNumber.set(yy+str(randbillno)+x)
						
						self.mynice_date()
						#Capture the Date Issued
						##y=str(datetime.now())
						PackagerIssuedDateStamp.set(today_date)
						
						#Call Functions to perform Total Given by acquiring price multiplier DBPrice, BBWPrice, SBWPrice and SPWPrice
						self.PackagerGivenTotal()
						#self.PriceMultiplier()
					
						#Remove Naira sign and comma from all TOTALs
						TotalPayable=PackagedTotal.get().replace("N","").replace(",","")			
			
						#TotalPayable=float(TotalPayable)
						#print(TotalPayable)
						if PackagerName.get()=="":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nPackager Name is mandatory")
							self.PackagerClear_data()
						elif TotalPayable=="" or TotalPayable=="0.00":
							messagebox.showerror("Add Data Error","Kindly make valid entry\nBillNo. and TotalBill are mandatory")
							self.PackagerClear_data()
						else:
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("insert into packagerbills values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PackagerBillNumber.get(),
																														DBPackaged.get(),
																														BBWPackaged.get(),
																														SBWPackaged.get(),
																														SPWPackaged.get(),
																														PackageDBP,
																														PackageBBWP,
																														PackageSBWP,
																														PackageSPWP,
																														TotalPayable,
																														PackagerPriceType.get(),
																														PackagerIssuedDateStamp.get(),
																														PackagerName.get(),
																														PackagerAddress.get(),
																														PackagerPhone.get(),
																														v,
																														"",
																														"",
																														""
																														))

							#Function of fetch_data is called here	
							con.commit()
							
							#NEWEST
							self.PackagerFetchDB_data()
							
							con.close()
							
							#Packager Bill Text Area
							self.PackagerAddBill_area()
							
							#Save Packager Bill to Text
							self.PackagerSaveBill()
							
							#NEWEST Auto Highlight the record that was added in the Packager Table TreeView
							#Auto focus the first record from the records returned after New Addition
							child_id = PackagerBill_table.get_children()[0]
							cursor_row=PackagerBill_table.focus(child_id)
							PackagerBill_table.selection_set(child_id)
							self.PackagerBillget_cursor(cursor_row)
							
							#Message box to indicate successfully added
							messagebox.showinfo('Successfully added!',"The record has been captured")
					else:
						pass
				
				#Total of all items in general given to all drivers to display below screen
				def PackagerDBTOTAL(self):
					#Using a try and catch error incase when the Database is wiped
					#Opening the app will automatically want to Calculate all Total Inventory
					try:
						#Amount=float(Amount.repalce("N","").replace(",",""))
						con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
						cur=con.cursor()
						cur.execute("SELECT sum(Amount) AS totalsum FROM packagerbills")
						result=cur.fetchall()
						for i in result:
							#print(i[0])
							PackagerTotalInventory.set("N"+str("{:0,.2f}".format(i[0])))
						con.commit()
					except TypeError:
						pass
				
				#NEW Function to fetch Price data
				def PackagerFetchDB_data(self):
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					#Sorting the data fetched to display in descending order of DateStamp
					cur.execute("select * from packagerbills order by DateStamp DESC")
					rows=cur.fetchall()
					if len(rows)!=0:
						PackagerBill_table.delete(*PackagerBill_table.get_children())
						for row in rows:
							PackagerBill_table.insert('',END,values=row)
						con.commit()
					self.PackagerDBTOTAL()
					con.close()
				
				
				
				
				
				#PACKAGER FUNCTIONS COMPUTE GIVEN TOTALS
				def PackagerGivenTotal(self):
					try:
						#Run function to Recapture the Current Price data from the DB as Variables and use as Multiplier
						self.PackagerPriceMultiplier()
						
						#This will automatically sum values in Currency of 2 decimal places		
						#Added a N for Naira sign, must be: self.TotalPayable.get().replace("N","").replace(",","") when calculating
						#GIVEN TOTAL
						PackagedTotal.set("N"+str("{:0,.2f}".format(
															float((str("{:0,.2f}".format(float(DBPackaged.get()*float(PackageDBP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(BBWPackaged.get()*float(PackageBBWP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(SBWPackaged.get()*float(PackageSBWP))))).replace(",",""))+
															float((str("{:0,.2f}".format(float(SPWPackaged.get()*float(PackageSPWP))))).replace(",",""))
															)))
						#self.DriverWelcome_bill()
							
					except TclError:
						#Display this message
						messagebox.showerror("Data Error","You have made an invalid \ndata entry")
				
				
				
				def PackagerClear_data(self):
					##PackagerTxtarea.config(state=NORMAL)
					#Clear Packager Data
					PackagerName.set("")
					PackagerPhone.set("")
					PackagerAddress.set("")
					#Clear Item Variables
					DBPackaged.set("0")
					BBWPackaged.set("0")
					SBWPackaged.set("0")
					SPWPackaged.set("0")
					#Clear Total Operation Menu Variables
					PackagedTotal.set("N0.00")
					PackagerBillNumber.set("")
					PackagerIssuedDateStamp.set("")
					self.PackagerWelcome_bill()
					#self.PackagerClearWelcome_bill()
					self.Packagerfetch_data()
					PackagerSearchedSumation.set("")	
					PackagerSearch.set("")
					PackagerSearch_Txt.set("")	
					FromPackagerReport.set("dd/mm/yyyy")
					ToPackagerReport.set("dd/mm/yyyy")
					PackagerName_txt.focus()
					PackagerTxtarea.config(state=DISABLED)
					AddPackager_btn['state']='normal'
					UpdatePackager_btn['state']='normal'
					#PackagerBill_table.selection_clear()
					PackagerBill_table.selection_set()
					#Set PackagerPriceType as DAY at default opening or clear
					PackagerPriceType_txt['state']='normal'
					PackagerPriceType.set("DAY")
					
	
				#LATEST Function to crate new window where current price can be Updated
				def createNewWindow(self):
					global PriceType
					global DBPrice
					global BBWPrice
					global SBWPrice
					global SPWPrice
					global PriceDate
					PriceType=StringVar()
					DBPrice=IntVar()
					BBWPrice=IntVar()
					SBWPrice=IntVar()
					SPWPrice=IntVar()
					PriceDate=StringVar()
					
					newWindow = tk.Toplevel(root)
					newWindow.focus()
					PriceList = tk.Label(newWindow, text = "Update Unit Price",bd=5,relief=GROOVE,font=("arial black",15,"bold"),bg="DarkGray",fg="DarkGreen")
					PriceList.pack(side=TOP,fill=X)
					#UpdateUnitPrice_btn = ttk.Button(newWindow, text = "New Window Button")
					#Size of the new window
					newWindow.geometry("750x320+350+200")
					
					#Frame for PriceDetails
					Frame0=LabelFrame(newWindow,bd=5,relief=GROOVE,text="Price Details",font=("Arial",10,"bold"),fg="DarkRed",bg=bg_color)
					Frame0.place(x=0,y=40,width=750,height=85)
					
					PriceType_lbl=Label(Frame0,text="Type",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=5,pady=5,sticky="w")
					PriceType_txt=Entry(Frame0,width=25,textvariable=PriceType,font=("arial",15,"bold"),bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=1,padx=3,pady=3)
					
					PriceDate_lbl=Label(Frame0,text="Date",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=2,padx=5,pady=5,sticky="w")
					PriceDate_txt=Entry(Frame0,width=25,textvariable=PriceDate,font=("arial",15,"bold"),bd=3,relief=SUNKEN,state='readonly').grid(row=0,column=3,padx=3,pady=3)
					
					#Frame for the Grocery Items Prices
					Frame1=LabelFrame(newWindow,bd=5,relief=GROOVE,text="Grocery Items Prices",font=("Arial",10,"bold"),fg="DarkRed",bg=bg_color)
					Frame1.place(x=0,y=95,width=750,height=120)
					
					#Labels and Text Entry for Prices
					#Dispenser Bottle Unit Price
					dpwprice_lbl=Label(Frame1,text="Dispenser Bottle",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=5,pady=5,sticky="w")
					dpwprice_txt=Entry(Frame1,width=10,textvariable=DBPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=0,column=1,padx=3,pady=3)
					
					#BIG Bottle water Unit Price
					bbwprice_lbl=Label(Frame1,text="BIG Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=5,pady=5,sticky="w")
					bbwprice_txt=Entry(Frame1,width=10,textvariable=BBWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=1,column=1,padx=3,pady=3)
					
					#Small Bottle water Unit Price
					sbwprice_lbl=Label(Frame1,text="Small Bottle Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=2,padx=5,pady=5,sticky="w")
					sbwprice_txt=Entry(Frame1,width=10,textvariable=SBWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=0,column=3,padx=3,pady=3)
					
					#Sachet Pure water Unit Price
					spwprice_lbl=Label(Frame1,text="Sachet Pure Water",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=1,column=2,padx=5,pady=5,sticky="w")
					spwprice_txt=Entry(Frame1,width=10,textvariable=SPWPrice,font=("arial",15,"bold"),bd=3,relief=SUNKEN).grid(row=1,column=3,padx=3,pady=3)
					
					#Clear Price Button
					ClearPrice_btn=Button(Frame1,text="Clear Price",command=self.ClearPrice_data,width=10,bd=3,bg=bg_color,fg="Black",font="arial 12 bold").grid(row=0,column=4,padx=2,pady=2)
					
					#Update Price Button
					UpdatePrice_btn=Button(Frame1,text="Update Price",command=self.UpdatePriceDB_data,width=10,bd=3,bg=bg_color,fg="Green",font="arial 12 bold").grid(row=1,column=4,padx=2,pady=2)
					
					#Price Bottom Frame
					PriceTable_Frame=LabelFrame(newWindow,bd=5,relief=RIDGE,bg=bg_color)
					PriceTable_Frame.place(x=0,y=200,width=750,height=120)
					
					#DISPLAY FOR PRICE ENTRY
					scroll_x=Scrollbar(PriceTable_Frame,orient=HORIZONTAL)
					scroll_y=Scrollbar(PriceTable_Frame,orient=VERTICAL)
					#Format for the required column headings that will be displayed
					global CurrentPrice_table
					CurrentPrice_table=ttk.Treeview(PriceTable_Frame,columns=("PriceType","Dispenser","BigBottle","SmallBottle","SachetWater","PriceDate","EnteredBy"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
					
					#Scroll bar direction and configuration
					scroll_x.pack(side=BOTTOM,fill=X)
					scroll_y.pack(side=RIGHT,fill=Y)
					scroll_x.config(command=CurrentPrice_table.xview)
					scroll_y.config(command=CurrentPrice_table.yview)
					
					#Connecting each heading to a column of the existing fields
					CurrentPrice_table.heading("PriceType",text="PriceType")
					CurrentPrice_table.heading("Dispenser",text="Dispenser")
					CurrentPrice_table.heading("BigBottle",text="BigBottle")
					CurrentPrice_table.heading("SmallBottle",text="SmallBottle")
					CurrentPrice_table.heading("SachetWater",text="SachetWater")
					CurrentPrice_table.heading("PriceDate",text="PriceDate")
					CurrentPrice_table.heading("EnteredBy",text="EnteredBy")
					#Enable heading of tables to show
					CurrentPrice_table['show']='headings'
					
					#Set column width for each field in the table
					CurrentPrice_table.column("PriceType",width=130)
					CurrentPrice_table.column("Dispenser", anchor="center", width=60)
					CurrentPrice_table.column("BigBottle", anchor="center", width=60)
					CurrentPrice_table.column("SmallBottle", anchor="center", width=60)
					CurrentPrice_table.column("SachetWater", anchor="center", width=60)
					CurrentPrice_table.column("PriceDate",width=150)
					CurrentPrice_table.column("EnteredBy", anchor="center", width=150)
					#To expand the table  
					CurrentPrice_table.pack(fill=BOTH,expand=1)
					#Enable selection of items in the Bill_table
					CurrentPrice_table.bind("<ButtonRelease-1>",self.get_DBprice)
					
					self.fetchDBPrice_data()
					
					PriceList.pack()
					
					#Lovely Code that will ensure Child Window remains active and Root remains inactive until Child is Closed 
					#After Clicking on Update Price the new Window to Update Price must be fully used and closed before using main interface
					newWindow.transient(root)
					newWindow.grab_set()
					root.wait_window(newWindow)	
					#UpdateUnitPrice_btn.pack()
				
				
				#PRICE FUNCTIONS
				#Function to get prices and data from the CurrentPrice_Table when clicked into each of the Textboxes	
				def get_DBprice(self,ev):
					#PriceTypeTimeObj=datetime.now()
					try:
						cursor_row=CurrentPrice_table.focus()
						contents=CurrentPrice_table.item(cursor_row)
						row=contents['values']
						PriceType.set(row[0])
						DBPrice.set(row[1])
						BBWPrice.set(row[2])
						SBWPrice.set(row[3])
						SPWPrice.set(row[4])
						PriceDate.set(row[5])
						#self.TotalPayable.set("N"+str("{:0,.2f}".format(float(row[5]))))
					except:
						pass	
				
				#Function to Update the variables after Updating in the interface into the DB
				def UpdatePriceDB_data(self):
					try:
						if DBPrice.get()==0 or BBWPrice.get()==0 or SBWPrice.get()==0 or SPWPrice.get()==0:
							messagebox.showerror("Update Error","Select record from table\n and Insert valid data")
						else:
							##PriceTypeTimeObj=datetime.now()
							#TotalPayable=self.TotalPayable.get().replace("N","").replace(",","")
							ask=messagebox.askyesno("Update Record","Are you sure to proceed with update!")
							if ask==True:
								self.mynice_date()
								PriceDate.set(today_date)
								con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
								cur=con.cursor()
								cur.execute("update price set Dispenser=%s,BigBottle=%s,SmallBottle=%s,SachetWater=%s,PriceDate=%s,EnteredBy=%s where PriceType=%s",(
																															DBPrice.get(),
																															BBWPrice.get(),
																															SBWPrice.get(),
																															SPWPrice.get(),
																															PriceDate.get(),
																															v,
																															PriceType.get()
																															))
								con.commit()
								#Function of fetch_data is called here
								self.fetchDBPrice_data()
								con.close()
					except:
						messagebox.showerror("Invalid Data","Kindly input numbers only")
				
				#Function to clear the data in the Update Price
				def ClearPrice_data(self):
					PriceType.set("")
					DBPrice.set(0.00)
					BBWPrice.set(0.00)
					SBWPrice.set(0.00)
					SPWPrice.set(0.00)
					PriceDate.set("")
					CurrentPrice_table.selection_set()
				
				#NEW Function to fetch Price data
				def fetchDBPrice_data(self):
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					cur.execute("select * from price")
					rows=cur.fetchall()
					if len(rows)!=0:
						CurrentPrice_table.delete(*CurrentPrice_table.get_children())
						for row in rows:
							CurrentPrice_table.insert('',END,values=row)
						con.commit()
					con.close()
				
				
				#NEWEST%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
				#Assigning Price From DB to Variable for Multiplier
				def PackagerPriceMultiplier(self):
					global PackageDBP
					global PackageBBWP
					global PackageSBWP
					global PackageSPWP
					
					PackagerDayDBP=IntVar()
					PackagerDayBBWP=IntVar()
					PackagerDaySBWP=IntVar()
					PackagerDaySPWP=IntVar()
					
					PackagerNightDBP=IntVar()
					PackagerNightBBWP=IntVar()
					PackagerNightSBWP=IntVar()
					PackagerNightSPWP=IntVar()					
					
					#Connection to the Database
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					cur.execute("select * from price")
					rows=cur.fetchall()
					
					#Assigning each tuple in rows to a and f
					a,b,c,d,e,f=rows
					
					#for records in e as price of packager day
					PackagerDayDBP=e[1]
					PackagerDayBBWP=e[2]
					PackagerDaySBWP=e[3]
					PackagerDaySPWP=e[4]
					
					#for records in f as price of packager night
					PackagerNightDBP=f[1]
					PackagerNightBBWP=f[2]
					PackagerNightSBWP=f[3]
					PackagerNightSPWP=f[4]					
					
					#If the RunningFunction is 2 as allocated in Packager Unit else pass
					if PackagerPriceType_txt.get()=='DAY':
						PackageDBP = PackagerDayDBP
						PackageBBWP = PackagerDayBBWP
						PackageSBWP = PackagerDaySBWP
						PackageSPWP = PackagerDaySPWP
					else:
						PackageDBP = PackagerNightDBP
						PackageBBWP = PackagerNightBBWP
						PackageSBWP = PackagerNightSBWP
						PackageSPWP = PackagerNightSPWP
				
				#NEWEST %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
				#Assigning Price From DB to Variable for Multiplier
				def OperatorPriceMultiplier(self):
					#Global variable to hold the current price from the DB
					global DBP
					global BBWP
					global SBWP
					global SPWP
					
					global OperateDBP
					global OperateBBWP
					global OperateSBWP
					global OperateSPWP

					#Variable Datatypes
					OperatorDayDBP=IntVar()
					OperatorDayBBWP=IntVar()
					OperatorDaySBWP=IntVar()
					OperatorDaySPWP=IntVar()
					
					OperatorNightDBP=IntVar()
					OperatorNightBBWP=IntVar()
					OperatorNightSBWP=IntVar()
					OperatorNightSPWP=IntVar()				
					
					#Connection to the Database
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					cur.execute("select * from price")
					rows=cur.fetchall()
					
					#Assigning each tuple in rows to a and f
					a,b,c,d,e,f=rows
					
					#for records in c as price of operator day
					OperatorDayDBP=c[1]
					OperatorDayBBWP=c[2]
					OperatorDaySBWP=c[3]
					OperatorDaySPWP=c[4]
					
					#for records in c as price of operator night
					OperatorNightDBP=d[1]
					OperatorNightBBWP=d[2]
					OperatorNightSBWP=d[3]
					OperatorNightSPWP=d[4]
					
					#Condition to either pick DAY or NIGHT payment
					if OperaterPriceType_txt.get()=='DAY':
						OperateDBP = OperatorDayDBP
						OperateBBWP = OperatorDayBBWP
						OperateSBWP = OperatorDaySBWP
						OperateSPWP = OperatorDaySPWP
					else:
						OperateDBP = OperatorNightDBP
						OperateBBWP = OperatorNightBBWP
						OperateSBWP = OperatorNightSBWP
						OperateSPWP = OperatorNightSPWP					
				
				#NEWEST
				#Assigning Price From DB to Variable for Multiplier
				def PriceMultiplier(self):
					#Global variable to hold the current price from the DB
					global DBP
					global BBWP
					global SBWP
					global SPWP
					
					#NEWLY ADDED DRIVER PRICE
					global DriverDBP
					global DriverBBWP
					global DriverSBWP
					global DriverSPWP

					#Variable Datatypes
					DBP=IntVar()
					BBWP=IntVar()
					SBWP=IntVar()
					SPWP=IntVar()
					
					DriverDBP=IntVar()
					DriverBBWP=IntVar()
					DriverSBWP=IntVar()
					DriverSPWP=IntVar()
										
					
					#Connection to the Database
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					cur.execute("select * from price")
					rows=cur.fetchall()
					
					#rows is a multiple tuple
					#print(type(rows))
					#print(rows)
					
					#Assigning each tuple in rows to a and b
					a,b,c,d,e,f=rows

					
					#For each record on the Database Record assign Price to each variables
					#for records in a as normal sales price
					DBP=a[1]
					BBWP=a[2]
					SBWP=a[3]
					SPWP=a[4]
					
					#for records in b as price of drivers
					DriverDBP=b[1]
					DriverBBWP=b[2]
					DriverSBWP=b[3]
					DriverSPWP=b[4]
					
					
				#These two functions below DisableGenBill and EnableGenBill will be helpful after performing a search
				#So that user will not mistakenly click on Generate Bill that will automatically save the existing data with new PK in DB but same file name in TextFile
				#Hence, the DB and TextFile will not tally
				#Function to Disable Generate Bill Button and the BillNo. field to avoid editing it
				def DisableGenBill(self):
					total_btn['state']='disabled'
					gbill_btn['state']='disabled'
					#Also disable the original existing BillNo field to avoid editing it
					cbill_txt.configure(state='readonly')
				
				#Function to Enable Generate Bill Button
				def EnableGenBill(self):
					total_btn['state']='normal'
					gbill_btn['state']='normal'
				
				#This function will delete Selected record on Both DB and TextFile
				def DeleteDBandText_data(self):
					#print(self.SearchBill.get())
					ask=messagebox.askyesno("Deleting Record","Are you sure to proceed with delete! \nYou cannot undo this action")
					if ask==True:
						con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
						cur=con.cursor()
						#-#cur.execute("delete from bills where BillNo=%s",self.SearchBill.get())
						cur.execute("delete from bills where BillNo=%s",self.BillNo.get())
						con.commit()
						con.close()
						#Function of fetch_data is called here
						self.fetch_data()
						self.ClearAfterDelete_data()
					###FilePathToDelete='C:/Bills/'+str(self.SearchBill.get())+".txt"
					#print(FilePathToDelete)
					###os.remove(FilePathToDelete)
					#print(self.SearchBill.get())
					#Function to clear the data from interface after Delete from DB
					
				
				#This function will obtain the Sub-Total of all items displayed after Searching
				#It will enable easy Sub-Total per Bill, Day, Month, Name etc
				def SearchedSum(self):
					#Variable Stubtotal is used as accumulator set at 0.00 float
					Stubtotal = 0.00
					#For Every child of the table
					for child in self.Bill_table.get_children():
						#Accumulate the sum of each item displayed
						Stubtotal += float(self.Bill_table.item(child,'values')[9])
					#Transferring the sum above into the Sub-total text holder
					self.SearchedSumation.set("N"+str("{:0,.2f}".format(Stubtotal)))
					#print(Stubtotal)
				
				#This function will enable the update or change in Qty of items of Data into the DB
				#Once the item is selected from the Table Tree it will display for correction
				#It generates total immediately, so that fresh data will be selected
				def UpdateDB_data(self):
					TotalPayable=self.TotalPayable.get()
					#-#if self.SearchBill.get()=="" or TotalPayable=="":
					if self.BillNo.get()=="" or TotalPayable=="":
						messagebox.showerror("Update Error","Select record from table\n and Insert valid data")
					else:
						self.total()
						TotalPayable=self.TotalPayable.get().replace("N","").replace(",","")
						ask=messagebox.askyesno("Update Record","Are you sure to proceed with update!")
						if ask==True:
							self.mynice_date()
							updatedate=today_date
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("update bills set Dispenser=%s,BigBottle=%s,SmallBottle=%s,SachetWater=%s,CostDispenser=%s,CostBigBottle=%s,CostSmallBottle=%s,CostSachetWater=%s,Amount=%s,DateStamp=%s,Name=%s,Phone=%s,PreviousTotal=%s,UpdatedBy=%s,UpdatedDate=%s where BillNo=%s",(
																																																						self.BottleDispenser.get(),
																																																						self.BigBottleWater.get(),
																																																						self.SmallBottleWater.get(),
																																																						self.SachetPureWater.get(),
																																																						DBP,
																																																						BBWP,
																																																						SBWP,
																																																						SPWP,
																																																						TotalPayable,
																																																						self.CurrentTime.get(),
																																																						self.CName.get(),
																																																						self.CPhone.get(),
																																																						PreviousAmount,
																																																						v,
																																																						updatedate,
																																																						self.BillNo.get()
																																																						))
							con.commit()
							
							#NEWLY To auto focus the selection Balanced is performed on any selected Record
							#Using variable xx and yy to get the current fucos and index of the focus iid
							#This is done before the fetching of Database from DB to the TreeView
							xx=self.Bill_table.focus()
							yy=self.Bill_table.index(xx)
							#print(yy)				
							
							#This is to print each row as list of data that one can manipulate
							#-#childrenz = self.Bill_table.get_children()
							#-#for child in childrenz:
								#-#print(self.Bill_table.set(child))
							
							#Empty List
							SpecificUpdate=[]	
							#For each item in the current table view
							for childz in self.Bill_table.get_children():
								#xyz is the 1st part of the 10th column which is Date Entered
								xyz=(self.Bill_table.item(childz)["values"][10].split(' ')[0])
								#Append all date to empty list
								SpecificUpdate.append(xyz)
							#print(SpecificUpdate)
							#variable result is appended to check if all values in the list are ==
							
							#In case a search was done to get specific bill, hence the list will have only 1 entry
							if len(SpecificUpdate)<=1:
								#then clear all the screen after making the update
								self.ClearAfterDelete_data()
							else:	
								result = all(element == SpecificUpdate[0] for element in SpecificUpdate)
								#Condition to do if result is equal
								if (result):
									#Just fetch data for today
									self.fetch_data()
								else:
									#Just fetch data for all record
									self.fetch_data_all()
							

							#Function of fetch_data is called here
							#-#self.fetch_data()	
								
							#NEWLY To auto focus the selection Balanced selected Record
							try:
								child_id = self.Bill_table.get_children()[yy]
								cursor_row=self.Bill_table.focus(child_id)
								self.Bill_table.selection_set(child_id)
							except IndexError:
								pass
							#Function of fetch_data is called here
							#-#self.fetch_data()
							
							#After fetching the data then save the text file too
							self.UpdateBill_area()
							
							#Disable Update Button
							UpdateRecord_btn['state']='disabled'
							
							#TO ENABLE SUPER-ADMIN VIEW TEXTFILE AS FIRST ENTRY BEFORE IT WAS UPDATED
							#-#self.UpdateText_bill()
							con.close()
				
				
				#This function will work with the above file so that the text files will also be edited
				def UpdateText_bill(self):
					#op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
					#if op>0:
					self.bill_data=self.txtarea.get('1.0',END)
					#print(self.bill_data)
					#-#f1=open("C:/Bills/"+str(self.SearchBill.get())+".txt","wt")
					f1=open("C:/Bills/"+str(self.BillNo.get())+".txt","wt")
					f1.write(self.bill_data)
					f1.close()
					#messagebox.showinfo("Saved",f"Bill No. : {self.BillNo.get()} saved Successfully")
					#else:
						#return

				#Updating the Text_Bill also requires Updating Generate Bill
				#But we do not need new features just needed the Qty and themount
				def UpdateBill_area(self):
					#Enabling the txtarea to allow modification
					self.txtarea.config(state=NORMAL)
					#self.Welcome_bill()
					#Condition if Qty of Bottle Dispenser is not NIL
					#Enable display of item name, qty and subtotal cost of any item whose Qty order is above 0
					self.UpdateWelcome_bill()
					if self.BottleDispenser.get()!=0:
						self.txtarea.insert(END,f"\n 18.5 Litre\t\t{self.BottleDispenser.get()}\t{self.TotalBottleDispenser.get()}")
					#Condition if Qty of Big Bottle Water is not NIL
					if self.BigBottleWater.get()!=0:
						self.txtarea.insert(END,f"\n 75cl Bottle \t\t{self.BigBottleWater.get()}\t{self.TotalBigBottleWater.get()}")
					#Condition if Qty of Small Bottle Water is not NIL
					if self.SmallBottleWater.get()!=0:
						self.txtarea.insert(END,f"\n 55cl Bottle \t\t{self.SmallBottleWater.get()}\t{self.TotalSmallBottleWater.get()}")
					#Condition if Qty of Sachet Pure Water is not NIL
					if self.SachetPureWater.get()!=0:
						self.txtarea.insert(END,f"\n 55cl Sachet \t\t{self.SachetPureWater.get()}\t{self.TotalSachetPureWater.get()}")	
					self.txtarea.insert(END,f"\n -----------------------------------")
					#Total Bill
					self.txtarea.insert(END,f"\n TOTAL BILL :\t\t\t{self.Total_Bill}")
					self.txtarea.insert(END,f"\n -----------------------------------")
					self.txtarea.insert(END,f"\n -----Thanks for your patronage-----")
					#NEW line below to append the current datestamp at bottom
					#self.CurrentTime.set(self.dateTimeObj)
					#Calling the function to automatically Save Bill
					#self.Save_bill()
					#Calling the function to automatically Add Bill to DB
					#self.Add_bills()
					
					#After generating and saving bill, there is need to disable the txtarea from been modified
					self.txtarea.config(state=DISABLED)	
				
				def UpdateWelcome_bill(self):
					self.txtarea.delete('1.0',END)
					#The use of \t for tab to indent location of he welcome message
					self.txtarea.insert(END,"    Welcome to Kwambal Table Water")
					#Capture Company Address
					self.txtarea.insert(END,f"\n    Plot 9 No.64 Opp. Trailer Park\n Pompomari Bypass M/guri, Borno State")
					#Calling the function to display timeframe at exact point of generating Bill
					self.txtarea.insert(END,f"\n \t{self.CurrentTime.get()}")
					#Adding more text with ability to capture Customer details
					#-#self.txtarea.insert(END,f"\n Bill Number   : {self.SearchBill.get()}")
					self.txtarea.insert(END,f"\n Bill Number   : {self.BillNo.get()}")
					self.txtarea.insert(END,f"\n Customer Name : {self.CName.get()}")
					self.txtarea.insert(END,f"\n Phone Number  : {self.CPhone.get()}")
					self.txtarea.insert(END,f"\n ===================================")
					self.txtarea.insert(END,f"\n Items\t\tQTY\tPrice")
					self.txtarea.insert(END,f"\n ===================================")

					
				def AutoFocusSearch(self):
					if self.search_by.get()!="":
						txt_search.focus()
				
				#Generate REPORT Normal Sales
				def GenerateReport_Normal(self):
					try:
						#If one or both of the criteria is/are empty
						if self.FromDateNormal.get()=="" or self.ToDateNormal.get()=="":
							messagebox.showerror("Report Error","Date From: and Date To: \nAre compulsory")
							
						elif self.FromDateNormal.get()=="dd/mm/yyyy" or len((str(self.FromDateNormal.get()).split('/')[2]))!=4 or int((str(self.FromDateNormal.get()).split('/')[1]))>12:
							messagebox.showerror("Data Error","Date FROM must be in dd/mm/yyyy format")
							fromtextnormal.focus()
						
						elif self.ToDateNormal.get()=="dd/mm/yyyy" or len((str(self.ToDateNormal.get()).split('/')[2]))!=4 or int((str(self.ToDateNormal.get()).split('/')[1]))>12:
							messagebox.showerror("Data Error","Date TO must be in dd/mm/yyyy format")
							totextnormal.focus()
							
						else:
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("select * from bills where DateStamp BETWEEN '"+str(self.FromDateNormal.get())+" 00:00:00.000000' AND '"+str(self.ToDateNormal.get())+" 99:99:99.999999'")
							self.Bill_table.delete(*self.Bill_table.get_children())
							rows=cur.fetchall()
							if len(rows)<1:
								con.close()
								messagebox.showinfo('No Data!',"No record was captured within date range")
							elif len(rows)>=1:
								self.Bill_table.delete(*self.Bill_table.get_children())
								for row in rows:
									self.Bill_table.insert('',END,values=row)
								con.commit()
								con.close()
								#Auto focus the last record from the records returned after search
								child_id = self.Bill_table.get_children()[-1]
								cursor_row=self.Bill_table.focus(child_id)
								self.Bill_table.selection_set(child_id)
								self.get_cursor(cursor_row)
								
								#Calling a function to do Sub-Total Sum all items displayed in table after every search performed
								self.SearchedSum()
								
								#NEWLY
								self.DisableGenBill()
								
								#SAVE but ask use first
								savereport=messagebox.askyesno("Save Report","Report Successfully Retrieved \nDo you want to Save this Report?")
								if savereport>0:
									self.SaveCurrentTableItem()
								else:
									pass
							
					except ValueError:
						messagebox.showerror("Data Report Error","Invalid data entry")
				
				
				
				#This function will search using the search_by and search_txt to populate the data from DB to Table
				def search_data(self):
					try:
						#If one or both of the criteria is/are empty
						if self.search_by.get()=="" or self.search_txt.get()=="":
							messagebox.showerror("Search Error","Select Search by and \nType correct keyword")
						else:
							con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
							cur=con.cursor()
							cur.execute("select * from bills where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
							rows=cur.fetchall()
							if len(rows)!=0:
								self.Bill_table.delete(*self.Bill_table.get_children())
								for row in rows:
									self.Bill_table.insert('',END,values=row)
								con.commit()
							con.close()
							#Auto focus the last record from the records returned after search
							child_id = self.Bill_table.get_children()[-1]
							cursor_row=self.Bill_table.focus(child_id)
							self.Bill_table.selection_set(child_id)
							self.get_cursor(cursor_row)
							
							#Calling a function to do Sub-Total Sum all items displayed in table after every search performed
							self.SearchedSum()
							#NEWLY
							self.DisableGenBill()
					except ValueError:
						messagebox.showerror("Data Search Error","You have made an invalid data search")
					
				#NEW Function to focus cusor, when any record on the table is clicked it should display all the info therein
				def get_cursor(self,ev):
					try:
						cursor_row=self.Bill_table.focus()
						contents=self.Bill_table.item(cursor_row)
						row=contents['values']
						#-#self.SearchBill.set(row[0])
						self.BillNo.set(row[0])
						self.BottleDispenser.set(row[1])
						self.BigBottleWater.set(row[2])
						self.SmallBottleWater.set(row[3])
						self.SachetPureWater.set(row[4])
						
						#Cost per items * Qty of Items
						self.TotalBottleDispenser.set(str("{:0,.2f}".format(float(row[1])*float(row[5]))))
						self.TotalBigBottleWater.set(str("{:0,.2f}".format(float(row[2])*float(row[6]))))
						self.TotalSmallBottleWater.set(str("{:0,.2f}".format(float(row[3])*float(row[7]))))
						self.TotalSachetPureWater.set(str("{:0,.2f}".format(float(row[4])*float(row[8]))))
						
						#self.TotalPayable.set(row[9])
						self.TotalPayable.set("N"+str("{:0,.2f}".format(float(row[9]))))
						
						#Previous amount will be assigned to global variable PreviousAmount
						global PreviousAmount
						PreviousAmount=(row[9])
						
						self.CurrentTime.set(row[10])
						self.CName.set(row[11])
						self.CPhone.set(row[12])
						
						#This code disable Update Record Button once it has been previously Updated 1ce
						if CurrentCategory == 'Super-Admin':
							UpdateRecord_btn['state']='normal'
						elif CurrentCategory == 'Admin':
							if (row[14]) != "":
								UpdateRecord_btn['state']='disabled'
							else:
								UpdateRecord_btn['state']='normal'
						#else:
							#UpdateRecord_btn['state']='disabled'
							
						#**********CHANGE THIS CODE TO FETCH DATA FROM DB NOT TEXTFILE********************#
						#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
						#NEWLY ADDED to automatically find the bill of any selected item from the textarea
						##self.Find_bill()
						self.GetcursorForBillarea()
						
						#self.total()
						#Function to disable the Generate Bill needed here to avoid duplicate saving
						self.DisableGenBill()
					except:
						pass
				
				def GetcursorForBillarea(self):
					#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
					#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
					self.txtarea.config(state=NORMAL)
					self.txtarea.delete('1.0',END)
					#The use of \t for tab to indent location of he welcome message
					self.txtarea.insert(END,"    Welcome to Kwambal Table Water")
					#Capture Company Address
					self.txtarea.insert(END,f"\n    Plot 9 No.64 Opp. Trailer Park\n Pompomari Bypass M/guri, Borno State")
					#Calling the function to display timeframe at exact point of generating Bill
					self.txtarea.insert(END,f"\n \t{self.CurrentTime.get()}")
					#Adding more text with ability to capture Customer details
					#-#self.txtarea.insert(END,f"\n Bill Number   : {self.SearchBill.get()}")
					self.txtarea.insert(END,f"\n Bill Number   : {self.BillNo.get()}")
					self.txtarea.insert(END,f"\n Customer Name : {self.CName.get()}")
					self.txtarea.insert(END,f"\n Phone Number  : {self.CPhone.get()}")
					self.txtarea.insert(END,f"\n ===================================")
					self.txtarea.insert(END,f"\n Items\t\tQTY\tPrice")
					self.txtarea.insert(END,f"\n ===================================")
					#Condition if Qty of Bottle Dispenser is not NIL
					#Enable display of item name, qty and subtotal cost of any item whose Qty order is above 0
					if self.BottleDispenser.get()!=0:
						self.txtarea.insert(END,f"\n 18.5 Litre\t\t{self.BottleDispenser.get()}\t{self.TotalBottleDispenser.get()}")
					#Condition if Qty of Big Bottle Water is not NIL
					if self.BigBottleWater.get()!=0:
						self.txtarea.insert(END,f"\n 75cl Bottle \t\t{self.BigBottleWater.get()}\t{self.TotalBigBottleWater.get()}")
					#Condition if Qty of Small Bottle Water is not NIL
					if self.SmallBottleWater.get()!=0:
						self.txtarea.insert(END,f"\n 55cl Bottle \t\t{self.SmallBottleWater.get()}\t{self.TotalSmallBottleWater.get()}")
					#Condition if Qty of Sachet Pure Water is not NIL
					if self.SachetPureWater.get()!=0:
						self.txtarea.insert(END,f"\n 55cl Sachet \t\t{self.SachetPureWater.get()}\t{self.TotalSachetPureWater.get()}")	
					self.txtarea.insert(END,f"\n -----------------------------------")
					#Total Bill
					self.txtarea.insert(END,f"\n TOTAL BILL :\t\t\t{self.TotalPayable.get()}")
					self.txtarea.insert(END,f"\n -----------------------------------")
					self.txtarea.insert(END,f"\n -----Thanks for your patronage-----")
					self.txtarea.config(state=DISABLED)
					
				#NEW function to add info to DB
				def Add_bills(self):
					#Calling the total function so that Generate Bill will also calculate current total in case of changes
					self.total()
					#Condition to enable users enter the exact fields required
					#If Total Bill and BillNo. are missing it will display error
					TotalPayable=self.TotalPayable.get().replace("N","").replace(",","")
					#TotalPayable=float(TotalPayable)
					#print(TotalPayable)
					#-#try:
					#if self.TotalPayable.get()=="" and self.BillNo.get()=="" and self.CurrentTime.get()=="":
					#If condition where the value of total is 0.00, no need to generate Bill
					if self.TotalPayable.get()=="N0.00":
						#Run the function of Welcome message of Bill without data entry
						self.Welcome_bill()
						#Display message to show that user did not make valid item entry
						messagebox.showerror("Invalid Action","No item was purchased")
					else:
						self.mynice_date()
						#NEW line below to append the current datestamp at bottom
						self.CurrentTime.set(today_date)
						#New Bill Code Starting With YYMMDD
						yy=str(datetime.now()).split(' ')[0]
						yy=str((yy[2:]).replace('-',''))
						#print(yy)
							
						x=str(datetime.now()).split('.')[1]+str("N")
						randbillno=random.randint(10000,99999)
						self.BillNo.set(yy+str(randbillno)+x)
						
						con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
						cur=con.cursor()
						cur.execute("insert into bills values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.BillNo.get(),
																			self.BottleDispenser.get(),
																			self.BigBottleWater.get(),
																			self.SmallBottleWater.get(),
																			self.SachetPureWater.get(),																	
																			DBP,
																			BBWP,
																			SBWP,
																			SPWP,
																			TotalPayable,
																			self.CurrentTime.get(),
																			self.CName.get(),
																			self.CPhone.get(),
																			v,
																			"",
																			"",
																			""
																			))

						#Function of fetch_data is called here	
						con.commit()
						self.fetch_data()
						#Function to clear the data after adding it to DB
						#self.Clear_data()
						con.close()
						self.Bill_area()
						#Message box to indicate successfully added
						
						#NEWEST Auto Highlight the record that was added in the Driver Table TreeView
						#Auto focus the first record from the records returned after New Addition
						child_id = self.Bill_table.get_children()[0]
						cursor_row=self.Bill_table.focus(child_id)
						self.Bill_table.selection_set(child_id)
						self.get_cursor(cursor_row)
						
						messagebox.showinfo('Successfully added!',"The record has been captured")
					#-#except Exception:
					#-#messagebox.showerror("Add Data Error","There is a duplicate entry")
				
				def DBTOTAL(self):
					#Using a try and catch error incase when the Database is wiped
					#Opening the app will automatically want to Calculate all Total Inventory
					try:
						#Amount=float(Amount.repalce("N","").replace(",",""))
						con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
						cur=con.cursor()
						cur.execute("SELECT sum(Amount) AS totalsum FROM bills")
						result=cur.fetchall()
						for i in result:
							#print(i[0])
							self.TotalInventory.set("N"+str("{:0,.2f}".format(i[0])))
						con.commit()
					except TypeError:
						pass
						
				#NEW Function to fetch data FOR TODAY
				def fetch_data(self):
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					#cur.execute("select * from packagerbills where
					self.mynice_date()
					##cur.execute("select * from bills where DateStamp LIKE '%"+str(datetime.now()).split(' ')[0]+"%'")
					cur.execute("select * from bills where DateStamp LIKE '%"+str(today_date).split(' ')[0]+"%' order by DateStamp DESC")
					#cur.execute("select * from bills")
					rows=cur.fetchall()
					
					##NEWLY
					global mydata
					mydata=rows
					
					if len(rows)!=0:
						self.Bill_table.delete(*self.Bill_table.get_children())
						for row in rows:
							self.Bill_table.insert('',END,values=row)
						con.commit()
					#This function will Fetch the total sum of amount from the DB
					self.DBTOTAL()
					con.close()
					#This function will clear the content of Sub-Total
					self.SearchedSumation.set("")
					cname_txt.focus()

				#NEW Function to fetch data ALL
				def fetch_data_all(self):
					con=pymysql.connect(host="localhost",user="root",password="",database="mbila")
					cur=con.cursor()
					cur.execute("select * from bills order by DateStamp ASC")
					rows=cur.fetchall()
					
					##NEWLY
					global mydata
					mydata=rows
					
					if len(rows)!=0:
						self.Bill_table.delete(*self.Bill_table.get_children())
						for row in rows:
							self.Bill_table.insert('',END,values=row)
						con.commit()
					#This function will Fetch the total sum of amount from the DB
					self.DBTOTAL()
					con.close()
					#This function will clear the content of Sub-Total
					self.SearchedSumation.set("")					


				
				#NEW Function still not in use
				def quantityFieldListener():
					global DquantityVar
					global BBquantityVar
					global SBQuantityVar
					global PWQuantityVar
					DQty = DquantityVar.get()
					BBQty = BBquantityVar.get()
					SBQty = SBQuantityVar.get()
					PWQty = PWQuantityVar.get()
					if DQty != "":
						try:
							DQty=float(DQty)
						except ValueError:
							DQty.set("0.00")
				
				#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ MODIFY ALL FILE LOCATION TO C\BILLS DRIVE
				#Have to set the printer to default when using
				def Print_bill(self):
					try:
						#THIS SECTION IS to see how I can copy content of file I want to Print
						#Modify the spaces to enable clean printing
						#Temporarily Place it in a file and Print it only.
						##Check if the Bill No. is blank string then it Prints using the Bill No. in the text area
						
						##*******************NEW CODE TO SAVE FILE BEFORE PRINTING
						self.bill_data=self.txtarea.get('1.0',END)
						#print(self.bill_data)
						if not os.path.exists(directory):
							os.makedirs(directory)
						#-#f1=open("C:/Bills/"+str(self.SearchBill.get())+".txt","w")
						f1=open("C:/Bills/"+str(self.BillNo.get())+".txt","w")
						f1.write(self.bill_data)
						f1.close()
						
						#-#if self.SearchBill.get()=="":
						if self.BillNo.get()=="":
							self.Save_bill()
							#Opens the main file using the Bill No.
							fin = open("C:/Bills/"+str(self.BillNo.get())+".txt","rt")
							#Create another temporary file mainly for printing format
							fout = open("C:/Bills/printout.txt","wt")
							#Condition statement for each line in the file main fin
							for line in fin:
								#If the line startswith Items then just print it like that
								if line.startswith(" Items"):
									fout.write(line)
								#Else try to replace double tabs \t\t on any other lines with single tab \t
								else:
									#print(line.rstrip().replace("\t\t","\t"))
									fout.write(line.replace("\t\t","\t"))
							#Close the files
							fin.close()
							fout.close()
							os.startfile("C:/Bills/printout.txt","print")
						##Else it will automatically PRINT using the Bill No. in the Search
						else:
							#-#fin = open("C:/Bills/"+str(self.SearchBill.get())+".txt","rt")
							fin = open("C:/Bills/"+str(self.BillNo.get())+".txt","rt")
							#Create another temporary file mainly for printing format
							fout = open("C:/Bills/printout.txt","wt")
							for line in fin:
								if line.startswith(" Items"):
									fout.write(line)
								else:
									#print(line.rstrip().replace("\t\t","\t"))
									fout.write(line.replace("\t\t","\t"))
							fin.close()
							fout.close()
							os.startfile("C:/Bills/printout.txt","print")
							
						############################################################################################
						
						
						##WORKING But had to use the code above is better
						##Check if the Bill No. is blank string then it Prints using the Bill No. in the text area
						#if self.SearchBill.get()=="":
							##Specifying filepath
							#os.startfile("C:/Users/blamidi/Desktop/Billing App/Bills/"+str(self.BillNo.get())+".txt","print")
						##Else it will automatically PRINT using the Bill No. in the Search 
						#else:
							#os.startfile("C:/Users/blamidi/Desktop/Billing App/Bills/"+str(self.SearchBill.get())+".txt","print")
						
						
					##Catching Exception of FileNotFoundError in case one enters character in BillNo
					except FileNotFoundError:
						messagebox.showerror("Bill Not Found","Kindly check Bill No.")
				
				
				#=======================Calculations
				#Function to calculate amount payable using the number of entries in Grocery Items
				#Using str float conversions
				def total(self):
					try:
						#Run function to Recapture the Current Price data from the DB as Variables and use as Multiplier
						self.PriceMultiplier()
						#Sub Total Values in Currency of 2 decimal places
						self.TotalBottleDispenser.set(str("{:0,.2f}".format(float(self.BottleDispenser.get()*float(DBP)))))
						self.TotalBigBottleWater.set(str("{:0,.2f}".format(float(self.BigBottleWater.get()*float(BBWP)))))
						self.TotalSmallBottleWater.set(str("{:0,.2f}".format(float(self.SmallBottleWater.get()*float(SBWP)))))
						self.TotalSachetPureWater.set(str("{:0,.2f}".format(float(self.SachetPureWater.get()*float(SPWP)))))
						
						#self.TotalBottleDispenser.set(str("{:0,.2f}".format(float(self.BottleDispenser.get()*350))))
						#self.TotalBigBottleWater.set(str("{:0,.2f}".format(float(self.BigBottleWater.get()*150))))
						#self.TotalSmallBottleWater.set(str("{:0,.2f}".format(float(self.SmallBottleWater.get()*100))))
						#self.TotalSachetPureWater.set(str("{:0,.2f}".format(float(self.SachetPureWater.get()*70))))
						
						#This will automatically sum the above Sub-Total values in Currency of 2 decimal places		
						#Added a N for Naira sign, must be: self.TotalPayable.get().repalce("N","").replace(",","") when calculating
						self.TotalPayable.set("N"+str("{:0,.2f}".format(
																	float(self.TotalBottleDispenser.get().replace(",",""))+
																	float(self.TotalBigBottleWater.get().replace(",",""))+
																	float(self.TotalSmallBottleWater.get().replace(",",""))+
																	float(self.TotalSachetPureWater.get().replace(",",""))
																	)))
						#Extracting total pay
						#Removing the N sign and currency commas from the string to convert to float
						self.Total_Bill=self.TotalPayable.get().replace("N","")
						#print(self.Total_Bill)
						#self.Total_Bill=float(self.TotalPayable.get().repalce("N","").replace(",",""))
						self.Welcome_bill()
					except TclError:
						#Display this message
						messagebox.showerror("Data Error","You have made an invalid \ndata entry")
						#Clear the content of all totals and reset the Bill Section
						self.TotalBottleDispenser.set("")
						self.TotalBigBottleWater.set("")
						self.TotalSmallBottleWater.set("")
						self.TotalSachetPureWater.set("")
						self.TotalPayable.set("")
						self.Welcome_bill()
						
				#Function to display text in the Bill Area
				#Welcome Message constant displaying
				def Welcome_bill(self):
					#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
					self.txtarea.delete('1.0',END)
					#The use of \t for tab to indent location of he welcome message
					self.txtarea.insert(END,"    Welcome to Kwambal Table Water")
					#Capture Company Address
					self.txtarea.insert(END,f"\n    Plot 9 No.64 Opp. Trailer Park\n Pompomari Bypass M/guri, Borno State")
					#Calling the function to display timeframe at exact point of generating Bill
					#self.txtarea.insert(END,f"\n \t{self.Time_get()}")
					self.txtarea.insert(END,f"\n \t{self.CurrentTime.get()}")
					#Adding more text with ability to capture Customer details
					self.txtarea.insert(END,f"\n Bill Number   : {self.BillNo.get()}")
					self.txtarea.insert(END,f"\n Customer Name : {self.CName.get()}")
					self.txtarea.insert(END,f"\n Phone Number  : {self.CPhone.get()}")
					self.txtarea.insert(END,f"\n ===================================")
					self.txtarea.insert(END,f"\n Items\t\tQTY\tPrice")
					self.txtarea.insert(END,f"\n ===================================")
					#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
					self.txtarea.config(state=DISABLED)
					
				#Function to input time frame in the Bill
				def Time_get(self):
					self.mynice_date()
					self.dateTimeObj=today_date
					##self.dateTimeObj=datetime.now()
					##return self.dateTimeObj
					#global dateTimeObj
					
				def ClearWelcome_bill(self):
					self.txtarea.config(state=NORMAL)
					self.txtarea.delete('1.0',END)
					#The use of \t for tab to indent location of he welcome message
					self.txtarea.insert(END,"    Welcome to Kwambal Table Water")
					#Capture Company Address
					self.txtarea.insert(END,f"\n    Plot 9 No.64 Opp. Trailer Park\n Pompomari Bypass M/guri, Borno State\n")
					#Adding more text with ability to capture Customer details
					self.txtarea.insert(END,"\n Bill Number   :")
					self.txtarea.insert(END,f"\n Customer Name : {self.CName.get()}")
					self.txtarea.insert(END,f"\n Phone Number  : {self.CPhone.get()}")
					self.txtarea.insert(END,f"\n ===================================")
					self.txtarea.insert(END,f"\n Items\t\tQTY\tPrice")
					self.txtarea.insert(END,f"\n ===================================")
					self.txtarea.config(state=DISABLED)
					
				def Bill_area(self):
					#Enabling the txtarea to allow modification
					self.txtarea.config(state=NORMAL)
					self.Welcome_bill()
					#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
					self.txtarea.config(state=NORMAL)
					#Condition if Qty of Bottle Dispenser is not NIL
					#Enable display of item name, qty and subtotal cost of any item whose Qty order is above 0
					if self.BottleDispenser.get()!=0:
						self.txtarea.insert(END,f"\n 18.5 Litre\t\t{self.BottleDispenser.get()}\t{self.TotalBottleDispenser.get()}")
					#Condition if Qty of Big Bottle Water is not NIL
					if self.BigBottleWater.get()!=0:
						self.txtarea.insert(END,f"\n 75cl Bottle \t\t{self.BigBottleWater.get()}\t{self.TotalBigBottleWater.get()}")
					#Condition if Qty of Small Bottle Water is not NIL
					if self.SmallBottleWater.get()!=0:
						self.txtarea.insert(END,f"\n 55cl Bottle \t\t{self.SmallBottleWater.get()}\t{self.TotalSmallBottleWater.get()}")
					#Condition if Qty of Sachet Pure Water is not NIL
					if self.SachetPureWater.get()!=0:
						self.txtarea.insert(END,f"\n 55cl Sachet \t\t{self.SachetPureWater.get()}\t{self.TotalSachetPureWater.get()}")	
					self.txtarea.insert(END,f"\n -----------------------------------")
					#Total Bill
					self.txtarea.insert(END,f"\n TOTAL BILL :\t\t\t{self.Total_Bill}")
					self.txtarea.insert(END,f"\n -----------------------------------")
					self.txtarea.insert(END,f"\n -----Thanks for your patronage-----")
					#NEW line below to append the current datestamp at bottom
					#-#self.CurrentTime.set(self.dateTimeObj)
					
					#Overrided Add bill should call this function rather
					##Calling the function to automatically Add Bill to DB
					#-#self.Add_bills()
					
					#Calling the function to automatically Save Bill
					self.Save_bill()
						
					#After generating and saving bill, there is need to disable the txtarea from been modified
					self.txtarea.config(state=DISABLED)
				
				def Save_bill(self):
					#-#op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
					#-#if op>0:
					self.bill_data=self.txtarea.get('1.0',END)
					#print(self.bill_data)
					if not os.path.exists(directory):
						os.makedirs(directory)
					f1=open("C:/Bills/"+str(self.BillNo.get())+".txt","w")
					f1.write(self.bill_data)
					f1.close()
					messagebox.showinfo("Saved",f"Bill No. : {self.BillNo.get()} saved Successfully")
					#-#else:
					#-#return
						
				def Find_bill(self):
					#Enabling the txtarea to allow modification
					self.txtarea.config(state=NORMAL)
					#Variable present is assigned to string "no"
					present="no"
					#For each files that are in the folder Bills
					for i in os.listdir("C:/Bills/"):
						#A print will display all the file names in the folder
						#print(i)
						#Conditional statement to split e.g. 11234.txt using the dot .
						#Concentrating on the index [0] which is the file name not extension [1] 
						#If the filename is same as the filename entered into the search text
						#-#if i.split('.')[0]==self.SearchBill.get():
						if i.split('.')[0]==self.BillNo.get():
							#Clear the content of txtarea
							self.txtarea.delete('1.0',END)
							#Open that same file for reading
							f1=open(f"C:/Bills/{i}","r")
							#The above read file should be inserted into txtarea on screen
							for data in f1:
								self.txtarea.insert(END,data)
								#self
							f1.close()
							self.txtarea.config(state=DISABLED)
							present="yes"
					if present=="no":
						#-#messagebox.showerror("Error",f"Invalid Bill No. {self.SearchBill.get()} \nKindly enter valid one.")
						messagebox.showerror("Error",f"Invalid Bill No. {self.BillNo.get()} \nKindly enter valid one.")
				
				def ResetFromTo(self):
					#Enabling the txtarea to allow modification
					self.txtarea.config(state=NORMAL)
					#Clear Customer Data
					self.CName.set("")
					self.CPhone.set("")
					#-#self.SearchBill.set("")
					self.BillNo.set("")
					#Clear Grocery Items Variables
					self.BottleDispenser.set("0")
					self.BigBottleWater.set("0")
					self.SmallBottleWater.set("0")
					self.SachetPureWater.set("0")
					#Clear Total Operation Menu Variables
					self.TotalBottleDispenser.set("")
					self.TotalBigBottleWater.set("")
					self.TotalSmallBottleWater.set("")
					self.TotalSachetPureWater.set("")
					self.TotalPayable.set("")
					self.CurrentTime.set("")
					self.SearchedSumation.set("")
					#Search Section of DB
					self.search_txt.set("")
					self.search_by.set("")
					
					#Clear Report From - To
					self.ToDateNormal.set("dd/mm/yyyy")
					self.FromDateNormal.set("dd/mm/yyyy")
					
					#BillNo. to change
					#-#self.BillNo=StringVar("")
					###randbillno=random.randint(1000,9999)
					#X is the miscrosecond last part of datetime
					###x=str(datetime.now()).split('.')[1]
					###self.BillNo.set(str(randbillno))
					#Newly added line of x is the microsecond
					###self.BillNo.set(str(randbillno)+x)
					self.ClearWelcome_bill()
					self.fetch_data()
					#To enable the Generate Bill again
					self.EnableGenBill()
					#Re-enable the BillNo field so that search can be performed from that section too
					#-#cbill_txt.configure(state='normal')
					#Automatically focus the cursor in the Customer Name section
					cname_txt.focus()
					
					self.Bill_table.selection_set()
					
					self.txtarea.config(state=DISABLED)
				
					
				def Clear_data(self):
					clear=messagebox.askyesno("Clear Data","Do you really want to Clear Screen?")
					if clear>0:
						#Enabling the txtarea to allow modification
						self.txtarea.config(state=NORMAL)
						#Clear Customer Data
						self.CName.set("")
						self.CPhone.set("")
						#-#self.SearchBill.set("")
						self.BillNo.set("")
						#Clear Grocery Items Variables
						self.BottleDispenser.set("0")
						self.BigBottleWater.set("0")
						self.SmallBottleWater.set("0")
						self.SachetPureWater.set("0")
						#Clear Total Operation Menu Variables
						self.TotalBottleDispenser.set("")
						self.TotalBigBottleWater.set("")
						self.TotalSmallBottleWater.set("")
						self.TotalSachetPureWater.set("")
						self.TotalPayable.set("")
						self.CurrentTime.set("")
						self.SearchedSumation.set("")
						#Search Section of DB
						self.search_txt.set("")
						self.search_by.set("")
						
						#Clear Report From - To
						self.ToDateNormal.set("dd/mm/yyyy")
						self.FromDateNormal.set("dd/mm/yyyy")
						
						#BillNo. to change
						#-#self.BillNo=StringVar("")
						###randbillno=random.randint(1000,9999)
						#X is the miscrosecond last part of datetime
						###x=str(datetime.now()).split('.')[1]
						###self.BillNo.set(str(randbillno))
						#Newly added line of x is the microsecond
						###self.BillNo.set(str(randbillno)+x)
						self.ClearWelcome_bill()
						self.fetch_data()
						#To enable the Generate Bill again
						self.EnableGenBill()
						#Re-enable the BillNo field so that search can be performed from that section too
						#-#cbill_txt.configure(state='normal')
						#Automatically focus the cursor in the Customer Name section
						cname_txt.focus()
						
						self.Bill_table.selection_set()
						
						self.txtarea.config(state=DISABLED)
				
				
				def ClearAfterDelete_data(self):
					##clear=messagebox.askyesno("Clear Data","Do you really want to Clear Screen?")
					##if clear>0:
					#Enabling the txtarea to allow modification
					self.txtarea.config(state=NORMAL)
					#Clear Customer Data
					self.CName.set("")
					self.CPhone.set("")
					#-#self.SearchBill.set("")
					self.BillNo.set("")
					#Clear Grocery Items Variables
					self.BottleDispenser.set("0")
					self.BigBottleWater.set("0")
					self.SmallBottleWater.set("0")
					self.SachetPureWater.set("0")
					#Clear Total Operation Menu Variables
					self.TotalBottleDispenser.set("")
					self.TotalBigBottleWater.set("")
					self.TotalSmallBottleWater.set("")
					self.TotalSachetPureWater.set("")
					self.TotalPayable.set("")
					self.CurrentTime.set("")
					self.SearchedSumation.set("")
					#Search Section of DB
					self.search_txt.set("")
					self.search_by.set("")
					
					#BillNo. to change
					#-#self.BillNo=StringVar("")
					#-#randbillno=random.randint(1000,9999)
					#X is the miscrosecond last part of datetime
					#-#x=str(datetime.now()).split('.')[1]
					#-#self.BillNo.set(str(randbillno))
					#Newly added line of x is the microsecond
					#-#self.BillNo.set(str(randbillno)+x)
					
					#Clear Report From - To
					self.ToDateNormal.set("dd/mm/yyyy")
					self.FromDateNormal.set("dd/mm/yyyy")
					
					self.ClearWelcome_bill()
					self.fetch_data()
					#To enable the Generate Bill again
					self.EnableGenBill()
					#Re-enable the BillNo field so that search can be performed from that section too
					cbill_txt.configure(state='normal')
					#Automatically focus the cursor in the Customer Name section
					cname_txt.focus()
					
					self.Bill_table.selection_set()
					
					self.txtarea.config(state=DISABLED)

				
				def Exit_app(self):
					exit=messagebox.askyesno("Exit Software","Do you really want to exit?")
					if exit>0:
						self.root.destroy()
				
				def SaveCurrentTableItem(self):
					#Empty list for each column in the treeview
					column1_list = []
					column2_list = []
					column3_list = []
					column4_list = []
					column5_list = []
					column6_list = []
					column7_list = []
					column8_list = []
					column9_list = []
					column10_list = []
					column11_list = []
					column12_list = []
					column13_list = []
					column14_list = []
					column15_list = []
					column16_list = []
					column17_list = []
					
					#running through the lines of the treeview in a "for" function, append to each column list the value of the column in each line
					for child in self.Bill_table.get_children():
						column1_list.append(self.Bill_table.item(child)["values"][0]) 
						column2_list.append(self.Bill_table.item(child)["values"][1]) 
						column3_list.append(self.Bill_table.item(child)["values"][2]) 
						column4_list.append(self.Bill_table.item(child)["values"][3]) 
						column5_list.append(self.Bill_table.item(child)["values"][4]) 
						column6_list.append(self.Bill_table.item(child)["values"][5]) 
						column7_list.append(self.Bill_table.item(child)["values"][6]) 
						column8_list.append(self.Bill_table.item(child)["values"][7]) 
						column9_list.append(self.Bill_table.item(child)["values"][8]) 
						column10_list.append(self.Bill_table.item(child)["values"][9]) 
						column11_list.append(self.Bill_table.item(child)["values"][10]) 
						column12_list.append(self.Bill_table.item(child)["values"][11])
						column13_list.append(self.Bill_table.item(child)["values"][12])
						column14_list.append(self.Bill_table.item(child)["values"][13])
						column15_list.append(self.Bill_table.item(child)["values"][14])
						column16_list.append(self.Bill_table.item(child)["values"][15])
						column17_list.append(self.Bill_table.item(child)["values"][16])
						

					
					#"BillNo","Dispenser","BigBottle","SmallBottle","SachetWater","CostDispenser","CostBigBottle","CostSmallBottle","CostSachetWater","Amount","DateStamp","Name","Phone"
										
					#create a dictionary from all the lists, using the header as the key and lists are the values as a list
					full_treeview_data_dict = {'BillNo': column1_list, 'Dispenser': column2_list, 'BigBottle': column3_list, 'SmallBottle': column4_list, 'SachetWater': column5_list, 'CostDispenser': column6_list, 'CostBigBottle': column7_list, 
												'CostSmallBottle': column8_list, 'CostSachetWater': column9_list, 'Amount': column10_list, 'DateStamp': column11_list, 'Name': column12_list, 'Phone': column13_list, 'EnteredBy': column14_list,
												'PreviousTotal': column15_list, 'UpdatedBy': column16_list, 'UpdatedDate': column17_list} 
					
					#Create a dataframe from the dictionary
					treeview_df = pd.DataFrame.from_dict(full_treeview_data_dict)
					
					#print(treeview_df)
					if len(mydata) < 1:
						messagebox.showerror("No Data","No data available to export")
						return False
					try:
					
						filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Save to Excel',defaultextension='.xlsx',filetypes=[("Excel file", "*.xlsx")])
						treeview_df.to_excel(filename, engine='xlsxwriter',index= False)
						messagebox.showinfo("Data Exported","Your data has been exported to "+os.path.basename(filename)+" successfully.")
					except:
						pass
				
				def SaveToCSVandExcel(self):
					#For empty data
					if len(mydata) < 1:
						messagebox.showerror("No Data","No data available to export")
						return False
					#Export to Save File Dailogbox
					try:
						filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Export as CSV and Excel",defaultextension='.csv',filetypes=[("CSV file", "*.csv")]) 		
						with open(filename, mode='w') as myfile:
							#w=os.getcwd()
							#print(w)
							exp_writer = csv.writer(myfile, delimiter=';')
							for i in mydata:
								exp_writer.writerow(i)
						messagebox.showinfo("Data Exported","Your data has been exported to "+os.path.basename(filename)+" successfully.")
						#print(filename)
						
						#Make use of the user's defined filename
						#filesaved=os.path.basename(filename)
						
						#Deleting all blank spaces in users CSV file
						df = pd.read_csv(filename)
						df.to_csv(filename, index=False)

						wb = Workbook()
						sheet = wb.active

						#Converting the CSV file to Excel File
						CSV_SEPARATOR = ";"
						with open(filename) as f:
							reader = csv.reader(f)
							for r, row in enumerate(reader):
								for c, col in enumerate(row):
									for idx, val in enumerate(col.split(CSV_SEPARATOR)):
										cell = sheet.cell(row=r+1, column=idx+1)
										cell.value = val
						
						excelfilename=filename.split('.')[0]
						#print(excelfilename)
						wb.save(excelfilename+'.xlsx')
					except:
						pass
				
				
				
			root=Tk()
			obj = Bill_App(root)
			root.mainloop()
			#Newly Added to show dialog box
			#UpdateUnitPrice_btn.pack()

		else:
			messagebox.showerror("Invalid Login Details","Kindly Input Valid \nUsername and Password")
	except:
		messagebox.showerror("Invalid DB Connection","Kindly check your Database Connection\Reconnect and Restart the Application. Thank you.")
		#Quit the app due to lack of database communication
		exit()
		

#Newly added
global master
master=Tk()
master.title("User Login")
master.wm_iconbitmap('icon.ico')
w=400
h=380
ws = master.winfo_screenwidth()
hs = master.winfo_screenheight()
#calculate position x, y automatically base on the screen in use
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
master.geometry('%dx%d+%d+%d' % (w, h, x, y))
master.resizable(0,0)
master.configure(bg="DarkGray")

#Image for the background of Login Dialog
bg_icon=ImageTk.PhotoImage(file="images/bgnew.jpg")
bg_lbl=Label(master,image=bg_icon).pack()

#Image Logo on the login page
logoframe=Frame(master,bd=4,relief=RIDGE,bg="Gray")
logoframe.place(x=140,y=10,width=110,height=160)
logo=ImageTk.PhotoImage(file="images/logo.png")
logo_lbl=Label(logoframe,image=logo).pack()

#Label for the login dialog box
label=Label(master,text=" KWAMBAL WATER LOGIN ",relief=GROOVE,font=("Arial",18,"bold"),fg="white",bg="green")
label.place(x=40,y=180)

#Making global variable of ery2 and ery3
global ery2,ery3,image

#Label to indicate instruction
label1=Label(master,text="Enter your login details",fg="Red",font=("Arial",12,"bold"))
label1.place(x=40,y=220)

#Username Label
label2=Label(master,text="UserName",relief=RIDGE,font=("Arial",10,"bold"),fg="Black")
label2.place(x=40,y=250)
#Text entry for Username
ery2=Entry(master,width=36)
ery2.place(x=140,y=250)
ery2.focus()

#Password Label
label2=Label(master,text="Password ",relief=RIDGE,font=("Arial",10,"bold"),fg="Black")
label2.place(x=40,y=290)
#Text entry for Password
ery3=Entry(master,show="*",width=36,fg="Red")
ery3.place(x=140,y=290)

#Login Button
button1=Button(master,text="Login",font=("Arial",10,"bold"),command=user_valid,fg="Green")
button1.place(x=140,y=320)

#Change Password Button
button2=Button(master,text="Change Password",font=("Arial",10,"bold"),command=change_password,fg="Blue")
button2.place(x=190,y=320)

#Quit Button
button3=Button(master,text="Quit ",font=("Arial",10,"bold"),command=login_quit,fg="Red")
button3.place(x=320,y=320)


master.mainloop()