from pathlib import Path
import shutil
from datetime import datetime
interesting=[]
list_files=[]


def print_files(files):
    sorted_files=sorted(files)
    for file in sorted_files:
        print(Path(file))
def function_R (p):
    temp=[]
    for file in p.iterdir():
        if Path(file).is_file()==False:
            temp.append(file)
            function_R(Path(file))
        else:
            list_files.append(file)
        print(file)
def function_A(p):
    for file in list_files:
        if Path(file).is_file()==False:
            function_A(Path(file))
        interesting.append(file)
def function_N(file_name):
    for file in list_files:
        if file_name in Path(file).name:
            interesting.append(Path(file))
def function_E(file_name):
    for file in list_files:
        if Path(file).suffix==file_name:
            interesting.append(Path(file))
def function_T(text, p):
    for file in list_files:
        if Path(file).is_file()==False:
            function_T(text,file)
        else:
            try:
                file_content = Path(file).read_bytes()
                with open(file, 'r', encoding='utf-8') as f:
                    if text.encode('utf-8') in file_content:
                        interesting.append(file)
            except (UnicodeDecodeError, UnicodeError):
                print("NOT TEXT")
            except Exception:
                print("NOT TEXT")
            
           
def byteSize(byte, p, sign):
    for file in list_files:
        if Path(file).is_file()==False:
            byteSize(byte,Path(file),sign)
        else:
            with open(file, 'r') as f:
                if sign*(file.stat().st_size)<sign*(byte):
                    interesting.append(Path(file))
                     
def find_directory():
    direct_name=input()
    split=direct_name.split(' ',1)
    result=''.join(split[1:])
    p=Path(result)
    if split[0] not in ['R', 'D']:
        print("ERROR")
    elif split[0]in['D']:
        for file in p.iterdir():
            if Path(file).is_file()==True:
                list_files.append(file.name)
                print(file)
        return
    else:
        return function_R(p)
    find_directory()  
    
def action():       
    direct_name=input()
    split=direct_name.split(' ',1)
    result=''.join(split[1:])
    p=Path(result)
    if direct_name=='A':
        return function_A(p)
    if len(direct_name)>1:
        if split[0] not in ['N', 'T', 'E', '<','>']:
            print("ERROR")
        elif split[0]=='N':
            return function_N(result)  
        elif split[0]=='T':
            return function_T(result,p) 
        elif split[0]=='E':
            if result.startswith('.'):
                return function_E(result)    
            else:
                result='.'+result
                return function_E(result)   
        elif split[0]=='<':
            return byteSize(int(result),p,1)
        elif split[0]=='>':
            return byteSize(int(result),p,-1)

    action()

def narrowed_action():
    action_name=input()
    interesting.sort()
    if action_name=='F':
        for file in interesting:
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    first_line = f.readline().rstrip('\n\r')
                    print(first_line)
            except (UnicodeDecodeError, UnicodeError):
                print("NOT TEXT")
            except Exception:
                print("NOT TEXT")
        return
    elif action_name=='D':
        for file in interesting:
            destination = str(file) + '.dup'
            return shutil.copy2(file, destination)
    elif action_name=='T':
        for file in interesting:
            return Path(file).touch()
    else:
        print('ERROR')
        narrowed_action()
        
sorted_list=interesting.sort()          
find_directory()
action()
if interesting != []:
    sorted_list=sorted(interesting)
    for file in sorted_list:
        print(Path(file))
    narrowed_action()


#D /Users/ayaanv/Desktop/ICSH32
##INPUT     |R /Users/ayaanv/Desktop/ICSH32/project1_test_2025-10-16-21-02-31
##OUTPUT    |/Users/ayaanv/Desktop/ICSH32/project1_test_2025-10-16-21-02-31/test1.txt
##OUTPUT    |/Users/ayaanv/Desktop/ICSH32/project1_test_2025-10-16-21-02-31/test2.txt
##OUTPUT    |/Users/ayaanv/Desktop/ICSH32/project1_test_2025-10-16-21-02-31/Sub/test1.txt
##EXPECTED  |/Users/ayaanv/Desktop/ICSH32/project1_test_2025-10-16-21-02-31/Sub/meee.txt
##          |                                                                   ^
