# Proyecto de Detección de Spam en Telegram

En este proyecto se desarrollará un modelo de clasificación binaria para detectar mensajes de spam en Telegram en español e inglés. Utilizaremos técnicas de procesamiento de lenguaje natural (NLP) para entrenar los modelos y un bot de Telegram para interceptar y gestionar los mensajes.

## Estructura del Proyecto
├── data/
│   ├── english.csv
│   └── spanish.csv
├── joblib/
│   ├── best_model_en.joblib
│   ├── vectorizer_en.joblib
│   ├── best_model_es.joblib
│   └── vectorizer_es.joblib
├── tg_bot.py
├── requirements.txt
├── start.sh
└── .gitignore

## Descripción de Archivos

- `data/`: Contiene los archivos CSV con los datos de entrenamiento en inglés (`english.csv`) y español (`spanish.csv`).
- `joblib/`: Contiene los modelos entrenados y los vectorizadores.
  - `best_model_en.joblib`: Modelo entrenado para detectar spam en inglés.
  - `best_model_es.joblib`: Modelo entrenado para detectar spam en español.
  - `vectorizer_en.joblib`: Vectorizador TF-IDF para inglés.
  - `vectorizer_es.joblib`: Vectorizador TF-IDF para español.
- `proyecto_clasificador_binario_NPL.ipynb`: Cuaderno Jupyter con el procesamiento de datos y el entrenamiento de los modelos.
- `tg_bot.py`: Script de configuración del bot de Telegram.
- `requirements.txt`: Lista de dependencias del proyecto.
- `README.md`: Este archivo.
- `.env`: Archivo para almacenar variables de entorno, como el token del bot de Telegram.
- `.gitignore`: Archivo para especificar qué archivos deben ser ignorados por Git.
- `stash.sh`: Script auxiliar (si aplica).

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. Crea un entorno virtual y actívalo:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Configura las variables de entorno:
    - Crea un archivo `.env` en la raíz del proyecto.
    - Añade tu token del bot de Telegram:
      ```
      TELEGRAM_BOT_TOKEN=tu_token_aqui
      ```

## Uso

1. Ejecuta el cuaderno Jupyter para entrenar los modelos y guardarlos en la carpeta `joblib/`:
    ```sh
    proyecto_clasificador_binario_NPL.ipynb
    ```

2. Inicia el bot de Telegram:
    ```sh
    python tg_bot.py
    ```

El bot interceptará los mensajes en el grupo de Telegram donde esté presente y eliminará aquellos que sean detectados como spam, notificando al usuario que los envió.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Autores

- Daniel Ramírez Vaquero
- Natalie Pilkington