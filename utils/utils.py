import ast
import re

def append_suffix(matched):
    tempstr = matched.group()
    tempstr = tempstr[0] + "\"" + tempstr[1:] + "\""
    return tempstr

def read_file(path, field):
    with open(path, "r", encoding='utf8') as f:
        data = f.read()
    
    data = data.replace("return", "").replace("=", ":").replace("[[", "\"").replace("]]", "\"")
    data = re.sub(r"[\[\]\. ]", "", data)
    data = re.sub(r"(\t|:)[a-zA-z0-9_]+", append_suffix, data)
    data = re.sub(r"\s+", "", data)
    with open("test.txt", "w", encoding="utf8") as f:
        f.write(data)
    data = ast.literal_eval(data)
    result = []
    for key, value in data.items():
        tmp = [key]
        for f in field[1:]:
            if isinstance(value[f], dict):
                tmp.append(value[f]['ja'])
            else:
                tmp.append(value[f])
        
        result.append(tuple(tmp))
    
    return result

def read_image(path):
    with open(path, 'r', encoding='utf8') as f:
        result = [tuple(l.split(' ')) for l in f]
    
    return result