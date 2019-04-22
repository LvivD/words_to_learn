# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import  requests
import json
# TODO: replace with your own app_id and app_key
app_id = '6a3b4fd4'
app_key = '2e6d4766ccc148128be6afbf75e18db2'
language = 'en'
word_id = 'was'
url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word_id.lower()
#url Normalized frequency
urlFR = 'https://od-api.oxforddictionaries.com:443/api/v1/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()
r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))
with open('tests/resaults '+word_id+'.json', 'w') as write_file:
    write_file.write(json.dumps(r.json()))
