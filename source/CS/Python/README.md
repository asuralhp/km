# Python

## Introduction



## Jupyter
  - Cheat Sheet : ![jupyter_keymap](static/jupyter_keymap.png)


## Syntax

### Decorator

```python
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
```