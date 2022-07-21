To configure the program you should execute the following command on the configure folder:

sudo chmod +x configure.sh

This command will give the permission to execute the configure program.
Now you need to execute the configure file(configure.sh) you can execute it with the following command:

./configure.sh

It will ask you some questions and after you answer all the questions you should change the line that has a variable like this:

func_regex = re.compile(r"function\([^)]+\)")

To a variable like this:

func_regex = re.compile(r"function\([^)]?\)")

*It's probably on line 152

You can find the parser.py with the following command:

sudo find / -name parser.py | grep pytube

And the configuration folder is on the root directory(/)

------------------------------------------------------------------------------------------------------------------------

If you want to execute the program manually, you can go the ./program/ folder and execute the following command:

python3 yt_downloader_current_icon.py

and if you want to see the source code, you can open the yt_downloader_current_icon.py file or the yt_downloader_root_icon.py file
