import wikipedia

def searcher(question):
    answer = wikipedia.summary(question).split('.')
    for line in answer:
        print(line)

if __name__ == "__main__":
    question  = input("Search Wikipedia for: ")
    searcher(question)
