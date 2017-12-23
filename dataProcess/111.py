from pyspark import SparkContext
from pyspark.sql import HiveContext

from pyspark.sql import SparkSession


# sc = SparkContext(master='spark://192.168.10.140:7077', appName='LGM Test')
# hiveCtx = HiveContext(sc)
# HiveContext.sql('show tables').show()
spark=SparkSession \
.builder \
.enableHiveSupport() \
.appName("LGM") \
.master("spark://ylymaster:7077") \
.config("spark.cores.max",1) \
.getOrCreate()

spark.sql('show tables').show()