
import io

def unpack(res):
    print(res)
    if isinstance(res, (bytes, bytearray)) is not True:
        raise BaseException(f'{res} is not bytes object')
    data = io.BytesIO(res)
    if len(data) == 0:
        raise InsufficientDataException()

    while len(data) < res:
        chunk = fp.read(res - len(data))
        data += chunk
    print(data)