
# peterhellberg

> A module for interacting with [PeterHellBerg](https://github.com/peterhellberg)'s
> [web application, for parsing humans.txt into JSON](https://github.com/peterhellberg/humans).
> The application is live at http://humans.herokuapp.com/


## installation:

```bash
$ pip install hellberg
```


## API:

```python
import hellberg
```


### retrieving humans.txt in JSON format:

Makes a HTTP request to the remote server. On success, returns a dict.
Otherwise, raises an exception.

```python
try:
    humans_json = hellberg.parse("humanstxt.org", use_ssl=False)
except Exception as exception:
    print(exception)
```


### diagnose errors:

Prints an appropriate message on why the request failed.

```python
hellberg.diagnose(exception)
```


## terminal:

The `get-humans` is available from this module.

```bash
$ get-humans humanstxt.org
```

To see **help information**:

```bash
$ get-humans --help
```

And **version information**:

```bash
$ get-humans --version
```


## license:

**The MIT License (MIT)**

Copyright &copy; 2015 GochoMugo <mugo@forfuture.co.ke>

