# ============================================================
# 1) DOCSTRING: DOCUMENTAÇÃO EM PYTHON
# ============================================================
#
# DEFINIÇÃO
# ------------------------------------------------------------
# Docstring é uma string literal colocada logo após a definição de um módulo,
# pacote, classe, método ou função. Ela descreve o "o quê" e o "como usar".
# O interpretador armazena a docstring em __doc__, acessível via help().
#
# BOAS PRÁTICAS (PEP 257)
# ------------------------------------------------------------
# - A primeira linha deve ser um resumo curto no modo imperativo: "Calcula ..."
# - Linha em branco após o resumo;
# - Corpo com detalhes, parâmetros, retorno, exceções e exemplos, se fizer sentido;
# - Evite repetir detalhes óbvios; foque no comportamento, efeitos colaterais,
#   pré-condições (suposições) e pós-condições (garantias).
#
# ESTILOS DE DOCSTRING (3 populares)
# ------------------------------------------------------------
# A) reStructuredText (reST) — usado por Sphinx (muito comum)
# B) NumPy/SciPy (numpydoc) — popular em ciência de dados
# C) Google Style — simples e legível
#
# Abaixo, mostramos uma função com os 3 estilos como COMENTÁRIOS, para consulta.
#
# --- Exemplo do estilo reST (Sphinx) ---
# def exemplo_soma(operando_um: int, operando_dois: int) -> int:
#     """
#     Soma dois inteiros.
#
#     :param operando_um: primeiro operando.
#     :type operando_um: int
#     :param operando_dois: segundo operando.
#     :type operando_dois: int
#     :returns: a soma de "operando_um" e "operando_dois".
#     :rtype: int
#     :raises ValueError: se os argumentos não forem inteiros.
#
#     Exemplos:
#         >>> exemplo_soma(2, 3)
#         5
#     """
#     ...
#
# --- Exemplo do estilo NumPy/SciPy ---
# def exemplo_soma(operando_um: int, operando_dois: int) -> int:
#     """Soma dois inteiros.
#
#     Parameters
#     ----------
#     operando_um : int
#         Primeiro operando.
#     operando_dois : int
#         Segundo operando.
#
#     Returns
#     -------
#     int
#         A soma dos operandos.
#
#     Raises
#     ------
#     ValueError
#         Se os argumentos não forem inteiros.
#
#     Examples
#     --------
#     >>> exemplo_soma(2, 3)
#     5
#     """
#     ...
#
# --- Exemplo do estilo Google ---
# def exemplo_soma(operando_um: int, operando_dois: int) -> int:
#     """Soma dois inteiros.
#
#     Args:
#         operando_um (int): Primeiro operando.
#         operando_dois (int): Segundo operando.
#
#     Returns:
#         int: A soma dos operandos.
#
#     Raises:
#         ValueError: Se os argumentos não forem inteiros.
#
#     Examples:
#         >>> exemplo_soma(2, 3)
#         5
#     """
#     ...
#
# NOTE: Escolha UM estilo por projeto e mantenha consistência. Em ciência de dados,
#       o formato NumPy/SciPy é amplamente aceito e integra bem com Sphinx+numpydoc.
#
# ============================================================
# 2) DOCS EM MÚLTIPLOS NÍVEIS: MÓDULO, PACOTE, FUNÇÃO, SCRIPT
# ============================================================
# - Módulo: docstring no topo do arquivo .py descrevendo propósito, uso rápido,
#   dependências padrão e pontos de extensão.
# - Pacote: docstring em __init__.py para visão geral e "public API" via __all__.
# - Função: docstring com assinatura, efeitos, erros e exemplos.
# - Script/CLI: defina argparse para --help consistente com a docstring do módulo.
#
"""Documentação profissional em Python para ciência de dados.
Execute "python doctest.py --help" para ver a CLI de exemplo.
Execute "python -m pydoc doctest" para ver a documentação gerada.
"""
__author__ = "Tio Rafa"
__version__ = "2.0.1"
# Convencional e muito usada: torna fácil inspecionar a versão em runtime
# (mod.__version__). Normalmente segue SemVer (MAJOR.MINOR.PATCH).

