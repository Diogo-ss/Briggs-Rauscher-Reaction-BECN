# BECN - UFABC - Briggs–Rauscher Reaction

## Processamento dos vídeos

O processamento das informações do experimento é feita utilizando um algoritmo em Python:

- **Captura dos Quadros:** O vídeo das reações é processado quadro a quadro. Utilizando a biblioteca OpenCV, o código configura o vídeo para ser lido em intervalos regulares, definidos por um intervalo de tempo (de 1.000ms por padrão). Cada quadro do vídeo é salvo em formato `.jpeg`.

- **Extração da Cor Predominante:** Para cada imagem salva, é utilizada a biblioteca ColorThief para identificar a cor predominante.

- **Filtragem de Cores Irrelevantes:** Cores que não são relevantes para o estudo são filtradas com base em uma lista de cores ignoradas. Se a cor extraída de um quadro estiver na lista de cores a serem ignoradas, ela é substituída por branco (`#FFFFFF`).

- **Dados:** As cores predominantes, associadas ao timestamp correspondente do vídeo, são armazenadas em um dicionário. Esse dicionário é então gravado em um arquivo `.json`.

## Gráficos (Saturação em função do Tempo)

- O dicionário data contém os tempos e as cores hexadecimais.
- As cores hexadecimais são convertidas para o HSV (Matiz, Saturação, Valor), onde apenas a saturação é utilizada.
- Os valores de saturação são suavizados usando uma spline cúbica, tornando o gráfico mais sauave.
- Saturação pode variar de 0 a 1.
- O eixo **X** mostra o tempo em segundos, e o eixo **Y** mostra a saturação.

## Uso

### Processado vídeo
> [!IMPORTANT]
> Use (preferencialmente) o Python `3.12.x`

- **Crie o ambiente virtual:**

  ```sh
  python -m venv .env
  ```

- **Ative o ambiente virtual:**

  ```sh
  source .env/bin/activate
  ```

- **Instale as dependências:**

  ```sh
  pip install -r requirements.txt
  ```

- **Substitua `seu_video.mp4` pelo nome do vídeo:**

> [!IMPORTANT]
> O vídeo deve estar dentro da pasta `assets`.

  ```sh
  python src/main.py --video-name=seu_video.mp4
  ```

### Plotando gráficos

- Após processar um vídeo, é gerado um arquivo `.json`.
- Copie o conteúdo e cole na variável `data` dentro do Notebook.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Diogo-ss/Briggs-Rauscher-Reaction-BECN/blob/main/src/Graphics.ipynb)


## Saiba mais:

- [HSV](https://en.wikipedia.org/wiki/HSL_and_HSV)
- [Spline](https://en.wikipedia.org/wiki/Spline_(mathematics))
- [Matplotlib](https://matplotlib.org/)

## License

Este projeto é distribuído sob a licença MIT
