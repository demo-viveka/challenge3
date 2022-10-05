import json

def getValues(obj: dict, key: str):
    if (type(obj) is  dict):
        for x in obj.keys():
            if x==key:
                return obj[x]
            else:
                if (type(obj[x]) is dict):
                    return  getValues(obj[x],key)
                else :
                    return 'Key Doesnt Exist'
    else:
        return obj[key]    

if __name__ == '__main__':
    #obj = {"a":{"b":{"c":"d"}}}
    #key = 'z'
    obj = input("Enter Object:")
    obj = json.loads(obj)
    key = input("Enter Key:")
    if (type(obj) is not dict):
        print('Not a valid object')
    else :
        final_values = getValues (obj, key)
        print('Value : ',final_values)
