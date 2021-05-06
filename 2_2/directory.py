from database import Simpledb
db = Simpledb('recipes.txt')
def recipe():
    print('What would you like to do: add, find, delete, update, print, or quit?')
    res=input().lower()
    if res.startswith('a'):
        print('Enter a recipe')
        key=input().upper()
        print ('Enter the ingredients')
        value=input()
        db.insert(key, value)
        print('Info added')
        recipe()
    elif res.startswith('f'):
        print('Enter a recipe')
        key=input().upper()
        val=db.select_one(key)
        print(val)
        recipe()
    elif res.startswith('d'):
        print('Enter a recipe. If a message is not returned, there is no matching name in the directory.')
        key=input().upper()
        db.delete(key)
        recipe()
    elif res.startswith('u'):
        print('Enter a recipe')
        key=input().upper()
        print('Enter the new ingredients. If a message is not returned, there is no matching recipe in the directory.')
        value=input()
        db.update(key, value)
        recipe()
    elif res.startswith('p'):
        db.__repr__()
        recipe()
    elif res.startswith('q'):
        pass
    else:
        recipe()
recipe()