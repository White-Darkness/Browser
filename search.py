from googlesearch import search
print("If you having any doubt then run README.md file")
data = input("Search here : - ")

for i in search(data, 50, advanced=True):
     print(i.url)
     print()
     print(i.title)
     print()
     print(i.description)
     print()
     print()
