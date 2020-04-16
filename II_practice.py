class Sentence(object):

    def __init__(self, sentence):
        self.words = sentence.split()
        self.end = len(self.words)
        self.value = 0

    # return self as iterator object
    def __iter__(self):
        return self

    # lets make it a proper iterator object
    def __next__(self):
        current = self.value
        if current >= self.end:
            raise StopIteration
        self.value += 1
        return self.words[current]


# need to be able to iterate over this
my_sentence = Sentence('this is a test')

for word in my_sentence:
    print(word)


print('-'*10)


def sentence(sent):
    words = sent.split()
    for word in words:
        yield word


my_sentence = 'this is a test'
my_s = sentence(my_sentence)
for s in my_s:
    print(s)
