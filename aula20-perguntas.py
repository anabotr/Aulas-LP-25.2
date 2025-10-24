"""
1 -	Siga a execução da função transfer().
	Identifique quais funções são chamadas e quais dados são passados entre 
    elas.
    
A função transfer chama find_account, que recebe como argumento o id de contas 
(passagem entre transfer e find_account).
Além disso, em caso de sucesso da transação, usa a fução record_transaction, 
que usa o id de ambas as contas, o montante e a descrição para registrar a 
transferência no banco (passagem entre transfer e record_transaction).

    
2 - Quantas vezes o programa verifica se uma conta existe ou se o valor é 
    positivo?
    Que problema isso causa?

Ele verifica se a conta exite 5 vezes (withdraw, transfer - 2, deposit, 
print_account_summary) e se o valor é positivo 3 vezes (withdraw, transfer, 
deposit).
O problema é que há dificuldade de testar o código - como o comportamente está 
em várias partes, é difícil saber aonde está o erro. Ainda, é muito difícil 
modificar/fazer a manutenção deste trecho, tendo em vista que ela está em 
vários lugares.
Código duplicado aumenta a chance de errar: se precisarmos modificar, vai ser 
muito difícil fazer com excelência em todas as aparições do trecho.
A inconsistência é um problema.


3 - O sistema usa uma variável global bank_data.
    Quais são os possíveis problemas dessa abordagem?
    
Está faltando encapsulamento, não há um limite claro de quem pode ou quem deve 
modificar o que. Não está claro quem deveria modificar e o que cada um pode 
modificar - isso pode causar erros.
A ideia é que devemos proteger os dados da nossa aplicação.
É muito difícil testar partes do código isoladas, porque elas usam uma variável
global que pode ser modificada por algum outro método.
Acomplamento forte: todas as funções depende de um estado globla - se eu quiser
usar outro estado global, será necessário reescrever todo o código: se eu mudar
o banco de dados terei que mudar todo o código. Isso significa que estpa tudo 
acoplado, um depende do outro.
Deveríamos usar o BAIXO acoplamento, tentando fazer essa dependência mínima e 
ALTA coesão -> bom encapsulamento.

4 - Onde estão representadas as responsabilidades de "Account" e "Customer"?
    Seria melhor movê-las para outro lugar?

Responsabilidades são as tarefas que alguma unidade deveria executar.
O cliente tem responsabilidade dos próprios dados e das contas associadas a 
eles. O banco (account) tem como responsabilidades de fato as ações bancárias: 
transferência, depósito, etc..
O problema aqui, é a falta de coesão, porque nesta aplicação não temos papéis 
bem definidos. 
Não sabemos que parte do banco deveria cuidar por exemplo, das transferências.
Ainda, há baixa legibilidade porque, para entender como algo funciona, 
precisamos ler várias partes do código - funções, banco de dados...
Não há também garantia de consistência: podem ocorrer vários erros.
O que resolve isso é o princípio de responsabilidade única: um tema/unidade 
deve ter uma responsabilidade clara e que é dele, e apenas dele. Isso ajuda a 
entender o código, testar, resolver problemas.
"""