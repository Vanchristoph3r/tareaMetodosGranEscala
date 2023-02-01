# Tarea 03

Traslado de jupyter notebook a un script modular

## Instalación
Debe tener [pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv) instalado y activar el ambiente virtual.

```bash 
pipenv shell
pipenv install
```

## Uso
Con el ambiente activado será suficiente ejecutar el siguiente comando.

```bash
python run.py
```

## Estructura
- data: contiene los datos *raw* y *outputs*
- eda: imágenes creadas por el *EDA*
- src: Código e implementación de limpieza, transformación y modelado
- config.yaml: variables de "entorno" a usar
- Pipfile: las dependencias usadas

## Autor

Christopher Chávez Jiménez

208762