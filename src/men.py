import os
import json
import time
import quo
from quo import clear, echo, print
from quo.color.rgb import aquamarine
from quo.keys import bind
from quo.prompt import Prompt
from quo.text import Text
from .out import *
from .system import *

red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
violate="\033[1;37m"
nc="\033[00m"

class Main:
  def install_tools(self):
    while True:
      tool=tools()
      num=1
      total=len(tool.names)
      clear()
      logo.install_tools()
      print(f" ")
      for tool_name in tool.names:
        echo(f"[", fg="vyellow", bold=True, nl=False)
        echo(f"{num} ", fg="vmagenta", italic=True, nl=False)
        echo(f"]", fg="vyellow", bold=True, nl=False)
        echo(f" Install ", nl=False)
        echo(f"{tool_name}", fg=aquamarine, bold=True)
        num+=1
      echo(f"")
      logo.back()
      echo(f"sshy", fg="vblue", italic=True, bold=True, nl=False)
      echo(f">>>", fg="cyan", bold=True, italic=True)

      #def main():
     #     history = quo.history.InMemoryHistory()
     #     history.append_string("import os")
     #     history.append_string('print("hello")')
     #     history.append_string('print("world")')

      session = Prompt(bottom_toolbar=Text(' <b>List of</b> <u>all</u> <style bg="red">tools</style>'), placeholder=Text('<gray>(please type something)</gray>'))
                  #history=history, auto_suggest=quo.completion.AutoSuggestFromHistory(), enable_history_search=True)
        #  while True:
        #      try:
      cmd = session.prompt(" ")
    #except KeyboardInterrupt:
      #            pass  # Ctrl-C pressed. Try again.
      #        else:
      #            break

      if cmd=="00" or cmd=="back":
          self.menu()
          break
      else:
        try:
            if int(cmd)>=1 and int(cmd)<=int(total):
                clear()
                logo.installing()
                print("<green>Installing...</green>")
                tool.install(tool.names[int(cmd)-1])
            else:
                echo(f"Sorry, '{cmd}', is an invalid input !!", fg="black", bg="red")
                sleep(1)
        except ValueError:
            echo(f"Error:",fg="black", bg="vred", nl=False)
            echo(f" {cmd}", nl=False, fg="yellow")
            echo(f" is an invalid input!!", fg="red")
            time.sleep(1)
  def category(self):
    while True:
      tool=tools()
      total=len(tool.category)
      num=1
      clear()
      logo.tool_header()
      print("")
      for cat in tool.category:
        echo(f"[", fg="yellow", nl=False, bold=True)
        echo(f" {num} ", fg="magenta", nl=False, italic=True)
        echo(f"]", fg="yellow", bold=True, nl=False)
        echo(f" {tool.category_data[cat]}", fg="vblue", bold=True)
        num+=1
      echo("")
      logo.back()
      session = Prompt(bottom_toolbar=Text(' <b>List of</b> <u>all</u> tools in <style bg="red">categories</style>'), placeholder=Text('<gray>(please type something)</gray>'))
      cmd = session.prompt("")

   
      if cmd=="00" or cmd=="back":
        self.menu()
        break
      else:
        try:
          if int(cmd) in range(1,int(total)+1):
            while True:
              print(int(cmd)-1)
              print(tool.category[int(cmd)-1])
              cnt=1
              clear()
              logo.tool_header()
              print(f"")
              tmp_cat_tool=[]
              for i in tool.names:
                if tool.category[int(cmd)-1] in tool.data[i]["category"]:
                  tmp_cat_tool.append(tool.data[i]['name'])
                  print(f" {green}[ {violate}{cnt} {green}] {yellow}Install {green}{tool.data[i]['name']}{nc}")
                  cnt+=1
              print(f"")
              logo.back()

              session =  Prompt(bottom_toolbar=Text(' <b>List of</b> <u>all</u> tools in <style bg="red">categories</style>'), placeholder=Text('<gray>(please type something)</gray>'))
              tcmd = session.prompt("$")

             # tcmd=inputc}@{blue}space {yellow}$ {nc}")
              if tcmd=="00" or tcmd=="back":
                break
              else:
                try:
                  cat_total=len(tmp_cat_tool)
                  if int(tcmd) in range(1,int(cat_total)+1):
                    clear()
                    logo.installing()
                    print(f"{green}Installing ....{nc}")
                    tool.install(tmp_cat_tool[int(tcmd)-1])
                  else:
                    print(f"\007{red}Sorry,{violate} '{tcmd}' {blue}: {red}invalid input !!{nc}")
                    time.sleep(1)
                except ValueError:
                  print(f"\007{red}Sorry,{violate} '{tcmd}' {blue}: {red}invalid input !!{nc}")
                  time.sleep(1)
          else:
            print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!{nc}")
            time.sleep(1)
        except ValueError:
          print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!{nc}")
          time.sleep(1)
  #######################

 # def category(self):
   # while True:
  #    tool=tools()
   #   total=len(tool.category)
   #   num=1
    #  quo.clear()
      #logo.tool_header()
      #print(f"")
     # for cat in tool.category:
      #  quo.echo(f"[", fg="vyellow", nl=False, bold=True)
      #  time.sleep(0.02)
     #   quo.echo(f"{num}", fg="vmagenta", italic=True, bold=True, nl=False)
     #   time.sleep(0.02)
      #  quo.echo(f" ]", fg="vyellow", nl=False, bold=True)
     #   time.sleep(0.02)
    #    quo.echo(f" {tool.category_data[cat]}", fg=aquamarine, bold=True)
    #    num+=1
  #    quo.echo(f"")
  #    logo.back()
  #    quo.echo(f"sshy ", fg="vgreen",


  def update(self):
    while True:
      clear()
      logo.update()
      echo(f"sshy", fg="vblue", nl=False, italic=True, bold=True)
      quo.echo(f">>>", fg="cyan", italic=True, bold=True)
      session = Prompt(bottom_toolbar=Text(' <b>Check/Download</b> <u>new</u>  <style bg="red">updates</style>'), placeholder=Text('<style color="#888888">(please type something)</style>'))

      cmd= session.prompt("")
      if cmd=="1":
        system=sys()
        if system.connection():
          clear()
          logo.updating()
          if system.sudo != None:
            if os.path.exists(system.home+"/sashay"):
              pass
            else:
              os.system(system.sudo+" git clone https://github.com/secretum-inc.git "+system.home+"/sashay")
            if os.path.exists(system.home+"/sashay/install.sshy"):
              os.system("cd "+system.home+"/sashay;"+system.sudo+" ./install.sshy")
              if os.path.exists(system.bin+"/sashay") and os.path.exists(system.conf_dir+"/sashay"):
                clear()
                logo.updated()
                cmd=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")
              else:
                clear()
                logo.update_error()
                cmd=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")
            else:
              quo.clear()
              logo.update_error()
              cmd=input(f"{blue}sshy@{blue}space {yellow}$ {nc}")
          else:
            if os.path.exists(system.home+"/sashay"):
              pass
            else:
              os.system("git clone https://github.com/secretum-inc/sashay.git "+system.home+"/sashay")
            if os.path.exists(system.home+"/sashay/install.sshy"):
              os.system("cd "+system.home+"/sashay;./install.sshy")
              if os.path.exists(system.bin+"/sashay") and os.path.exists(system.conf_dir+"/sashay"):
                clear()
                logo.updated()
                cmd=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")
              else:
                clear()
                logo.update_error()
                cmd=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")
            else:
              clear()
              logo.update_error()
              cmd=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")
        else:
          clear()
          logo.nonet()
          tmp=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")
      elif cmd=="0" or cmd=="back":
        self.menu()
        break
      else:
        echo(f"Invalid input !!", fg="vred")
        time.sleep(1)
      if cmd == "0" or cmd =="back":
          self.menu()
          break
      else:
          echo(f"")

  def about(self):
    while True:
      tool=tools()
      total=len(tool.names)
      clear()
      logo.about(total)
      session = Prompt(bottom_toolbar=Text(' <b>About <red>Sashay</red></b>'), placeholder=Text('<gray>(please type something)</gray>'))
      cmd = session.prompt("sshy@space $ ")
    #  cmd=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")
      self.menu()
      break

  @classmethod
  def menu(self):
    while True:
      tool=tools()
      total=len(tool.names)
      quo.clear()
      logo.menu(total)

      session = Prompt(bottom_toolbar=Text('<b>Main</b>  <style bg="red">menu</style>'), placeholder=Text('<style color="#888888">(please type something)</style>'))
      cmd = session.prompt("")
      if cmd == "1":
        self.install_tools(self)
        break
      elif cmd == "2":
        self.category(self)
        break
      elif cmd == "3":
        self.update(self)
        break
      elif cmd == "4":
        self.about(self)
        break
      elif cmd=="x" or cmd=="X" or cmd=="exit":
        clear()
        logo.exit()
        break
      elif cmd=="rm -sashay" or cmd=="rm -sshy" or cmd=="uninstall sashay" or cmd=="unistall sshy":
        system=sys()
        if system.sudo:
          os.system(system.sudo+" rm -rf "+system.bin+"/sashay")
          os.system(system.sudo+" rm -rf "+system.bin+"/sshy")
          os.system(system.sudo+" rm -rf "+system.conf_dir+"/sashay")
        else:
          os.system("rm -rf "+system.bin+"/sashay")
          os.system("rm -rf "+system.bin+"/sshy")
          os.system("rm -rf "+system.conf_dir+"/sashay")
        clear()
        logo.exit()
        break
      else:
        print(Text(f"<style fg='black' bg='red'><b>Sorry, '{cmd}' is an invalid input !!</b></style>"))
        time.sleep(1)

