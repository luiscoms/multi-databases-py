Multi Databases
===============

Given 3 databases

* **Very sensible database** - [mysql](#mysql)
* **Light sensible database** - mongodb
* **Fast database** - elasticsearch

## <a name="mysql"></a>mysql

* CPF
* Endereço
* Nome
* Lista de dívidas

## <a name="mongodb"></a>mongodb

(Score de credito - rating)

* Idade
* Lista de bens
* Endereço
* Fonte de renda

## <a name="elasticsearch"></a>elasticsearch


* Ultima consulta por cpf
* Movimentação financeira
* Ultima compra



Esta solução conta com um serviço de consulta por CPF que disponibiliza os dados da pessoa física armazenados no mysql.
A cada consulta nesse serviço um evento é enviado para uma fila de eventos.
Um worker processa esses eventos e armazena nomongodb e atualiza o ultimo registro no elasticsearch.


/whois/<cpf>


/events/<cpf>

Serviço de consulta de eventos por CPF que disponibiliza os ultimos eventos relacionados a um cpf.

