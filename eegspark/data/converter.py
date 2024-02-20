from pyspark import SparkContext
from fetcher import Source  # 确保 fetcher.py 在相同的目录或PYTHONPATH中

class Converter:
    def __init__(self, spark_context: SparkContext):
        """
        Initialize the Converter with a SparkContext.

        Parameters:
        - spark_context (SparkContext): The SparkContext to be used for RDD operations.
        """
        self.spark_context = spark_context

    def convert_mat_to_rdd(self, file_path: str):
        """
        Convert a .mat file data to an RDD. Each RDD element is a tuple with a time identifier and channel data.
        
        Parameters:
        - file_path (str): Path to the .mat file.

        Returns:
        - RDD: An RDD representation of the .mat file data where each element is a tuple (time identifier, channel data).
        """
        # Create Source instance and load data
        source = Source(file_path)
        loaded_data = source.load_data()
        
        # Check if 'data' is loaded
        if 'data' not in loaded_data:
            raise ValueError("No 'data' key found in loaded .mat file.")
        
        # Extract the time identifiers and channel data
        # Assuming first column is time and the rest are channel data
        time_channel_rdd = self.spark_context.parallelize(loaded_data['data']).map(
            lambda row: (row[0], row[1:])  # (time_identifier, channel_data)
        )
        return time_channel_rdd
