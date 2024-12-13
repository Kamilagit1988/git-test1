import unittest

def skip_if_frozen(cls):
    for attr in dir(cls):
        if attr.startswith('test'):
            method = getattr(cls, attr)
            if callable(method):
                if cls.is_frozen:
                    @unittest.skip("Тесты в этом кейсе заморожены!")
                    def skip(*args, **kwargs):
                        pass
                    setattr(cls, attr, skip)
    return cls
@skip_if_frozen
class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_challenge(self):
        '''
        тесты для RunnerTest
        :return:
        '''
        pass

    def test_run(self):
        pass

    def test_walk(self):
        pass

@skip_if_frozen
class TournamentTest(unittest.TestCase):
    is_frozen = True

    def test_first(self):
        '''
        тесты для TournamentTest
        :return:
        '''
        pass

    def test_second(self):
        pass

    def test_third(self):
        pass