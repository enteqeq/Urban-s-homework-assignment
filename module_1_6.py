my_dict = {"Mark" : 1984, "Pavel" : 1984, "Steve" : 1978}
print(my_dict)
print(my_dict.get("Mark"))
print(my_dict.get("Adeline"))
del my_dict["Steve"]
print(my_dict.get("Steve"))
print(my_dict)

my_set = {0, 0, 1, 1, "Song", "Movie", "Song",}
print(my_set)
my_set.add("Food"), my_set.add(5)
print(my_set)
my_set.remove("Song")
print(my_set)