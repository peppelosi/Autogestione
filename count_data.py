import time

def int_tag(tags_trial):
    
    for i in range(0, len(tags_trial)-1):
        tags_trial[i] = tags_trial[i][len(tags_trial[i])-5:len(tags_trial[i])-3]
        tags_trial[i] = int(tags_trial[i])
        
    return tags_trial

def array_time(tags):

    #lettura data_array from db
    data_array = [time(12, 36, 40), time(12, 36, 40), time(12, 36, 40), time(12, 36, 40), time(12, 36, 40)]

    for i in range(0, len(data_array)-1):
        for j in range(0, len(tags)-1):
            if tags[j] == i:
                update_array('tag presente')
                
    #definire controlli in caso di mancata presenza del tag

    

def update_array(message):
    mes = message
