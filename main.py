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
        if i['title'] not in data['done']:
            
            print(i['title'])
            _body = i['title']
            print("len befor traduction",len(_body))
            body = traduction(_body)
            if len(body) > 280:
                data['done'].append(i['title'])
                print("to long skkipng")
                break
               
                    
                    


            else:
                body = hashtag(body)
                
                img = i['image']
                print(body,img)
                tweet(img,body)
                data['done'] = data['done']+[i['title']]
                break
        
        

    

    save_json(data)
    time.sleep(60 )

    
    pass
