# BECN - UFABC - Briggs–Rauscher Reaction

## Processamento das Informações

O processamento das informações do experimento é feita utilizando um algoritmo em Python:

- **Captura dos Quadros:** O vídeo das reações é processado quadro a quadro. Utilizando a biblioteca OpenCV, o código configura o vídeo para ser lido em intervalos regulares, definidos por um intervalo de tempo (de 1.000ms por padrão). Cada quadro do vídeo é salvo em formato (`JPEG`).

- **Extração da Cor Predominante:** Para cada imagem salva, é utiliza a biblioteca ColorThief para identificar a cor predominante.

- **Filtragem de Cores Irrelevantes:** Cores que não são relevantes para o estudo são filtradas com base em uma lista de cores ignoradas. Se a cor extraída de um quadro estiver na lista de cores a serem ignoradas, ela é substituída por branco (`#FFFFFF`).

- **Dados:** As cores predominantes, associadas ao timestamp correspondente do vídeo, são armazenadas em um dicionário. Esse dicionário é então gravado em um arquivo JSON.

## Uso

- **Crie o ambiente virtual:**

  ```sh
  python -m venv .env
  ```

- **Ative o ambiente virtual:**

  ```sh
  source .env/bin/activate
  ```

- **Instale as dependências:**:

  ```sh
  pip install -r requirements.txt
  ```

- **Substita `seu_video.mp4` pelo nome do seu vídeo:**

> [!IMPORTANT]
> O vídeo deve estar dentro da pasta `assets`.

  ```sh
  python src/main.py --video-name=seu_video.mp4
  ```

## License

Este projeto é distribuído sob a licença MIT
