a = int(input('Enter the number:'))
for i in range(2, a):
    if a % i == 0:
        print(a,'is not prime because',
              i,'x',a//i,'=',a)
        break
else:
    print(a,'is prime')
