from analyzer_functions import transform_text, analyze_text, word_frequency

text = input("Enter your text: ").strip()
if not text:
    print("No text provided.")
    exit()

while True:
    print("Choose an option: ")
    print("1. Analyze text")
    print("2. Transform text")
    print("3. Word frequency")
    print("4. Exit")
    option = input("Choose an option: ").strip()

    if option == "1":
        print("-- TEXT ANALYSIS --")
        print(analyze_text(text))
    elif option == "2":
        print("-- TEXT TRANSFORM --")
        mode = input("Choose mode (upper/lower/title/reverse): ").strip().lower()
        print(transform_text(text, mode))
    elif option == "3":
        print("-- WORD FREQUENCY --")
        print(word_frequency(text))
    elif option == "4":
        print("See you next time!")
        break
    else:
        print("Invalid option. Please try again.")