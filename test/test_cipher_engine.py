import unittest
import sys
sys.path.append("src")

from CipherEngine.CipherEngine import CipherEngine, EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError

class CipherTest( unittest.TestCase ):
    """
    Unit Tests for text encryption

    Pruebas unitarias para encriptar o desencriptar texto
    """

    def test_correct_encryption(self):
        """ Normal input text and key  """
        text_to_encrypt = "Prueba"
        key = "12"

        expected_encrypted_text = "a@DWSS"

        encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

        self.assertEqual(encrypted_text, expected_encrypted_text)
     
    def test_correct_encryption2(self):
        """ Normal input text and key  """
        text_to_encrypt = "Emily and Harry were sitting in the park"
        key = "258"

        expected_encrypted_text = "wXQ^LS[\}Y@GAB]@PA\LF\VUQ\LZPBTJY"

        encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

        self.assertEqual(encrypted_text, expected_encrypted_text)

    def test_correct_encryption3(self):
        """ Normal input text and key  """
        text_to_encrypt = "Los computadores no hacen lo que uno quiere, sino lo que uno les dice"
        key = "2380541"

        expected_encrypted_text = "~\KV[\BFLQQ[CW@^ZYSP]^X^BMUA_]IE\QCWC\Z^_WDATFV_XTA\YVQ"

        encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

        self.assertEqual(encrypted_text, expected_encrypted_text)

    def test_same_characters_key(self):
        """ Repeated characters input key """
        text_to_encrypt = "Si la vida te da limones"
        key = "55555"

        expected_encrypted_text = "f\YTC\QTAPQTY\XZ[PF"

        encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

        self.assertEqual(encrypted_text, expected_encrypted_text)
    
    def test_same_characters_text(self):
        """ Repeated characters input text """
        text_to_encrypt = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        key = "30372595"

        expected_encrypted_text = "rqrvstxtrqrvstxtrqrvstxtrqrvstxtrqrvstxtrq"

        encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

        self.assertEqual(encrypted_text, expected_encrypted_text)

    def test_number_text(self):
        """ Number input text """
        text_to_encrypt = "3.14159265359"
        key = "Pi"

        expected_encrypted_text = "cGa]a\i[f\c\i"

        encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

        self.assertEqual(encrypted_text, expected_encrypted_text)

    def test_empty_text(self):
        """ empty input text """
        text_to_encrypt = None
        key = "6042380541"

        self.assertRaises( EmptyTextError, CipherEngine.EncryptText, text_to_encrypt, key )

    def test_empty_key(self):
        """ empty input key """
        text_to_encrypt = "Mañana te espero detrás de la fuente"
        key = None

        self.assertRaises( EmptyKeyError, CipherEngine.EncryptText, text_to_encrypt, key )

    def test_special_character_key(self):
        """ special characters input key """
        text_to_encrypt = "Mañana hay examen de cálculo"
        key = "$oñ@r."

        self.assertRaises( KeyCharacterError, CipherEngine.EncryptText, text_to_encrypt, key )

    def test_longer_key(self):
        """ Input key is longer than the input text """
        text_to_encrypt = "P"
        key = "1025789634"

        self.assertRaises( LongerKeyError, CipherEngine.EncryptText, text_to_encrypt, key )


    def test_correct_decryption(self):
        """ Normal input encrypted text and key  """
        encrypted_text = "a@DWSS"
        key = "12"

        expected_og_text = "Prueba"

        decrypted_text = CipherEngine.DecryptText(encrypted_text, key)

        self.assertEqual(decrypted_text, expected_og_text)

    def test_correct_decryption2(self):
        """ Normal input encrypted text and key  """
        encrypted_text = "wXQ^LS[\}Y@GAB]@PA\LF\VUQ\LZPBTJY"
        key = "258"

        expected_og_text = "Emily and Harry were sitting in the park"

        decrypted_text = CipherEngine.DecryptText(encrypted_text, key)

        self.assertEqual(decrypted_text, expected_og_text)
    
    def test_correct_decryption3(self):
        """ Normal input encrypted text and key  """
        encrypted_text = "~\KV[\BFLQQ[CW@^ZYSP]^X^BMUA_]IE\QCWC\Z^_WDATFV_XTA\YVQ"
        key = "2380541"

        expected_og_text = "Los computadores no hacen lo que uno quiere, sino lo que uno les dice"

        decrypted_text = CipherEngine.DecryptText(encrypted_text, key)

        self.assertEqual(decrypted_text, expected_og_text)

    def test_alphanumeric_key(self):
        """ Alphanumeric input encryption key """
        encrypted_text = "R@ES"
        key = "pw12"

        expected_og_text = "encriptar"

        decrypted_text = CipherEngine.DecryptText(encrypted_text, key)

        self.assertEqual(decrypted_text, expected_og_text)

    def test_one_character_key(self):
        """ One character input encryption key """
        encrypted_text = "APUCPBEC^"
        key = "1"

        expected_og_text = "padrastro"

        decrypted_text = CipherEngine.DecryptText(encrypted_text, key)

        self.assertEqual(decrypted_text, expected_og_text)
 
    def test_same_cipher_key(self):
        """ Repeated characters input encryption key """
        encrypted_text = "4	"
        key = "fffff"

        expected_og_text = "Repetido"

        decrypted_text = CipherEngine.DecryptText(encrypted_text, key)

        self.assertEqual(decrypted_text, expected_og_text)

    def test_empty_encrypted_text(self):
        """ empty input encrypted text """
        encrypted_text = None
        key = "6042380541"

        self.assertRaises( EmptyTextError, CipherEngine.DecryptText, encrypted_text, key )

    def test_empty_encryption_key(self):
        """ empty input encryption key """
        encrypted_text = "w@SJMSSJBM@\N_\X\Y"
        key = None

        self.assertRaises( EmptyKeyError, CipherEngine.DecryptText, encrypted_text, key )

    def test_special_character_encryption_key(self): 
        """ special characters input encryption key """
        encrypted_text = "}/_��T#	"
        key = "5@lu.dº"

        self.assertRaises( KeyCharacterError, CipherEngine.DecryptText, encrypted_text, key )

    def test_longer_encryption_key(self):
        """ Input encryption key is longer than the input encrypted text """
        encrypted_text = "p\GQZ\^A"
        key = "Dispositivodevision"

        self.assertRaises( LongerKeyError, CipherEngine.DecryptText, encrypted_text, key )


if __name__ == '__main__':
    unittest.main()