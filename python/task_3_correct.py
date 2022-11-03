def counter(phrase: list) -> dict[int]:
    """
    Keeps track of items and their count.
    """
    dict_phrase = {}

    for word in phrase.lower().split():
        if word not in dict_phrase:
            dict_phrase[word] = 1
        else:
            dict_phrase[word] += 1
    return dict_phrase


class CountVectorizer:
    def __init__(self, corpus=None):
        self.corpus = corpus

    @staticmethod
    def get_feature_names() -> list[str]:
        """
        Gets vocabulary
        """
        base = []

        for phrase in corpus:
            for word in phrase.lower().split():
                if word not in base:
                    base.append(word)
        return base

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """"
        Return document-term matrix.
        """
        self.corpus = corpus
        base = self.get_feature_names()
        count_matrix = []

        for phrase in corpus:
            dict_phrase = counter(phrase)
            counter_list = [dict_phrase[word] if word in phrase.lower().split() else 0 for word in base]
            count_matrix.append(counter_list)
        return count_matrix


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(count_matrix)
