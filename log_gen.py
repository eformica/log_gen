from datetime import datetime

"""
Gerador automatico de logs de execucao

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

"""

def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__: # there's propably a better way to do this
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate

class LogGen:
    def __init__(self, msg=""):
        #variavel onde os logs serao armazenados:
        self.__logs = ""
        
        if msg is not None:
            self._add_msg_log(msg)
    
    def _add_func_log(self, func, args, kwargs, status=None):
        registro = f"{datetime.now()} Funcao: '{func.__name__}', args: {args[1:]}, kwargs: {kwargs} Status '{status}'"
        self.__logs += "\n" + registro
        
    def _add_msg_log(self, msg):
        registro = f"{datetime.now()} {msg}"
        self.__logs += "\n" + registro

    def lprint(self, msg):
        print(msg)
        self._add_msg_log(msg)

    def decorator(self, func):
        def wrapper(*args, **kwargs):
            self._add_func_log(func=func, args=args, kwargs=kwargs, status="Iniciado")
            try:
                res = func(*args, **kwargs)
                self._add_func_log(func=func, args=args, kwargs=kwargs, status="OK")
                return res
            
            except Exception as err:
                self._add_func_log(func=func, args=args, kwargs=kwargs, status=err)
                print(err)
                
        return wrapper
    
    def get_logs(self):
        self._add_msg_log("Log gerado.")
        return self.__logs

#-----------------------TESTS-----------------------

if __name__ == "__main__":
    Log = LogGen("Pipeline")

    @for_all_methods(decorator=Log.decorator)
    class C:
        def __init__(self):
            pass

        def m1(self):
            print("afsfsafsaf")
            pass

        def m2(self, x):
            raise Exception("ERRO")


    X = C()

    X.m1()

    X.m2()

    Log.get_log()

    #X.m2(2)
