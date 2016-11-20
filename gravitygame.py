#!/usr/bin/env python3


import random
import tkinter 
from tkinter import ttk
from tkinter import messagebox


class GravityGame(object):

	def __init__(self):
		self.root = tkinter.Tk()
		self.style = ttk.Style()
		self.style.theme_use('default')
		self.root.title('GravityGame')

		self.form = ttk.Frame(self.root)
		self.content = ttk.Frame(self.form)              
		self.planet_label = ttk.Label(self.content, text='Planet:      ', justify='right')
		self.planet_name = tkinter.StringVar()
		self.planets = ['Earth', 'Moon', 'Jupiter']
		self.planet_name.set(self.planets[0])
		self.planet_combo = ttk.Combobox(self.content, textvariable=self.planet_name,
										 values=self.planets)
		self.box_velocity_label = ttk.Label(self.content, text='Box velocity:', justify='right')
		self.box_velocity = tkinter.DoubleVar()
		self.box_velocity.set(25.0)
		self.box_velocity_entry = ttk.Entry(self.content, textvariable = self.box_velocity )
		self.box_ms_label = ttk.Label(self.content, text='m/s', justify='left')
		self.drop_button = ttk.Button(self.content, text='Drop', command=self.drop)
		self.start_button = ttk.Button(self.content, text='Start', command=self.start_box)
		self.reset_button = ttk.Button(self.content, text='Reset', command=self.reset_to_start) 
		self.canvas = tkinter.Canvas(self.content,width=640, height=480, bg='white')
		self.canvas['borderwidth']=2
		self.result_label= ttk.Label(self.content, text = "Result:")
		self.result_var = tkinter.StringVar()
		self.result_var.set("")
		self.result_entry= ttk.Entry(self.content, textvariable=self.result_var)
		self.result_entry["state"]="disabled"
		self.filler = tkinter.Frame(self.form, padx=5,pady=5)



		# placement of the widgets on the from

		self.form.grid(row=0, column=0, rowspan=3,columnspan=3)
		self.content.grid(row=1, column=1, rowspan=5, columnspan=3)
		self.filler.grid(row=4, column=0, rowspan=3, ipadx=5, ipady=50)
		self.planet_label.grid(row=0, column=1, sticky=('E','W'))
		self.planet_combo.grid(row=0, column=2, columnspan=2)
		self.box_velocity_label.grid(row=1, column=1, sticky=('E','W'))
		self.box_velocity_entry.grid(row=1, column=2)
		self.box_ms_label.grid(row=1, column=3, ipadx=5, sticky=('E','W'))
		self.start_button.grid(row=2, column=1)
		self.drop_button.grid(row=3, column=1)
		self.reset_button.grid(row=4, column=1, pady=100)
		self.result_label.grid(row=5, column=1)
		self.result_entry.grid(row=5, column=2)
		self.canvas.grid(row=0, column=4, rowspan=4)



	def drop(self):
		print("dropbutton pressed")
		self.result_var.set("kaka gedropt")
		
		pass

	def start_box(self):
		print("start button pressed")
		pass

	def reset_to_start(self):
		print("reset button pressed")
		pass

	
	def change_style(self, event=None):
		"""set the Style tot the content of the Combobox"""
		content = self.combo.get()
		try:
			self.style.theme_use(content)
		except tkinter.TclError as err:
			messagebox.showerror('Error', err)
		else:
			self.root.title(content)

			
app = GravityGame()
app.root.mainloop()
