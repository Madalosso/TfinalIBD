from sys import argv
script, filename = argv
tabela = open(filename)

print "Nome do arquivo: %r"  % filename
print tabela.read()