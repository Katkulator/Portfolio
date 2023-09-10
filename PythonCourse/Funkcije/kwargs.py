def fav_colors(**kwargs):
    for person,color in kwargs.items():
        print(f"{person}'s favorite color is: {color}")

fav_colors(Matko="Ljubičasta", Matija="Zelena",Netko="Nešto")

def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"]=="special":
        return "You get a special greeting, David."
    elif "David" in kwargs:
        return "Hello David"
    return "I don't know who you are?"

# print(special_greeting(David="special"))
# print(special_greeting(David="Hello"))
# print(special_greeting(Mike="Whatsup"))
print(special_greeting(Heather="Hello",David="special"))


#Write a function called combine_words  which accepts a single string called word
#and any number of additional key word arguments.  If a prefix is provided,
#return the prefix followed by the word.  If a suffix is provided,
#return the word followed by the suffix.  If neither is provided, just return the word. 
#It might sound confusing, but the examples should make this a lot clearer!
#combine_words("child", prefix="man")  #'manchild'

def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "sufix" in kwargs:
        return word + kwargs["sufix"]
    return word

print(combine_words("child"))
print(combine_words("child", prefix="man"))
print(combine_words("child", sufix="ish"))
print(combine_words("work", sufix="er"))
print(combine_words("work", prefix="home"))




def calculate(**kwargs):
    operations = {
        "add" : kwargs.get("first", 0) + kwargs.get("second",0),
        "subtract" : kwargs.get("first",0) - kwargs.get("second",0),
        "divide" : kwargs.get("first",0) / kwargs.get("second",0),
        "mulitply" : kwargs.get("first",0) * kwargs.get("second",0)
    }

    is_float = kwargs.get("make_float",False)

    operation_value = operations[kwargs.get("operation", "")]

    if is_float:
        final =   f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final =  f"{kwargs.get('message','The result is')} {int(operation_value)}"
    return final


print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))