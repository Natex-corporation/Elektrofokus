from time import sleep
import numpy as np
import pandas as pd
import os
from difflib import SequenceMatcher 
import pandas as pd

def similar (a,b):
    return SequenceMatcher(None, a, b).ratio()

def csv_generator(directory, destination):
    directory_files = os.listdir(directory)
    print(directory_files, 'files')
    for file in directory_files:
        print(file, 'you are in this file')
        file_name = file
        if file.endswith('.txt'):
            lines = [[]]
            results=[[]]
            headers = []
            subsidiery_values = [[]]
            lolec = []
            data_checker = False
            with open(directory + '/' + file, 'r') as f:
                catcher = 0
                #data_checker = False
                for line in f:
                    #print (line, 'luul')
                    #sleep(1)
                    if similar(line,'L E G E N D') > 0.9:
                        #print (similar(line,'L E G E N D')) #for word in line:
                        catcher = 1
                    if line[0] == 'C' and catcher == 1:
                        line = line.split('\t')
                        line = line[1]
                        #value.append(line)
                        if similar(line, 'U rms') < 0.5:
                            line = line.split('\n')
                            headers.append(line[0])
                    place_holder = []
                    if line[0] == 'A' or line[0] == 'B':
                        unit = ''
                        line = line.split(' ')
                        for i in range(len(line)):
                            if i > 1:
                                line[i] = line[i].split('\n')[0]
                                line_placeholder = line[i].split('\t')
                                if len(line_placeholder) > 1:
                                    #print(line_placeholder)
                                    line[i] = line_placeholder[1]
                                    if unit == '':
                                        unit = line_placeholder[0]
                                else:
                                    line[i] = line_placeholder[0]
                                #print(line[i])
                                place_holder.append(line[i])
                        place_holder.append(unit)
                        subsidiery_values.append(place_holder)
                        #print (line)
                    #print (line)
                    #print (data_checker, 'datachecker')
                    if similar(line,'0,0') > 0.3 and line[0] == '0' or data_checker == True:
                        data_checker = True 
                        #print(line, 'this should be data', type(line))
                        line = line.split('\t')
                        for i in range(len(line)):
                            line[i] = line[i].split('\n')[0]
                            line[i] = line[i].replace(',','.')
                            #print (line[i], 'line[i]')
                        lolec.append(line)
                        #line = line.split('\n')
                #print(len(lolec), 'biggest lolec')
                line_np = np.array(lolec)
                #print (line_np)
                df = pd.DataFrame(line_np, columns=['time', '[' + subsidiery_values[1][4] + ']', '[' + subsidiery_values[2][4] + ']'])
                df.to_csv(destination + '/' + file_name.split('.')[0]+'.csv', index='False')
                #print (line_np)
                #print ('start',headers,'headers', subsidiery_values)
                #df = pd.DataFrame(line)
                #print (df)
                #return headers, subsidiery_values