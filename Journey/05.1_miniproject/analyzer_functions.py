def transform_text(text, mode):
    text = str(text).strip()
    
    if text == "":
        return "No text provided."
    elif mode not in ("upper", "lower", "title", "reverse"):
        return "Invalid mode."
    
    if mode == "upper":
        text = text.upper()
    elif mode == "lower":
        text = text.lower()
    elif mode == "title":
        text = text.title()
    elif mode == "reverse":
        text = text[::-1]
    return text

def analyze_text(text):
    text = str(text).strip()

    if text == "":
        return 0, 0, None
    
    symbols = ".,!?;:"

    for s in symbols:
        text = text.replace(s, "")
    
    total_words = len(text.split())
    total_letters = len(str(text).replace(" ", ""))
    longest_word = max(text.split(), key = len)
    
    return f"The number of words is: {total_words}\nThe number of letters is: {total_letters}\nThe largest word is: {longest_word}"

def word_frequency(text):
    text = text.lower()

    symbols = ".,!?;:"
    for s in symbols:
        text = text.replace(s, "")

    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    result = " | ".join([f"{word}: {count}" for word, count in word_count.items()])
    return result