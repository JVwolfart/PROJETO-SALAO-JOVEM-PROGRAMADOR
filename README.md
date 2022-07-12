# PROJETO-SALAO-JOVEM-PROGRAMADOR

Esse foi meu projeto final do Jovem Programador módulo 2

Esse projeto na verdade é uma evolução natural do projeto da padaria, pois me baseei bastante no projeto da padaria para desenvolver este projeto com inúmeras melhorias e também para que ele ficasse com um nível mais avançado do que o anterior (projeto da padaria).

Principais evoluções em relação ao projeto da padaria:
- Melhoramento da seção de estatísticas
- Inclusão de uma seção de agendamento, além de registro de venda pelo agendamento
- Sistema de fidelização de clientes
- Mais opções de consulta de registros

O projeto consiste basicamente em:
- Um cadastro de usuários (somente permitido a usuários com permissão ROOT)
- Permissão de acessos dependendo do nível do usuário
- Cadastro simples de clientes
- Cadastro de funcionários
- Cadastro de serviços
- Cadastro de formas de pagamento
- Registro de vendas (simula emissão de uma nota fiscal)
- Estatísticas dos dados
- Agenda de atendimentos

É utilizado o banco de dados Sqlite3.

Regra de negócio deste projeto:

O usuário deve ser cadastrado apenas pelo ROOT ou por algum usuário com permissões de ROOT, este por sua vez poderá, no momento do cadastro, ou a qualquer momento, setar as permissões dos demais usuários, incluindo dar a eles permissão de ROOT, as permissões possíveis são:

- Somente cadastro (permite apenas inserir novos clientes, produtos e formas de pagamento, além de alterar os que já existem, porém não é capaz de desativar ou reativar registros, nem de fidelizar ou desfidelizar clientes, pois essas funções são exclusivas do usuário com permissão de ROOT)
- Faturamento (permite, além do cadastro e manutenção de registros, o acesso a área de faturamento)
- Estatísticas (permite, além do cadastro e manutenção de registros, o acesso a área de estatísticas)
- Agenda (permite, além do cadastro e manutenção de registros, o acesso a área de agenda)
- ROOT (permite acesso a todo o sistema)

OBS: Um usuário pode acumular várias permissões de acordo com o que for setado pelo ROOT.

Assim como no projeto da oficina e da padaria, existe um superusuário que através dele poderá ser setado ao primeiro usuário cadastrado a permissão de ROOT e após isso esse primeiro usuário já pode setar as permissões aos demais usuários.

Ao entrar no sistema o usuário deve receber uma mensagem de boas vindas informando suas permissões.
De acordo com suas permissões será as opções que ele deve ter disponível na tela.

Caso seja apenas cadastro ele terá acesso apenas ao menu de cadastros de forma parcial, pois algumas funções não ficarão disponíveis, como por exemplo o cadastro de usuários, e também ele não poderá fazer desligamento ou reativação de registros, nem fidelização ou desfidelização de clientes, pois essas são prerrogativas apenas do ROOT.

Se a permissão for faturamento, ele vai poder, além das opções de cadastro, acessar a área de faturamento.

Se a permissão for estatísticas, ele vai poder, além das opções de cadastro, acessar a área de estatísticas.

Se a permissão for agenda, ele vai poder, além das opções de cadastro, acessar a área de agenda.

Caso o usuário tenha permissão de ROOT ele poderá setar as permissões para ele mesmo e os demais usuários, portanto 
se ele tiver a permissão de ROOT ele consegue fazer o que quiser no sistema.

Área de faturamento:

É a área responsável pelo registro das vendas, as opções são:

- Emissão de nota fiscal avulsa (quando o cliente é atendido sem agendamento)
- Emissão de nota fiscal pelo agendamento (quando o cliente fez um agendamento prévio e foi atendido e o setor de agenda libera para emissão automática da nota baseado nos dados do agendamento)
- Manutenção e consulta de notas fiscais (permite consultar notas emitidas e também fazer cancelamento de nota, ou em caso de notas pendentes de emissão, concluir a emissão da nota)

Quanto aos registros de venda (notas fiscais):

