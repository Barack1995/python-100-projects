
def count_text(sentence):
    words = sentence.split()
    word_count = len(words)
    characters = len(sentence)
    return word_count, characters

while True:

        sentence = input("Enter a sentence: ")
        if not sentence.strip():
            print("Please enter a valid sentence.")
            continue
    
        word_count, character_count = count_text(sentence)
        print(f"Word count: {word_count}")
        print(f"Character count: {character_count}")
        break
