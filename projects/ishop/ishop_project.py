#проблемы и развитие:
#- добавить использование опциональных параметров при создании объекта
#- разграничить сферу ответственности (например, фото товара не может быть добавлено покупателем)
#- сделать генератор для id
#- при регистрации проверять уникальность логина
#- добавить проверку соответствия  логина и пароля
#- добавить super()
#- добавить декораторы
#- заполнить классы и методы
#- чёрная метка - если пользователь или данный адрес не забрал товар - при активации промо-кода считать его неверным

class User:
	def __init__(self, user_name):
		self.user_id = user_id
#user_id должен браться из какого-то генератора
#вариант генерации id: дата в обратном порядке, время и генерируемая цифра - 2212111405011 (22-12-11 14:05:01_1)
		self.user_name = user_name
		self.user_login = user_login
#при регистрации проверять уникальность логина
		self.user_password = user_password
		self.user_avatar = user_avatar
	def __str__(self):
		return self.user_name

class Real_object:
	def __init__(self, name):
		self.name = name

class Real_Item(Real_object):				#товар
	def __init__(self, name, price, description, category, photo, rating, review) -> bool:
		self.making_result = False
		self.item_id = 11111111111111111111	#item_id должен браться из какого-то генератора
		self.name = name					#название товара
		self.price = price					#цена
		self.description = description		#описание
		self.category = category			#категория
		self.photo = photo					#фото
		self.rating = rating				#рейтинг
		self.review = review				#отзывы
		self.visible = visible				#видимость товара - например, чтобы показывать его, только если он есть на складе (или понижать при поиске?)
		self.making_result = True
		return self.making_result			#результатом должно стать True в качестве подтверждения того, что товар был успешно создан
		
class Customer(User):						#помимо всего прочего, должен иметь возможность писать отзывы и выставлять рейтинг товара
	def __init__(self, customer_first_name, customer_second_name, customer_last_name, customer_email, customer_phone, customer_bonus):
		self.customer_first_name = customer_first_name
		self.customer_second_name = customer_second_name
		self.customer_last_name = customer_last_name 
		self.customer_address = customer_address
		self.customer_email = customer_email
		self.customer_phone = customer_phone
		self.customer_cummulitive_sum = customer_cummulitive_sum
		self.customer_bonus = customer_bonus
	def __str__(self):
		return self.user_name
#
		
class Photographer(User, Real_Item): #фотограф - добавляет фотки товаров
	def __init__(self):
		pass
	def __str__(self):
		return self.user_name

class Storekeeper(User):					#кладовщик - пишет о поступлении товаров, отгружает...
	def __init__(self):
		pass
	def __str__(self):
		return self.user_name

class Financier(User):						#финансист - отслеживает факты поступления оплаты и получения товара
	def __init__(self):
		pass
	def __str__(self):
		return self.user_name
		
class Admin(User):							#добавляет новые товары, пишет описание товаров, выставляет категории и цену
	def __init__(self):
		pass
	def __str__(self):
		return self.user_name

class Ownder(User):							#разрешает добавление новых владельцев, и персонала, может удалять существующих, имеет все права
	def __init__(self):
		pass
	def __str__(self):
		return self.user_name



class Real_stock(Real_Item):	#склад
	def __init__(self):
		self.stock = stock					#здесь должен находиться словарь: id_товара - количество
	def Change_stock(self, item_id, item_quantity):
		self.item_id = item_id
		self.item_quantity = item_quantity
		
		
class Virtual_object:
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return self.name

class Main_page(Virtual_object):			#главная страница
	def __init__(self, name):
		self.name = name

class Registration_page(Virtual_object):	#страница регистрации
	def __init__(self, name):
		self.name = name

class Order_page(Virtual_object):			#страница оформления заказа
	def __init__(self, name):
		self.name = name

class Add_item_page(Virtual_object):		#страница внесения товара в магазин (для админа)
	def __init__(self, name):
		self.name = name

class Edit_item_page(Virtual_object):		#страница редактирования свойств товара (для админа)
	def __init__(self, name):
		self.name = name
		
class Personal_settings_page(Virtual_object): #страница персональных настроек пользователя
	def __init__(self, name):
		self.name = name
		
class Showcase(Virtual_object):				#витрина (остальные страницы магазина)
	def __init__(self, category, show_quantity):
		self.category = category
		self.show_quantity = show_quantity	#количество отображаемых позиций
	def to_find_items(self, fragment):
		self.search_results = (11111111111) #здесь должен будет происходить поиск по названиям товаров и выдаваться кортеж из id подходящих под условия
		return self.search_results			#дополнительно предусмотреть вариант когда ничего не найдено и когда товаров нет
	def to_filter(self, fragment):
		self.filter_results = (11111111111) #здесь должна будет происходить фильтрация по названиям товаров и выдаваться кортеж из id подходящих под условия
		return self.filter_results			#дополнительно предусмотреть вариант когда ничего не найдено и когда товаров нет
		
class Customer_basket(Virtual_object, User): #корзина
	def __init__(self):
		self.basket_id = 111111111111111111	#basket_id должен браться из какого-то генератора и должен быть связан с покупателем (id корзины, разделитель, id покупателя?)
		self.content = content				#здесь должен быть словарь: id_товара - количество
		self.customer_bonus = customer_bonus #здесь по количеству товара должна вычисляться текущая стоимость корзины
		self.sum = sum						#здесь по количеству товара должна вычисляться текущая стоимость корзины
	def add_item(self, item_id):			#у покупателя должна быть возможность добавить товар в корзину
		pass								#...но не со страницы корзины? должна быть отдельная страница корзины? или страница оформления заказа?
	def change_quantity_items(self, item_id, quantity): #у покупателя должна быть возможность изменить количество товара в корзине
		pass
	def remove_item(self, item_id):			#у покупателя должна быть возможность убрать товар из корзины
		pass
	def clear_basket(self):					#у покупателя должна быть возможность очистить корзину
		pass
		
class Customer_order(Customer_basket): #заказ должен формироваться из корзины покупателя
	def __init__(self, order_address, order_sum):
		order_id.self = order_id
		self.order_address = order_address
		self.order_bonus = order_bonus		#здесь должна быть система, которая сравнивает введённый промокод с базой и если он совпал, то добавляет скидку
											#систему ввода промо-кода тоже нужно где-то прописать
		self.customer_bonus = customer_bonus #накопительный бонус покупателя (надо продумать)
		self.delivery_method = delivery_method
		self.pay_method = pay_method		
		self.pay_time = pay_time			#оплата авансом или при получении заказа
		self.order_sum = order_sum			#при подсчёте суммы должны учитываться оба бонуса - накопительный бонус покупателя и разовый

#Customer1 = Customer()