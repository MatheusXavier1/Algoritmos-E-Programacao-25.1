def serieMatematica(n,a,b,c):
	output = 0
	for i in range(n+1):
		if i>0:
			output+=(-1)**(c+i) * (1+a*i)/(3*(b**i))
	return round(output,3)
print(serieMatematica(1,1,1,1))

