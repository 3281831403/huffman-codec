# Huffman 编码：树、码表与位流

压缩后的音频包解不回原字节：频率统计漏掉单字符，建树没有按频率合并，码表分配左右反了，编码没有拼接位流，解码没有按前缀树，单字符没有兜底码，压缩比按字节数而不是位数，空输入崩溃，批量编码只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
codec/__init__.py
codec/huffman.py
tests/test_huffman.py
```

## 当前状态

`codec/huffman.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_huffman.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 频率统计
2. 按频率建树
3. 码表左右一致
4. 位流拼接
5. 前缀树解码
6. 单字符兜底
7. 压缩比按位数
8. 空输入处理

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `codec/huffman.py`
后 15 条用例应全部通过。
