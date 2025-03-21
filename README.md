# 🌦️ Previsão do Tempo - Aplicativo Tkinter

Este é um aplicativo de previsão do tempo desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica. Ele obtém dados meteorológicos da API do OpenWeatherMap e exibe informações como temperatura, umidade, pressão e descrição do clima em uma interface intuitiva.

## 🛠️ Recursos

- 🔍 Busca de previsão do tempo para qualquer cidade
- 🌡️ Exibição de temperatura, umidade, pressão atmosférica e descrição do clima
- 🎨 Mudança dinâmica de cores e ícones conforme o horário do dia
- 🌍 Tradução automática das descrições do clima para o português

## 💻 Tecnologias Utilizadas

- 🐍 Python
- 🖥️ Tkinter
- 🌐 Requests
- 🖼️ PIL (Pillow)
- 🔐 dotenv
- ⏳ pytz

## 📋 Requisitos

- ✅ Python 3.x instalado
- ✅ Conta no [OpenWeatherMap](https://openweathermap.org/) para obter uma chave de API

## 📥 Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Crie um arquivo `.env` e adicione sua chave de API:
   ```
   API_KEY=sua_chave_aqui
   ```
4. Execute o aplicativo:
   ```sh
   python app.py
   ```

## 🚀 Como Usar

1. ⌨️ Insira o nome da cidade desejada no campo de texto.
2. 🌍 Clique no botão **"Ver Clima"**.
3. 📊 O aplicativo exibirá as informações do clima da cidade selecionada.