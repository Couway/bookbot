from stats import num_of_words, num_of_symbols, get_report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = num_of_words(text)
    symbols = num_of_symbols(text)
    report = get_report(symbols)
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char in report:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")



def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
        

main()