# 📚 README - Projetos Internos

Este documento centraliza a documentação e instruções dos diversos scripts desenvolvidos, organizados por categoria e índice.

---

## 📌 Índice Geral

- [1. Bots de Excel](#1-bots-de-excel)
  - [1.1 bot_de_transferencia_de_dados_xlsx_para_sistemas.py](#11-bot_de_transferencia_de_dados_xlsx_para_sistemspy)

---

## 1. Bots de Excel

### 1.1 bot_de_transferencia_de_dados_xlsx_para_sistemas.py

#### 📝 Descrição

O script **bot_de_transferencia_de_dados_xlsx_para_sistemas.py** automatiza a transferência de dados provenientes de arquivos Excel (.xlsx) diretamente para sistemas específicos, garantindo agilidade, eficiência e minimizando erros humanos no processo manual.

Este bot faz uso da biblioteca `mymouseinfo` para capturar com precisão as coordenadas de tela necessárias para interação com interfaces gráficas de sistemas que não dispõem de API direta.

---

#### 🚧 Pré-requisitos e Dependências

- **Python 3.8 ou superior**
  - [Download Python](https://www.python.org/)

- **Bibliotecas necessárias:**

  | Biblioteca   | Descrição                                    | Instalação                   |
  | ------------ | -------------------------------------------- | ---------------------------- |
  | openpyxl     | Manipulação de arquivos Excel (.xlsx)        | `pip install openpyxl`       |
  | pandas (opcional) | Manipulação avançada de dados tabulares | `pip install pandas`         |
  | mymouseinfo  | Captura coordenadas da tela (automação GUI)  | `pip install mymouseinfo`    |
  | pyautogui    | Automação de ações no mouse e teclado        | `pip install pyautogui`      |

- **Ferramentas auxiliares:**
  - Excel ou outra ferramenta compatível com arquivos .xlsx.

---

#### 🚀 Instruções de Execução

##### 🔹 Passo 1: Clonagem ou download do projeto

Clone o repositório ou faça o download do script diretamente.

git clone https://github.com/seu_usuario/repositorio.git
🔹 Passo 2: Captura das coordenadas com mymouseinfo
Antes da primeira execução, utilize o mymouseinfo para obter as coordenadas exatas dos campos da tela:

bash
Copiar
Editar
mymouseinfo
Instruções de uso:
Após executar mymouseinfo, posicione o mouse nos campos desejados e anote as coordenadas exibidas. Insira essas coordenadas no script nas variáveis apropriadas.
🔹 Passo 3: Execução do script principal
Execute o script usando o terminal ou prompt de comando:

Forma básica:

bash
Copiar
Editar
python bot_de_transferencia_de_dados_xlsx_para_sistemas.py
Forma avançada com parâmetros:

bash
Copiar
Editar
python bot_de_transferencia_de_dados_xlsx_para_sistemas.py --arquivo_entrada dados.xlsx --sistema_destino SistemaERP
--arquivo_entrada: Caminho do arquivo Excel a ser processado.
--sistema_destino: Identificador ou nome do sistema-alvo.
📌 Funcionamento do Script (Fluxograma Básico)
O funcionamento geral do script segue as etapas abaixo:

📂 Leitura dos dados Excel

Abre o arquivo Excel especificado e lê os dados necessários usando openpyxl ou pandas.
✅ Validação dos dados

Checa se existem campos vazios ou inconsistências antes de prosseguir.
🔐 Autenticação (se necessário)

Autentica automaticamente no sistema destino (login via interface gráfica ou API).
🖱️ Transferência/Automação

Utiliza pyautogui em conjunto com as coordenadas obtidas pelo mymouseinfo para preencher formulários e campos específicos no sistema destino.
📝 Feedback e geração de logs

Ao fim do processamento, gera um arquivo de log contendo o status de cada dado transferido (sucesso ou falha).
⚠️ Possíveis erros e suas soluções rápidas
Erro Comum	Solução Sugerida
Erro de leitura XLSX	Verifique se o arquivo Excel não está aberto ou corrompido e está no formato correto.
Falha na automação de GUI	Reveja as coordenadas obtidas pelo mymouseinfo e ajuste novamente.
Erro nas dependências Python	Certifique-se de instalar corretamente todas as dependências mencionadas acima.
Problema ao acessar o sistema	Verifique se há falhas na conexão ou erros de login no sistema alvo.
