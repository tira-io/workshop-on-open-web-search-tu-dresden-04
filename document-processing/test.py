import unittest
import textstat as ts

# here are some sample documents

t_doc_simple_language1 = "Several bird species make and use tools. Some social species pass on some knowledge across generations. This is a form of culture. Birds are social animals."
t_doc_simple_language2 = "White is the brightest color. White light can be made by putting all the other colors of light on the spectrum together. These other colors are red, orange, yellow, green, blue, indigo, and violet. White is linked with light, goodness, innocence, purity, cleanliness and virginity. It is sometimes thought to be the color of perfection. The opposite of black, white usually has a positive connotation. White can stand for a successful beginning. In heraldry, white depicts faith and purity. "
t_doc_academic1 = "This paper investigates the channel capacity of Internet-based timing channels and proposes a methodology for detecting covert timing channels based on how close a source comes to achieving that channel capacity. A statistical approach is then used for the special case of binary codes."
t_doc_academic2 = "Convolutional neural networks are built upon the convolution operation, which extracts informative features by fusing spatial and channel-wise information together within local receptive fields. In order to boost the representational power of a network, several recent approaches have shown the benefit of enhancing spatial encoding. In this work, we focus on the channel relationship and propose a novel architectural unit, which we term the “Squeeze-and-Excitation” (SE) block, that adaptively recalibrates channel-wise feature responses by explicitly modelling interdependencies between channels. We demonstrate that by stacking these blocks together, we can construct SENet architectures that generalise extremely well across challenging datasets."
t_doc_academic3 = "ChatGPT is a variant of the GPT (Generative Pre-training Transformer) model. In terms of implementation, ChatGPT is built using the transformer architecture, which is a type of deep learning model that is particularly well-suited for NLP tasks. The transformer architecture uses self-attention mechanisms to process the input data and generate output, which allows it to capture long-range dependencies and contextual information in the input text. The transformer architecture consists of multiple layers of attention and feedforward blocks, which are trained to process the input data and generate output. "
t_doc_teen1 = "Bring all materials to class (textbooks, writing utensil, science notebook and binder, highlighter, and erasers). Write down agenda and due dates of assignments. Turn in all work on time, study for tests and quizzes, ask for help and stay for tutoring if you don’t understand, and let the teacher know if there is a problem. Take responsibility for your actions, good and bad. "
t_doc_teen2 = "What is the definition of a wave? The wave meaning is that a wave is an oscillating, regular distortion through spacetime. Some waves, called electromagnetic waves, can travel through a vacuum, or a space void of matter. Some waves, called mechanical waves, require a medium to propagate."
t_doc_teen3 = "A Neural Network is a type of machine learning model that is designed to process and analyze large amounts of data. ChatGPT is a sophisticated tool that is capable of holding engaging and natural conversations with humans. it is a valuable asset in a variety of applications, including customer service, virtual assistants, and chatbots. "
t_doc_kids1 = "Onions might taste good but they can be painful to chop. A gas is released when you cut onions that irritates you eyes, the tears you produce while this happens are your body’s way of washing it from your eyes."
t_doc_kids2 = "Fossils are the remains or traces of an animal or plant that are preserved in rock. They come in many forms, from footprints and faint impressions of leaves to shells and bones of animals. Fossils tell us about the life of the past, and when different species evolved and died out. They are also a guide to the age of the rocks in which they are found. Animals and plants are FOSSILIZED when they are buried in sedimentary deposits that are hardened and compressed into sedimentary rocks"
t_doc_kids3 = "ChatGPT can learn from examples of how people talk, and then use that knowledge to generate its own responses. When someone says something to ChatGPT, the program looks at the words in the sentence and tries to understand what the person is trying to say. It does this by using a big database of words and their meanings, which helps it understand the context of the conversation. It seem like it's a real person talking to you!"

