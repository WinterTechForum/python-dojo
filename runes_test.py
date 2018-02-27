import pytest
import runes

@pytest.fixture
def BREVE_LINE():
    return '016D;LATIN SMALL LETTER U WITH BREVE;Ll;0;L;0075 0306;;;;N;LATIN SMALL LETTER U BREVE;;016C;;016C'

@pytest.fixture
def BREVE_CODEPOINT_NAME():
    return 'LATIN SMALL LETTER U WITH BREVE'

@pytest.fixture
def EMPTY_LINE():
    return ''

@pytest.fixture
def TEST_LINES():
    return [
        '0020;SPACE;Zs;0;WS;;;;;N;;;;;',
        '0021;EXCLAMATION MARK;Po;0;ON;;;;;N;;;;;',
        '0022;QUOTATION MARK;Po;0;ON;;;;;N;;;;;',
        '0023;NUMBER SIGN;Po;0;ET;;;;;N;;;;;',
        '0024;DOLLAR SIGN;Sc;0;ET;;;;;N;;;;;',
    ]

def test_getlines():
    lines = runes.getlines()
    assert len(lines) > 10000


def test_splitline(BREVE_LINE):
    code, codepoint_name = runes.splitline(BREVE_LINE) # splittling on ';'
    assert code == '016D'
    assert codepoint_name == 'LATIN SMALL LETTER U WITH BREVE'

def test_matchline_no_match(EMPTY_LINE):
   testMatch = 'BREVE'
   result = runes.matchline(testMatch, EMPTY_LINE)
   assert not result

def test_matchline_one_match(BREVE_CODEPOINT_NAME):
   testMatch = 'BREVE'
   result = runes.matchline(testMatch, BREVE_CODEPOINT_NAME)
   assert result

def test_matchline_partial_no_match(BREVE_CODEPOINT_NAME):
   testMatch = 'LET'
   found = runes.matchline(testMatch, BREVE_CODEPOINT_NAME)
   assert not found

def test_matchline_multi_words_in_order_match(BREVE_CODEPOINT_NAME):
    testMatch = 'SMALL LETTER'
    found = runes.matchline(testMatch, BREVE_CODEPOINT_NAME)
    assert found

def test_matchline_multi_words_out_of_order_match(BREVE_CODEPOINT_NAME):
    testMatch = 'LETTER SMALL'
    found = runes.matchline(testMatch, BREVE_CODEPOINT_NAME)
    assert found

def test_matchline_case_insensitive_match(BREVE_CODEPOINT_NAME):
    testMatch = 'small'
    found = runes.matchline(testMatch, BREVE_CODEPOINT_NAME)
    assert found

def test_matchlines_no_match(TEST_LINES):
    found = runes.matchlines('FOO',TEST_LINES)
    assert len(list(found)) == 0

def test_matchlines_one_match(TEST_LINES):
    found = runes.matchlines('QUOTATION',TEST_LINES)
    assert len(list(found)) == 1


