from pathlib import Path
interesting=[]
list_files=[]



def function_R (p):
    for file in p.iterdir():
        if Path(file).is_file()==False:
            function_R(Path(file))
        print(file)
        list_files.append(Path(file).name)
def function_A(p):
    for file in p.iterdir():
        if Path(file).is_file()==False:
            function_A(Path(file))
        interesting.append(Path(file))
def function_N(file_name):
    for file in list_files:
        if Path(file).name==file_name:
            interesting.append(Path(file))
def function_E(file_name):
    for file in list_files:
        if Path(file).suffix==file_name:
            interesting.append(Path(file))
def function_T(text, p):
    for file in p.iterdir():
        if Path(file).is_file()==False:
            function_T(text,Path(file))
        else:
            with open(Path(file), 'rb') as f:
                file_content = Path(file).read_bytes()
                if text.encode('utf-8') in file_content:
                    interesting.append(Path(file))
def byteSize(byte, p, sign):
    for file in p.iterdir():
        if Path(file).is_file()==False:
            byteSize(byte,Path(file),sign)
        else:
            with open(Path(file), 'r') as f:
                if sign*(Path(file).stat().st_size)<sign*(byte):
                    interesting.append(Path(file))
                     
while True:
    direct_name=input()
    split=direct_name.split(' ',1)
    result=''.join(split[1:])
    p=Path(result)
    if split[0] not in ['R', 'D']:
        print("ERROR")
    elif split[0]in['D']:# D function
        for file in p.iterdir():
            if Path(file).is_file()==True:
                list_files.append(file.name)
                print(file)
                list_files.append(file)
        break
    else:
        function_R(p)
        break
    
while True:       
    direct_name=input()
    split=direct_name.split(' ',1)
    result=''.join(split[1:])
    p=Path(result)
    if direct_name='A':
        function_A(p)
    if len(direct_name)>1:
        if split[0] not in ['N', 'T', 'E', '<','>']:
            print("ERROR")
        elif split[0]=='N':
            function_N(result)
            break
        elif split[0]=='T':
            function_T(result,p)
            break
        elif split[0]=='E':
            if result.startswith('.'):
                result='.'+result
                function_E(result)
                break
            else:
                function_E(result)
                break
        elif split[0]=='<':
            byteSize(int(num),p,1)
            break
        elif split[0]=='>':
            byteSize(int(num),p,-1)
            break
for file in interesting:
    print(file.name)
