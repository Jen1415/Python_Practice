from collections import Counter
import re

class Word_Counter:

    STOP_WORDS = {
        "the", "is", "and", "a", "an", "of", "to", "in",
        "on", "for", "with", "that", "this", "it", "as",
        "at", "by", "from", "but", "not", "only", "also",
        "has", "have", "was", "were", "where"}
        

    def __init__ (self, filename):
        self.filename = filename
        self.word_cloud = Counter()



    def count_words(self):
        with open(self.filename,"r") as t:
        
            for line in t:
                line = line.lower()
                words = re.findall(r"[a-z]+", line)
            
            
                for word in words:
                    word = word.strip(",.!?'\"\\/<>\{\}[]:;()")
                    if word and word not in self.STOP_WORDS:
                        self.word_cloud[word] += 1

        return self.word_cloud
                


    def top_n_words(self, n = 5):
        return self.word_cloud.most_common(n)
          
    def words_alphabetical(self):
        return sorted(self.word_cloud.items())
        
def main():
    wc = Word_Counter("text.txt")
    wc.count_words()

    print("Top 5 most common words:")
    for word, count in wc.top_n_words(5):
        print(f"{word}: {count}")

    print("-----------------------------------")
    
    print("Words in alphabetical order:")
    for word, count in wc.words_alphabetical():
        print(f"{word}: {count}")
   

    # print top n common words
    # print the words in alphabetical order

main()