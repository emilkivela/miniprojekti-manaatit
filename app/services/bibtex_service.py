
class BibtexService:

    def __init__(self, filename, books, articles):
        self._filename = filename
        self._books = self._escape_special_chars(books)
        self._articles = self._escape_special_chars(articles)

    def create_bibtex_file(self):
        bibtex_str = self._generate_bibtex_str()

        with open("app/" + self._filename, "w", encoding="utf-8") as file:
            file.write(bibtex_str)

    def _generate_bibtex_str(self):
        bibtex_str = ""

        for book in self._books:
            bibtex_str += self._stringify_book(book)

        for article in self._articles:
            bibtex_str += self._stringity_article(article)

        return bibtex_str

    def _stringify_book(self, book):
        return (
            f"@book{{{book[1]},\n"
            f"  title = \"{book[2]}\",\n"
            f"  author = \"{book[3]}\",\n"
            f"  year = \"{book[4]}\"\n"
            f"}}\n\n"
            f''
        )

    def _stringity_article(self, article):
        return (
            f"@article{{{article[1]},\n"
            f"  title = \"{article[2]}\",\n"
            f"  author = \"{article[3]}\",\n"
            f"  journal = \"{article[4]}\",\n"
            f"  year = \"{article[5]}\",\n"
            f"  volume = \"{article[6]}\",\n"
            f"  pages = \"{article[7]}\"\n"
            f"}}\n\n"
        )

    def _escape_special_chars(self, ref_list):
        result = []
        for ref in ref_list:
            new_ref = []
            for field in ref:
                field = str(field)
                edited_field = field.replace('"', '\\"') \
                                .replace('$', '\$') \
                                .replace('{', '\{') \
                                .replace('}', '\}')
                new_ref.append(edited_field)
            result.append(new_ref)

        return result
