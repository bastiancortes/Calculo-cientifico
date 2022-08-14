def mult(x, res) :
    res = res
    res_size=len(res)
    carry = 0  
    i = 0
    while i < res_size :
        prod = res[i] *x + carry
        res[i] = prod % 10; 
        carry = prod//10; 
        i = i + 1
 
    while (carry) :
        res.append( carry % 10)

        carry = carry // 10
    return res
 


 

def potencia(x,k):
	start=[1]
	while k>=1:
		start = mult(x,start)
		k=k-1
	return start
def factorial(n):
	start = [1]
	while n>=1:
		start = mult(n,start)
		n=n-1
	return start

if __name__ == '__main__':

	#print(mult(7,[7,2,0,1,2][::-1])[::-1]) solo testeo
	number_1=str()
	number_2 = str()
	number_3 = str()


	part_1 = mult(4002,factorial(1000))[::-1]
	part_2 = potencia(4,999)[::-1]

	for i in part_1:
		number_1 = number_1+str(i)
	#print(number_1) # ACA OBTENEMOS 1000! * 4002


	for i in part_2:
		number_2 = number_2+str(i)
	#print(int(number_2)) #ACA OBTENEMOS 4^999

	
	part_3 = mult(int(number_2),part_1[::-1])[::-1]

	for i in part_3:
		number_3 = number_3 + str(i)
	#print(number_3) # ACA OBTENEMOS 4^999 * 1000! *4002
