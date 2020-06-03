import io
import pyqrcode
from base64 import b64encode
import eel
import sys
import os

eel.init('web')


@eel.expose
def dummy(dummy_param):
    print("I got a parameter: ", dummy_param)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}

@eel.expose
def play_sound(soundname):
    print(soundname)

def generate_gui(path):
    gui_1 = open('data/base.html').read()
    if os.path.exists(path):
        files = os.listdir(path)
        sounds = []
        for i in range(len(files)):
            if '.mp3' in files[i] or '.wav' in files[i]:
                print('Found a', files[i].split('.')[1],'soundfile: ', files[i].split('.')[0])
                sounds.append(files[i])
                gui_1 += (open('data/section.html').read().replace('HOB', files[i])).replace('SOUND', files[i].split('.')[0])
        gui_1 +=('</div></body></html>')
        open('web/gui.html', 'w').write(gui_1)
    else:
        sys.exit()

generate_gui(r'Z:\Content\Soundboard')
eel.start('gui.html', size=(1000, 600))
