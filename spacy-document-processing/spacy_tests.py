import spacy
import textdescriptives as td
# we need this bigger model which comes with word vectors
nlp = spacy.load("en_core_web_md")

# extreme examples for non-/coherence, let's check if the metrics reflect this 
nlp.add_pipe("textdescriptives/coherence") 
t_doc_garbage = nlp("The world is changed. Ice cream is pretty rad. Cheese cheese cheese oh yeah cheese. Henry Frottey is a master of wateriness. It's fun to stay at the Y M C A. Cupbards on the highway")
t_doc_coherent = nlp("White is the brightest color. White light can be made by putting all the other colors of light on the spectrum together. These other colors are red, orange, yellow, green, blue, indigo, and violet. White is linked with light, goodness, innocence, purity, cleanliness and virginity. It is sometimes thought to be the color of perfection. The opposite of black, white usually has a positive connotation. White can stand for a successful beginning. In heraldry, white depicts faith and purity.")

t_doc_garbage._.coherence
garb = td.extract_df(t_doc_garbage)
coh = td.extract_df(t_doc_coherent)
print(garb, coh)
# they do