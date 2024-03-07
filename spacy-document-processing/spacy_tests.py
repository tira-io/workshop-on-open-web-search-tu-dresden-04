import spacy
import textstat as ts
import textdescriptives as td
import unittest

class Test_Spacy_Func(unittest.TestCase):

    def test_coherence(self):
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

    def test_ts_comparison(self):

        kln = spacy.load("en_core_web_sm")
        kln.add_pipe("textdescriptives/readability")
        t_doc_academic = "Convolutional neural networks are built upon the convolution operation, which extracts informative features by fusing spatial and channel-wise information together within local receptive fields. In order to boost the representational power of a network, several recent approaches have shown the benefit of enhancing spatial encoding. In this work, we focus on the channel relationship and propose a novel architectural unit, which we term the “Squeeze-and-Excitation” (SE) block, that adaptively recalibrates channel-wise feature responses by explicitly modelling interdependencies between channels. We demonstrate that by stacking these blocks together, we can construct SENet architectures that generalise extremely well across challenging datasets."

        cl = td.extract_df(kln(t_doc_academic))["coleman_liau_index"]
        self.assertAlmostEqual(float(cl.iloc[0]), ts.coleman_liau_index(t_doc_academic), delta = 1)
        # spaCy returns 19.30097, textstat returns 20.19, so despite using the same formulas, the libraries get different results.
        
        
if __name__ == '__main__':
    unittest.main()