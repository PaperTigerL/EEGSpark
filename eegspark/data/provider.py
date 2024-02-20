from eegspark.data.fetcher import Source
from converter import Converter
from pyspark import SparkContext, RDD

class RDDProvider:
    def __init__(self, spark_context: SparkContext):
        self.spark_context = spark_context
        self.converter = Converter(spark_context)

    def source_to_rdd(self, file_path: str) -> RDD:
        # 创建 Source 实例
        source = Source(file_path)
        # 使用 Converter 将数据从 Source 转换为 RDD
        rdd_data = self.converter.convert_mat_to_rdd(file_path)
        return rdd_data

# 这里我们已经假设 Converter 类中的 convert_mat_to_rdd 方法接受一个 file_path，
# 创建 Source，并在内部调用其 load_data 方法。

# Usage example:
# if __name__ == "__main__":
#     sc = SparkContext("local", "RDDProviderExample")
#     rdd_provider = RDDProvider(sc)
#     rdd_data = rdd_provider.source_to_rdd('path_to_your_file.mat')
#     print(rdd_data.collect())  # To print data for verification
