from module import *

from flask import render_template, request

""" Structures """
SETTING_TEMPLATE = {
	"index":"index.html",
	"detail":"detail.html",
}

global_data = {
	"NAME_SHOP":"Магазин"
}

# Товары
product = StaticObjectsStructure(["Название", "Описание", "Стоимость"])
# Передавать 3 аргумента name, description, price
# Копируйте сточку ниже и пишите между скобок свои данные, удачи
product.add_row(name="Очень", description="Очень", price="299.99")
product.add_row(name="Топовый", description="Топовый", price="299.99")
product.add_row(name="Товар", description="Товар", price="299.99")
product.add_row(name="Только", description="Только", price="299.99")
product.add_row(name="Сегодня", description="Сегодня", price="299.99")

# ВАМ ТУДА НЕ НАДО
# ВАМ НУЖНО ВЫШЕ 
print(product.table)

for a in product.structure:
	a["short_description"] = a["description"][:60]

global_data['allproduct'] = product.structure

global_data['header_color'] = 'dark'
global_data['header_color_text'] = 'ligth'

global_data['footer_color'] = 'dark'
global_data['footer_color_text'] = 'ligth'

""" Sites """
site = App(__name__)
# logic

@site.site.route("/")
def index():
	notifications = []

	data = None

	return render_template(SETTING_TEMPLATE["index"], data=data, global_data=global_data, notifications=notifications)

@site.site.route("/<int:id>")
def detail(id):
	notifications = []
	data = product.search_to_structure(obj=id)

	return render_template(SETTING_TEMPLATE["detail"], data=data, global_data=global_data, notifications=notifications)

# Starting
site.start(debug=True)