class User():
	"""Простая модель пользователя"""
	def __init__(self, login):
		self.password=login
		self.login=login
		self.post='none'
		
	def check_pass(self):
		if self.password==login:
			print("Поменяйте пароль!")
			self.change_pass()
		
	def change_pass(self):
		new_pass=input("Введите новый пароль: ")
		new_pass_2=input("Подтвердите новый пароль: ")
		if new_pass==new_pass_2:
			self.password=new_pass
		else:
			print("Ошибка, пароли не совпадают.")

class Student(User):
	"""Простая модель студента"""
	def __init__(self, login, info):
		super().__init__(login)
		self.surname=info[0]		 
		self.name=info[1]
		self.sursurname=info[2]	
		self.group=info[3]
		self.post=info[4]
		self.password=[5]
		self.full_name=self.name.title()+self.surname.title()
			
	def make_starosta(self):
		self.post='староста'
		print(self.full_name+' теперь назначен как '+self.post+'!')
		print('Поздравляем, '+self.full_name+'!')
		
	def make_proforg(self):
		self.post='профорг'
		print(self.full_name+' теперь назначен как '+self.post+'!')
		print('Поздравляем, '+self.full_name+'!')
		
	def make_gruoporg(self):
		self.post='группорг'
		print(self.full_name+' теперь назначен как '+self.post+'!')
		print('Поздравляем, '+self.full_name+'!')
		
	def make_student(self):
		self.post='студент'
		print(self.full_name+' теперь назначен как '+self.post+'!')
		print('Поздравляем, '+self.full_name+'!')
		
	def make_note(self):
		if self.post=='староста':
			Notepad().create_new()
			
			
class Notepad():
	"""Простая модель блокнота"""
	def __init__(self, note={}):
		self.note=note
		
	def show_desk():
		for zagolovok, texts in note.items():
			print(zagolovok+": ")
			for text in texts:
				print(text)
	
	def create_new(self):
		zagolovok=input('Введите заголовок(допускается меньше 20 символов): ')
		
		if len(zagolovok)>20:
			print("Вы ввели больше 20!")
			self.create_new()
		
		text=[]
		print("Нажмите -q, чтобы выйти.")
		
		while(not k=="-q"):
			message=input("Введите заметку: ")
			text=text.append(message)
		
		note[zagolovok]=text
		
	def delete_note(self):
		note.clear()
		print("Записи были удалены.")
		
	def delete_note(self):
		zagolovok=input("Название заметки для удаления: ")
		if note[zagolovok]:
			note.pop(zagolovok)	
		else: 
			print("Такой заметки нет! Попробуйте еще раз")
			
"""class Teacher(User):
	Простая модель учителя
		def __init__(self, login, info):
		super().__init__(login)
		self.surname=info[0]		 
		self.name=info[1]
		self.sursurname=info[2]	
		self.groups=info[3]
		self.predmets=info[4]
		self.full_name=self.name.title()+self.surname.title()
		
		def make_note(self):
			Notepad().create_new()"""
				
			
		
		
		