Para emitir o registro de venda avulsa, o usuário seleciona o cliente, e em seguida ele é direcionado para a tela onde vai adicionar os serviços e os funcionários que efetuaram os serviços, após adicionar todos os itens ele tem a opção de fechar a tela de emissão de notas, e com isso a nota ficaria com status de pendente, pois ela não foi emitida de fato, enquanto ela estiver pendente é considerado que a venda não se realizou ainda, e portanto o usuário pode entrar nela novamente, incluindo ou excluindo serviços, alterando dados da nota, após o usuário concluir ele deve emitir a nota, e com isso a nota passará pro status de emitida, e passará a constar como registro para as estatísticas, e a partir disso não será mais possível fazer nenhuma alteração na nota, a não ser o seu cancelamento (se o usuário tiver essa permissão). Ao cancelar a nota fiscal o seu status passa para cancelada, seu valor é zerado e ela automaticamente não é mais considerada nas estatísticas.

Para emitir o registro de venda por agendamento, o sistema aproveita os dados do agendamento para o registro da venda, bastando para isso que o setor de agendamento sinalize que o serviço já foi efetuado.

Detalhe importante: O ideal é que não hajam notas pendentes, pois o objetivo da nota é ser emitida, portanto, sempre que o usuário com permissões de faturamento entrar no sistema, ou fizer logout, o sistema verifica se existe alguma nota pendente e informa o usuário para que ele corrija.

Quanto a agenda:

Nesta área é possível fazer o agendamento de serviços, para isso deve informar a data prevista e então o sistema vai mostar todos os serviços agendados a partir daquela data selecionada, é possível também ver a agenda dos profissionais, e também ver todos os agendamentos pendentes.

O que são agendamentos pendentes?

Ao entrar no sistema, o sistema checa automaticamente todos os agendamentos anteriores a data atual do sistema que estejam com status de "Agendado", e altera seu status para "Pendente", pois por algum motivo a pessoa responsável por cuidar da agenda não alterou o status daquele agendamento até a data prevista para sua execução, pois quando o serviço é efetuado deve ser alterado o status da agenda de "Agendado" para "Serviço efetuado", ou caso o serviço não tenha sido efetuado por algum motivo, setar o status que justifique o agendamento.

Os status de agendamento possível são:
- Agendado (quando é feito o agendamento)
- Serviço efetuado (quando o serviço foi efetuado)
- Cancelado pelo cliente (quando o cliente cancela o agendamento, essa opção também pode colocar o cliente na lista negra, fazendo com que ele possa perder seu status de fidelizado)
- Cliente não compareceu (quando o cliente não comparece, e também não entra em contato para cancelar, essa opção também pode colocar o cliente na lista negra, fazendo com que ele possa perder seu status de fidelizado)
- Eliminar agendamento (quando o agendamento foi feito de forma errada, e precisa ser eliminado sem causar prejuízo ao cliente que fez o agendamento)
- Nota fiscal emitida (quando o serviço já foi efetuado e a nota já foi emitida pelo faturamento)
- Pendente (quando o agendamento, até sua data não obteve troca de status, ele é setado automaticamente pelo sistema para "Pendente")

Detalhe importante: Sempre que o usuário com status de agenda acessa o sistema, ou faz logout ele recebe o aviso se tem algo pendente, semelhante a como acontece com o usuário de faturamento, caso o usuário tenha as duas permissões, ele recebe ambos os avisos, do faturamento e da agenda.


Quanto as estatísticas:

As opções de estatísticas são:
- Estatísticas de vendas realizadas (leva em consideração apenas o que já foi emitido de notas fiscais)
- Estatísticas de projeções futuras baseadas na agenda (leva em consideração a previsão de faturamento baseado nos agendamentos, ou seja, aquilo que ainda não foi realizado, mas está agendado)
- Estatísticas de vendas por gênero (semelhante as estatísticas por vendas realizadas, porém levando em consideração apenas o gênero do cliente)
- Estatísticas de projeções futuras por gênero (semelhante as estatísticas de projeções futuras, porém levando em consideração apenas o gênero do cliente)

Todas as opções de estatísticas têm opções de consulta por todo o período, ou por intervalo de datas.

Opções das estatísticas de vendas realizadas:
- Total de vendas
- Ranking por serviço
- Ranking por cliente
- Ranking por profissional
- Ranking por forma de pagamento

OBS: Essas opções podem ser selecionadas para todo o período, que vai levar em conta todos os registros do banco de dados, ou apenas por um intervalo de datas que levará em conta apenas os registros que estão naquele intervalo de datas.


Opções das estatísticas de projeções futuras:

