Piano Simples com Python
Este é um projeto de um piano virtual simples desenvolvido em Python. Ele utiliza a biblioteca tkinter para a criação da interface gráfica e a biblioteca pygame para a reprodução dos sons das notas musicais.

✨ Funcionalidades
Interface Gráfica: Exibe uma fileira de teclas de piano brancas.

Interatividade: Toca o som de uma nota musical ao:

Clicar em uma tecla na janela.

Pressionar a tecla do teclado correspondente.

Feedback Visual: As teclas pressionadas mudam de cor e relevo, simulando o ato de tocar um piano real.

Mapeamento de Teclado: As teclas Z, X, C, V, B, N, M são mapeadas para as notas Dó, Ré, Mi, Fá, Sol, Lá, Si, respectivamente.

📋 Pré-requisitos
Antes de começar, você precisará ter o Python 3 instalado em sua máquina.

As bibliotecas Python necessárias são:

pygame: para manipulação de áudio.

tkinter: para a interface gráfica (geralmente já vem incluída na instalação padrão do Python).

🚀 Instalação e Configuração
Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

1. Clonar o Repositório
Primeiro, clone este repositório para a sua máquina local usando o comando:

Bash

git clone <URL_DO_SEU_REPOSITORIO_GIT>
cd <NOME_DO_DIRETORIO_DO_PROJETO>
2. Criar e Ativar o Ambiente Virtual (Recomendado)
É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

No Linux ou macOS:

Bash

python3 -m venv venv
source venv/bin/activate
No Windows:

Bash

python -m venv venv
.\venv\Scripts\activate

3. Instalar as Dependências
Com o ambiente virtual ativado, instale a biblioteca pygame:

Bash


4. Organizar os Arquivos de Áudio
Para que o piano funcione, você precisa dos arquivos de som em formato .mp3.

Crie uma pasta chamada mp3 Notes no mesmo diretório onde está o seu script Python.

Coloque os seguintes arquivos de áudio dentro desta pasta:

c3.mp3

d3.mp3

e4.mp3

f3.mp3

g3.mp3

a3.mp3

b3.mp3

A estrutura final do seu projeto deve ser semelhante a esta:

seu-projeto/
├── seu_script_de_piano.py  # O arquivo de código que você criou
├── venv/                     # Pasta do ambiente virtual
└── mp3 Notes/                # Pasta com os arquivos de som
    ├── c3.mp3
    ├── d3.mp3
    ├── e4.mp3
    ├── f3.mp3
    ├── g3.mp3
    ├── a3.mp3
    └── b3.mp3
▶️ Como Executar
Após concluir a instalação e configuração, certifique-se de que seu ambiente virtual (venv) está ativado e execute o seguinte comando no terminal:

Bash

python seu_script_de_piano.py
(Substitua seu_script_de_piano.py pelo nome real do seu arquivo Python)

A janela do piano virtual será aberta e você poderá começar a tocar.

🎹 Controles
Você pode tocar as notas usando o mouse ou as seguintes teclas do seu teclado:

Tecla	Nota Musical
Z	Dó
X	Ré
C	Mi
V	Fá
B	Sol
N	Lá
M	Si
