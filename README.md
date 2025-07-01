**`<div align="center">`**

# 🚗 Carros App 🚗

### *Sistema Inteligente de Gestão de Concessionária*

**`</div>`**

**`<p align="center">`
<img alt="Python" src="**[https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&amp;logo=python](https://www.google.com/search?q=https://img.shields.io/badge/Python-3.10%252B-blue%3Fstyle%3Dfor-the-badge%26logo%3Dpython "null")">
<img alt="Django" src="[https://img.shields.io/badge/Django-4.2%2B-darkgreen?style=for-the-badge&amp;logo=django](https://www.google.com/search?q=https://img.shields.io/badge/Django-4.2%252B-darkgreen%3Fstyle%3Dfor-the-badge%26logo%3Ddjango "null")">
<img alt="License" src="[https://img.shields.io/badge/Licen%C3%A7a-MIT-purple?style=for-the-badge](https://www.google.com/search?q=https://img.shields.io/badge/Licen%25C3%25A7a-MIT-purple%3Fstyle%3Dfor-the-badge "null")">

</p>

**`<p align="center">`
Bem-vindo ao `<strong>`Carros App`</strong>`, uma solução completa e inteligente para o gerenciamento de concessionárias de veículos. Este projeto, construído com o poder do Django e a inteligência da OpenAI, automatiza e otimiza o controle do seu inventário de carros.

</p>**

## ✨ Funcionalidades Principais

* **👤 ****Autenticação Completa:** Sistema seguro de registro e login para a equipe.
* **🏷️ ****Gestão de Marcas:** Adicione e organize facilmente as marcas dos veículos.
* **🚘 ****CRUD de Carros Completo:**
  * **Criação:** Cadastre novos veículos com todos os detalhes: modelo, marca, ano, valor, placa e fotos.
  * **Visualização:** Navegue por uma lista completa de carros e acesse páginas de detalhes individuais.
  * **Edição:** Atualize qualquer informação de um carro existente com poucos cliques.
  * **Exclusão:** Remova veículos do inventário de forma segura.
* **🤖 ****Descrições com IA:** Ao cadastrar um carro, uma descrição de marketing atraente é **gerada automaticamente** pela API da GeminiAPI, economizando tempo e impulsionando as vendas!
* **📊 ****Controle de Estoque:** O inventário é atualizado em tempo real a cada novo carro adicionado.
* **🔍 ****Busca Inteligente:** Encontre qualquer carro no seu inventário instantaneamente.

## 🚀 Tecnologias Utilizadas

**Este projeto une tecnologias robustas para entregar a melhor experiência:**

* **Backend:** Python | Django
* **Banco de Dados:** SQLite3 (padrão)
* **Inteligência Artificial:** Gemini API
* **Frontend:** HTML5 | CSS3 (Templates Django)
* **Deployment:** uWSGI

## 🛠️ Configuração e Instalação

**Prepare-se para acelerar! Siga os passos para ter o projeto rodando na sua máquina.**

#### **1. Clone o Repositório**

```
git clone <url-do-seu-repositorio>
cd carros

```

#### **2. Crie e Ative o Ambiente Virtual**

```
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

```

#### **3. Instale as Dependências**

```
pip install -r requirements.txt

```

#### **4. Configure as Variáveis de Ambiente**

**Crie um arquivo **`<span class="selected">.env</span>` na raiz do projeto e adicione sua chave da GEMINI_API:

```
GEMINI_API_KEY=sua_chave_secreta_da_api_aqui

```

#### **5. Execute as Migrações**

```
python manage.py migrate

```

#### **6. Crie um Superusuário**

```
python manage.py createsuperuser

```

*Siga as instruções para criar seu usuário administrador.*

## 🏃‍♂️ Executando o Projeto

**Ligue os motores!**

1. **Inicie o servidor:**
   ```
   python manage.py runserver

   ```
2. **Acesse a aplicação no seu navegador:**
   * **Showroom de Carros:**`<span class="selected">http://127.0.0.1:8000/cars/</span>`
   * **Painel Admin:**`<span class="selected">http://127.0.0.1:8000/admin/</span>`

## 🤝 Contribuições

**Contribuições são super bem-vindas! Se você tem ideias para novas funcionalidades ou melhorias, sinta-se à vontade para abrir uma ***issue* ou enviar um  *pull request* **.**

1. **Faça um ***fork* do projeto.
2. **Crie uma nova ***branch* (`<span class="selected">git checkout -b feature/nova-feature</span>`).
3. **Faça o ***commit* das suas alterações (`<span class="selected">git commit -m 'Adiciona nova feature'</span>`).
4. **Faça o ***push* para a *branch* (`<span class="selected">git push origin feature/nova-feature</span>`).
5. **Abra um ** *Pull Request* **.**
