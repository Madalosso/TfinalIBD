import sys

nCampos = -1

#remove espacos em branco da query retorna lista de termos
def getTermos(string):
	termos = string.split(" ")
	while "" in termos:
		termos.remove("")
	return termos
	

def getResultFromSelect(string,cont):
	returnSQL = ""
	global nCampos
	
	termos = getTermos(string)
	
#verifica existencia da clausula SELECT
	if termos[0]=="SELECT":

#lista os indices dos campos a serem recuperados
		campos = termos[1].split(',')
		for nCol in campos:
			t = int(nCol)
			if t<0:
				print "Erro\n Indice solicitado incorreto."
				exit(1)
		# print nCampos
		# print campos
		# print nCampos
		if(nCampos==-1):
			nCampos = len(campos)
		else:
			if(nCampos!=len(campos)):
				print "Erro!\n Diferente numeros de argumentos selecionados na consulta.\n"+"A primeira consulta seleciona "+str(nCampos)+" colunas. Na consulta "+str(cont+1)+", sao "+str(len(campos))+" colunas"
				exit(1)

#verifica a existencia do FROM
		if termos[2]=="FROM":

#obtem nome do arquivo(tabela)
			nomeTabela = termos[3]
			try:
				with open(nomeTabela) as tabela1:
	#abre tabela e le arquivo, para cada linha, adiciona o indice desejado na string de retorno
					dataTable1 = tabela1.readlines()
					for line in dataTable1:
						line = line.rstrip()
						reg = line.split(',')

						# print reg
						for nArgs in campos:
							t  = int(nArgs)-1
							if t > len(reg):
								print "Erro!\n Indice solicitado incorreto"
								exit(1)
							returnSQL+=reg[t]
							returnSQL+=", "
						returnSQL+="\n"
			except:
				print "Erro!\n Problema na leitura da tabela"
				exit(1)
		else:
			print "Erro!\n A query %d nao possui o FROM da consulta" % cont
			exit(1)
	else:
		print "Erro!\n A query %d nao possui o SELECT da consulta" % cont
		exit(1)
	return returnSQL

def clearDuplicates(s):
	unicos = list(set(s))
	unicos.remove("")
	return unicos



def main(argv):
	global nCampos;
	#CONSULTA COMPOSTA POR : SELECT * FROM * UNION
	sqlReturn = ""
	queryFileName = argv[1]
	#abre arquivo com consulta
	with open(queryFileName) as q:
		#le arquivo inteiro como uma unica string e separa as diferentes consultas
		data=q.read().replace('\n', ' ')
		queries = data.split("UNION")

		#executa cada consulta separadamente e une os resulados
		for i, q in enumerate(queries):
			sqlReturn += getResultFromSelect(q,i)

		# sqlReturn = list(set(sqlReturn))
		sqlReturn = clearDuplicates(sqlReturn.split('\n'))
		#retorno da consulta
		for l in sqlReturn:
			print l


if __name__ == "__main__": main(sys.argv)