Nesta opção é necessário selecionar o intervalo de datas que deseja ver a previsão baseada na agenda, a data inicial precisa ser igual ou superior a data do sistema, e também selecionar a data final da estatística.
Com isso o sistema vai mostrar os seguintes dados:

- Previsão por dia
- Previsão por cliente
- Previsão por profissional

Também vai mostrar na última aba uma "lista negra" de clientes que cancelaram ou não apareceram em agendamentos, e esta informação pode ser útil para definir se o cliente pode perder o status de fidelizado, perdendo assim os descontos.

Estatísticas por gênero:

No caso das vendas realizadas vai mostrar o total por gênero, baseado nas vendas realizadas, e tem a opção de escolher intervalo de datas. 
No caso das projeções futuras, a mesma coisa, porém baseado nos agendamentos futuros.

Fidelização de clientes:

O ROOT tem a prerrogativa de fidelizar ou desfidelizar os clientes, de acordo com as regras de negócio estabelecida e também os dados estatísticos que o sistema fornece.
Quando o cliente é fidelizado ele possui a possibilidade de receber um desconto especial, que deve ser definido na hora do registro da venda pelo faturamento, esse desconto pode ser de 0 até 20% dependendo da regra de negócio.
Caso o cliente não seja fidelizado, no momento da emissão da nota não haverá a opção do desconto, mas caso ele seja fidelizado, no momento da emissão da nota vai aparecer um slider permitindo setar o percentual de desconto para o serviço a ser faturado.

Assim como no projeto da padaria, existem várias opções de consultas de vendas, que podem ser acessadas no menu faturamento, na opção manutenção de notas, são elas:

- Todas as notas (mostra as últimas 50 notas)
  - Todas as notas emitidas (mostra as últimas 50 notas emitidas)
  - Todas as notas pendentes (mostra as últimas 50 notas pendentes)
  - Todas as notas canceladas (mostra as últimas 50 notas canceladas)
- Notas por data da venda (selecionar a data desejada)
  - Todas as notas por data de venda
  - Notas emitidas por data de venda
  - Notas pendentes por data de venda
  - Notas canceladas por data de venda
- Notas por cliente (selecionar o cliente desejado)
  - Todas as notas por cliente
  - Notas emitidas por cliente
  - Notas pendentes por cliente
  - Notas canceladas por cliente
- Notas por intervalo de notas (informar o intervalo de notas que deseja)
  - Todas as notas por intervalo de notas
  - Notas emitidas por intervalo de notas
  - Notas pendentes por intervalo de notas
  - Notas canceladas por intervalo de notas
- Notas por intervalo de datas (informar o intervalo de datas desejado)
  - Todas as notas por intervalo de datas
  - Notas emitidas por intervalo de datas
  - Notas pendentes por intervalo de datas
  - Notas canceladas por intervalo de datas
 

Em resumo, podemos ver que esse sistema é relativamente complexo, e é uma grande evolução em relação ao sistema da oficina e da padaria, pois já possui uma complexidade considerável e grandes evoluções. Neste projeto consegui explorar bastante a linguagem SQL para fazer as consultas e as estatísticas do banco de dados, mas o que achei um pouco mais complexo de desenvolver é a lógica das vendas levando em consideração a fidelização do cliente.

Também esse sistema foi super importante para exercitar a lógica de permissão, do que os usuários podem ou não podem fazer, dependendo de suas permissões, e também a lógica dos registros de vendas e dos dados para formação das estatísticas.

Um grande desafio foi fazer a emissão de nota automaticamente através do agendamento, e também o controle dos agendamentos pendentes que é feito unico e exclusivamente pelo sistema, tanto no login quanto no logout do usuário, levando em consideração suas permissões.

Esse projeto foi um grande desafio, mas consegui a nota máxima ao apresentar ele como projeto integrador no final do curso no Senac.

Quem quiser ver como ficou basta baixar esse projeto, e instalar as dependências (basicamente pyqt5) e o Python na versão 3.x

Para poder cadastrar um usuário e setar suas permissões deve utilizar inicialmente o superusuário ROOT e a senha manager.

Para executar o sistema utilize o arquivo menu.py, que vai abrir a tela de login, onde você poderá logar com o superusuário ROOT, cadastrar um usuário, setar suas permissões e em seguida logar novamente com o usuário que você cadastrou e testar para ver como ficou esse meu projeto final do Jovem Programador Senac módulo 2.
