#This file is part of sashay and may be subject to redistribution and commercial restrictions. Please visit our website
#for more information on licensing and terms of use.
#
#
import spinher
import quo
with spinher.whirl():
  quo.secho(f'CREATED BY GERRISHON SIRERE', fg='black', bg='cyan')

class logo:
  @classmethod
  def tool_header(self):
    print('''\007

\033[1;33m                                                                                                            
                         888                       
                         888                      
     .oooo.o    .oooo.o  888888bo.   ooo    ooo
    d88(  "8   d88(  "8 o888888888b  `88.  .8'
   `"Y88b.    `"Y88b.    888    888    `88..8'
   o.  )88b   o.  )88b   888    888     `888'
   8""888P'   8""888P'  o888o  o888o    "888" 
                                         d8'
                                    .o...P' 




\033[1;36m $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\033[1;m
\033[1;33m |          INSTALL USEFUL TOOLS               |
\033[1;36m $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\033[00m''')

  @classmethod
  def tool_footer(self):
    quo.secho(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', fg='blue', bg='black') 


  @classmethod
  def not_ins(self):
    self.tool_header()
    print ('''
\033[1;31m  [ x ]  \033[1;31mSashay can't be installed at the moment.\033[1;m
\033[1;31m  [ x ]  \033[1;31mAn error occurred.\033[1;m
\033[1;31m  [ x ]  \033[1;31mPlease try again later.\033[1;m''')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header() 
    quo.secho(f'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.', fg='black', bg='white')
    quo.secho(Installing this tool means you agree with all terms', fg='black', bg='red') 
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    print ('''
\033[1;33m    [ ✓ ] \033[1;32msashay is installed successfully.
\033[1;33m    [ ✓ ] \033[1;32mType sashay or sshy to run this tool from anywhere in your terminal.''')
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    print ('''
\033[1;33m  [ 1 ] \033[1;32mUpdate sashay.
\033[1;33m  [ 0 ] \033[1;32m<< Go Back.\033[00m''')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    print ('''
\033[1;33m      [ ✓ ] \033[1;32mCongratulations!! sashay has been updated successfully.
\033[1;33m      [ ✓ ] \033[1;32mPress Enter to continue.\033[00m''')
    self.tool_footer()

  @classmethod
  def nonet(self):
    self.tool_header()
    print ('''
\033[1;31m  [ x ]  \033[1;31mNo network connectivity.\033[1;m
\033[1;31m  [ x ]  \033[1;31mPlease try again after some time.\033[00m''')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    print ('''
\033[1;31m  [ x ]  \033[1;33msshy can't be updated at this time.\033[1;m
\033[1;31m  [ x ]  \033[1;31mPlease try again later.\033[00m''')
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    quo.secho(f'[✓] sashay', fg='byellow', bg='black')
    quo.secho(f'[✓] By Gerrishon Sirere(viewerdiscretion)', fg='black', bg='blue')
    quo.secho(f'[✓] With great power comes great responsibility', fg='black', bg='cyan')
    quo.secho(f'[✓] 360+ tools', fg='red', bg='black')
    quo.secho(f'[✓] Made for Linux based systems', fg='byellow', bg='black') 

    self.tool_footer()


  @classmethod
  def install_tools(self):
    quo.secho(f'#############################################', fg='black', bg='cyan')
    quo.secho(f'//////////////SELECT YOUR TOOL///////////////', fg='red', bg='white') 
    quo.secho(f'#############################################', fg='black', bg='cyan')

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;32mSorry ??
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m is already Installed !!
''')
    self.tool_footer()

  @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;32mInstalled successfully !!
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m has been installed Successfully! 
''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;31mSorry ??
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;31m has not been installed! 
''')
    self.tool_footer()

  @classmethod
  def back(self):
    quo.secho(f'#############################################', fg='black', bg='cyan')
    quo.secho(f'00) Go back', fg='yellow', bg='black') 
    quo.secho(f'#############################################', fg='black', bg='cyan')

  @classmethod
  def updating(self):
    quo.secho(f'#############################################', fg='black', bg='cyan')
    quo.secho(f'//////////////////UPDATING///////////////////', fg='red', bg='white') 
    quo.secho(f'#############################################', fg='black', bg='cyan')

  @classmethod
  def installing(self):
    quo.secho(f'#############################################', fg='black', bg='cyan')
    quo.secho(f'/////////////////INSTALLING//////////////////', fg='red', bg='white') 
    quo.secho(f'#############################################', fg='black', bg='cyan')

  @classmethod
  def menu(self,total):
    self.tool_header()
    quo.secho(f'[ 1 ] Show all tools', bg='cyan', fg='white')
    quo.secho(f'[ 2 ] Show all categories', bg='white', fg='cyan')
    quo.secho(f'[ 3 ] Update sashay', fg='byellow', bg='black')
    quo.secho(f'[ 4 ] About us', fg='black', bg='byellow')
    quo.secho(f'[ x ] Exit sashay, fg='white', bg='black')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    quo.secho(f'We hope to see you back soon', fg='black', bg='red')
    quo.secho(f'Goodbye for now...', fg='white', bg='black') 
    self.tool_footer()
