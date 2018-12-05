# BoringStuff
My **python** scripts to ease my life.

## Set up
### Configuration
Copy file BoringStuff.ini from root of the project to the user HOME directory.

### Python 
Python should be installed and configured. 

### Running Scripts from Command Line.
Directory ./script should be added on the system Path. Now I support only Windows like bat files. 
If you want to check if everything works fine, just type in command line.
Run command

hello

to ensure that scrips can be run from CMD. 
  

### Documentation notes
Each folder contains readme file for description of available scripts

### Dependencies:


#### Selenium

 **- geckodriver for Selenium**
 
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.

First of all you will need to download latest executable geckodriver from 
https://github.com/mozilla/geckodriver/releases
to run latest firefox using selenium

Actually The Selenium client bindings tries to locate the geckodriver executable from the system PATH. You will need to add the directory containing the executable to the system path.

On Unix systems you can do the following to append it to your system’s search path, if you’re using a bash-compatible shell:

export PATH=$PATH:/path/to/directory/of/executable/downloaded/in/previous/step
On Windows you will need to update the Path system variable to add the full directory path to the executable geckodriver manually or command line(don't forget to restart your system after adding executable geckodriver into system PATH to take effect). The principle is the same as on Unix.