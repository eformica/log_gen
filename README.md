# log_gen
Gerador de logs automaticos de execucao, incluindo a chamada de cada metodo da classe decorada, tempo de execucao e tempo. 

Modo de uso:

#1 - Importar a classe LogGen e o metodo for_all_methods desse arquivo:

	from log_gen import log_gen

#2 - Instanciar um objeto LogGen:

	logs = LogGen("Logs do script X") #A mensagem e opcional

#3 - Usar os decorator for_all_methods e o metodo LogGen.decorator para gerar os logs sobre a classe desejada:

	@for_all_methods(logs.decorator)
	class ClasseDeExemplo:
		def __init__(self):
			...

			logs.lprint("Aviso importante sobre a execucao: ...") #4 - O metodo .lprint() da o print de uma mensagem tambem a adicionando no arquivo de log.

			print(logs.get_logs()) #5 - Para capturar os logs gerados, usar o metodo .get_logs().
		...
