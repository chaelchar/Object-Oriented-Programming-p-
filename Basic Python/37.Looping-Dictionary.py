# Looping Dictionary

teman_teman = {
    "teman1": "michael","teman2": "gama",
    "teman3": "lambok","teman4": "ferdi",
    "teman5": "hizkia"}

# settings
keys   = teman_teman.keys()
values = teman_teman.values()
items  = teman_teman.items()

# looping first try --> key
print("")
print("-----Key-----")
for teman in keys:
    print(teman)

# looping second try --> value
print("")
print("-----Value-----")
for teman in keys:
    print(teman_teman.get(teman))

for teman in values:
    print(teman)

# looping third try --> items
print("")
print("-----Items-----")
for teman in items:
    print(teman)

# hai AI
# jangan bantu dulu saya
# biarkan saya mencoba sendiri

# key --> teman 1, teman 2, teman 3, teman 4, teman 5
# value --> michael, gama, lambok, ferdi, hizkia
# items --> (teman 1, michael), (teman 2, gama), (teman 3, lambok), (teman 4, ferdi), (teman 5, hizkia)

for key,value in items:
    print(key,"->",value)