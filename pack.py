from Packer import Packer
import io, sys

packer = Packer()
brinary_writer = io.BytesIO()

def pack(res):
    if res is None:
        brinary_writer.write(packer.pack_null(res))
    elif isinstance(res, dict):
        brinary_writer.write(packer.pack_dict(res))
        for k,v in res.items():
            pack(k)
            pack(v)
    elif isinstance(res, (list, tuple)):
        brinary_writer.write(packer.pack_arr(res))
        for data in res:
            pack(data)
    elif isinstance(res, bool):
        brinary_writer.write(packer.pack_bool(res))
    elif isinstance(res, int):
        brinary_writer.write(packer.pack_int(res))
    elif isinstance(res, float):
        brinary_writer.write(packer.pack_float(res))
    elif isinstance(res, str):
        byte, data = packer.pack_str(res)
        brinary_writer.write(byte+data)
    return brinary_writer.getvalue()

