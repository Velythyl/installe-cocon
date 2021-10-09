apts:
	sudo apt-get update && sudo apt-get upgrade
	sudo apt-get install build-essential python-dev python3-dev python3-pip neovim wget curl zsh bat -y

pips:
	sudo pip3 install pywal
	pip3 install tqdm numpy lit-review

varied:
	cd /tmp && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && sudo apt install ./google-chrome-stable_current_amd64.deb
	
manual:
	./manual_install.py spotify discord intellij-toolbox pycharm intellij
