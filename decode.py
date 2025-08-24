import marshal, imp, struct, time

# Read the obfuscated file
with open(".Akun/.Rt", "rb") as f:
    data = f.read()

# Try to interpret it as marshal payload
code = marshal.loads(data)

# Dump to .pyc
with open("decoded.pyc", "wb") as f:
    f.write(imp.get_magic())
    f.write(struct.pack("i", int(time.time())))
    marshal.dump(code, f)

print("[+] Saved to decoded.pyc")
