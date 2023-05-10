from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager
import speech_recognition as sr
import pyttsx3
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                          options = options)

driver.get('https://www.cstimer.net/')
#driver.maximize_window()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()
microphone = sr.Microphone()

actions = ActionChains(driver)

# Function for computer speaking
def speak(query): 
    engine.say(query)
    engine.runAndWait()

# Function for recognizing user input speech
def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit = 3)
        response = ''
        try:
            response = recognizer.recognize_google(audio)
        except:
            response = "Error"
    return response

# Opens settings
driver.find_element(By.CLASS_NAME, 'mybutton.c1').click()

# Change to dark theme
select_color = Select(driver.find_element(By.NAME, 'color'))
select_color.select_by_value("4")

# Change from timer to virtual cube
select_virtual = Select(driver.find_element(By.NAME, 'input'))
select_virtual.select_by_value("v")

# Changes base speed of virtual cube from 10 to 5
select_speed = Select(driver.find_element(By.NAME, 'vrcSpeed'))
select_speed.select_by_value("200")

# Closes settings
driver.find_element(By.CLASS_NAME, 'buttonOK').click()

speak("Virtual cube opened")

# Starts listening to commands
while True:
    
    command = recognize_speech().lower()
    print(command)

    # MISC COMMANDS

    # Start inspection
    if command == 'begin' or command == 'start':
        actions.send_keys(' ')
        actions.perform()
        speak("Starting inspection")

    # Stop this solve
    elif command == 'stop':
        actions.send_keys(Keys.ESCAPE)
        actions.perform() 
        speak('Move performed')

    # Exit out of the program
    elif command == 'quit':
        driver.close()
        quit()


    # ROTATIONS

    # y'
    elif command in ['rotate left']:
        actions.send_keys('a')
        actions.perform()  
        speak('Move performed')
    # y
    elif command in ['rotate right']:
        actions.send_keys(';')
        actions.perform()
        speak('Move performed')
    # y2
    elif command in ['rotate to', 'rotate twice']:
        actions.send_keys(';;')
        actions.perform()
        speak('Move performed')

    # x
    elif command == 'rotate up':
        actions.send_keys('n')
        actions.perform()
        speak('Move performed')
    # x'
    elif command in ['rotate down']:
        actions.send_keys('y')
        actions.perform()
        speak('Move performed')

    
    # BASIC TURNS

    # R
    elif command == 'turn right': 
        actions.send_keys('i')
        actions.perform()
        speak('Move performed')
    # R'
    elif command in ['turn right prime', 'turn rights prime', 'turn lights prime', 'write prime']: 
        actions.send_keys('k')
        actions.perform()
        speak('Move performed')

    # L
    elif command == 'turn left': 
        actions.send_keys('d')
        actions.perform()
        speak('Move performed')
    # L'
    elif command in ['turn left prime', 'left prime']: 
        actions.send_keys('e')
        actions.perform()
        speak('Move performed')

    # D
    elif command in ['turn down']: 
        actions.send_keys('s')
        actions.perform()
        speak('Move performed')
    # D'
    elif command in ['turn down prime']: 
        actions.send_keys('l')
        actions.perform()
        speak('Move performed')

    # U
    elif command in ['turn up']: 
        actions.send_keys('j')
        actions.perform()
        speak('Move performed')
    # U'
    elif command in ['you prime', 'turn you prime', 'turn up prime', 
                     'up prime']: 
        actions.send_keys('f')
        actions.perform()
        speak('Move performed')

    # F
    elif command in ['turn front']:
        actions.send_keys('h')
        actions.perform()
        speak('Move performed')
    # F'
    elif command in ['f prime', 'turn front prime']: 
        actions.send_keys('g')
        actions.perform()
        speak('Move performed')

    # B
    elif command in ['turn back']:
        actions.send_keys('w')
        actions.perform() 
        speak('Move performed')
    # B'
    elif command in ['back prime', 'turn back time', 'turn back prime']: 
        actions.send_keys('o')
        actions.perform()
        speak('Move performed')

    # M
    elif command in ['turn middle']: 
        actions.send_keys('6')
        actions.perform()
        speak('Move performed')
    # M'
    elif command in ['turn middle prime']: 
        actions.send_keys('.')
        actions.perform()
        speak('Move performed')


    # DOUBLE MOVES

    # R2
    elif command in ['turn right to', 'write 2']: 
        actions.send_keys('ii')
        actions.perform()
        speak('Move performed')

    # L2
    elif command in ['turn left two', 'left to', 'turn left to']: 
        actions.send_keys('ee')
        actions.perform()
        speak('Move performed')

    # U2
    elif command in ['turn up to', 'turn up two', 'up to']: 
        actions.send_keys('jj')
        actions.perform()
        speak('Move performed')

    # F2
    elif command in ['turn front two', 'turn front to']: 
        actions.send_keys('hh')
        actions.perform()
        speak('Move performed')

    # D2
    elif command in ['turn down to']: 
        actions.send_keys('ll')
        actions.perform()
        speak('Move performed')
    
    # B2
    elif command in ['turn back to']: 
        actions.send_keys('oo')
        actions.perform()
        speak('Move performed')

    # M2
    elif command in ['turn middle two']: 
        actions.send_keys('..')
        actions.perform()
        speak('Move performed')


    # WIDE TURNS

    # Rw
    elif command in ['turn small right', 'turn white right', 'turn wide right']: 
        actions.send_keys('u')
        actions.perform()
        speak('Move performed')
    # Rw'
    elif command in ['small right prime', 'turn small right prime', 
                     'turn small rights prime', 'turn small right time', 
                     'small rights prime', 'all rights prime', 
                     'turn small rice prime', 'turn wide right prime',
                     'turn wide right price', 'wide right prime',
                     'turn my right pie', 'turn why rights prime']: 
        actions.send_keys('u')
        actions.perform()
        speak('Move performed')

    # Uw
    elif command in ['turn small up']: 
        actions.send_keys(',')
        actions.perform()
        speak('Move performed')
    # Uw'
    elif command in ['turn small up prime', 'turn small up time', 
                     'small up prime', 'turn small off prime', 
                     'small up time']: 
        actions.send_keys('c')
        actions.perform()
        speak('Move performed')

    # Dw
    elif command in ['turn small down', 'small town']: 
        actions.send_keys('z')
        actions.perform()
        speak('Move performed')
    # Dw'
    elif command in ['turn small down prime']: 
        actions.send_keys('/')
        actions.perform()
        speak('Move performed')
    

    # SHORTCUT MOVES

    # Sexy (R U R' U')
    elif command in ['sexy']: 
        actions.send_keys('ijkf')
        actions.perform()
        speak('Move performed')

    # Double Sexy (R U R' U')(R U R' U')
    elif command in ['double sexy']: 
        actions.send_keys('ijkfijkf')
        actions.perform()
        speak('Move performed')
    
    # Triple Sexy (R U R' U')(R U R' U')(R U R' U')
    elif command in ['triple sexy', 'triple sex']: 
        actions.send_keys('ijkfijkfijkf')
        actions.perform()
        speak('Move performed')

    # Sledgehammer (R' F R F')
    elif command in ['sledgehammer', 'sledge']: 
        actions.send_keys('khig')
        actions.perform()
        speak('Move performed')

    # R U R'
    elif command in ['join', 'join right']: 
        actions.send_keys('ijk')
        actions.perform()
        speak('Move performed')
    
    # R U' R'
    elif command in ['insert', 'inserts', 'insert right']: 
        actions.send_keys('ifk')
        actions.perform()
        speak('Move performed')

    # L' U' L
    elif command == 'join left': 
        actions.send_keys('efd')
        actions.perform()
        speak('Move performed')

    # L' U L
    elif command in ['insert left', 'inserts left']: 
        actions.send_keys('ejd')
        actions.perform()
        speak('Move performed')

    # OLL - EDGE CONTROL

    # No Edges (F R U R' U' F' f R U R' U' f')
    elif command in ['no edge', 'no edges']:
        actions.send_keys('hijkfgffhjifkg')
        actions.perform()
        speak('Move performed')

    # Bar/Line case (say 'opposite edges') (F R U R' U' F')
    elif command in ['opposite edges', 'opposite patches', '']:
        actions.send_keys('hijkfg')
        actions.perform()
        speak('Move performed')

    # Adjacent edges (say 'adjacent' or 'adjacent edges)
    # (put them in the left and top) (F U R U' R' F')
    elif command in ['adjacent', 'adjacent edges', 'adjacent address']:
        actions.send_keys('hjifkg')
        actions.perform()
        speak('Move performed')

    
    # OLL - EDGES DONE

    # Sune (R U R' U R U2 R')
    elif command in ['soon']: 
        actions.send_keys('ijkjiffk')
        actions.perform()
        speak('Move performed')
    # Back Sune ((U') R' U2 R U R' U R)
    elif command in ['back soon']: 
        actions.send_keys('kffijkji')
        actions.perform()
        speak('Move performed')

    # Antisune (R U2 R' U' R U' R')
    elif command in ['auntie soon']:
        actions.send_keys('iffkfifk')
        actions.perform()
        speak('Move performed')
    # Other Antisune (R' U' R U' R' U2 R)
    elif command in ['other auntie soon', 'other answers soon', 
                     'other and too soon', 'mother and to soon', ]:
        actions.send_keys('kfifkffi')
        actions.perform()
        speak('Move performed')

    # L (say 'bowtie) (F' r U R' U' r' F R)
    elif command in ['bow tie']:
        actions.send_keys('gujkfmhi')
        actions.perform()
        speak('Move performed')

    # Pi (R U2 R2' U' R2 U' R2' U2' R)
    elif command in ['pie']:
        actions.send_keys('iffiifiifiiffi')
        actions.perform()
        speak('Move performed')

    # H (say "H") (R U2 R' U' R U R' U' R U' R')
    elif command in ['h']:
        actions.send_keys('iffkfijkfifk')
        actions.perform()
        speak('Move performed')

    # U (say 'U' or 'headlights) (R U R' U' R U' R' U2 R U' R' U2 R U R')
    elif command in ['headlights']:
        actions.send_keys('ijkfifkffifkffijk')
        actions.perform()
        speak('Move performed')

    # T (say 'chameleon')(r U R' U' r' F R F')
    elif command in ['chameleon']:
        actions.send_keys('ujkfmhig')
        actions.perform()
        speak('Move performed')


    # PLL


    # Aa Perm (x R' U R' D2 R U' R' D2 R2)
    elif command in ['aa', 'aa perm', 'pay a perm']:
        actions.send_keys('tkjkssifksskknb')
        actions.perform()
        speak('Move performed')

    # Ab Perm (x R2 D2 R U R' D2 R U' R)
    elif command in ['ab perm', 'baby', 'baby perm', 'baby perma']:
        actions.send_keys('tkkssijkssifinb')
        actions.perform()
        speak('Move performed')

    # E Perm (x' R U' R' D R U R' D' R U R' D R U' R' D')
    elif command in ['e perm']:
        actions.send_keys('bifksijklijksifkl')
        actions.perform()
        speak('Move performed')

    # F Perm (R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R)
    elif command in ['of perm', 'half perm', 'afternoon', 
                     'f perm', 'half term']:
        actions.send_keys('kfgijkfkhiifkfijkji')
        actions.perform()
        speak('Move performed')

    # Ga Perm (R2 U R' U R' U' R U' R2 D U' R' U R D')
    elif command in ['ga perm', 'ga']:
        actions.send_keys('iijkjkfifiifskjil')
        actions.perform()
        speak('Move performed')

    # Gb Perm ( F' U' F R2 u R' U R U' R u' R2)
    elif command in ['gb perm']:
        actions.send_keys('gfhii,kjifilhh')
        actions.perform()
        speak('Move performed')

    # Gc Perm (R2 F2 R U2 R U2 R' F R U R' U' R' F R2)
    elif command in ['easy perm', 'gc perm']:
        actions.send_keys('kkhhiffiffkhijkfkhkk')
        actions.perform()
        speak('Move performed')

    # Gd Perm (R U R' U' D R2 U' R U' R' U R' U R2 D')
    elif command in ['gd perm', 'jd perm']:
        actions.send_keys('ijksfiififkjkjkkl')
        actions.perform()
        speak('Move performed')

    # H Perm (say 'age perm') (M2 U' M2 U2 M2 U' M2)
    elif command in ['each term', 'hp', 'h-tron', 'age perm', 
                     'each turn', 'age term', 'each perm']:
        actions.send_keys('..f..ff..f..')
        actions.perform()
        speak('Move performed')

    # Ja Perm (R' U L' U2 R U' R' U2 R L)
    elif command in ['ja perm', 'ja', 'j a perm']:
        actions.send_keys('kjejjifkjjdi')
        actions.perform()
        speak('Move performed')

    # Jb Perm (R U R' F' R U R' U' R' F R2 U' R')
    elif command in ['jb perm', 'jb per', ]:
        actions.send_keys('ijkgijkfkhiifk')
        actions.perform()
        speak('Move performed')

    # Na Perm 
    elif command in ['and a perm', 'and a per', "i'm a perm"]:
        actions.send_keys('ijkjijkgijkfkhiifkffifk')
        actions.perform()
        speak('Move performed')

    # Nb Perm (R' U R U' R' F' U' F R U R' F R' F' R U' R)
    elif command in ['nb perm', 'and be perm']:
        actions.send_keys('kjifkgfhijkhkgifi')
        actions.perform()
        speak('Move performed')

    # Ra Perm (R U' R' U' R U R D R' U' R D' R' U2 R')
    elif command in ['for a perm', 'are a perm']:
        actions.send_keys('ifkfijiskfilkffk')
        actions.perform()
        speak('Move performed')

    # Rb Perm (R' U2 R U2 R' F R U R' U' R' F' R2)
    elif command in ['barbie perm', 'rb perm', 'rb10', ]:
        actions.send_keys('kffiffkhijkfkgkk')
        actions.perform()
        speak('Move performed')

    # T Perm (R U R' U' R' F R2 U' R' U' R U R' F')
    elif command in ['t perm', 't-burn']:
        actions.send_keys('ijkfkhiifkfijkg')
        actions.perform()
        speak('Move performed')

    # Ua Perm (R U' R U R U R U' R' U' R2)
    elif command in ['you a perm']:
        actions.send_keys('ifijijifkfkk')
        actions.perform()
        speak('Move performed')

    # Ub Perm (R2 U R U R' U' R' U' R' U R')
    elif command in ['you be perm', 'you beeper', 'ub perm', 'you perm me', 
                     'you turn me', 'perm be']:
        actions.send_keys('iijijkfkfkjk')
        actions.perform()
        speak('Move performed')

    # V Perm (R' U R' d' R' F' R2 U' R' U R' F R F)
    elif command in ['the perm', 'v perm', 'the v perm']:
        actions.send_keys('kjk/kgiifkjkhih')
        actions.perform()
        speak('Move performed')

    # Y Perm (F R U' R' U' R U R' F' R U R' U' R' F R F')
    elif command in ['why perm']:
        actions.send_keys('hifkfijkgijkfkhig')
        actions.perform()
        speak('Move performed')

    # Z Perm (say "zed perm") (M' U' M2 U' M2 U' M' U2 M2)
    elif command in ['dead perm', 'that perm', 'bedtime', 'set perm', 
                     'zed perm', 'said perm', '']:
        actions.send_keys('.f..f..f.ff..')
        actions.perform()
        speak('Move performed')
    
    else:
        speak('Not recognized')
        