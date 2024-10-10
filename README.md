# Django Store Management System

Este é um sistema de gerenciamento de loja criado com Django que permite o cadastro de clientes, funcionários, produtos e o registro de vendas. O projeto utiliza Django REST Framework para a criação de APIs e Django Filters para facilitar a filtragem de dados.

## Funcionalidades

- **Cadastro de clientes**: Gerencie informações dos clientes, como nome, e-mail, telefone, etc.
- **Cadastro de funcionários**: Adicione, edite e remova funcionários da loja.
- **Cadastro de produtos**: Gerencie o catálogo de produtos da loja, incluindo nome, descrição, preço e estoque.
- **Registro de vendas**: Registre e acompanhe as vendas realizadas na loja, associando clientes, produtos e funcionários responsáveis.

## Tecnologias Utilizadas

- **Django**: Framework web utilizado para a criação da aplicação.
- **Django REST Framework**: Biblioteca utilizada para criação das APIs REST.
- **Django Filters**: Ferramenta para facilitar a filtragem de dados nas APIs.
- **SQLite**: Banco de dados padrão utilizado para armazenar os dados.

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu_usuario/django-store-management.git
cd django-store-management
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Realize as migrações do banco de dados

```bash
python manage.py migrate
```

### 5. Crie um superusuário para acessar o painel de administração

```bash
python manage.py createsuperuser
```

### 6. Inicie o servidor

```bash
python manage.py runserver
```

Agora você pode acessar o projeto em `http://127.0.0.1:8000/` e o painel de administração em `http://127.0.0.1:8000/admin/`.

## API Endpoints

### Clientes

- `GET /api/clients/`: Listar todos os clientes.
- `POST /api/clients/`: Criar um novo cliente.
- `GET /api/clients/{id}/`: Detalhes de um cliente específico.
- `PUT /api/clients/{id}/`: Atualizar as informações de um cliente.
- `DELETE /api/clients/{id}/`: Deletar um cliente.

### Funcionários

- `GET /api/employees/`: Listar todos os funcionários.
- `POST /api/employees/`: Criar um novo funcionário.
- `GET /api/employees/{id}/`: Detalhes de um funcionário específico.
- `PUT /api/employees/{id}/`: Atualizar as informações de um funcionário.
- `DELETE /api/employees/{id}/`: Deletar um funcionário.

### Produtos

- `GET /api/products/`: Listar todos os produtos.
- `POST /api/products/`: Criar um novo produto.
- `GET /api/products/{id}/`: Detalhes de um produto específico.
- `PUT /api/products/{id}/`: Atualizar as informações de um produto.
- `DELETE /api/products/{id}/`: Deletar um produto.

### Vendas

- `GET /api/sales/`: Listar todas as vendas.
- `POST /api/sales/`: Registrar uma nova venda.
- `GET /api/sales/{id}/`: Detalhes de uma venda específica.

## Filtragem

Utilizamos o Django Filters para facilitar a filtragem nas listas de clientes, funcionários, produtos e vendas. Para utilizar filtros, basta adicionar parâmetros à URL, por exemplo:

```bash
GET /api/products/?price__lte=100  # Filtra produtos com preço menor ou igual a 100
```

## Testes

Para rodar os testes unitários do projeto:

```bash
python manage.py test
```

## Contribuição

Se deseja contribuir com o projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch: `git checkout -b minha-feature`.
3. Faça suas alterações e adicione commits: `git commit -m 'Minha nova feature'`.
4. Envie suas alterações: `git push origin minha-feature`.
5. Crie um pull request para revisão.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Sinta-se à vontade para adaptar este README conforme necessário para o seu projeto específico.
