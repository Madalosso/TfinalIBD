import sys

keyWords = ["SELECT","FROM","WHERE","UNION"]

#remove espacos em branco da query retorna lista de termos
def getTermos(string):
	termos = string.split(" ")
	n = len(termos)
	i=0
	while i<len(termos):
		if termos[i]=="":
			termos.pop(i)
			i-=1
		i+=1
	return termos
	

def getResultFromSelect(string,cont):
	returnSQL = ""
	
	termos = getTermos(string)
	
#verifica existencia da clausula SELECT
	if termos[0]=="SELECT":

#lista os indices dos campos a serem recuperados
		campos = termos[1].split(',')

#verifica a existencia do FROM
		if termos[2]=="FROM":

#obtem nome do arquivo(tabela)
			nomeTabela = termos[3]
			with open(nomeTabela) as tabela1:
#abre tabela e le arquivo, para cada linha, adiciona o indice desejado na string de retorno
				dataTable1 = tabela1.readlines()
				for line in dataTable1:
					reg = line.split(',')
					for nArgs in campos:
						returnSQL+=reg[int(nArgs)-1]
						returnSQL+=", "
					returnSQL+="\n"
		else:
			print "Erro!\n A query %d nao possui o FROM da consulta" % cont
	else:
		print "Erro!\n A query %d nao possui o SELECT da consulta" % cont
	return returnSQL

def clearDuplicates(s):
	unicos = list(set(s))
	unicos.remove("");
	return unicos



def main(argv):
	#CONSULTA COMPOSTA POR : SELECT * FROM * WHERE * UNION
	sqlReturn = ""
	queryFileName = argv[1]
	#abre arquivo com consulta
	with open(queryFileName) as q:
		#le arquivo inteiro como uma unica string e separa as diferentes consultas
		data=q.read().replace('\n', ' ')
		queries = data.split("UNION")

		#executa cada consulta separadamente e une os resulados
		cont=0
		for q in queries:
			print q
			sqlReturn += getResultFromSelect(q,cont)
			cont+=1

		# sqlReturn = list(set(sqlReturn))
		sqlReturn = clearDuplicates(sqlReturn.split('\n'))

		#retorno da consulta
		for l in sqlReturn:
			print l


if __name__ == "__main__": main(sys.argv)