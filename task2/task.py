from pyspark.sql import SparkSession
import pyspark.sql.functions as F
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
    {'category_name': 'кошка', 'product_name': ['кот подсолнух']},
    {'category_name':'игрушка', 'product_name': ['кот подсолнух', 'кубик рубика']},
    {'category_name':'мониторы', 'product_name': ['монитор hp', 'монитор asus']},
    {'category_name':'блокноты', 'product_name': ['ежедневник']},
    {'category_name':'канцтовары', 'product_name': ['ежедневник']}
])


multirows = relations.select(relations.category_name, F.explode_outer(relations.product_name))
compare_1 = multirows.drop('category_name')
uncategorized = products.subtract(compare_1)
uncategorized = uncategorized.withColumn("category_name", F.lit(None))
result = multirows.union(uncategorized)

result.show()
