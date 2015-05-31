import sys

keyWords = ["SELECT","FROM","WHERE","UNION"]
sqlReturn = ""
campos

def getResultFromSelect(string,cont):
	termos = string.split(" ")

	if termos[0]=="SELECT":


		if string.find("FROM")!=-1:
			

		else:
			print "Erro!\n A query %d nao possui o FROM da consulta" % cont
	else:
		print "Erro!\n A query %d nao possui o SELECT da consulta" % cont
	return 0

def main(argv):
	#CONSULTA COMPOSTA POR : SELECT * FROM * WHERE * UNION

	queryFileName = argv[1]
	with open(queryFileName) as q:
		data=q.read().replace('\n', ' ')
		queries = data.split("UNION")
		cont=0
		for q in queries:
			getResultFromSelect(q,cont)
			cont+=1
		print queries


if __name__ == "__main__": main(sys.argv)