__all__ = ["juros_simples", "juros_compostos", "taxa_efetiva"]
# Define a API pública do módulo para from modulo import *

__docformat__ = "restructuredtext"  # Sphinx-friendly
# Pista opcional para ferramentas de documentação indicando o formato das docstrings.

#
# TIP: __all__ define a "API pública" ao usar from modulo import * (desencorajado,
#      mas útil para sinalizar intenções). Ajuda também a ferramentas de docs.
#
# ============================================================
# 3) COMENTÁRIOS VS DOCSTRINGS
# ============================================================
# - Comentários (#): explicam intenções, decisões de design e "porquês" locais.
# - Docstrings: contrato e documentação externa para quem usa a API.
#
# Convenções úteis em comentários:
#   TODO: tarefa a fazer futuramente;
#   FIXME: algo conhecido como quebrado e que precisa de correção;
#   NOTE: anotação relevante para entendimento;
#   WARNING: riscos e armadilhas;
#   TIP: dica prática.
#
# Exemplo de uso correto de um comentário de multilinha:
#
# TODO (time-dados, 2025-08-15): Refatorar agregação.
#    - Extrair cálculo de métricas para "metrics.py"
#    - Cobrir com testes de borda (NaN, inf)
#    - Documentar no README (seção "Métricas")



# Níveis de warning:
#     Debug = 10
    
#     Info = 20
    
#     Warning = 30
    
#     Error = 40
    
#     Critical = 50
    
    
#------------------------------------------------------------------------------
#TIP: Aula 8 - 27/08


import argparse
import logging
import math
import sys
import textwrap
import warnings
from typing import Sequence, TypeAlias

#Define que queremos um logging de info ou superior
#levelname é warning, critical, etc
#ta escrito em documentação sphinx
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s%(levelname)s:%(name)s:%(message)s",
    force = True)
#Depois que se cria a configuração do logging, ela é permanentemente setada,
#mesmo que mude no código, não vai mudar no objeto. Pra modificar, é necessário
#usar force = True


logger1 = logging.getLogger('documentacao_avancada')
logger2 = logging.getLogger('qqrcoisa')

#ele está emitindo um aviso do nível info, debug, warning, etc de acordo com o 
#o que passamos para ele que deveria ser passado

# logger1.info("Tarefa Iniciada")
logger1.debug("Deveria ser invisível")
# logger1.warning("Período próximo ao limite para cálculo")
# logger1.error("Erro de parâmetro")


#criamos um tipo (como int, string, etc), porém, esse tipo novo é só um apelido
#para uma tupla com dois elementos floats
ResultadoFinanceiro:TypeAlias = tuple[float,float]

def juros_simples(capital:float,
                  taxa_percentual:float,
                  periodos:float) -> ResultadoFinanceiro:
    """ Calcula montante e juros em regime de juros simples.

    Parameters
    ----------
    capital : float
        Valor incial sobre o qual incidem os juros (precisa ser >= 0).
    taxa_percentual : float
        Taxa por período (5 significa 5%, precisa ser >= 0).
    periodos : float
        Número de períodos (precisa ser >= 0).

    Returns
    -------
    tuple[float, float]
        (montante, juros), ambos arredondados para duas casas decimais.


    Raises
    -------
    ValueError
        Se qualquer parâmetro for negativo.

    """
    if capital < 0 or taxa_percentual < 0 or periodos < 0:
        raise ValueError("Parâmetros negativos não são aceitos.")
    
    juros = capital*(taxa_percentual/100.0) * periodos
    montante = capital + juros
    
    return (round(montante, 2), round(juros, 2))


def juros_compostos():
    pass
def taxa_efetiva():
    pass


def demonstracao_pydoc_help() -> None:
    print("#"*60)
    print("Demonstração de help() e __doc__")
    print(" - help(juros_simples): ")
    help(juros_simples)
    primeira_linha = juros_simples.__doc__
    if isinstance(primeira_linha, str):
        primeira_linha = primeira_linha.strip().splitlines()[0]
        print(" - Primeira linha da docstring de juros simples:\n", 
              primeira_linha)

