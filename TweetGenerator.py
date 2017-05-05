from HashTable import HashTable


class TweetGenerator(object):

    def __init__(self, textfiles=None, table_size=10):
        """Initialize the Markov Chain with the given data"""
        self.hashtable = HashTable(table_size)
        if textfiles:
            if isinstance(textfiles, list):
                for text in textfiles:
                    self.fill(text)
            else:
                self.fill(textfiles)

    def append(self, item):
        self.hashtable.set(item, 1)

    def fill(self, textfile):
        word_list = self.file_to_word_list(textfile)
        word_shutter = []
        for index, word in enumerate(word_list):
            if index <= 1:
                word_shutter.append(word)
                print(word_shutter)
                continue
            else:
                key = (word_shutter[0], word_shutter[1])
                self.hashtable.set(key, word)
                word_shutter.pop(0)
                word_shutter.append(word)

    # Function takes in a file and splits it into its words.
    # Then function stores those words in a list
    def file_to_word_list(self, filename):
        # Create empty list to store words from the document.
        word_list = []
        # Use 'with' to also close file when the function is complete
        with open(filename) as f:
            # Split the file into its lines
            for line in f:
                # Split the line into its words
                for word in line.split():
                    # Take the word and lowercase it
                    word = word.lower()
                    # Add word to the list
                    word_list.append(word)

        # Return the full word_list
        return word_list


print(TweetGenerator('spacexarticle').hashtable.__str__)
