#comment sau dau thang
print("Dang")
a,b,c=1,"tran dang",3.14
print(type(a))
type(b)
type(c)
#tring
#('' "" ''' """)
#cong chuoi( str1+str2)
#nhan chuoi(str1*5)
k ='t' in b #tra ve true,flase
d= b[1] #d= 'r'
e=len(b) #ham lay do dai
a=b[1:5:2] # vi tri 1:5 buoc nhay 2.-2 de lay nguoc chuoi
#ep kieu
s=int("69")
s=float(6.9)
s=str(60)
#dinh dang chuoi bang %
a= 'my team is %s %s' %('dang','2')
print(a)
#dinh dang chuoi
print("a,b,c %s" %('d')) # dung %s,d,r,f
value1='0123'
rs=f'b c :{value1}' #dung f-string
print(rs)

print('1:{1} 2:{0}'.format(1,2)) #dung fomat
print('1: {name} 2:{add}'.format(name='dang',add='hanoi'))
#can le {:(c)<n}
# (c) la ky tu ben canh, n so phan tu <,>,^
print('{:k^11}'.format('aaa'))