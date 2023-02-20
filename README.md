**Activate the virtual environment**
```
source blockchain-env/bin/activate
```

**Install all packages**
```
pip install -r requirements.txt
```

**Run the tests**

Make sure to activate the virtual environment.

```
python3 -m pytest backend/tests
```

**Run the application and API**

Make sure to activate the virtual environment.

```
python3 -m backend.app
```

**Run a peer instance**

Make sure to activate the virtual environment.

```
export PEER=True && python3 -m backend.app
```

or create PEER in your .env file and set in to True

**Run the frontend**

In the frontend directory:
```
npm run start
```

**Seed the backend with data**

```
export SEED_DATA=True && python -m backend.app
```

or create SEED_DATA in your .env file and set in to True
