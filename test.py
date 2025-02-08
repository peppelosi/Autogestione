from asyncio.windows_events import NULL
import socket
import time
import redis
import requests

def count_tag(tags_trial):
    
    for i in range(0, len(tags_trial)-1):
        tags_trial[i] = tags_trial[i][len(tags_trial[i])-5:len(tags_trial[i])-3]
        tags_trial[i] = int(tags_trial[i])
        
    return tags_trial  

def main():
    import time
    # import datetime
    vvv = time.asctime()
    print(vvv)
    x = requests.post('http://www.poggiolevante.net/autogestione/update.php', {'update': '1', 'tag': str(1), 'time_rel': vvv})

    print(x.text)
    
    
    # message = '[020100]'

    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(('10.10.11.17', 10001))
    # s.send(message.encode())
    
    
    # # tags_trial = ['[7F00000401]', '[8A00000301]', '[7900000501]', '[8500000101]', '[0401]']
    # # count_tag(tags_trial) 

    # # while(True):
    # #     print(s.recv(1024).decode())
    # #     print('\n'+time.asctime()+'\n\n\n')
    # time_1 = str(time.asctime())    
    # time_1 = int(datetime.time(int(time_1[11: 13]), int(time_1[14: 16]), int(time_1[17: 19])).minute)   

    # time_2 = str(time.asctime())   
    # time_2 = int(datetime.time(int(time_2[11: 13]), int(time_2[14: 16]), int(time_2[17: 19])).minute)
    # delta = time_2 - time_1
    # print(delta)
    
    # # r = redis.Redis(host='localhost', port=0, db=0)

    # # r.set('foo', 'bar')
    # # value = r.get('foo')
    # # print(value) 
    
    
if __name__ == '__main__':
    main()
