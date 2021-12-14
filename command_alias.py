import os, random

print("[Thread/Info] Create command alias")
print("[Thread/Info] Set save directory for sh-file (press enter for default directory '~/.sh/):")
save_directory = input("~/")

if save_directory == "":
    save_directory = ".sh"
    print("[Thread/Info] No directory set, proceeding with default directory: '~/.sh/'")
else:
    print("[Thread/Info] Set directory to '~/" + save_directory + "'")

print("[Thread/Info] Attempting to create new directory '~/" + save_directory + "'. Ignoring if already exists.")
os.system("mkdir ~/" + save_directory)

print("[Thread/Info] Set the command name:")
command_alias = input("~/" + save_directory + "/")

if command_alias == "":
    command_alias = "command_alias-" + str(random.randint(100, 999))
    print("[Thread/Info] No command alias set, proceeding with: '" + command_alias + "'")
else:
    print("[Thread/Info] Set command alias to '" + command_alias + "'")

print("[Thread/Info] Creating new file '" + command_alias + ".sh' in directory '~/" + save_directory + "'")
os.system("touch ~/" + save_directory + "/" + command_alias + ".sh")

print("touch ~/" + save_directory + "/" + command_alias + ".sh")
print("~/" + save_directory + "/" + command_alias + ".sh", "w")

print("[Thread/Info] Formating file for shell script use.")
print("[Thread/Info] File location: " + os.path.expanduser('~') + "/" + save_directory + "/" + command_alias + ".sh")
command_alias_file = open(os.path.expanduser('~') + "/" + save_directory + "/" + command_alias + ".sh", "w")
command_alias_file.write("#! /usr/bin/sh\n")

print("[Thread/Info] Insert new command. Press enter to proceed to next line. Press enter on blank input to exit editor.")

command_input = input(">>")
command_alias_file.write(command_input + "\n")

while command_input != "":
    command_input = input(">>")
    command_alias_file.write(command_input + "\n")
    print(command_input)
command_alias_file.close()

print("[Thread/Info] File editor closed. Applying command alias to system")
bashrc = open(os.path.expanduser('~') + "/.bashrc", "a")
bashrc.write("\nalias " + command_alias + "='~/" + save_directory + "/" + command_alias + ".sh'")
bashrc.close()
print("[Thread/Info] bashrc file editing successful.")
print("[Thread/Info] EXECUTE COMMAND 'source ~/.bashrc' OR RESTART YOUR DEVICE IN ORDER FOR THE ALIAS TO BE APPLIED!")