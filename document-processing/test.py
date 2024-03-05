import unittest


# here are some sample documents

t_doc_simple_language = "Several bird species make and use tools. Some social species pass on some knowledge across generation. This is a form of culture. Birds are social animals."
t_doc_academic_paper = "This paper investigates the channel capacity of Internet-based timing channels and proposes a methodology for detecting covert timing channels based on how close a source comes to achieving that channel capacity. A statistical approach is then used for the special case of binary codes."
t_doc_school_physics = "What is the definition of a wave? The wave meaning is that a wave is an oscillating, regular distortion through spacetime. Some waves, called electromagnetic waves, can travel through a vacuum, or a space void of matter. Some waves, called mechanical waves, require a medium to propagate."
t_doc_kids = "Onions might taste good but they can be painful to chop. A gas is released when you cut onions that irritates you eyes, the tears you produce while this happens are your body’s way of washing it from your eyes."
# t_doc_inappropriate_for_kids = "bitch, fuck, "
# t_doc_colloquial = "y u always mad????"


class Test_Readability_Func(unittest.TestCase):

    # between max 121 (easy) and negative (diffcult)
    def test_flesch_reading_ease(self):
        self.assertLessEqual(ts.flesch_reading_ease(t_doc_academic_paper), 30)
        self.assertGreaterEqual(ts.flesch_reading_ease(t_doc_simple_language), 80)

    def test_grade_levels(self):
        # grade level necessary for comprehension, score appr. grade
        self.assertLessEqual(ts.automated_readability_index(t_doc_school_physics), 10)
        # score proportional to grade, < 4.9: <4th grade, 9.0-9.9: college student
        self.assertLessEqual(ts.dale_chall_readability_score(t_doc_kids), 6.9)
        self.assertGreaterEqual(ts.dale_chall_readability_score(t_doc_academic_paper), 9)