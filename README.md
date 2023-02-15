# Tarea 03

Traslado de jupyter notebook a un script modular

## Instalación
Debe tener [pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv) instalado y activar el ambiente virtual.

Para instalar pipenv solo basta con
```bash
pip3 install pipenv
```
Después instalar y activar el ambiente
```bash 
pipenv install
pipenv shell
```

## Uso
Con el ambiente activado será suficiente ejecutar el siguiente comando.

```bash
python run.py [-f your_config_file.yaml]
```

Por default tiene un archivo de configuración pero puedes agregar el tuyo en un argumento.

## Estructura
- data: contiene los datos *raw* y *outputs*
- eda: imágenes creadas por el *EDA*
- src: Código e implementación de limpieza, transformación y modelado
- config.yaml: variables de "entorno" a usar
- Pipfile: las dependencias usadas

## Autor

Christopher Chávez Jiménez

208762