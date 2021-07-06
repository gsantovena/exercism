def abbreviate(words):
    words = words.replace("-", " ").replace("_", "").upper()
    return "".join([w[0] for w in words.split()])
