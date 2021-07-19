# Messagepack Practice

This project is trying to impliment messagepack in python.
Messagepack is a serializer like JSON, but it smaller.
The impliment spec you can ref here: [ref](https://github.com/msgpack/msgpack/blob/master/spec.md).

## File structure
```
├── Packer.py  # impliment messagepack type serizal
├── main.py  # Run demo
├── pack.py  # detect object type
```
Run unit test
```sh
pip install pytest
pytest -v
```
## Run Demo
```sh
python main.py
```
