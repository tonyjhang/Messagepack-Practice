import struct

class Packer:
    @staticmethod
    def pack_null():
        return b"\xc0"

    @staticmethod
    def pack_str(data):
        data = data.encode('utf-8')
        data_len = len(data)
        if data_len < 32:
            return struct.pack("B", 0xa0 | data_len), data
        elif data_len < 2**8:
            return b'\xd9%b' % (struct.pack("B", data_len)), data
        elif data_len < 2**16:
            return b"\xda%b" % (struct.pack(">H", data_len)), data
        elif data_len < 2**32:
            return b"\xdb%b" % (struct.pack(">I", data_len)), data
        else:
            raise f'{data} size is too large'
    
    @staticmethod
    def pack_int(data):
        if data > 0:
            if data < 128:
                return struct.pack("B", data)
            elif data < 2 ** 8:
                return b"\xcc%b" % (struct.pack("B", data))
            elif data < 2 ** 16:
                return b"\xcd%b" % (struct.pack(">H", data))
            elif data < 2 ** 32:
                return b"\xce%b" % (struct.pack(">I", data))
            elif data < 2 ** 64:
                return b"\xcf%b" % (struct.pack(">Q", data))
            else:
                raise f'{data} is too large'
        else:
            if data >= -32:
                return struct.pack("b", data)
            elif data >= -2 ** 7:
                return b"\xd0%b" % (struct.pack("b", data))
            elif data >= -2 ** 15:
                fp.write(b"\xd1" + struct.pack(">h", data))
            elif data >= -2 ** 31:
                fp.write(b"\xd2" + struct.pack(">i", data))
            elif data >= -2 ** 63:
                fp.write(b"\xd3" + struct.pack(">q", data))
            else:
                raise f'{data} is too small'

    @staticmethod
    def pack_float(data):
        return b'\xcb%b' % (struct.pack(">d", data))

    @staticmethod
    def pack_bool(data):
        return b"\xc3" if data else b"\xc2"

    @staticmethod
    def pack_arr(data):
        data_len = len(data)
        if data_len < 16:
            return struct.pack("B", 0x90 | data_len)
        elif data_len < 2 ** 16:
            return b"\xdc%b" % (struct.pack(">H", data_len))
        elif data_len < 2 ** 32:
            return b"\xdd%b" % (struct.pack(">I", data_len))
        else:
            raise f'array {data} is too large'

    @staticmethod
    def pack_dict(data):
        data_len = len(data)
        if data_len < 16:
           return struct.pack("B", 0x80 | data_len)
        elif data_len < 2 ** 16:
            return b"\xde%b" % (struct.pack(">H", data_len))
        elif data_len < 2 ** 32:
            return b"\xdf%b" % (struct.pack(">I", data_len))
        else:
            raise f'dict {data} is too large'
