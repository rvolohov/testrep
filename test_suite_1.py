__author__ = 'roman'

from distutils.core import setup, Command

class Test_SanityTestSuite:
    def test_1(self):
        x = "sanity"
        assert 'san' in x

    def test_2(self):
        x = "hello"
        assert 'ello' in x
    def test_3(self):
        word = "new test"
        assert 'new' in word
    def test_4(self):
        word = "new test 2"
        assert 'new' in word
    def test_5(self):
        word = "cloudlock"
        assert 'cloud' in word