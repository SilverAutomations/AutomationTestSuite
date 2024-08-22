import json


class JSONHandler:
    """
    Class for handling JSON data.
    """

    def __init__(self, file_path):
        """
        Initializes the JSONHandler with the specified file path.

        Args:
            file_path (str): Path to the JSON file.
        """
        self.file_path = file_path
        self.data = {}

    def load(self):
        """
        Loads JSON data from the file into memory.

        Returns:
            dict: Loaded JSON data as a Python dictionary.
        """
        try:
            with open(self.file_path, 'r') as f:
                self.data = json.load(f)
            return self.data
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in '{self.file_path}'.")
            return {}

    def write(self, data):
        """
        Writes the given data to the JSON file.

        Args:
            data (dict): Data to be written to the file.
        """
        try:
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError:
            print(f"Error: Could not write to file '{self.file_path}'.")

    def get_data(self):
        """
        Returns the currently loaded JSON data.

        Returns:
            dict: Loaded JSON data.
        """
        return self.data

    def set_data(self, data):
        """
        Sets the JSON data to be written to the file.

        Args:
            data (dict): Data to be set.
        """
        self.data = data

    def update_data(self, key, value):
        """
        Updates a value in the JSON data.

        Args:
            key (str): Key of the value to update.
            value (any): New value for the key.
        """
        self.data[key] = value

    def delete_data(self, key):
        """
        Deletes a key-value pair from the JSON data.

        Args:
            key (str): Key to be deleted.
        """
        if key in self.data:
            del self.data[key]

# # Example usage
# json_handler = JSONHandler('data.json')
# data = json_handler.load()  # Load existing data (if any)
#
# # Modify data
# data['name'] = 'Alice'
# data['age'] = 30
#
# # Write data back to file
# json_handler.write(data)
#
# # Access data
# print(json_handler.get_data())
