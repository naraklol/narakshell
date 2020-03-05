import os

class Command:

    def __init__(self):
        self.command_string = ""
        self.program = ""
        self.arguments = []

        self.input_redirection = False
        self.output_redirection = False
        self.input_file = ""
        self.output_file = ""

    def parse_command(self, string):

        # set the command string and split based on spaces
        self.command_string = string
        self.arguments = self.command_string.split()

        # extract the first element as the program name
        self.program = self.arguments[0]

def print_error(error):
    print(error)
    exit()


def main():

    print("Welcome to narakshell (narak shell or naraks hell)\n")

    while True:
        command = Command()
        command.parse_command(input("narakshell$ "))

        # check for change directory command
        if(command.program == "cd"):

            try:
                os.chdir(command.command_string.split(' ', 1)[1])
            except:
                print_error("cd: Invalid path provided")

            # get new command after changing directory
            continue

        # fork to execute command
        pid = os.fork()

        # child process (command executed here)
        if pid == 0:

            try:
                os.execvp(command.program, command.arguments)
            except FileNotFoundError:
                print_error("Error: command not found")

        # parent process
        elif pid > 0:
            finish = os.waitpid(0, 0)


        else:
            print("Error in forking. Exiting now.")
            exit()


main()
