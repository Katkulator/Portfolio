print("Koliko kilometara ste odvezli danas?")
km = float(input())
milje = km/1.60934
milje = round ( milje, 2S) 
print(f"{km} kilometara je jednako {milje} milja.")

#data = input("What's your favourite color?")
#print ("You said" + data)

print("What's your favourite color?") #ovo printa input u drugom redu
data = input()
print ("You said " + data)
