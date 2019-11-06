class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def update_file(self, text_data):
        self.file_name += text_data

    def read_file(self):
        return self.file_name
		#-------cw8--------------