
class EmptyMessageError( Exception ):
    pass

class EmptyKeyError( Exception ):
    pass

class KeyLengthError( Exception ):
    pass

class OneCharacterMessageError( Exception ):
    pass

class EmptyEncryptedMessageError( Exception ):
    pass

class EmptyEncryptionKeyError( Exception ):
    pass

class WrongKeyError( Exception ):
    pass

class CorruptEncryptedMessageError( Exception ):
    pass

#  Lógica detrás del motor de encripción
def EncryptMessage(message, key):

    pass

def DecryptMessage(encrypted_message, key):

    pass

