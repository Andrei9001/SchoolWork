import requests
import json
import translators.server as tss

def lapas_parb(url):
    requests.get(url)
    r = requests.get(url)
    r.status_code
    if r.status_code == 200:
        print('Jā! Tāda mājaslapa eksistē')
    elif r.status_code == 404:
        print('Nē! Tāda mājaslapa neeksistē.')
        return None
    print("statusa kods: {}".format(r.status_code))
    #print("HTML dokuments: {}".format(r.text))

def Norris():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url, timeout=10)
    joke_dict = json.loads(response.text)
    lat = tss.google(joke_dict['value'], to_language=('lv'))
    return joke_dict['value'],lat

lapas_parb("https://api.chucknorris.io/")
print(Norris())
