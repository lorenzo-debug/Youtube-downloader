#!/bin/bash

echo -e "Everything that you don't have is going to be installed\n"

echo -n "Do you have python3.8 installed?[y/n]"
read pyi
echo -n "Do you have pip 20.0.2 installed?[y/n]"
read pipins

if [ $pyi = "y" ] || [ $pyi = "Y" ]; then
    if [ $pipins = "y" ] || [ $pipins = "Y" ]; then
        sudo pip3 install -r requirements.txt
        sudo apt-get install python3-tk
        python3 -m pip install --upgrade pytube
    elif [ $pipins = "n" ] || [ $pipins = "N" ]; then
        sudo apt install python3-pip
        echo "Pip installed!"
        sudo pip3 install -r requirements.txt
        sudo apt-get install python3-tk
        python3 -m pip install --upgrade pytube
    fi
    echo "Everything is installed!"
elif [ $pyi = "n" ] || [ $pyi = "N" ]; then
    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.8
    echo "Python3.8 installed!"
    sudo apt install python3-pip
    sudo pip3 install -r requirements.txt
    sudo apt-get install python3-tk
    python3 -m pip install --upgrade pytube
fi
clear
echo "Everything is installed!"

echo -n "Would you like to create a desktop shortcut for the program?[y/n]"
read ds

if [ $ds = "y" ] || [ $ds = "Y" ]; then
    echo -n "Would you like to create a desktop shortcut automatically or manually?[a/m]"
    read aorm

    if [ $aorm = "a" ] || [ $aorm = "A" ]; then
        mkdir yt_downloader
        sudo mv yt_downloader / 
        cp -r ../program/icons/ /yt_downloader
        ex="#!/bin/bash\n\npython3 /yt_downloader/yt_downloader_root_icon.py"
        echo -e $ex > execute.sh
        chmod +x execute.sh
        sudo mv execute.sh /yt_downloader 
        cp ../program/yt_downloader_root_icon.py /yt_downloader
        dsfl="[Desktop Entry]\nName=Youtube Downloader\nComment=Download videos from youtube\nExec=/yt_downloader/execute.sh\nIcon=/yt_downloader/icons/yt-image-small.png\nTerminal=false\nType=Application\nCategories=Game;"
        echo -e $dsfl > yt-downloader.desktop
        sudo mv yt-downloader.desktop /yt_downloader
        cp /yt_downloader/yt-downloader.desktop ~/Desktop
    elif [ $aorm = "m" ] || [ $aorm = "M" ]; then
        echo -n "What is your linux distribution?[Ubuntu/Debian/Arch Linux/Fedora/OpenSUSE]"
        read lds

        if [ $lds = "Ubuntu" ]; then
            sudo apt install alacarte
            sudo alacarte
            elif [ $lds = "Debian" ]; then
                sudo apt-get install alacarte
                sudo alacarte
            elif [ $lds = "Arch Linux" ]; then
                sudo pacman -S alacarte
                sudo alacarte
            elif [ $lds = "Fedora" ]; then
                sudo dnf install alacarte -y
                sudo alacarte
            elif [ $lds = "OpenSUSE" ]; then
                sudo zypper install alacarte
                sudo alacarte
        fi
    fi
fi
clear