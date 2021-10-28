import re

ZScores = [-2.326, -2.054, -1.881, -1.751, -1.645, -1.555, -1.476, -1.405, -1.341, -1.282, -1.227, -1.175,
           -1.126, -1.08, -1.036, -0.994, -0.954, -0.915, -
           0.878, -0.842, -0.806, -0.772, -0.739, -0.706,
           -0.674, -0.643, -0.613, -0.583, -0.553, -0.524, -
           0.496, -0.468, -0.44, -0.412, -0.385, -0.358,
           -0.332, -0.305, -0.279, -0.253, -0.228, -0.202, -
           0.176, -0.151, -0.126, -0.1, -0.075, -0.05,
           -0.025, 0.0, 0.025, 0.05, 0.075, 0.1, 0.126, 0.151, 0.176, 0.202, 0.228, 0.253, 0.279, 0.305,
           0.332, 0.358, 0.385, 0.412, 0.44, 0.468, 0.496, 0.524, 0.553, 0.583, 0.613, 0.643, 0.674,
           0.706, 0.739, 0.772, 0.806, 0.842, 0.878, 0.915, 0.954, 0.994, 1.036, 1.08, 1.126, 1.175,
           1.227, 1.282, 1.341, 1.405, 1.476, 1.555, 1.645, 1.751, 1.881, 2.054, 2.326]


def tokenize(text):
    # you may want to use a smarter tokenizer
    for match in re.finditer(r'\w+', text, re.UNICODE):
        yield match.group(0)


def getPercentileFromZScore(arg):
    x = len(ZScores)
    if (arg <= ZScores[0]):
        return 1.0
    if (arg >= ZScores[x - 1]):
        return x

    for idx, val in enumerate(ZScores):
        #print(idx, val)
        if (ZScores[idx] == arg):
            return idx+1
        if (arg > ZScores[idx] and arg < ZScores[idx + 1]):
            return idx + 1 + (arg - ZScores[idx]) / (ZScores[idx + 1] - ZScores[idx])

    return 0


def a(dict: dict, word: str):
    # return dict[word] if word in dict else 0
    if (word in dict):
        return dict[word]
    else:
        return 0


def calcClout(dict, tokenCount):
    f1 = a(dict, "we") + a(dict, "you") + a(dict, "social")
    f1 = f1 - a(dict, "i") - a(dict, "swear") - \
        a(dict, "negate")-a(dict, "differ")
    f1 = f1 / tokenCount * 100.0
    f1 = f1 + 10
    f1 = f1 - 10
    f1 = f1 / 10

    return getPercentileFromZScore(f1)


def calcAnalytic(dict, tokenCount):
    f1 = ((30.0 + (a(dict, "article") + a(dict, "prep") - a(dict, "pronoun") -
                   a(dict, "auxverb") - a(dict, "negate") - a(dict, "conj") - a(dict, "adverb"))
           / tokenCount * 100.0) - 9.5) / 14.0

    return getPercentileFromZScore(f1)


def calcAuthentic(dict, tokenCount):
    f1 = a(dict, "i") + a(dict, "insight") + a(dict, "differ") + \
        a(dict, "relativ") - a(dict, "discrep") - a(dict, "shehe")
    f1 = f1 / tokenCount * 100.0
    f1 = f1 - 21.0
    f1 = f1 / 6.0

    return getPercentileFromZScore(f1)


def calcTone(dict, tokenCount):
    f1 = a(dict, "posemo") - a(dict, "negemo")
    f1 = f1 / tokenCount * 100.0
    f1 = f1 - 1.3
    f1 = f1/2.0

    return getPercentileFromZScore(f1)
