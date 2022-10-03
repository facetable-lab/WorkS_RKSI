import re
import unidecode


def slugify(text: str) -> str:
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text)

