from googlesearch import search
print()
print("Instagram >> cyber_d_hkr")
print()
print("If you having any doubt then run README.md file")
print()
data = input("Search here : - ")

for i in search(data, 50, advanced=True):
     print(i.url)
     print()
     print(i.title)
     print()
     print(i.description)
     print()
     print()
