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

        expected_encrypted_message = "Oay7xvZPa+tzpwFCcVrJR1Et4wkfnJKVdDWZcFyPsUmCuXdR1asmy7HbycFuX6fSIVvLLaICTBx0c9YnLh3g7a/E5n1SDPE8X3FT1RBHoxsv9VTbbmZq3Yi77P/vezsTeNfYswwtmAQE/wls1rBv962qC8Wh6FXqxWax/JAfji7f9Gn5TbdOfYpce18JzIlfhGgBMQuJjvSa30DMvBRxOQ"

        encrypted_message = CipherEngine.EncryptMessage(message, key)

        self.assertEqual(encrypted_message, expected_encrypted_message)

     #  Test #2: Evalua si el mensaje se encriptó
    def test_correct_encryption2(self):
        message = "Orgánulo de las células eucariontes en el que tiene lugar la respiración celular."
        key = "mitocrondria"

        expected_encrypted_message = "Sm7I2OCYaND0qMfUWbWysk4RUhGS6xpGBkP2XSAi8xQ+tAsVEzdG4w3QfxRMImpGoLBLCq+v9ZPB3n8VyW8e9jmlwecY2nWn6Pqc7eZHqA93rYhS6idGFrW1PoaU1wRwIYOHeO98IQahh8uO6E269rc/AjZsQK6GDwPSKTu006w"

        encrypted_message = CipherEngine.EncryptMessage(message, key)

        self.assertEqual(encrypted_message, expected_encrypted_message)

     #  Test #3: Evalua si el mensaje se encriptó
    def test_correct_encryption3(self):
        message = "Los computadores no hacen lo que uno quiere, sino lo que uno les dice"
        key = "VerdadDolorosa1"

        expected_encrypted_message = "yLtQNG58ot+DT6jST7ko0OQO0X7p4LZyk/uupu6tnIpn9RNlzfukAQ6ne7qcPTH89ov28aBf0xXYpQ5uGoB7kvAB0rwOCBtxA0Pj8MHW1Qpd9A1eN3cHVGuiTPn+Mib32deocNCNv3XOwJkWZrU8sg"

        encrypted_message = CipherEngine.EncryptMessage(message, key)

        self.assertEqual(encrypted_message, expected_encrypted_message)

    #   - TEST CASOS DE PRUEBA EXCEPCIONALES -
     #  Test #4: Prueba de mensaje con caracteres especiales:
    def test_special_characters_message(self):
        message = "¡H0l@ Mundo$!"
        key = "abcdefghij"

        expected_encrypted_message = "8L9kUjZDKBCOsA/ELD7q0WJDocmelECECcm+qQOEb1ThM7FQyP22nP5+bEKvRW4v"

        encrypted_message = CipherEngine.EncryptMessage(message, key)

        self.assertEqual(encrypted_message, expected_encrypted_message)
    
     #  Test #5: Prueba de mensaje con caracteres repetidos:
    def test_upper_message(self):
        message = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        key = "Repeticion1010"

        expected_encrypted_message = "hqCio76k4VmwQoesOLvZMoagoqO+pOFZsEKHrDi72TKkJdrJIHoa1lYUTfZpK37q1lkmQ9iGBnv7ZCEU4lNoS66ECznFbFEmlg1OkSLx2gI"

        encrypted_message = CipherEngine.EncryptMessage(message, key)

        self.assertEqual(encrypted_message, expected_encrypted_message)

     #  Test #6: Prueba con números como mensaje:
    def test_number_message(self):
        message = "3.14159265359"
        key = "PiTresPuntoCatorce"

        expected_encrypted_message = "40vgakMhWpYSV+3yZTJ1R2d0SfT5joIhKntolZWG0iTPffoDZKX139JytPjqXuXX"

        encrypted_message = CipherEngine.EncryptMessage(message, key)

        self.assertEqual(encrypted_message, expected_encrypted_message)


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

        expected_og_message = "Hola que hace"

        decrypted_message = CipherEngine.DecryptMessage(encrypted_message, key)

        self.assertEqual(decrypted_message, expected_og_message)

     #  Test #12: Evalua si el mensaje encriptado se desencriptó
    def test_correct_decryption2(self):
        encrypted_message = "yLtQNG58ot+DT6jST7ko0OQO0X7p4LZyk/uupu6tnIpn9RNlzfukAQ6ne7qcPTH89ov28aBf0xXYpQ5uGoB7kvAB0rwOCBtxA0Pj8MHW1Qpd9A1eN3cHVGuiTPn+Mib32deocNCNv3XOwJkWZrU8sg"
        key = "VerdadDolorosa1"

        expected_og_message = "Los computadores no hacen lo que uno quiere, sino lo que uno les dice"

        decrypted_message = CipherEngine.DecryptMessage(encrypted_message, key)

        self.assertEqual(decrypted_message, expected_og_message)
    
     #  Test #13: Evalua si el mensaje encriptado se desencriptó
    def test_correct_decryption3(self):
        encrypted_message = "Sm7I2OCYaND0qMfUWbWysk4RUhGS6xpGBkP2XSAi8xQ+tAsVEzdG4w3QfxRMImpGoLBLCq+v9ZPB3n8VyW8e9jmlwecY2nWn6Pqc7eZHqA93rYhS6idGFrW1PoaU1wRwIYOHeO98IQahh8uO6E269rc/AjZsQK6GDwPSKTu006w"
        key = "mitocondria"

        expected_og_message = "Orgánulo de las células eucariontes en el que tiene lugar la respiración celular."

        decrypted_message = CipherEngine.DecryptMessage(encrypted_message, key)

        self.assertEqual(decrypted_message, expected_og_message)

    #   - TEST CASOS DE PRUEBA EXCEPCIONALES -
     #  Test #14: Prueba de llave con caracteres especiales
    def test_special_characters_key(self):
        encrypted_message = "WPRjS7GVyaipziC6eRt3sSlYkBAw1GVqcxiVbRDSgAQEMV8ev4GqmV34vZjpT0wt"
        key = "(0nTr4$eña.13"

        expected_og_message = "excepcional"

        decrypted_message = CipherEngine.DecryptMessage(encrypted_message, key)

        self.assertEqual(decrypted_message, expected_og_message)

     #  Test #15: Prueba donde la llave tiene espacios:
    def test_blank_key(self):
        encrypted_message = "B+eo6fXMfJVMvihvl+Dl82oVGNlaqSHGF1FBHVhBPsTdIHtVJsKUmFG6xWg6JG4dR8X78QX0v+4haIt0uW6Tkw"
        key = "deberia estudiar más"

        expected_og_message = "La respuesta es la B"

        decrypted_message = CipherEngine.DecryptMessage(encrypted_message, key)

        self.assertEqual(decrypted_message, expected_og_message)

     #  Test #16: Prueba de llave con mismo caracter
    def test_same_characters_key(self):
        encrypted_message = "VEYjL2aBVRHXLGZxIvZsQcY1aaAd+DtrprxywJyeXf09Xh65q2cRkFIk0rQmauzRUBN18AP9jWzKAwdlB3yrEw"
        key = "rrrrrrrrrrrrrrrrrrr"

        expected_og_message = "Carácter repetido"

        decrypted_message = CipherEngine.DecryptMessage(encrypted_message, key)

        self.assertEqual(decrypted_message, expected_og_message)

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