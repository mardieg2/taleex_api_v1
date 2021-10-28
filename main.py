import os
import calculation
from liwc import Liwc

LIWC_FILEPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'dict/LIWC2015_English_Flat.dic'))


if __name__ == "__main__":
    liwc = Liwc(LIWC_FILEPATH)

    # print(liwc.categories)
    # print(liwc.lexicon)

    # print(liwc.search('beautiful'))

#     text = """When denial (his or ours) can no longer hold and we finally have to admit to ourselves that we’ve been lied to, we search frantically for ways to keep it from disrupting our lives. So we rationalize. We find “good reasons” to justify his lying, just as he almost always accompanies his confessions with “good reasons” for his lies. He tells us he only lied because…. We tell ourselves he only lied because…. We make excuses for him: The lying wasn’t significant/Everybody lies/He’s only human/I have no right to judge him.

# Allowing the lies to register in our consciousness means having to make room for any number of frightening possibilities:

# • He’s not the man I thought he was.
# • The relationship has spun out of control and I don’t know
# what to do
# • The relationship may be over.

# Most women will do almost anything to avoid having to face these truths. Even if we yell and scream at him when we discover that he’s lied to us, once the dust settles, most of us will opt for the comforting territory of rationalization. In fact, many of us are willing to rewire our senses, short-circuit our instincts and intelligence, and accept the seductive comfort of self-delusion.”  # .split(' ')
# """
# info': {'clout': 50, 'analytics': 92.83501006036217, 'authentic': 1.0, 'tone': 25.774193548387096}

#     text = """
#     His lying is not contigent on who you are or what you do. His lying is not your fault. Lying is his choice and his problem, and if he makes that choice with you, he will make it with any other woman he’s with. That doesn’t mean you’re an angel and he’s the devil. It does mean that if he doesn’t like certain things about you, he has many ways to address them besides lying. If there are sexual problems between you, there are many resources available to help you. Nothing can change until you hold him responsible and accountable for lying and stop blaming yourself.

# The lies we tell ourselves to keep from seeing the truth about our lovers don’t feel like lies. They feel comfortable, familiar, and true. We repeat them like a mantra and cling to them like security blankets, hoping to calm ourselves and regain our sense that the world works the way we believe it ought to.
# Self-lies are false friends we look to for comfort and protection—and for a short time they may make us feel better. But we can only keep the truth at bay for so long. Our self-lies can’t erase his lies, and as we’ll see, the longer we try to pretend they can, the more we deepen the hurt.”
#     """


text = """
In the study, published to arXiv, the researchers from Cornell University developed an Android messaging app to collect sample texts from a large number of participants.

Over the course of seven days, the team gathered a total of 1,703 conversations.

They then removed the conversations that did not contain any lies, leaving them with 351.

After separating the lying and truthful messages, the team averaged word counts for each type of message, as well as for gender and student status.

They also looked at the percentages of ‘self-words’ (such as I/I’m), ‘other-words,’ (you), and noncommittal phrases (probably, possible, sure, etc).

‘Pronouns are particularly interesting in deception because one actively chooses which pronouns he/she wants to use when communicating,’ the authors explain in the paper.

‘Self-oriented pronouns show ownership and responsibility while other-oriented pronouns can signal distance and lack of accountability.’
"""

tokens_enum = calculation.tokenize(text)
tokens = list(tokens_enum)

l = len(tokens)

result = liwc.parse(tokens)

print({
    # 'classification': result,
    'info': {
        'clout': calculation.calcClout(result, l),
        'analytics': calculation.calcAnalytic(result, l),
        'authentic': calculation.calcAuthentic(result, l),
        'tone': calculation.calcTone(result, l)
    }
})
