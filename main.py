
def main ():
    
    def read_book():
        with open("books/frankenstein.txt") as f:
            content = f.read()
        return content
    
    def count_words(content):
        words = content.split()
        count = len(words)
        return count
    
    def count_letters(content):    
        letter_count = {}
        for letter in content:
            if letter.isalpha():  # Only count alphabetic characters
                letter = letter.lower()
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
        return letter_count
    
    def generate_report(content, letter_count, word_count):
        report = []
        report.append(f"--- Begin report of books/frankenstein.txt ---")
        report.append(f"{word_count} words found in the document")
        
        sorted_letters_count = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
        
        for letter, count in sorted_letters_count:
            report.append(f"The '{letter}' character was found {count} times")
        
        report.append("--- End Report ---")

        return '\n'.join(report)
        
    
    content = read_book()
    word_count = count_words(content)
    letters = count_letters(content)
    report = generate_report(content, letters, word_count)
    
    print(report)

main()