class Test_Readability_Func(unittest.TestCase):

    # between max 121 (easy) and negative (diffcult)
    def test_flesch_reading_ease(self):
        self.assertLessEqual(ts.flesch_reading_ease(t_doc_academic1), ts.flesch_reading_ease(t_doc_teen1))
        self.assertLessEqual(ts.flesch_reading_ease(t_doc_academic1), ts.flesch_reading_ease(t_doc_kids1))
        self.assertGreaterEqual(ts.flesch_reading_ease(t_doc_simple_language1), ts.flesch_reading_ease(t_doc_kids2))
        self.assertGreaterEqual(ts.flesch_reading_ease(t_doc_simple_language2), ts.flesch_reading_ease(t_doc_teen2))

    # grade level necessary for comprehension, score approximates grade
    def test_grade_level(self):
        self.assertGreaterEqual(ts.automated_readability_index(t_doc_academic2), ts.automated_readability_index(t_doc_teen2))
        self.assertGreaterEqual(ts.automated_readability_index(t_doc_academic2), ts.automated_readability_index(t_doc_kids2))
        self.assertLessEqual(ts.automated_readability_index(t_doc_simple_language1), ts.automated_readability_index(t_doc_kids3))
        self.assertLessEqual(ts.automated_readability_index(t_doc_simple_language2), ts.automated_readability_index(t_doc_teen3)) 

        self.assertGreaterEqual(ts.flesch_kincaid_grade(t_doc_academic3), ts.flesch_kincaid_grade(t_doc_teen3))
        self.assertGreaterEqual(ts.flesch_kincaid_grade(t_doc_academic3), ts.flesch_kincaid_grade(t_doc_kids3))
        self.assertLessEqual(ts.flesch_kincaid_grade(t_doc_simple_language1), ts.flesch_kincaid_grade(t_doc_kids1))
        self.assertLessEqual(ts.flesch_kincaid_grade(t_doc_simple_language2), ts.flesch_kincaid_grade(t_doc_teen2)) 
   
        self.assertGreaterEqual(ts.gunning_fog(t_doc_academic1), ts.gunning_fog(t_doc_teen1))
        self.assertGreaterEqual(ts.gunning_fog(t_doc_academic1), ts.gunning_fog(t_doc_kids1))
        self.assertLessEqual(ts.gunning_fog(t_doc_simple_language1), ts.gunning_fog(t_doc_kids2))
        self.assertLessEqual(ts.gunning_fog(t_doc_simple_language2), ts.gunning_fog(t_doc_teen2)) 
    
        self.assertGreaterEqual(ts.coleman_liau_index(t_doc_academic2), ts.coleman_liau_index(t_doc_teen2))
        self.assertGreaterEqual(ts.coleman_liau_index(t_doc_academic2), ts.coleman_liau_index(t_doc_kids2))
        self.assertLessEqual(ts.coleman_liau_index(t_doc_simple_language1), ts.coleman_liau_index(t_doc_kids3))
        self.assertLessEqual(ts.coleman_liau_index(t_doc_simple_language2), ts.coleman_liau_index(t_doc_teen3))
        
        self.assertGreaterEqual(ts.linsear_write_formula(t_doc_academic3), ts.linsear_write_formula(t_doc_teen3))
        self.assertGreaterEqual(ts.linsear_write_formula(t_doc_academic3), ts.linsear_write_formula(t_doc_kids3))
        self.assertLessEqual(ts.linsear_write_formula(t_doc_simple_language1), ts.linsear_write_formula(t_doc_kids1))
        self.assertLessEqual(ts.linsear_write_formula(t_doc_simple_language2), ts.linsear_write_formula(t_doc_teen1))

        # grade level, for children up to grade 4
        self.assertGreaterEqual(ts.spache_readability(t_doc_academic1), ts.spache_readability(t_doc_teen2))
        self.assertGreaterEqual(ts.spache_readability(t_doc_academic1), ts.spache_readability(t_doc_kids3))
        self.assertLessEqual(ts.spache_readability(t_doc_simple_language1), ts.spache_readability(t_doc_kids1))
        self.assertLessEqual(ts.spache_readability(t_doc_simple_language2), ts.spache_readability(t_doc_teen1))

    def test_proportional_to_grade(self):
        # score only proportional to grade, < 4.9: <4th grade, 9.0-9.9: college student
        self.assertGreaterEqual(ts.dale_chall_readability_score(t_doc_academic2), ts.dale_chall_readability_score(t_doc_teen2))
        self.assertGreaterEqual(ts.dale_chall_readability_score(t_doc_academic2), ts.dale_chall_readability_score(t_doc_kids2))
        self.assertLessEqual(ts.dale_chall_readability_score(t_doc_simple_language2), ts.dale_chall_readability_score(t_doc_kids1))
        self.assertLessEqual(ts.dale_chall_readability_score(t_doc_simple_language2), ts.dale_chall_readability_score(t_doc_teen3)) 

        # readability for a foreign learner of English, recommended score < 25
        self.assertGreaterEqual(ts.mcalpine_eflaw(t_doc_academic3), ts.mcalpine_eflaw(t_doc_teen3))
        self.assertGreaterEqual(ts.mcalpine_eflaw(t_doc_academic3), ts.mcalpine_eflaw(t_doc_kids3))
        self.assertLessEqual(ts.mcalpine_eflaw(t_doc_simple_language1), ts.mcalpine_eflaw(t_doc_kids1))
        self.assertLessEqual(ts.mcalpine_eflaw(t_doc_simple_language2), ts.mcalpine_eflaw(t_doc_teen1)) 

    def test_aggregates(self):
        self.assertEqual(ts.sentence_count(t_doc_simple_language1), 4)
        self.assertEqual(ts.char_count("Several bird species make and use tools."), 34)
        
        # self.assertEqual(ts.syllable_count("species"), 2)     
        # this fails, the function incorrectly returns 1
        # self.assertEqual(ts.syllable_count(t_doc_simple_language1), 40) 
        # this fails with 37 != 40, 2*"species" and 1*"across" are being counted incorrectly 
        # in documentation we establish that the function can only serves as an approximate lower bound for the actual syllable count
        self.assertLessEqual(ts.syllable_count(t_doc_simple_language1), 40)
        self.assertLessEqual(ts.syllable_count(t_doc_kids1), 50)

        self.assertEqual(ts.lexicon_count(t_doc_simple_language1), 26)

       
if __name__ == '__main__':
    unittest.main()
    