class GrumpyDict(dict):
    def __repr__(self):
        print("none of your business")
        return super().__repr__()

    def __missing__(self, key):
        print(f"you want {key}? it ain't here")

    def __setitem__(self, key, value):
        print(("you want to change dict?"))
        print(("okay..fine"))
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("No, it ain't here")
        return False


data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data["city"] = "Tokyo"
print(data)
"city" in data
