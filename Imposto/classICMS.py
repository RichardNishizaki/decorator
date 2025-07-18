from Imposto import Impostos

class ICMS(Impostos.Impostos):
    def __init__(self, outroImposto):
        self.outroImposto = outroImposto

    def calcula_imposto(self, orcamento):
        return orcamento.valor * 0.18 + self.CalculoDoOutroImposto(orcamento)
    
    def CalculoDoOutroImposto(self, orcamen):
        if self.outroImposto == None:
            return 0
        return self.outroImposto.calcula_imposto(orcamen)
