def transform_text(text, mode):
    text = str(text).strip()
    
    if text == "":
        return "No text provided."
    elif mode not in ("upper", "lower", "title", "reverse"):
        return "Invalid mode."
    
    if mode == "upper":
        text = text.upper()
        return text
    elif mode == "lower":
        text = text.lower()
        return text
    elif mode == "title":
        text = text.title()
        return text
    elif mode == "reverse":
        text = text[::-1]
        return text

print(transform_text("hola mundo", "reverse"))