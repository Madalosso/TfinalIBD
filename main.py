from sys import argv

script, filename = argv
tabela = open(filename)

#retorno
sqlRetorno = ""

#le arquivo
with open(filename) as f: 
	#le o conteudo do arquivo para lista de strings
	content = f.readlines()
	line = content[0].split();

	if line[0] != 'SELECT':
		print "Erro!"
		print "Consultas devem iniciar com o termo 'SELECT'\n"
		exit()

	#armazena argumentos que devem ser retornados.
	selects1 = line[1].split(',')

	#caso os argumentos nao tenham sido declarados.
	if len(selects1)==0:
		print "Erro!"
		print "Eh necessario especificar quais argumentos devem ser retornados pela pesquisa"
		exit()

	#verificar se a linha termina ou nao (tratar casos de quando a consulta
	#eh feita toda em uma linha?)(tratar professor sacaneando)
	line = content[1].split();
	if line[0] == 'FROM':
		nomeTabela1 = line[1];
		#print "Nome tabela1 : %r" % nomeTabela1
		with open(nomeTabela1) as tabela1:
			contentTabela1 = tabela1.readlines()
			for l in contentTabela1:
				words = l.split(',')

				for nArg in selects1:
					#print "Argumentos requisitados: %r" % nArg
					sqlRetorno+=words[int(nArg)-1]

					#tentar remover o ',' de cada ultima linha de resultado.
					sqlRetorno+=","
				sqlRetorno+="\n"


			#if line[0] == 'WHERE': 
			#tratar where depois de resolver o UNION

	else:
		print "Erro!"
		print "NAO TEM FROM"
	line = content[2].split();




	print sqlRetorno