import unittest
from app.services.bibtex_service import BibtexService

class TestBibtexService(unittest.TestCase):
    def setUp(self):
        book1 = ("1",
                 'This name contains "quotation" marks', 
                 "This title contains $ sign", 
                 "Author contains {curly} braces", 
                 "2001")

        book2 = ("2",
                 "BOOK2", 
                 "Title B2", 
                 "Author B2", 
                 "2002")

        article1 = ("1",
                    "ARTICLE1", 
                    "Title A1", 
                    "Author A1", 
                    "Journal A1", 
                    "2021", "1", 
                    "11-12")

        article2 = ("2",
                    "ARTICLE2", 
                    "Title A2", 
                    "Author A2", 
                    "Journal A2", 
                    "2022", 
                    "2", 
                    "22-23")

        self.books = [book1, book2]
        self.articles = [article1, article2]

        self.bibtex_service = BibtexService(self.books, self.articles)

    def test_generate_bibtex_srt_returns_empty_str_if_no_refs(self):
        bibtex_service = BibtexService([], [])
        bibtex_srt = bibtex_service.generate_bibtex_str()

        self.assertEqual(bibtex_srt, "")

    def test_generate_bibtex_str_includes_all_ref_keys(self):
        bibtex_str = self.bibtex_service.generate_bibtex_str()

        book_keys = list(map(lambda ref: ref[0], self.books))
        article_keys = list(map(lambda ref: ref[0], self.articles))
        keys =  book_keys + article_keys

        self.assertTrue(all(key in bibtex_str for key in keys))

    def test_generate_bibtex_str_escapes_dollar_sign_correctly(self):
        bibtex_srt = self.bibtex_service.generate_bibtex_str()

        self.assertTrue("contains \\$" in bibtex_srt)

    def test_generate_bibtex_str_escapes_quotation_mark_correctly(self):
        bibtex_srt = self.bibtex_service.generate_bibtex_str()

        self.assertTrue('\\"quotation\\"' in bibtex_srt)

    def test_generate_bibtex_str_escapes_curly_braces_correctly(self):
        bibtex_srt = self.bibtex_service.generate_bibtex_str()

        self.assertTrue("\\{curly\\}" in bibtex_srt)
