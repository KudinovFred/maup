import pickle


t1 = {"jlk":"jkhk"}

s = pickle.dumps(t1)

#save in memory
t2 = pickle.loads(s)
print(t2)


my_file = open("text.txt", "wb")
pickle.dump(t1, my_file)

my_file = open("text.txt", "rb")
x = pickle.load(my_file)

print(x["jlk"])




import shelve

shelf = shelve.open("text.txt")


shelf["key"] = [1,2,3,4]
shelf["key"].append(5)
print(shelf["key"])


lst = shelf["key"]
lst.append(4)
shelf["key"] = lst
print(shelf["key"])