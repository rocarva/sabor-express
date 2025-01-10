
# Sabor Express

Aplicação em **FastAPI** que faz o consumo de um arquivo JSON remoto com cardápios de restaurantes, oferecendo endpoints para listar ou filtrar esses dados. Além disso, inclui um script que baixa o arquivo JSON e gera arquivos `.json` individuais para cada restaurante.

---

## Sumário
- [Como Baixar o Projeto](#como-baixar-o-projeto)
- [Instalação e Configuração](#instalação-e-configuração)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalando o Projeto](#instalando-o-projeto)
- [Executando a Aplicação](#executando-a-aplicação)
- [Endpoints Disponíveis](#endpoints-disponíveis)
- [Gerando Arquivos JSON por Restaurante](#gerando-arquivos-json-por-restaurante)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Como Baixar o Projeto

1. **Baixar via Git**  
   Se você prefere usar o Git, basta clonar o repositório:
   ```bash
   git clone https://github.com/rocarva/sabor-express.git
   ```
   Em seguida, entre na pasta:
   ```bash
   cd sabor-express
   ```

2. **Baixar o ZIP**  
   Caso não queira usar o Git, você pode clicar em **Code** > **Download ZIP** diretamente no [repositório do GitHub](https://github.com/rocarva/sabor-express). Depois, extraia o conteúdo do arquivo ZIP em uma pasta de sua preferência.

---

## Instalação e Configuração

### Pré-requisitos
- **Python 3.8+** instalado
- **pip** (gerenciador de pacotes do Python)
- **Virtualenv** (opcional, mas recomendado)

### Instalando o Projeto

1. **(Opcional) Crie e ative o ambiente virtual**:
   ```bash
   python -m venv venv
   # Ativando no Windows:
   venv\Scripts\activate
   # Ativando no Linux ou Mac:
   source venv/bin/activate
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Executando a Aplicação

Após a instalação das dependências:

1. **Executar com Uvicorn** (método recomendado para desenvolvimento):
   ```bash
   uvicorn main:app --reload
   ```
   - `main` é o arquivo onde a instância `app` do FastAPI está definida.
   - `--reload` recarrega a aplicação sempre que há mudanças no código.

2. **Executar com Python** (se tiver um `main.py` configurado):
   ```bash
   python main.py
   ```

A aplicação estará disponível em:
```
http://127.0.0.1:8000
```

---

## Endpoints Disponíveis

1. **`/api/hello`**  
   - Método: `GET`  
   - Descrição: Retorna uma saudação simples do mundo da programação.
   
   **Exemplo de retorno**:
   ```json
   {
     "Hello": "World"
   }
   ```

2. **`/api/restaurantes/`**  
   - Método: `GET`  
   - Descrição: Retorna todos os cardápios ou filtra por restaurante específico.
   - Parâmetro opcional: `restaurante`  
     - Se nenhum valor for enviado, retorna todos os cardápios.
     - Se um nome de restaurante for enviado, retorna apenas o cardápio desse restaurante.
   
   **Exemplo de requisição**:
   ```
   GET /api/restaurantes/?restaurante=KFC
   ```
   **Exemplo de resposta**:
   ```json
   {
     "Restaurante": "KFC",
     "Cardapio": [
       {
         "item": "Fried Chicken Bucket",
         "price": 39.99,
         "description": "Balde de frango crocante"
       },
       ...
     ]
   }
   ```

---

## Gerando Arquivos JSON por Restaurante

O projeto inclui um script que:
1. Faz requisição ao [arquivo JSON remoto](https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json).
2. Separa os itens por restaurante.
3. Cria arquivos `<NomeDoRestaurante>.json`.

**Exemplo de uso** (no terminal):
```bash
python gerar_arquivos.py
```
*(Assumindo que o script esteja salvo como `gerar_arquivos.py` ou qualquer outro nome definido por você.)*

---

## Contribuição

Contribuições são muito bem-vindas!  
Para reportar bugs ou sugerir melhorias, abra uma [issue](https://github.com/rocarva/sabor-express/issues).  
Se deseja colaborar com código, crie um fork do projeto, faça suas alterações e envie um **pull request**.

---

## Licença

Este projeto está licenciado sob a [MIT License](https://choosealicense.com/licenses/mit/).  
Fique à vontade para utilizar, modificar e distribuir de acordo com os termos da licença.
