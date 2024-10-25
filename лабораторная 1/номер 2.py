discval = 1.44*1024*1024
str = 50
symb = 25
pages = 100
ansv = int(discval//(str*symb*pages*4))
print("Количество книг, помещающихся на дискету:", ansv)
