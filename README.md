# Simple REST API with Python
Este repositório foi feito para um tutorial no blog [Simples mas Complexo](https://simplesmascomplexo.com.br/construindo-uma-api-em-python/)

## Instalando Python e PIP
Para instalar Python3 e PIP, que é o nosso gerenciador de dependências, execute os comandos abaixo se você tiver usando Ubuntu
```bash
$ sudo apt update
$ sudo apt install python3 python3-pip
```

## Rodando o projeto
Execute o comando na pasta do projeto:
```bash
$ python3 main.py
```

## Banco de Dados
O projeto usa banco de dados PostgreSQL. Abaixo tem a criação do database e da tabela que usamos no projeto.
```sql
-- Para criar a database
create database sample_w_flask;
```
```sql
-- Para criar a tabela
create table if not exists swf_user (
     id VARCHAR(36) primary key,
     name VARCHAR(100),
     email VARCHAR(100),
     active INTEGER default 1
 )
```
## Schema
Existe dois schemas JSON definidos, o schema de retorno e o schema de envio. Única diferença entre os dois é que quando enviamos, não precisamos setar o parametro _id_.

### Schema de retorno
```json
{
  "active": 1,
  "email": "chewie@wookie.sw",
  "id": "6b966e56-1f31-430f-b4de-12803bc78375",
  "name": "Chewbacca"
}
```

### Schema de envio
```json
{
	"name":"Chewbacca",
	"email":"chewie@wookie.sw",
	"active": 1
}
```

## Rotas
As rotas criadas estão expostas nos seguintes endereços:

### Salvar novo usuario
```http
PUT /user/create/ HTTP/1.1
Content-Type: application/json
Host: localhost:5000
Content-Length: 66

{
	"name":"Chewbacca",
	"email":"chewie@wookie.sw",
	"active": 1
}
```
### Listar usuários
```http
GET /user/list/ HTTP/1.1
Host: localhost:5000
```
### Pesquisar usuários por nome
```http
GET /user/find/?name=Chew HTTP/1.1
Content-Type: application/json
Host: localhost:5000
```
### Remover usuário
```http
DELETE /user/6b966e56-1f31-430f-b4de-12803bc78375 HTTP/1.1
Host: localhost:5000
```
by: [@caiofabioa](https://caiodearaujo.com.br)
