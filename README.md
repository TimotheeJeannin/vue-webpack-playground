# vue-webpack-playground

> A repository where I can test various ways to combine vue, flask and webpack.

## Frontend setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```

## Backend setup

``` bash
# install dependencies
python3 -m venv env
./env/bin/pip install --upgrade pip
./env/bin/pip install -r requirements.txt

# run the flask application
FLASK_APP=src/backend.py ./env/bin/flask run
```
