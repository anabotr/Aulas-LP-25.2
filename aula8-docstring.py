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
Execute "python 06_doctest_aula_02.py --help" para ver a CLI de exemplo.
Execute "python -m pydoc 06_doctest_aula_02" para ver a documentação gerada.
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

def juros_simples():
    pass
def juros_compostos():
    pass
def taxa_efetiva():
    pass


import argparse
import logging
import math
import sys
import textwrap
import warnings

from typing import Sequence, TypeAliasType


#Define que queremos um logging de info ou superior
#levelname é warning, critical, etc
#ta escrito em documentação sphinx
logging.basicConfig(level = logging.INFO, fomat = "%(levelname)s:%(name)s:%(message)s")
logger1 = logging.getLogger('documentacao_avancada')
logger2 = logging.getLogger('qqrcoisa')

#ele está emitindo um aviso do nível info
logger1.info("Tarefa Iniciada")
logger1.debug("Deveria ser invisível")
logger1.warning("Período próximo ao limite para cálculo")
logger1.error("Erro de parâmetro")

'''Níveis de warning:
    Debug = 10
    
    Info = 20
    
    Warning = 30
    
    Error = 40
    
    Critical = 50
    
    '''