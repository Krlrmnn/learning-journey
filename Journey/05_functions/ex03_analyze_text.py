def analyzer(text1):
    text1 = str(text1).strip()

    if text1 == "":
        return 0, 0, None
    
    symbols1 = ".,!?;:"

    for s in symbols1:
        text1 = text1.replace(s, "")
    
    total_words = len(text1.split())
    total_letters = len(str(text1).replace(" ", ""))
    longest_word = max(text1.split(), key = len)
    
    return f"The number of words is: {total_words}\nThe number of letters is: {total_letters}\nThe largest word is: {longest_word}"


print(analyzer("Testing the code!"))