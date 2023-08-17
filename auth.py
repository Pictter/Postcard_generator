def md5_hash(text: str) -> str:
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()

app.secret_key = md5_hash("your_secret_string_here")