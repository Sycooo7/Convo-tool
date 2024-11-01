import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
import random
import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading

# Server handler for GET request
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"THEW MOZZ")

# Function to execute the server
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
        
# Clear the terminal based on OS
def cls():
    if system() == 'Linux' or system() == 'Darwin':
        os.system('clear')
    elif system() == 'Windows':
        os.system('cls')

# Constants for colors and formatting
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;31m'
RESET = '\033[0m'
BLUE = "\033[1;34m"
WHITE = "\033[1;37m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
GREEN = "\033[1;32m"
BOLD = '\033[1;1m'

# Function to display logo
def logo():
    clear = "\x1b[0m"
    colors = [31, 34, 36]

    x = """
 
          .         .                                                             
              ,8.       ,8.           ,o888888o.   8888888888',8888' 8888888888',8888' 
             ,888.     ,888.       . 8888     `88.        ,8',8888'         ,8',8888'  
            .`8888.   .`8888.     ,8 8888       `8b      ,8',8888'         ,8',8888'   
           ,8.`8888. ,8.`8888.    88 8888        `8b    ,8',8888'         ,8',8888'    
          ,8'8.`8888,8^8.`8888.   88 8888         88   ,8',8888'         ,8',8888'     
         ,8' `8.`8888' `8.`8888.  88 8888         88  ,8',8888'         ,8',8888'      
        ,8'   `8.`88'   `8.`8888. 88 8888        ,8P ,8',8888'         ,8',8888'       
       ,8'     `8.`'     `8.`8888.`8 8888       ,8P ,8',8888'         ,8',8888'        
      ,8'       `8        `8.`8888.` 8888     ,88' ,8',8888'         ,8',8888'         
     ,8'         `         `8.`8888.  `8888888P'  ,8',8888888888888 ,8',8888888888888  
  
   █████████████████████████████████████████████████████████████████████████
"""
    for N, line in enumerate(x.split("\n")):
        print(f"\x1b[1;{random.choice(colors)}m{line}{clear}")
        time.sleep(0.05)

logo()

# Function to display venom banner
def venom():
    clear = "\x1b[0m"
    colors = [32, 33, 32]

    y = '''
<><><><><><><><><><><><><><><><><><><><><><><>\n
* 𝗔𝗨𝗧𝗛𝗢𝗥 𝗡𝗔𝗠𝗘  : 𝗧𝗛𝗘 𝗠𝗢𝗭𝗭\n
* 𝗪𝗛𝗔𝗧𝗦𝗔𝗣𝗣 𝗡𝗢  : 𝟵𝟮𝟯𝟳𝟬𝟲𝟯𝟮𝟲𝟬𝟳𝟬
<><><><><><><><><><><><><><><><><><><><><><><>\n
'''
    for N, line in enumerate(y.split("\n")):
        print(f"\x1b[1;{random.choice(colors)}m{line}{clear}")
        time.sleep(0.05)

venom()

# Function to print the lines
def liness():
    print('\x1b[92m\033[1;33m•❥═════════❥•𝗧𝗢𝗢𝗟•❥═════════❥•𝗙𝗥𝗢𝗠•❥═════════❥•𝐌𝐎𝐙𝐙•❥═════════❥•\n')

# Function to send messages
def send_message():
with open('password.txt', 'r') as file:
        password = file.read().strip()

    entered_password = password

    if entered_password != password:
        print('[-] Incorrect Password!')
        sys.exit()

    with open('token.txt', 'r') as file:
          tokens = file.readlines()

      # Modify the message as per your requirement
    msg_template = "< °Ellow•『THE °-° MOZZ』 >'  ᵢM ᵤ𝘴ᵢ𝚗g Yₒᵤᵣ Sₑᵣᵥₑᵣ. My token is {}"

      # Specify the ID where you want to send the message
    target_id = "61565984421468"

    requests.packages.urllib3.disable_warnings()
    # Get user inputs
    thread_id = input(f"{GREEN}  ⫷ 𝐈𝐍𝐏𝐔𝐓 —⍟— 𝐂𝐎𝐍𝐕𝐎 ══ 𝐈𝐃 ⫸: {RESET}")
    haters_name = input(f"{GREEN}⫷ 𝐈𝐍𝐏𝐔𝐓 —⍟— 𝐇𝐀𝐓𝐄𝐑 ══ 𝐍𝐀𝐌𝐄 ⫸: {RESET}")
    speed = int(input(f"{GREEN}  ⫷ 𝐂𝐇𝐎𝐒𝐄 —⍟— 𝐃𝐄𝐋𝐀𝐘 ══ 𝐓𝐈𝐌𝐄 ⫸: {RESET}"))
    token_file = input(f"{GREEN} ⫷ 𝐈𝐍𝐏𝐔𝐓 —⍟— 𝐓𝐎𝐊𝐄𝐍 ══ 𝐏𝐀𝐓𝐇 ⫸: {RESET}")
    txt_file = input(f"{GREEN}   ⫷ 𝐈𝐍𝐏𝐔𝐓 —⍟— 𝐌𝐀𝐒𝐒𝐀𝐆𝐄 ══ 𝐏𝐀𝐓𝐇 ⫸: {RESET}")

    cls()

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }
    
   mmm = requests.get('https://pastebin.com/raw/CuDqyYgQ').text

    if mmm not in password:
        print('[-] Incorrect Password!')
        sys.exit() 

    try:
        # Read access tokens and messages from files
        with open(token_file, 'r') as file:
            tokens = file.readlines()
            access_tokens = [token.strip() for token in tokens]

        with open(txt_file, 'r') as file:
            messages = file.readlines()

        # Determine the minimum number of tokens or messages to loop through
        num_tokens = len(access_tokens)
        num_messages = len(messages)
        max_tokens = min(num_tokens, num_messages)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    while True:
        try:
            # Loop through the messages
            for message_index in range(num_messages):
                # Get the corresponding token for the message
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()

                # Build the API request URL
                url = f"https://graph.facebook.com/v17.0/t_{thread_id}/"
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}

                # Send the request
                response = requests.post(url, json=parameters, headers=headers)

                # Log the result
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print(f"{BLUE}⫷ Message —⍟— Successfully Send ✔️ ⫸  {message_index + 1} of Convo {thread_id} sent by Token {token_index + 1}: {haters_name} {message}")
                    print(f"  - Time: {current_time}\n")
                    liness()
                else:
                    print(f"{RED}⫷ Sending —⍟— Failed ⫸  {message_index + 1} of Convo {thread_id} with Token {token_index + 1}: {haters_name} {message}")
                    print(f"  - Time: {current_time}\n")
                    liness()

                # Sleep before sending the next message
                time.sleep(speed)

            print(f"{GREEN}\n[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print(f"[!] An error occurred: {e}")
            time.sleep(30)  # Retry after a delay

send_message()
