# chocolate
# @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
# make
# choco install make

MANAGE_FILE:=manage
SERVER_PORT:=80
ROOT_LINK:=https://raw.githubusercontent.com/huoquandace/test/main

.PHONY: push
push:
	git add .
	git commit -m up
	git push

.PHONY: all
all:
	python $(MANAGE_FILE).py makemigrations
	python $(MANAGE_FILE).py migrate
	python $(MANAGE_FILE).py shell -c "from django.contrib.auth import get_user_model; \
		get_user_model().objects.filter(username='admin').exists() or \
		get_user_model().objects.create_superuser('admin', 'admin@admin.com', 'admin')"
	python $(MANAGE_FILE).py runserver $(SERVER_PORT)

.PHONY: server
server:
	python $(MANAGE_FILE).py runserver $(SERVER_PORT)

.PHONY: admin
admin:
	python $(MANAGE_FILE).py shell -c "from django.contrib.auth import get_user_model; \
		get_user_model().objects.filter(username='admin').exists() or \
		get_user_model().objects.create_superuser('admin', 'admin@admin.com', 'admin')"

# Create new app
ifeq (app,$(firstword $(MAKECMDGOALS)))
  ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(ARGS):;@:)
endif
.PHONY: app
app:
	python manage.py startapp $(ARGS)

.PHONY: init
init:
	curl -s -o .gitignore $(ROOT_LINK)/.gitignore
	
.PHONY: rm
rm:
	rmdir __pycache__ /s /q
	rmdir apps /s /q
	rmdir emails /s /q
	rmdir locale /s /q
	rmdir static /s /q
	rmdir templates /s /q
	rmdir uploads /s /q
	del __init__.py
	del db.sqlite3
	del manage.py
	del requirements.txt