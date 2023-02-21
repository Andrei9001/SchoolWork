import requests
import pandas as pd
import json
import matplotlib.pyplot as plt

link = 'https://random-data-api.com/api/users/random_user'


def generate_user():
    user_raw=requests.get(link)
    user_json = json.loads(user_raw.text)
    pop = ['employment','address','credit_card','subscription']
    for j in pop:
        user_json.pop(j)
    return user_json

indx = 0
user_json = generate_user()
df_base = pd.DataFrame(user_json, index=[indx])

for i in range(99):
    indx += 1
    user_json = generate_user()
    df_temp = pd.DataFrame(user_json, index=[indx])
    df_base = pd.concat([df_base,df_temp])
df_base['date_of_birth'] = pd.to_datetime(df_base['date_of_birth'])

#   histogrammas izveide
plt.hist(df_base['date_of_birth'],bins=10)
plt.show()

#   sakarto date_of_birth augošā secībā; JSON fails tiek saglabāts darbavirsmas sākuma mapītē
df_base.sort_values(by='date_of_birth', ascending=True, inplace=True)
df_base.to_json('users.json')
