#!/usr/bin/env python
# # -*- coding: utf-8 -*-

import pytest
from .. import pycaesarcrypt


@pytest.fixture
def pycc():
    pycc = pycaesarcrypt.pycaesarcrypt()
    return pycc


class TestVariables(object):
    def test_alphabet_variable(self, pycc):
        assert 'abcdefghijklmnopqrstuvwxyz' == pycc.alphabet


class TestCaesarFunction(object):
    def test_caesar_encrypt_17_only_with_alphabet(self, pycc):
        enc = pycc.caesar('The quick brown fox jumps over the lazy dog', 17)
        assert enc == 'Kyv hlztb sifne wfo aldgj fmvi kyv crqp ufx'

    def test_caesar_encrypt_15_with_special_chars(self, pycc):
        enc = pycc.caesar('Test! The quick brown fox jumps over the lazy dog.', 15)
        assert enc == 'Ithi! Iwt fjxrz qgdlc udm yjbeh dktg iwt apon sdv.'

    def test_caesar_decrypt_12_only_with_alphabet(self, pycc):
        enc = pycc.caesar('Ftq cguow ndaiz raj vgybe ahqd ftq xmlk pas', -12)
        assert enc == 'The quick brown fox jumps over the lazy dog'

    def test_caesar_decrypt_4_with_special_chars(self, pycc):
        enc = pycc.caesar('Xiwx! Xli uymgo fvsar jsb nyqtw sziv xli pedc hsk.', -4)
        assert enc == 'Test! The quick brown fox jumps over the lazy dog.'


class TestEncryptDecryptFunctions(object):
    def test_encrypt_25_only_with_alphabet(self, pycc):
        enc = pycc.encrypt('The quick brown fox jumps over the lazy dog', 25)
        assert enc == 'Sgd pthbj aqnvm enw itlor nudq sgd kzyx cnf'

    def test_encrypt_7_with_special_chars(self, pycc):
        enc = pycc.encrypt('Test! The quick brown fox jumps over the lazy dog.', 7)
        assert enc == 'Alza! Aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.'

    def test_decrypt_19_only_with_alphabet(self, pycc):
        enc = pycc.decrypt('Max jnbvd ukhpg yhq cnfil hoxk max etsr whz', 19)
        assert enc == 'The quick brown fox jumps over the lazy dog'

    def test_decrypt_2_with_special_chars(self, pycc):
        enc = pycc.decrypt('Vguv! Vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi.', 2)
        assert enc == 'Test! The quick brown fox jumps over the lazy dog.'


class TestRot13Function(object):
    def test_encrypt_rot13_only_with_alphabet(self, pycc):
        enc = pycc.rot13('The quick brown fox jumps over the lazy dog')
        assert enc == 'Gur dhvpx oebja sbk whzcf bire gur ynml qbt'

    def test_encrypt_rot13_with_special_chars(self, pycc):
        enc = pycc.rot13('Test! The quick brown fox jumps over the lazy dog.')
        assert enc == 'Grfg! Gur dhvpx oebja sbk whzcf bire gur ynml qbt.'

    def test_decrypt_rot13_only_with_alphabet(self, pycc):
        enc = pycc.rot13('Gur dhvpx oebja sbk whzcf bire gur ynml qbt')
        assert enc == 'The quick brown fox jumps over the lazy dog'

    def test_decrypt_rot13_with_special_chars(self, pycc):
        enc = pycc.rot13('Grfg! Gur dhvpx oebja sbk whzcf bire gur ynml qbt.')
        assert enc == 'Test! The quick brown fox jumps over the lazy dog.'
