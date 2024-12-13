# Panel de Control de Aplicación Web

Este proyecto consiste en construir y desplegar un panel de control basado en una aplicación web, utilizando herramientas de desarrollo de software como Streamlit y servicios de despliegue en la nube. El objetivo es practicar habilidades clave en la ingeniería de software, desde la configuración de entornos virtuales hasta el despliegue en Render.

## Funcionalidades

- Análisis exploratorio de datos.
- Visualizaciones interactivas:
  - Histogramas.
  - Gráficos de dispersión.
- Interacción a través de botones y casillas de verificación.

## Requisitos

- **Python 3.x**
- Entorno virtual con las siguientes dependencias:
  - pandas
  - plotly_express
  - streamlit

## Estructura del Proyecto

```
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── notebooks
│   └── EDA.ipynb
└── .streamlit
    └── config.toml
```

## Instrucciones Rápidas

1. **Configura el entorno:**
   ```bash
   python -m venv vehicles_env
   source vehicles_env/bin/activate
   pip install -r requirements.txt
   ```

2. **Realiza el análisis exploratorio:**
   - Abre `EDA.ipynb` en Jupyter Notebook y experimenta con visualizaciones usando plotly-express.

3. **Desarrolla la aplicación web:**
   - Ejecuta `streamlit run app.py` para probar localmente.

4. **Despliega en Render:**
   - Enlaza el repositorio a Render.
   - Usa los siguientes comandos:
     - Build Command: `pip install --upgrade pip && pip install -r requirements.txt`
     - Start Command: `streamlit run app.py`

5. **Accede a la aplicación:**
   - URL de la aplicación: `https://sprint-7-ds-project.onrender.com/`

## Enlaces

- [Repositorio en GitHub](https://github.com/Lloyd-B-Anderson/app.git)
- [Aplicación en Render](https://sprint-7-ds-project.onrender.com/)
