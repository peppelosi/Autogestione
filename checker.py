import datetime
import requests 



def count_tag(tag, time_rel, all_times, presence, time_max):
    
    for i in range(5):
        if tag == i+1:
            all_times[i] = time_rel
            
            if presence[i] == False:
                x = requests.post('http://www.poggiolevante.net/autogestione/update.php', {'update': '1', 'tag': str(i+1), 'time_rel': str("")})
                presence[i] = True
        
        else: 
            if delta_time(time_rel, all_times[i]) >= time_max and presence[i] == True:
                x = requests.post('http://www.poggiolevante.net/autogestione/update.php', {'update': '0', 'tag': str(i+1), 'time_rel': str(all_times[i])})
                presence[i] = False

    return [presence, all_times]
    

def delta_time(time_1, time_2):

    time_1 = int(datetime.time(int(time_1[11: 13]), int(time_1[14: 16]), int(time_1[17: 19])).minute)
    time_2 = int(datetime.time(int(time_2[11: 13]), int(time_2[14: 16]), int(time_2[17: 19])).minute)
    
    return time_1 - time_2