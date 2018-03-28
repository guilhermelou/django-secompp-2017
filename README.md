# django-secompp-2017

## Referências:

#### Sobre Rest
[REST não é simplesmente retornar JSON - TreinaWeb](https://www.treinaweb.com.br/blog/rest-nao-e-simplesmente-retornar-json-indo-alem-com-apis-rest/)

[Arquitetura REST](http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)


#### Sobre Sessões

[Entendendo Cookies e Sessões](https://klauslaube.com.br/2012/04/05/entendendo-os-cookies-e-sessoes.html)
[PHP Sessions](http://www.fernandolobo.info/daw/slides/PHP_sessions.pdf)


#### Principais Passos
Os passos principais para o projeto são a seguinte sequência de comandos

```bash
django-admin.py startproject django-secompp-2017 # cria um novo projeto
python manage.py runserver # roda o projeto em um servidor local no endereço http://127.0.0.1:5000
python manage.py startapp profile # inicializa um no app com o nome profile
python manage.py startapp myprofile # inicializa um novo app com o nome myprofile
python manage.py makemigrations # realiza a montagem das migrações necessárias no banco de dados
python manage.py migrate # implementa as alterações (migrações) no banco de dados
python manage.py createsuperuser # cria um super usuário pelo qual temos acesso ao "back-office" do projeto
```
