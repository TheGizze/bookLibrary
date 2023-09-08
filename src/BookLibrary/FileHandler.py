class FileHandler:

    def __init__(self, data_source):
        self.data_source = data_source

    def read_data(self):
        try:
            with open(self.data_source, 'r') as file:
                data = file.read().splitlines()
            return data
        except FileNotFoundError:
            print("\n" + self. data_source + " not found!\n" + self. data_source +
                  " file will be created once you add your first book!")
            return []


    def write_data(self, data_set):
        with open(self.data_source, 'w') as file:
            for data in data_set:
                file.write("%s\n" % data)
