#RMI server
import Pyro4


@Pyro4.expose
class RMI_Server(object):
    def __init__(self):
        self.file_to_execute_path = "serverFiles/"
        self.filename_to_execute = ""
        self.is_compilable = False
        self.file_to_execute = 0
        self.execution_file_source_code_in_array = []

    def receive_source_code(self, filename, file_in_array):
        self.filename_to_execute = self.file_to_execute_path
        self.filename_to_execute += filename
        self.execution_file_source_code_in_array = file_in_array
        try:
            self.file_to_execute = open(self.filename_to_execute, 'w+')
            for item in self.execution_file_source_code_in_array:
                self.file_to_execute.write("%s" % item)

            self.file_to_execute.close()
        except Exception as e:
            print(e)

    def is_file_compilable(self): #To do
        self.is_compilable = True
        return self.is_compilable


daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(RMI_Server)   # register the greeting maker as a Pyro object
ns.register("My_RMI_Server", uri)   # register the object with a name in the name server
print("Server is ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls
