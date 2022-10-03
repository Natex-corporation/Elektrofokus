from time import sleep
import pandas as pd
import os
from difflib import SequenceMatcher 

def similar (a,b):
    return SequenceMatcher(None, a, b).ratio()

def csv_generator(directory, destination):
    directory_files = os.listdir(directory)
    for file in directory_files:
        print(file)
        if file.endswith('.txt'):
            lines = [[]]
            results=[[]]
            headers = []
            subsidiery_values = [[]]
            with open(file,'r') as f:
                catcher = 0
                for line in f:
                    #print (line)
                    #sleep(1)
                    if similar(line,'L E G E N D') > 0.9:
                        print (similar(line,'L E G E N D')) #for word in line:
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
                                print(line[i])
                                place_holder.append(line[i])
                        place_holder.append(unit)
                        subsidiery_values.append(place_holder)
                        #print (line)
                    #print (line)
                    if similar(line,'0,0') > 0.1:
                        line = line.split('\t')
                        for i in range(len(line)):
                            line[i] = line[i].split('\n')[0]
                        #line = line.split('\n')
                        print (line)
                print (headers, subsidiery_values)

