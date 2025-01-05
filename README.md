<b><h2> Descrição do Projeto:</h2> </b>

Este projeto tem como objetivo a criação de uma ferramenta de análise e prevenção contra ataques de phishing. O código original foi baseado no repositório cibersecurity-desafio-phishing, que serve como ponto de partida para a construção de um sistema de detecção de emails fraudulentos.

<b><h2>Objetivos do Projeto:</h2> </b>

  Analisar URLs suspeitas: A ferramenta verifica se uma URL está relacionada a sites de phishing, comparando com uma lista de sites conhecidos.
  Verificação de e-mails: A partir de palavras-chave e padrões em e-mails, a ferramenta consegue identificar tentativas de phishing.
  Relatório de risco: Geração de um relatório indicando a probabilidade de o e-mail ser fraudulento ou seguro.

<b><h2>Melhorias Realizadas:</h2> </b>

  Integração com API de listas negras: Eu integrei uma API de listas negras para verificar URLs em tempo real e melhorar a precisão da análise de phishing. (arquivo listas_negras_API.py)
  Interface Gráfica (GUI): Desenvolvi uma interface simples utilizando Tkinter para facilitar o uso da ferramenta, permitindo que qualquer usuário possa realizar as verificações sem a necessidade de linha de comando.
  Automação de Detecção de Phishing em Massa: Implementei um script para fazer a varredura de uma lista de e-mails em massa, gerando um relatório detalhado ao final.
  Melhoria na Documentação: Adicionei documentação detalhada para que outros desenvolvedores possam facilmente entender o funcionamento do código e contribuir com melhorias.

<b><h2>Tecnologias Utilizadas:</h2> </b>

  Python 3.x: Linguagem de programação principal utilizada no desenvolvimento da ferramenta.
  Tkinter: Biblioteca para a criação da interface gráfica.
  Requests: Para fazer requisições HTTP e integrar com APIs externas.
  BeautifulSoup: Para análise de conteúdo de URLs.
  APIs de Listas Negras: Para verificar URLs em tempo real e aumentar a precisão da detecção de phishing.

<b><h2>Contribuições Futuras:</h2> </b>

  Implementação de aprendizado de máquina para classificar e-mails de phishing com base em modelos preditivos.
  Aprimoramento da interface com novas funcionalidades, como verificação de anexos e conteúdo de e-mails.
  Aprimoramento da precisão da análise de URLs, utilizando mais fontes de listas negras e algoritmos de detecção de fraude.