#demonstracao_pydoc_help()

#Essa parte mostra todos os handlers dentro do logging que configuramos
# for index_, handler_ in enumerate(logging.getLogger().handlers):
#     print(index_, type(handler_), getattr(handler_.formatter, "_fmt", None))

#-----------------------------------------------------------------------------
#TIP: aula 10 - 03/09

def construir_parser() -> argparse.ArgumentParser():
    """ Cria um parer de linha de comando para deonstração
    
    Retorna um parser com subcomandos:
     - simples : calcula juros simples.
    """
    
    parser_principal = argparse.ArgumentParser(
        prog= "aula de documentação", #nome do parser
        description= "Exemplo de CLI documentada utilizando Argparse",
        formatter_class= argparse.RawDescriptionHelpFormatter(), 
        #vai ser usado pelo parser para saber como ler uma string
        epilog= textwrap.dedent(
            """
            Exemplos:
                python doctest.py simples --capital 1000 --taxa 5 --tempo 2
            """))
            
    #para cada comando que queremos, adicionamos um subparser
    #aqui, falamos que dentro do parser tem um subparser (dentro de um cara que
    #faz algo tem outros carinhas que fazem coisas)
    #esse nome comando vai ter um comando como "simples", "composto", etc
    subcomandos = parser_principal.add_subparsers(dest="nome_comando", 
                                                  required= True)
    
    #esse parser busca dentro da string principal o comando simples, sempre que
    #ele encontra o simples, ele cria um subcomando em que nome_comando é simples
    parser_simples = subcomandos.add_parser(
        "simples", 
        help="Calcula montante e juros em regime de juros simples")
    #o parser simples vai pegar tembém os argumentos abaixo
    parser_simples.add_argument("--capital", 
                                type = float, 
                                required = True, 
                                help ="Valor inicial sobre o qual incidem os juros")
    parser_simples.add_argument("--taxa", 
                                type = float, 
                                required = True,
                                help = "Taxa por período (em porcentagem)")
    parser_simples.add_argument("--tempo", 
                                type = float, 
                                required= True,
                                help = "Tempo da aplicação em juros simples")
    
    return parser_principal

#saída 0 significa sucesso, qualquer coisa diferente significa falha
def executar_CLI(lista_argumentos : Sequence[str]) -> int:
    """
    Executa a CLI de demonstração

    Parameters
    ----------
    lista_argumentos : Sequence[str]
        Argumentos recebidos via CLI.

    Returns
    -------
    int
        Código de saída (0 para sucesso).

    """
    
    #criamos o parser e chamamos o método parse_args, onde tem os argumentos
    #do parser
    parser_principal = construir_parser()
    argumentos = parser_principal.parse_args(lista_argumentos)
    
    #os nomes do parametros vão ser os pegados em parse
    #é bom que se padronizem os nomes!!!!!!!!!!!!!!!
    if argumentos.nome_comando == "simples":
        montante, juros = juros_simples(argumentos.capital, 
                                        argumentos.taxa, 
                                        argumentos.tempo)
        print(f"Montante: {montante:.2f} e Juros = {juros:.2f}")
    else:
        parser_principal.error("Subcomando desconhecido.")
    
    return 0

def main() -> int:
    pass
#vai ficar pra proxima aula mas vai ser a função que o driver code vai chamar

#main retorna um inteiro, se chamamos main usando systemexit no raise, forçamos
#que o retorno da main vá para o sistema operacional como status de saída do seu
#programa. Seu programa ta executando mas o raise fica no ar pq a main ainda ta 
#rodando o return da main vai pro system exit e ele é uma exceção que quebra o 
#programa, levando pro SO o que foi retornado
if __name__ == "__main__":
    print("Versão do módulo:", __version__, "\n")
    raise SystemExit(main())
    
    
#TODO: fazer as funções de juros compostos e taxas efetivas, e integrar eles a
#tudo o que fizemos, como por exemplo no parser.
#padronizar nomes de variáveis
#colocar raise, exceção, documentação e etc etc etc
#criar o main para executar o código! ela retorna 0 ou 1: ela pega os argumentos 
#que vieram no seu programa e executa a cli