#  Importación del módulo de pruebas unitarias
import unittest

import CipherEngine

#  Construcción pruebas unitarias

class CipherTest( unittest.TestCase ):

    #  <ENCRIPTACIÓN>
    #  - TEST CASOS DE PRUEBA NORMALES -

     #  Test #1: Evalua si el mensaje se encriptó
    def test_correct_encryption(self):
        message = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja."
        key = "Pangrama1223"

        encrypted_message = CipherEngine.EncryptMessage(message, key)

        self.assertNotEqual(message, encrypted_message)

     #  Test #2: Evalua si el mensaje se encriptó
    def test_correct_encryption2(self):
        message = "Orgánulo de las células eucariontes en el que tiene lugar la respiración celular."
        key = "mitocrondria"

        encrypted_message = CipherEngine.EncryptMessage(message, key)

        self.assertNotEqual(message, encrypted_message)

     #  Test #3: Evalua si el mensaje se encriptó
    def test_correct_encryption3(self):
        message = "Los computadores no hacen lo que uno quiere, sino lo que uno les dice"
        key = "VerdadDolorosa1"

        encrypted_message = CipherEngine.EncryptMessage(message, key)

        self.assertNotEqual(message, encrypted_message)

    #   - TEST CASOS DE PRUEBA EXCEPCIONALES -
     #  Test #4: Prueba de mensaje con caracteres especiales:
    def test_special_characters_message(self):
        message = "¡H0l@ Mundo$!"
        key = "abcdefghij"

        encrypted_message = CipherEngine.EncryptMessage(message, key)

        self.assertNotEqual(message, encrypted_message)
    
     #  Test #5: Prueba de mensaje con caracteres repetidos:
    def test_upper_message(self):
        message = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        key = "Repeticion1010"

        encrypted_message = CipherEngine.EncryptMessage(message, key)

        self.assertNotEqual(message, encrypted_message)

     #  Test #6: Prueba con números como mensaje:
    def test_number_message(self):
        message = "3.14159265359"
        key = "PiTresPuntoCatorce"

        encrypted_message = CipherEngine.EncryptMessage(message, key)

        self.assertNotEqual(message, encrypted_message)


    #   - TEST CASOS DE PRUEBA ERROR -
     
     #  Test #7: Evalua si no se registró el mensaje
    def test_empty_message(self):
        message = None
        key = "6042380541"

        self.assertRaises( CipherEngine.EmptyMessageError, CipherEngine.EncryptMessage, message, key )

     #  Test #8: Evalua si no se registró la llave
    def test_empty_key(self):
        message = "Mañana te espero detrás de la fuente"
        key = None

        self.assertRaises( CipherEngine.EmptyKeyError, CipherEngine.EncryptMessage, message, key )

     #  Test #9: Evalua la longitud de la llave
    def test_key_length(self):
        message = "Mañana hay examen de cálculo"
        key = "12345"

        self.assertRaises( CipherEngine.KeyLengthError, CipherEngine.EncryptMessage, message, key )

     #  Test #10: Evalua si solo se entregó un caracter en el mensaje
    def test_one_character(self):
        message = "P"
        key = "1025789634"

        self.assertRaises( CipherEngine.OneCharacterMessageError, CipherEngine.EncryptMessage, message, key )


    #  <DESENCRIPTACIÓN>
    #  - TEST CASOS DE PRUEBA NORMALES -
        
     #  Test #11: Evalua si el mensaje encriptado se desencriptó
    def test_correct_decryption(self):
        encrypted_message = "oDKX72chZkebm15fiFryBed48GciGOg+XpYR9fog/hVJtGP7wWiAQtZWl5LcFm/f"
        key = "Saludo12345"

        decrypted_message = CipherEngine.DecryptMessage(encrypted_message, key)

        self.assertNotEqual(encrypted_message, decrypted_message)

     #  Test #12: Evalua si el mensaje encriptado se desencriptó
    def test_correct_decryption2(self):
        encrypted_message = "yLtQNG58ot+DT6jST7ko0OQO0X7p4LZyk/uupu6tnIpn9RNlzfukAQ6ne7qcPTH89ov28aBf0xXYpQ5uGoB7kvAB0rwOCBtxA0Pj8MHW1Qpd9A1eN3cHVGuiTPn+Mib32deocNCNv3XOwJkWZrU8sg"
        key = "VerdadDolorosa1"

        decrypted_message = CipherEngine.DecryptMessage(encrypted_message, key)

        self.assertNotEqual(encrypted_message, decrypted_message)
    
     #  Test #13: Evalua si el mensaje encriptado se desencriptó
    def test_correct_decryption3(self):
        encrypted_message = "Sm7I2OCYaND0qMfUWbWysk4RUhGS6xpGBkP2XSAi8xQ+tAsVEzdG4w3QfxRMImpGoLBLCq+v9ZPB3n8VyW8e9jmlwecY2nWn6Pqc7eZHqA93rYhS6idGFrW1PoaU1wRwIYOHeO98IQahh8uO6E269rc/AjZsQK6GDwPSKTu006w"
        key = "mitocondria"

        decrypted_message = CipherEngine.DecryptMessage(encrypted_message, key)

        self.assertNotEqual(encrypted_message, decrypted_message)

    #   - TEST CASOS DE PRUEBA EXCEPCIONALES -
     #  Test #14: Prueba de llave con caracteres especiales
    def test_special_characters_key(self):
        encrypted_message = "WPRjS7GVyaipziC6eRt3sSlYkBAw1GVqcxiVbRDSgAQEMV8ev4GqmV34vZjpT0wt"
        key = "(0nTr4$eña.13"

        decrypted_message = CipherEngine.DecryptMessage(encrypted_message, key)

        self.assertNotEqual(encrypted_message, decrypted_message)

     #  Test #15: Prueba donde la llave tiene espacios:
    def test_blank_key(self):
        encrypted_message = "WaR6L4HnlksdA/IuII6lVLprBepWnrxFG3uRmdW0e2EMx/37Pj8hgTtTRKf9vEPFU9ewPNA7rU5I6Dz9mcOJug"
        key = "deberia estudiar más"

        decrypted_message = CipherEngine.DecryptMessage(encrypted_message, key)

        self.assertNotEqual(encrypted_message, decrypted_message)

     #  Test #16: Prueba de llave con mismo caracter
    def test_same_characters_key(self):
        encrypted_message = "VEYjL2aBVRHXLGZxIvZsQcY1aaAd+DtrprxywJyeXf09Xh65q2cRkFIk0rQmauzRUBN18AP9jWzKAwdlB3yrEw"
        key = "rrrrrrrrrrrrrrrrrrr"

        decrypted_message = CipherEngine.DecryptMessage(encrypted_message, key)

        self.assertNotEqual(encrypted_message, decrypted_message)

    #   - TEST CASOS DE PRUEBA ERROR -

     #  Test #17: Evalua si no se registró el mensaje encriptado
    def test_empty_encrypted_message(self):
        encrypted_message = None
        key = "contraseña147"

        self.assertRaises( CipherEngine.EmptyEncryptedMessageError, CipherEngine.DecryptMessage, encrypted_message, key )

     #  Test #18: Evalua si no se registró la llave para desencriptar
    def test_empty_encryption_key(self):
        encrypted_message = "oDKX72chZkebm15fiFryBed48GciGOg+XpYR9fog/hVJtGP7wWiAQtZWl5LcFm/f"
        key = None

        self.assertRaises( CipherEngine.EmptyEncryptionKeyError, CipherEngine.DecryptMessage, encrypted_message, key )

    #  Test #19: Prueba con una llave errónea
    def test_wrong_key(self): 
        encrypted_message = "Tx0GDfLbXysB5rU0SMJ/QFs9/70VZXSvAOFP1vVxn2O623SpLFiwW9x8XsvmVbh2"
        key = "HolaMundo1320"

        self.assertRaises( CipherEngine.WrongKeyError, CipherEngine.DecryptMessage, encrypted_message, key )

    #  Test #20: Prueba con un mensaje encriptado corrupto
    def test_corrupt_encripted_message(self):
        encrypted_message = "Tx0GDfLbXysB5rU0SMJ/QFs9/70VZXS"
        key = "Chao_Mundo"

        self.assertRaises( CipherEngine.CorruptEncryptedMessageError, CipherEngine.DecryptMessage, encrypted_message, key )


if __name__ == '__main__':
    unittest.main()
        



