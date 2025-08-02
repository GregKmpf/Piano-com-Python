

🎹 Piano Simples com Python
Um piano virtual feito em Python, usando tkinter para a interface e pygame para o som.

É um projeto simples, ótimo para quem está começando a programar com interfaces gráficas ou simplesmente quer um passatempo musical no computador.

O que ele faz?
Interface limpa com as teclas de um piano.

Toque de duas formas: você pode usar o mouse para clicar nas teclas ou usar o teclado do seu computador para uma resposta mais rápida.

Feedback visual: a tecla que você pressiona muda de cor, para você saber exatamente o que está tocando.

Como Instalar e Rodar
Para rodar o projeto na sua máquina, siga estes passos:

1. Clone o projeto
Use o git para baixar os arquivos do repositório:

Bash

git clone <URL_DO_SEU_REPOSITORIO_GIT>
cd <NOME_DA_PASTA_DO_PROJETO>
2. Crie um ambiente virtual (Opcional, mas recomendado)
Isso ajuda a manter as dependências do projeto organizadas e separadas do resto do seu sistema.

Bash

# No Linux ou macOS
python3 -m venv venv
source venv/bin/activate

# No Windows
python -m venv venv
.\venv\Scripts\activate
3. Instale o pygame
O projeto precisa da biblioteca pygame para tocar os sons. Instale-a com o pip:

Bash

pip install pygame
(O tkinter geralmente já vem com o Python, então não precisa se preocupar com ele).

4. Adicione os sons das notas
O piano precisa dos arquivos de áudio .mp3 para funcionar.

Na pasta principal do projeto, crie um novo diretório chamado mp3 Notes.

Coloque os arquivos de som das notas dentro dessa pasta.

A estrutura de pastas deve ficar assim:

seu-projeto/
├── seu_script_de_piano.py
├── venv/
└── mp3 Notes/
    ├── c3.mp3
    ├── d3.mp3
    ├── e4.mp3
    ├── f3.mp3
    ├── g3.mp3
    ├── a3.mp3
    └── b3.mp3
▶️ Executando o Piano
Com tudo pronto, basta rodar o script Python no seu terminal:

Bash

python seu_script_de_piano.py
A janela do piano vai aparecer, e é só começar a tocar!

🎹 Controles do Teclado
Use o mouse para clicar nas teclas ou use a fileira de baixo do seu teclado para tocar as notas:

Tecla	Nota Musical
Z	Dó
X	Ré
C	Mi
V	Fá
B	Sol
N	Lá
M	Si
