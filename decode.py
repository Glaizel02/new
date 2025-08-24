import marshal, imp, struct, time

# paste your blob here (keep as str, not bytes)
data = '''c\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\xa5...'''

code = marshal.loads(data)

# write a valid .pyc file
with open("decoded.pyc", "wb") as f:
    f.write(imp.get_magic())
    f.write(struct.pack("i", int(time.time())))
    marshal.dump(code, f)

print("[+] Saved to decoded.pyc — now run uncompyle6 to decompile it")
