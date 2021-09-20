print('INIT STARTED')

import time
from Tweet import tweet
from Log import save_json, load_json
from News_api import get_news
from Translation import traduction
from Hashtag import hashtag

print('MAIN LOOP STARTEING')
while True:
    print('MAIN LOOP ')
    data = load_json()
    
    for i in get_news():
        if i['id'] not in data['done']:
            
            print(i['id'])
            _body = i['summary']
            print("len befor traduction",len(_body))
            body = traduction(_body)
            if len(body) > 280:
                _body = i['title']
                body = traduction(_body)
                print('summary to long going for title')
                if len(body) > 280:
                    data['done'].append(i['id'])
                    print("to long skkipng")
                    break



            body = hashtag(body)
            
            img = i['imageUrl']
            print(body,img)
            tweet(img,body)
            data['done'] = data['done']+[i['id']]
            break
        
        

    

    save_json(data)
    time.sleep(60*60 )

    
    pass
