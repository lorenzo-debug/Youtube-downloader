Para configurar o programa, você deve executar o seguinte comando na pasta de configuração:

sudo chmod +x configure.sh

Este comando dará permissão para executar o programa de configuração.
Agora você precisa executar o arquivo de configuração (configure.sh), você pode executá-lo com o seguinte comando:

./configure.sh

Ele fará algumas perguntas e depois de responder a todas as perguntas, você deve alterar a linha que tem uma variável como esta:

func_regex = re.compile(r"function\([^)]+\)")

Para uma variável como esta:

func_regex = re.compile(r"function\([^)]?\)")

*Provavelmente está na linha 152

Você pode encontrar o parser.py com o seguinte comando:

find -name parser.py | grep pytube

E a pasta de configuração está no diretório raiz (/)

--------------------------------------------------------------------------------------------------------------------

Se você deseja executar o programa manualmente, você pode ir para a pasta youtube_downloader/program/ e executar o seguinte comando:

python3 yt_downloader_current_icon.py

e se você quiser ver o código fonte, você pode abrir o arquivo yt_downloader_current_icon.py ou o arquivo yt_downloader_root_icon.py
