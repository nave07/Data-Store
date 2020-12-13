#datastore CRD
import threading
import time
# dictionary for data store
dict = {}

# create operation
def createData(key, value, ttl=0):
    if key in dict:
        print("Key already exists")
    else:
        if (key.isalpha()):
            # constraints for file size
            if len(dict) < (1024 * 1020 * 1024)
                if value <= (16 * 1024 * 1024):
                    if ttl == 0:
                        l = [value, ttl]
                    else:
                        l = [value, time.time() + ttl]
                    if len(key) <= 32:
                        dict[key] = l
            else:
                print("ALERT : EXCEEDED MEMORY LIMIT")
        else:
            print("ALERT : INVALID KEY NAME")

#read operation
def readData(key):

    if key in dict:
        b = dict[key]
        if b[1] != 0:
            if time.time() < b[1]:
                stri = str(key) + ":" + str(b[0])
                return stri
            else:
                print("KEY EXPIRED")
        else:
            stri = str(key) + ":" + str(b[0])
            return stri

    else:
        print("ALERT : KEY NOT PRESENT")

# for modify operation
def modifyData(key, value):
    b = dict[key]
    if b[1] != 0:
        if time.time() < b[1]:
            if key in dict:
                l = []
                l.append(value)
                l.append(b[1])
                dict[key] = l
            else:
                print("ALERT : KEY NOT VALID")
        else:
            print("ALERT : KEY EXPIRED")
    else:

        if key in dict:
            l = []
            l.append(value)
            l.append(b[1])
            d[key] = l
        else:
            print("ALERT : KEY DOES NOT EXIST")

# delete operation

def deleteData(key):
    if key not in dict:
        print("ALERT : KEY DOES NOT EXIST")
    else:
        b = dict[key]
        if b[1] != 0:
            if time.time() < b[1]:
                del dict[key]
                print("KEY DELETED")
            else:
                print("ALERT : KEY EXPIRED")
        else:
            del dict[key]
            print("KEY DELETED")



# creates a key with a given value
createData("python", 35)
# creates a key with a given value with time to live property
createData("java", 85, 3000)
# returns error as key already exists
createData("python", 50)
# returns 'python:35'
readData("python")
# returns key if time to live is not expired
readData("java")
# modifies the key with new value
modifyData("python", 55)
# deletes the key and its value
deleteData("python")

# multiple threads
thread = Thread(target=(create or read or delete), args=(key_name, value, timeout))
thread.start()
thread.sleep()




