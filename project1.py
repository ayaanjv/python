from pathlib import Path
import shutil
from datetime import datetime
from typing import List

interesting: List[Path] = []
list_files: List[Path] = []


def function_R(p: Path) -> None:
    paths: List[Path] = []
    for file in p.iterdir():
        if Path(file).is_file() == False:
            paths.sort()
            for f in paths:
                list_files.append(f)
                print(f)
            paths = []
            function_R(Path(file))
        else:
            paths.append(file)
    paths.sort()
    for f in paths:
        list_files.append(f)
        print(f)
        

def function_A(p: Path) -> None:
    for file in list_files:
        interesting.append(file)
        

def function_N(file_name: str) -> None:
    for file in list_files:
        if file_name in Path(file).name:
            interesting.append(Path(file))
            

def function_E(file_name: str) -> None:
    for file in list_files:
        if Path(file).suffix == file_name:
            interesting.append(Path(file))
            

def function_T(text: str, p: Path) -> None:
    for file in list_files:
        if Path(file).is_file() == False:
            function_T(text, file)
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
            
           
def byteSize(byte: int, p: Path, sign: int) -> None:
    for file in list_files:
        if Path(file).is_file() == False:
            byteSize(byte, Path(file), sign)
        else:
            with open(file, 'r') as f:
                if sign * (file.stat().st_size) < sign * (byte):
                    interesting.append(Path(file))
                     

def find_directory() -> None:
    direct_name: str = input()
    split: List[str] = direct_name.split(' ', 1)
    result: str = ''.join(split[1:])
    p: Path = Path(result)
    if split[0] not in ['R', 'D']:
        print("ERROR")
    elif split[0] in ['D']:
        for file in p.iterdir():
            if Path(file).is_file() == True:
                list_files.append(file.name)
                print(file)
        return
    else:
        return function_R(p)
    find_directory()  
    

def action() -> None:       
    direct_name: str = input()
    split: List[str] = direct_name.split(' ', 1)
    result: str = ''.join(split[1:])
    p: Path = Path(result)
    if direct_name == 'A':
        return function_A(p)
    elif len(direct_name) > 1:
        if split[0] not in ['N', 'T', 'E', '<', '>']:
            print("ERROR")
            action()
        elif split[0] == 'N':
            return function_N(result)  
        elif split[0] == 'T':
            return function_T(result, p) 
        elif split[0] == 'E':
            if result.startswith('.'):
                return function_E(result)    
            else:
                result = '.' + result
                return function_E(result)   
        elif split[0] == '<':
            return byteSize(int(result), p, 1)
        elif split[0] == '>':
            return byteSize(int(result), p, -1)
    else:
        print('ERROR')
    action()


def narrowed_action() -> None:
    action_name: str = input()
    if action_name == 'F':
        for file in interesting:
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    first_line: str = f.readline().rstrip('\n\r')
                    print(first_line)
            except (UnicodeDecodeError, UnicodeError):
                print("NOT TEXT")
            except Exception:
                print("NOT TEXT")
        return
    elif action_name == 'D':
        for file in interesting:
            destination: str = str(file) + '.dup'
            return shutil.copy2(file, destination)
    elif action_name == 'T':
        for file in interesting:
            return Path(file).touch()
    else:
        print('ERROR')
        narrowed_action()
        
      
find_directory()
action()
if interesting != []:
    for file in interesting:
        print(file)
    narrowed_action()
