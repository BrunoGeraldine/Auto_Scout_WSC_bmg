
![Alt text](image.png)


**WebScraping_Python_BMG**

---

### Descrição do Projeto

Este projeto realiza Web Scraping em múltiplas páginas para a ingestão eficiente de produtos em um banco de dados. Utilizando Python, implementa a biblioteca Requests para realizar requisições na URL e o Beautiful Soup para buscar e construir uma lista de produtos em um site dinâmico. Além disso, a linguagem REGEX é aplicada para a limpeza eficaz dos dados extraídos.

---

### Funcionalidades Principais

1. **Web Scraping:**
   - Utilização da biblioteca Requests para efetuar requisições HTTP nas páginas relevantes.

2. **Beautiful Soup:**
   - Implementação para analisar e extrair informações HTML das páginas web, facilitando a construção da lista de produtos.

3. **REGEX (Expressões Regulares):**
   - Aplicação da linguagem REGEX para limpeza e formatação dos dados extraídos, garantindo consistência e precisão.

4. **Ingestão Eficiente:**
   - Processo otimizado para a ingestão de dados em um banco de dados, tornando-o adequado para aplicações diversas.

---

### Arquitetura

1. **Ingestão:**
   - Captura de dados utilizando a técnica **Web scraping** e gerando arquivo no formato .CSV

2. **Armazenamento e Orquestração:**
   - Utilização do Azure Databricks para armazenamento e orquestração eficiente do pipeline.

3. **Tratamento:**
   - Processamento de dados utilizando PysPark no ambiente Databricks.

4. **Camadas (Layers):**
   - **Bronze:** Dados brutos, sem qualquer transformação.
   - **Silver:** Dados tratados, transformados e limpos, destinados a cientistas de dados e profissionais de negócios.
   - **Gold:** Dados transformados, agregados e modelados para avaliação e visualização, atendendo a analistas de dados, dashboards e insights.

---

### Como Utilizar

1. **Instalação de Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configuração:**
   - Adapte o código para a URL específica do site que deseja realizar o Web Scraping.

3. **Execução:**
   ```bash
   python webscraping.py
   ```

4. **Banco de Dados:**
   - Os dados extraídos podem ser armazenados em um banco de dados ou no formato desejado para utilização posterior.

---

### Fonte de Dados

Os dados utilizados neste projeto foram obtidos do Kaggle, disponíveis em [AutoScout24](https://www.autoscout24.com/).

---

### Tecnologias Utilizadas

- **Python:** Linguagem principal para o desenvolvimento.
- **Requests:** Biblioteca para realizar requisições HTTP.
- **Beautiful Soup:** Ferramenta para fazer o parsing de documentos HTML/XML.
- **REGEX:** Utilizado para a limpeza e formatação eficiente dos dados extraídos.

---

### Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou enviar pull requests para aprimorar a eficiência e funcionalidades do Web Scraping.

---

### Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
