import os
import time

list_files = os.listdir("dickens")

while True:    
    word = input("Enter Word To Search: ")
    time_start = time.time()
    
    for i in list_files:
        fp = open(f"dickens/{i}", 'r', encoding="utf-8')")
        # read all lines in a list
        list_lines = fp.readlines()
        
        for line in list_lines:
            
            def print_results(file, line, text):
                print(f"File:==> {i} **** Line:==> {line} **** Text:==> {text}")
            
            def search(search_entry):
                    # check if string present on a current line
                if line.find(word) != -1:    
                    print_results(i, list_lines.index(line), line)      
                        
            search(word)
    time_stop = time.time()
    print(f"{time_stop - time_start} Seconds Left you have 5 seconds to read results...")
    time.sleep(5)
    os.system('cls')
                    