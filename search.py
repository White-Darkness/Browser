from Googlesearch import search
data = input("Search here : - ")

for i in search(data, 25, advanced=True):
     print(i.url)
     print(i.title)
     print(i.discription)
     print()
     print()
