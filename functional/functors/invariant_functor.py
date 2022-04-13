
class InvariantFunctor:
    def __init__(self, decoder, encoder):
        self.decoder = decoder
        self.encoder = encoder

    def encode(self, value):
        pass

    def decode(self, value):
        pass

    def imap(self, decoder, encoder):
        pass


class Codec(InvariantFunctor):
    def encode(self, value):
        pass

    def decode(self, value):
        pass

    def imap(self, decoder, encoder):
        return InvariantFunctor(decoder(self.decoder), encoder(self.encoder))




"""
Resumen:
Functores (covariantes): si tenemos un functor F[B] y existe una funcion B->A entonces A son todos los 
supertipos de B. (en realidad, existe un mapeo, podria no ser un supertipo propiamente dicho).
Functores contravariantes: va a los subtipos
Functores invariantes: 

"""