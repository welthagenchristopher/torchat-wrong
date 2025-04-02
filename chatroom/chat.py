from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS
import os, stem.process, re, requests, json, sys
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc


class torconnect():

    def __init__(self):

        self.PORT = 9050
        self.PATH = os.path.normpath(os.getcwd()+"\\tor\\tor.exe")

        self.process =stem.process.launch_tor_with_config(

            config={

                'SocksPort': str(self.PORT),
            },

            init_msg_handler = lambda line: print(line) if 
        re.search('Bootstrapped', line) else False,
        tor_cmd = self.PATH
        )
        super().__init__()

    def proxy(self):

        global PROXIES
        PROXIES = {

            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'

        }

        response = requests.get('http://ip-api.com/json/', proxies=PROXIES)
        result = json.loads(response.content)
        print('TOR IP [%s]: %s %s' % (datetime.now().strftime("%d-%m-%Y %H:%M:%S"), result["query"], result["country"]))


class mydriver(uc.Chrome):

    def __init__(self):

        self.options = Options()
        self.options.add_argument(f"--proxy-server=socks5://127.0.0.1:9050")
        self.options.page_load_strategy = 'normal'
        self.options.add_argument("--start-maximized")
        self.use_subprocess=True
        self.service=Service(service=Service(executable_path=ChromeDriverManager().install()))
        self.keep_alive=True
        

        super(mydriver, self).__init__(service=self.service, options=self.options, keep_alive=self.keep_alive)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
#wrap app in CORS to for all cross origin routes
#still generating 400 code - possibly some incompatability with packages?
#no impact to functionality
cors = CORS(app)
socketio = SocketIO(app)
#cors_allowed_origins='https://localhost') - argument to provide when
#initiating app to test local CRUD operations


@app.route('/')
def sessions():
    return render_template('sessions.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

#callbacks yadayada, socketio.emit - 
#post grabbed from client side
@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True, use_reloader=False)

    t = torconnect()
    t.proxy()
    d = mydriver()




#I knew at the time, but if you held a gun to my head and asked me why this line prevents
#the script from crashing, I wouldn't be able to tell you.
sys.stdin.read()
