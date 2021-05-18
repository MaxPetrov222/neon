from prettytable import PrettyTable
from colorama import Fore

from datetime import datetime as dt

from flask import Flask, render_template

class App():
	def __init__(self, name:str=__name__, template_folder:str="templates"):
		self.site = Flask(name, template_folder=template_folder)
		print(f"{Fore.GREEN}Приложение создано{Fore.RESET}")

	def start(self, debug=False, port=5000):
		self.site.run(debug=debug, port=port)

""" Время """
def GetTime():	
	time = str(dt.now())[11:19]
	day = str(dt.now())[8:10]
	month = str(dt.now())[5:7]
	year = str(dt.now())[0:4]

	return f"{time} {day}/{month}/{year}"

""" Структура товаров """
class StaticObjectsStructure():
	def __init__(self, rows):
		self.structure = []

		self.rows = rows
		self.last_id = 1

		# Красивая таблица структуры
		rowstable = [f"{Fore.YELLOW}ID{Fore.RESET}"]
		for row in rows:
			rowstable.append(f"{Fore.YELLOW}{row}{Fore.RESET}")
		
		self.table = PrettyTable(rowstable)

	def add_row(self, **structure):
		# Добавление товаров
		row = {"id":self.last_id}

		# Таблица
		coltable = [self.last_id]

		for name, obj in structure.items():
			row[name] = obj

			# Добавление елементов в масив
			coltable.append(obj)

		self.last_id += 1


		# Добавление в таблицу
		self.table.add_row(coltable)


		# Добавление в структуру
		self.structure.append(row)

	def search_to_structure(self, row='id', obj=None):
		# Поиск по структуре
		for objs in self.structure:
			if objs[row] == obj:
				return objs