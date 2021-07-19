from Packer import Packer

packer = Packer()

def test_null():
    assert packer.pack_null() == b'\xc0'

def test_int():
    case1 = packer.pack_int(123456768111)
    case2 = packer.pack_int(-13)
    assert case1 == b'\xcf\x00\x00\x00\x1c\xbe\x98\xc8o'
    assert case2 == b'\xf3'

def test_bool():
    assert packer.pack_bool(True) == b'\xc3'
    assert packer.pack_bool(False) == b'\xc2'

def test_float():
    case1 = 0.138348412337
    case2 = -1.334
    assert packer.pack_float(case1) == b'\xcb?\xc1\xb5f\x998p\xa7'
    assert packer.pack_float(case2) == b'\xcb\xbf\xf5X\x10bM\xd2\xf2'

def test_str():
    case1 = 'foo'
    byte, data = packer.pack_str(case1)
    assert byte == b'\xa3'
    assert data == b'foo'

def test_dict():
    case1 = { 'foo':'bar' }
    assert packer.pack_dict(case1) == b'\x81'

def test_arr():
    case1 = ['covid', 19]
    assert packer.pack_arr(case1) == b'\x92'
