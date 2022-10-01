import json

def jsonwriter(jdata):
            # print('writter')
            # print('json writer')
            json.dumps(jdata)
            with open('DB/Botplace.json', mode='w') as f:
                f.write(json.dumps(jdata, indent=2))