def name(str):
    def txt():
        print(str)
        txt()


print(name("Naresh"))