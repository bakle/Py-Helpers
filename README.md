# Python Helpers

This package includes multiple helpers for string, email and urls.
<br>
<br>

# Use

<br>

## Str Helper
<br>

### Is a String

Validate if the given value is string type

```python
from bakle_helpers.str import Str

Str.is_a_string('Test') # True
Str.is_a_string(12345) # False
```

### Ends With

Validate if a string ends with the given value

```python
from bakle_helpers.str import Str

# Validate with case sensitive
Str.ends_with('Hello Pyhton', 'ton') # True
Str.ends_with('Hello Pyhton', 'Ton') # False
Str.ends_with('Hello Pyhton', 'not') # False

# Validate with case insensitive
Str.ends_with('Hello Pyhton', 'ton', True) # True
Str.ends_with('Hello Pyhton', 'Ton', True) # True
Str.ends_with('Hello Pyhton', 'not', True) # False
```

### Starts With

Validate if a string starts with the given value

```python
from bakle_helpers.str import Str

# Validate with case sensitive
Str.starts_with('Hello Pyhton', 'He') # True
Str.starts_with('Hello Pyhton', 'he') # False
Str.starts_with('Hello Pyhton', 'lo') # False

# Validate with case insensitive
Str.starts_with('Hello Pyhton', 'He', True) # True
Str.starts_with('Hello Pyhton', 'he', True) # True
Str.starts_with('Hello Pyhton', 'lo', True) # False
```

### After

Returns everything after the given string

```python
from bakle_helpers.str import Str

Str.after('test@mail.com', '@') # mail.com
```


### Before

Returns everything before the given string

```python
from bakle_helpers.str import Str

Str.before('test@mail.com', '@') # test
```


### Contains

Validate if the given value is in the given string

```python
from bakle_helpers.str import Str

# Validate with case sensitive
Str.contains('Hello Python', 'Python') # True
Str.contains('Hello Python', 'python') # False
Str.contains('Hello Python', 'World') # False

# Validate with case sensitive
Str.contains('Hello Python', 'Python', True) # True
Str.contains('Hello Python', 'python', True) # True
Str.contains('Hello Python', 'World', True) # False
```


### Limit

Returns the truncated string by the specific length

```python
from bakle_helpers.str import Str

# With ellipses
Str.limit('Lorem ipsum', 8) # Lorem ip...

# Without ellipses
Str.limit('Lorem ipsum', 8, False) # Lorem ip
```


### Random

Returns a random string of the specific length

```python
from bakle_helpers.str import Str

Str.random(8) # OxPMUwHC
```

<br>
<br>

## Email Helper
<br>

### Is valid

Validate if the given email is valid

```python
from bakle_helpers.str import Email

Email.is_valid('test@mail.com') # True
Email.is_valid('test') # False
```

### Random

Returns a random email

```python
from bakle_helpers.str import Email

Email.random() # leota@hotmail.com
```

<br>
<br>

## Url Helper
<br>

### Is valid()

Validate if the given url is valid

```python
from bakle_helpers.str import Url

Url.is_valid('http://test.com') # True
Url.is_valid('test') # False
```

### Random()

Returns a random url

```python
from bakle_helpers.str import Url

Url.random() # http://www.tippetttroymii.com
```