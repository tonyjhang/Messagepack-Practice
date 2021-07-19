from pack import pack
import sys

res = {
    "a list": [1, 42, 3.141, 1337, "help"],
    "a string": "bla",
    "another dict": {"foo": "bar", "key": "value", "the answer": 42}
}
packed_res = pack(res)
print(sys.getsizeof(packed_res), packed_res)