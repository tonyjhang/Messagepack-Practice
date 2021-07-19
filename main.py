from pack import pack
import sys

res = {
    "a list": [1, 42, 3.141, 1337, "help"],
    "a string": None,
    "another dict": {"foo":True, "key": "value", "the answer": 42}
}

packed_res = pack(res)
print(f'Packed size:{sys.getsizeof(packed_res)}, data: {packed_res}')