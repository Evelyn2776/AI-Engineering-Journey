from string_tools import clean_text, word_count

def test_clean_text():
    assert clean_text("  HELLO ") == "hello"

def test_word_count():
    assert word_count("I love Python") == 3  