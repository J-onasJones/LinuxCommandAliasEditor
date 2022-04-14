# BashCommandAliasEditor
This program helps you to create and edit command aliases on Linux and MacOS (with the Bash Shell)

# How to use
### Windows and Linux
1. Download the executable for your OS (clearly labeled) and execute it.

### MacOS (manually) and Windows and Linux (alternative to above)
1. Download the most recent verson of the python file
2. Open a terminal and locate your Download directory ( if Downloaded in the default downlaods folder type: 'cd ~/Downloads'
3. type 'python3 --version' to check if python is installed (install python3 if not already installed)
4. Install all Dependencies. os: `pip3 install os` (install pip3 if not already installed)
5. type 'python3 [name_of_python-file] (example: 'python3 command_alias-editor_v1.0'
6. The program should be executed. Follow all further instructions shown in the terminal
7. Dont forget to execute 'source ~/.bashrc' at the end.

### Why do I have to manualy execute 'source ~/.bashrc'?
The reason that this can't be done by the program itself is that it wouldn't be applied to the main shell but only for the runtime of the program itself. After the program exits, all changes will be reverted. 

This problem could technically be solved by using subprocesses but ffs I'm not in the mood for doing that. It's some work which I don't wanna do