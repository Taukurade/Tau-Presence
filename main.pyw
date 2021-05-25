
from pypresence import Presence
import time
import vk_api

RPC = Presence('844861871693234196')#discord app`s client id
RPC.connect()   
vk_session = vk_api.VkApi('', '')#vk.com login,password
vk_session.auth()
vk = vk_session.get_api()

def tr(string):

    capital_letters = {u'А': u'A',
                       u'Б': u'B',
                       u'В': u'V',
                       u'Г': u'G',
                       u'Д': u'D',
                       u'Е': u'E',
                       u'Ё': u'E',
                       u'Ж': u'Zh',
                       u'З': u'Z',
                       u'И': u'I',
                       u'Й': u'Y',
                       u'К': u'K',
                       u'Л': u'L',
                       u'М': u'M',
                       u'Н': u'N',
                       u'О': u'O',
                       u'П': u'P',
                       u'Р': u'R',
                       u'С': u'S',
                       u'Т': u'T',
                       u'У': u'U',
                       u'Ф': u'F',
                       u'Х': u'H',
                       u'Ц': u'Ts',
                       u'Ч': u'Ch',
                       u'Ш': u'Sh',
                       u'Щ': u'Sch',
                       u'Ъ': u'',
                       u'Ы': u'Y',
                       u'Ь': u'',
                       u'Э': u'E',
                       u'Ю': u'Yu',
                       u'Я': u'Ya',}

    lower_case_letters = {u'а': u'a',
                       u'б': u'b',
                       u'в': u'v',
                       u'г': u'g',
                       u'д': u'd',
                       u'е': u'e',
                       u'ё': u'e',
                       u'ж': u'zh',
                       u'з': u'z',
                       u'и': u'i',
                       u'й': u'y',
                       u'к': u'k',
                       u'л': u'l',
                       u'м': u'm',
                       u'н': u'n',
                       u'о': u'o',
                       u'п': u'p',
                       u'р': u'r',
                       u'с': u's',
                       u'т': u't',
                       u'у': u'u',
                       u'ф': u'f',
                       u'х': u'h',
                       u'ц': u'ts',
                       u'ч': u'ch',
                       u'ш': u'sh',
                       u'щ': u'sch',
                       u'ъ': u'',
                       u'ы': u'y',
                       u'ь': u'',
                       u'э': u'e',
                       u'ю': u'yu',
                       u'я': u'ya',}

    translit_string = ""

    for index, char in enumerate(string):
        if char in lower_case_letters.keys():
            char = lower_case_letters[char]
        elif char in capital_letters.keys():
            char = capital_letters[char]
            if len(string) > index+1:
                if string[index+1] not in lower_case_letters.keys():
                    char = char.upper()
            else:
                char = char.upper()
        translit_string += char

    return translit_string



def check():
    x=vk.status.get()['text']
    try:
        d=x.split('—')
        return [tr(d[0]),tr(d[1]),'music','Spotify sucks']
    except:
        return [vk.status.get()['text'],'taukurade@airi.gq','vk_ava','idling or doing something']
print(vk.status.get()['text'])
print(check())
while True:
    RPC.update(details=check()[0],
               state=check()[1],
               buttons=[{
                            'label':'github',
                            'url':"http://github.com/taukurade/"
                        },
                        {
                            'label':'kill me please',
                            'url':'http://vk.com/taukurade'
                        }],
               large_image=check()[2],
               large_text=check()[3])
    time.sleep(1)



