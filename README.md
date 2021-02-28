# Python Projects
Contains all sorts of projects. 
Coding for fun and to develop my own skills. 

### IntruderSnapper.py
Got the idea to commit to this file when i bought an external webcam. While running, checking if the screen turns to LoginUI. If yes, 
it checks for any security events added to the Windows Event Log. Events like these, while the LoginUI is up, may be failed login attempts. 
At detection of Security events, it snaps a picture of the possible intruder. Can be allowed to run in the background contiously with locking 
the screen multiple times without the need of restarting the program. 

Limitations: Must be run with Admin privileges (This is to gain access to Security log), requires installment of 'pywin32' and 'opencv-python' 

Downsides: Collects all security events, including successful logons. This might not be preferred, unless you really like photos of yourself. 

### FileAndFlag.py
In some flag challenges, flags are hidden as human readable strings in the file. With the suitable unix command 'strings', such a flag can easily be retrieved. However, on a Windows system, it's not always as easy to retrieve the strings. This python script provides information regarding any file, and if the file contains any string with the keywords (flag/FLAG/ctf etc..), or has a simple hidden steganography message, it reveals it. Script file takes the name of the file to be investigated as argument. 

### BrowserHistory.py
Retrieves browser history from Firefox and Chrome and enables a printing report of the 
found sites, i.e. how many URLs have been through trading sites, or social media. 
Other categories can be added for interest.

### Password generator.py
Using Tkinter, a secure password can be generated with a basic GUI. This is a simple service and is 
offered by multiple password managers and most modern web browsers when entering password. However, in some
cases, local passwords are also needed... Supports combination of letters (Lower- and uppercase), numbers and symbols. 
6-100 characters in length. 

### Steganography example.py
Also using Tkinter, a message can be encoded within an image. The following py-file allows for encoding and decoding. However,
as of now it may only produce encoded .png files. Although, this also means that it can encode jpg/jpeg/png files and save them to .png.
In addition, there's also the possibility of reading the messages. 

### Caesar cipher.py
Script for using substutitution encryption technique caesar cipher that shifts characters in a message. 
Allows for encoding of input with desired number of shifts. For decoding a message, prints all possible combinations incase the number of shifts is unknown. 

### Whatsup.py
By using Selenium i've created a small script that enables tagging/pinging a contact in a group chat on WhatsApp multiple times. 
My brother is sometimes hard to get in contact with where this script can be quite handy. 
Requires installment of Selenium and download of GeckoDriver. The location of the driver needs to be included in the system path.

### CryptoTable.py [Incomplete]
PyQT is another great GUI module for python. A bit better than Tkinter when it comes to creating a Table. This script calls for the CoinGecko API to retrieve
the Top 100 cryptocurrencies and details regarding them such as the current price, market cap and rank. An ideal addition would be to enable a notifier to if 
the value of a currency changes and to visualize market change through a period of time. 

### Minesweeper.py
Not an infosec oriented project. Used pygame to construct my own version of Minesweeper as a coding challenge. Intended to enable a start screen in which the 
number of tiles could be chosen as different difficulties. In addition, there's also room for increasing the number of mines spawned. Although, that would most likely conflict with user experience. 

![alt text](https://raw.githubusercontent.com/H4NM/PythonProjects/main/images/minesweeperpic.png)
