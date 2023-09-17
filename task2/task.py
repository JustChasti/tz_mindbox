from pyspark.sql import SparkSession
import findspark


findspark.init()


# questions
# "В датафреймах заданы продукты, категории и связь между ними" Исходя из текста я делаю предположение что исходных датафрейма 3
# По причине того что у каждого из продуктов несколько категорий и у каждой категории несколько продуктов, 
# В products и categories по 1 столбцу, а в relations сколько угодно. Надеюсь я все верно понял?)
# Не очень ясная изначальная структура таблиц, от нее многое зависит в решении

spark = SparkSession.builder.getOrCreate()

products = spark.createDataFrame([
    {'product_name': 'кот подсолнух'},
    {'product_name':'кубик рубика'},
    {'product_name':'монитор hp'},
    {'product_name':'энергетик redbull'},
    {'product_name':'монитор asus'},
    {'product_name':'ежедневник'}
])

categories = spark.createDataFrame([
    {'category_name': 'кошка'},
    {'category_name':'игрушка'},
    {'category_name':'монитор'},
    {'category_name':'блокноты'},
    {'category_name':'канцтовары'},
    {'category_name':'пустая'}
])

relations = spark.createDataFrame([
    {'category_name': 'кошка', 'products': ['кот подсолнух']},
    {'category_name':'игрушка', 'products': ['кот подсолнух', 'кубик рубика']},
    {'category_name':'мониторы', 'products': ['монитор hp', 'монитор asus']},
    {'category_name':'блокноты', 'products': ['ежедневник']},
    {'category_name':'канцтовары', 'products': ['ежедневник']}
])

multirow = relations.filter(len(relations.products))

# по идее должно получиться так 
# ([
#     {'product_name': 'кот подсолнух', 'category_name': 'кошка'}, 
#     {'product_name': 'кот подсолнух', 'category_name': 'игрушка'},
#     {'product_name': 'кубик рубика', 'category_name': 'игрушка'}, 
#     {'product_name': 'монитор HP', 'category_name': 'монитор'},
#     {'product_name': 'монитор asus', 'category_name': 'монитор'},
#     {'product_name': 'ежедневник', 'category_name': 'блокноты'},
#     {'product_name': 'ежедневник', 'category_name': 'канцтовары'}
#     {'product_name': 'энергетик redbull', 'category_name': None}
# ])

# print(products.show())
# print(categories.show())
print(multirow.show())