class tools:
  data=None
  names=None
  category=None
  category_data=None
  def __init__(self):
    system=sys()
    with open(system.conf_dir+"/sashay/assets/data.json") as data_file:
      self.data=json.load(data_file)
    with open(system.conf_dir+"/sashay/assets/cat.json") as cat_file:
      self.category_data=json.load(cat_file)
    self.names=list(self.data.keys())
    self.category=list(self.category_data.keys())

  def install(self,name):
    package_name=self.data[name]["package_name"]
    package_manager=self.data[name]["package_manager"]
    url=self.data[name]["url"]
    req=list(self.data[name]["dependency"])
    system=sys()

    if system.connection():
      if len(req)!=0 and req[0]!=None:
        for dep in req:
          if os.path.exists(system.bin+"/"+dep):
            pass
          else:
            if system.sudo != None:
              os.system(system.sudo+" "+system.pac+" install "+dep+" -y")
            else:
              os.system(system.pac+" install "+dep+" -y")

      if package_manager=="package_manager":
        if os.path.exists(system.bin+"/"+package_name):
          clear()
          logo.already_installed(name)
          tmp=input(f"sshy@space $ ")
        else:
          if system.sudo != None:
            os.system(system.sudo+" "+system.pac+" install "+package_name+" -y")
          else:
            os.system(system.pac+" install "+package_name+" -y")
          # check tool is installed or not
          if os.path.exists(system.bin+"/"+package_name):
            clear()
            logo.installed(name)
            tmp=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")
          else:
            clear()
            logo.not_installed(name)
            tmp=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")

      elif package_manager=="git":
        if os.path.exists(system.home+"/"+package_name):
          clear()
          logo.already_installed(name)
          tmp=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")
        else:
          if system.sudo != None:
            os.system(system.sudo+" git clone "+url+" "+system.home+"/"+package_name)
          else:
            os.system("git clone "+url+" "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            clear()
            logo.installed(name)
            tmp=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")
          else:
            clear()
            logo.not_installed(name)
            tmp=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")

      elif package_manager=="wget":
        if os.path.exists(system.home+"/"+package_name):
          clear()
          logo.already_installed(name)
          tmp=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")
        else:
          if system.sudo != None:
            os.system(system.sudo+" wget "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("wget "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            clear()
            logo.installed(name)
            tmp=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")
          else:
            clear()
            logo.not_installed(name)
            tmp=input(f"{blue}sshy{nc}@{blue}space {yellow}$ {nc}")

      elif package_manager=="curl":
        if os.path.exists(system.home+"/"+package_name):
          clear()
          logo.already_installed(name)
          tmp=input(f"sshy@space $")
        else:
          if system.sudo != None:
            os.system(system.sudo+" curl "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("curl "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            clear()
            logo.installed(name)
            tmp=input(f"sshy@space $")
          else:
            clear()
            logo.not_installed(name)
            tmp=input(f"sshy@space $")
    else:
      clear()
      logo.nonet()
      tmp=input(f"sshy@space $")
