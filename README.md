## Installing Flask
```
pip install Flask
```

## Setting up project

If you are on Windows, the environment variable syntax depends on command line interpreter. 

Make sure you **change path** to the same folder where `controller.py` is located before

```
cd C:\path\to\app
```

On Command Prompt:
```
set FLASK_APP=controller.py
```

And on PowerShell:
```
$env:FLASK_APP="controller.py"
```

## Run Project

```
python -m flask run
```
