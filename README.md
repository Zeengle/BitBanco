# BitBanco
Projeto de pyhon para a criação de um banco ficticio de compra de criptomoedas

CC1612 - FUNDAMENTOS DE ALGORITMOS
Projeto de fundamentos de algoritmos: Documentação (Manual de 
instruções do projeto)

1. Início:
1.0 - Introdução dos dados:
> Aqui é onde o usuário informa seus dados para ter acesso ao menu de investimentos do 
aplicativo.
> Colocados nesta seguinte ordem, com o CPF contendo 11 dígitos e a senha com 6 
dígitos numéricos como dito na imagem acima, após isso, o investidor terá acesso ao 
menu de investimentos.

2. Menu:
2.0 - Menu inicial de investimentos:
> Esse é o menu inicial do investidor:
> Aqui, o usuário poderá escolher qualquer aba acima que queira acessar apenas 
digitando o número correspondente a cada aba, tornando a navegação simples e prática, 
como por exemplo o investidor quer acessar a aba “Depositar”, apenas digite “3” que você 
será redirecionado a página correspondente.

2.1 - Consultar Saldo:
> Ao entrar na aba “Consultar saldo”, é pedido a senha do usuário.
> Depois que o acesso é concedido, aparece ao investidor todos os seus saldos 
disponíveis na conta.
> Para voltar a aba de menu do investidor, apenas digite qualquer tecla do teclado e envie.

2.2 - Consultar extrato:
> Ao acessar a aba de “Consultar extrato” é pedido a senha do usuário.
> Depois do acesso ser concedido, é mostrado ao usuário todas suas ações realizadas no 
programa, dês da criação do usuário.
> Todas essas informações são salvas em um arquivo .json em tempo real, assim, 
podendo analisar extratos feitos a dias atrás pelo mesmo usuário.

2.3 - Depositar:
> Quando o usuário acessar a aba de deposito, é mostrado ao investidor seus reais atuais 
e qual o valor que ele deseja depositar, que será automaticamente adicionado a sua 
conta. Caso não deseje depositar nada, apenas digite “0”.

2.4 - Sacar:
> Quando o usuário acessar a aba de saque, é mostrado ao investidor seus reais atuais e 
qual o valor que ele deseja retirar, que será automaticamente removido de sua conta.
Caso não deseje retirar nada, apenas digite “0”.

2.5 - Comprar criptomoedas:
> Ao acessar a aba de “Comprar criptomoedas” é pedido a senha do usuário.
> Quando o acesso for permitido, é mostrado ao investidor o seu saldo, a cotação das 
criptomoedas que são utilizadas e pergunta ao usuário qual moeda deseja comprar.
> Após isso é questionado ao investidor qual criptomoeda deseja comprar, entre Bitcoin, 
Ethereum e Ripple, que suas respectivas abas são acessadas ao digitar a letra B, E ou R.
> Ao selecionar uma criptomoeda desejada é mostrado os reais disponíveis, a cotação da 
moeda novamente, junto com a quantidade atual que o usuário possui. Caso não deseje 
comprar nada, apenas digite “0”.
> Depois do usuário digitar os reais que deseja gastar na moeda, a quantidade da 
criptomoeda escolhida é adicionada de acordo com sua cotação e sua taxa é cobrada 
automaticamente do investidor, após isso é mostrado seu saldo após a compra.

2.6 - Vender criptomoedas:
> Ao acessar a aba de “Vender criptomoedas” é pedido a senha do usuário.
> Funciona com a mesma dinâmica da compra de bitcoins.
> Ao selecionar uma criptomoeda desejada é mostrado a cotação da moeda novamente, 
junto com a quantidade atual que o usuário possui.
> Depois do investidor digitar o número de criptomoedas que deseja vender, a taxa é 
cobrada automaticamente junto com a cotação da moeda. Após isso é mostrado seu saldo 
atual. Caso não deseje vender nada, apenas digite “0”.

2.7 - Atualizar cotação:
> Ao acessar a aba “Atualizar cotação”, as cotações de todas as três criptomoedas 
trabalhadas atualizam automaticamente e mostram ao usuário seu valor atual depois da 
mudança, agora com os valores mudados, o usuário pode comprar criptomoedas mais 
baratas e vender quando estiverem mais caras.

2.8 - Sair:
> Quando o usuário desejar fechar o programa, apenas digite “8” no menu de investidor que 
o programa será fechado.
