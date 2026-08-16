import csv

def jobmap(data=None) -> str:
    job = ''
    num = 1
    with open('jobmap.csv', 'a') as jf:
        csvw = csv.writer(jf)

        for j in data:
        
            if not '>' in j:
                job+=j
            
            else:
                csvw.writerows(job)
                num+=1
                job=''


jobmap(data="test1>testty>I AM GUFFY>YOU ARE GUFFY>WE ARE GUFFY")
