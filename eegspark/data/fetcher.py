import scipy.io as sio

class Source:
    """
    Class for loading data from .mat files.
    """

    def __init__(self, file_path: str) -> None:
        """
        Initialize the Source object with the file path.
        
        Parameters:
        - file_path (str): Path to the .mat file containing the data.
        """
        self.file_path = file_path

    def load_data(self) -> dict:
        """
        Load EEG data from a .mat file.

        Returns:
        - dict: A dictionary containing the 'data' array loaded from the .mat file.
        """
        try:
            data = sio.loadmat(self.file_path)
            return {'data': data['data']} if 'data' in data else {}

        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except sio.matlab.miobase.MatReadError as e:
            print(f"MAT file read error: {e}")
        except Exception as e:
            print(f"Error occurred while loading EEG data: {e}")

        return {}

# Usage example:
# if __name__ == "__main__":
#     file_path = 'path_to_your_file.mat'
#     source = Source(file_path)
#     data = source.load_data()
#     print(data)  # or perform further processing
