try:
    a=10
    print (a)
    raise NameError("Hello")
except NameError as e:
		print ("Mot Exception xuat hien")
		print (e)