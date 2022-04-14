VERSION = "2.0"

def main():
    try:
        from os import system, mkdir
        import os.path

        # STEP ONE save directory for the Shell Script Files
        print("Welcome to Bash Command Alias Editor v" + VERSION + " by Jonas_Jones")
        print("\n1. Set the script directory (leave blank for default):")
        save_directory = input("~/")
        if save_directory == "":
            save_directory = os.path.expanduser("~") + "/.sh"
        else:
            save_directory = os.path.expanduser("") + "/" + save_directory
        print("Directory set to " + save_directory)

        try:
            if not os.path.exists(save_directory):
                os.mkdir(save_directory)
                print("uwu")
        except:
            print("Something went wrong while creating the directory.")
            exit()

        # STEP TWO command alias name
        print("\n2. Choose the name for the command alias:")
        command_alias = input(save_directory + "/")
        print("Command Alias script for '" + command_alias + "' is saved at '" + save_directory + "/" + command_alias)

        # STEP THREE commands to be executed
        print("\n3. Type the command(s) you wish to be executed upn running the alias. Press Enter for new lines, press enter on empty line to quit the editor.")
        command = None
        print(save_directory + "/" + command_alias + ".sh")

        command_alias_file = open(save_directory + "/" + command_alias + ".sh", 'w')

        command_alias_file.write("#! /usr/bin/sh\n")

        while command != "":
            command = input(">> ")
            command_alias_file.write(command + "\n")
        command_alias_file.close()

        # STEP FOUR Apply alias to shell
        print("\n4. Applying alias to the shell.")
        try:
            bashrc = open(os.path.expanduser('~') + "/.bashrc", "a")
            bashrc.write("\nalias " + command_alias + "='" + save_directory + "/" + command_alias + ".sh'")
            bashrc.close()
        except:
            print("ERROR: Couldn't open the bashrc file. Are you using the Bash shell? Is the file missing or requires higher permission levels?")
            exit()
        system("./.temp.sh")
        system("chmod u+x " + save_directory + "/" + command_alias + ".sh")
        system("rm .temp.sh")
        print("Execute the command 'source ~/.bashrc' in the terminal to complete the final step.")



    except:
        print("Something went wrong. Please make sure that all dependencies are installed.")



if __name__ == "__main__":
    main()