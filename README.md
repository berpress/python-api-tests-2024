# python-api-tests-2024
Python API


<h1>
  Attention
 </h1>
 Since the service herokuapp is down, you need to use docker
 
```
docker run -d -p 56733:80 litovsky/flask-api-test
```
And check in browser

```
http://localhost:56733/
```

You will see response

```
{
"GitHub": "https://github.com/berpress/flask-restful-api",
"swagger": "https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0"
}
```

### How to start

Use python 3.8 +
Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

### Run all tests

```python
pytest
```

Some requests require an authorization token. Use header like
```angular2html
"Authorization": "JWT {token}"
```
