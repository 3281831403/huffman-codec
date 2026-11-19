"""Huffman 编码：树、码表与位流：待实现的核心模块。"""


def frequencies(data):
    """统计字符频率。"""
    raise NotImplementedError

def build_codes(frequencies):
    """按频率构建前缀码。"""
    raise NotImplementedError

def encode(data, codes):
    """编码为位流。"""
    raise NotImplementedError

def decode(bits, codes):
    """按码表解码。"""
    raise NotImplementedError

def compression_ratio(data, bits):
    """压缩比。"""
    raise NotImplementedError
