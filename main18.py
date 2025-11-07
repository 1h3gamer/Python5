student_data = {
    'id1':{
        'name':['Sara'],
        'class':['V'],
        'subject':['science','math','history']
    },
    'id2':{
        'name':['David'],
        'class':['V'],
        'subject':['science','math','history']
    },
    'id3':{
        'name':['Sara'],
        'class':['V'],
        'subject':['science','math','history']
    },
    'id4':{
        'name':['Charlie'],
        'class':['V'],
        'subject':['science','math','history']
    },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key]=value

print(result)