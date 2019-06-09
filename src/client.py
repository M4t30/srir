#RMI client
import Pyro4
import os


# Keep presets

class Client:
    def __init__(self):
        self.filename_to_execute = ""
        self.file_to_execute = 0
        self.is_file_exists = False
        self.filepath = "clientFiles/"
        self.is_compilable = False
        self.execution_file_source_code_in_array = []
        self.server_connection = Pyro4.Proxy("PYRONAME:My_RMI_Server")    # use name server object lookup uri shortcut

    def create_filename_to_execute(self):
        print("Enter filename you want to execute:")
        self.filename_to_execute = input()
        self.filename_to_execute += ".py"

    def read_file_to_array(self):
            self.execution_file_source_code_in_array.clear()
            self.is_file_exists = os.path.isfile(self.filepath + self.filename_to_execute)
            if self.is_file_exists:
                try:
                    self.file_to_execute = open(self.filepath + self.filename_to_execute)
                    for line in self.file_to_execute:
                        self.execution_file_source_code_in_array.append(line)

                    self.file_to_execute.close()
                except Exception as e:
                    print(e)

            else:
                print("Plik nie istnieje")


    def send_file_to_server(self):
        self.read_file_to_array()
        if (self.is_file_exists):
            self.server_connection.receive_source_code(self.filename_to_execute, self.execution_file_source_code_in_array)
            print("File was uploaded to server")


client = Client()

infinite_loop = 1
while infinite_loop != 0:
    print("Type 1 and press Enter to continue")
    print("Type 0 and press Enter to exit")
    infinite_loop = input()
    if infinite_loop == '0':
        break

    if (infinite_loop == '1'):
        client.create_filename_to_execute()
        client.send_file_to_server()
        #client.is_compilable = client.server_connection.is_file_compilable()
