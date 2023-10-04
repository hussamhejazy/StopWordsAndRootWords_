import spacy

nlp = spacy.load("en_core_web_sm")


def get_tokens(words = []):
    tokens = []
    for sentence in words:
        doc = nlp(sentence)

        for token in doc:
            tokens.append(token)
            # print(f"{token.text}\t\t{token.pos_}\t{token.dep_}")
    return tokens
