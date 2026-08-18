GRUPO: GM Software Company.

Integrantes: Marcos V. e Guilherme P.

Loja de Jogos API

A Loja de Jogos API é um sistema desenvolvido em Python utilizando FastAPI para o gerenciamento de jogos disponíveis em uma loja.

O sistema permite organizar informações sobre os jogos, como nome, preço, plataforma e categoria.

O projeto possui duas tabelas relacionadas: Jogos e Categorias.

A tabela Jogos é a entidade principal e a tabela Categorias é a entidade relacionada. Cada jogo possui uma categoria.

Tabela 1 — Jogos

Tabela principal responsável pelo cadastro dos jogos disponíveis na loja.

Campo	Tipo	Descrição
id	inteiro	
nome	texto	Nome do jogo
preco	decimal	Preço do jogo
plataforma	texto	Plataforma em que o jogo está disponível
categoria_id	inteiro	Chave estrangeira relacionada à categoria
Tabela 2 — Categorias

Tabela relacionada responsável pela organização dos jogos por categoria.

Campo	Tipo	Descrição
id	inteiro	Identificador único da categoria
nome	texto	Nome da categoria

O campo categoria_id da tabela Jogos referencia o campo id da tabela Categorias.

Contrato das Rotas HTTP

Método	Rota	Descrição
GET	/jogos	Lista todos os jogos
GET	/jogos/{id}	Busca um jogo pelo ID
POST	/jogos	Cadastra um novo jogo
PUT	/jogos/{id}	Atualiza um jogo existente
DELETE	/jogos/{id}	Remove um jogo
Rotas Implementadas

Nesta primeira versão da aplicação foram implementadas duas rotas GET:

Método	Rota	Descrição
GET	/	Retorna uma mensagem informando que a API está funcionando
GET	/jogos	Retorna uma lista com 5 jogos mockados em memória
Tecnologias
Python
FastAPI
Uvicorn
