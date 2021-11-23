# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:35:15 2021

@author: Radyck
"""

from desig import *
from funciones import *
class MainWindow(QtWidgets.QMainWindow, Ui_ventanaPrincipal):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        #self permutacion
        self.botonCalcularPermutacion.clicked.connect(self.metodoPermutacion)
        self.botonLimpiarPermutacion.clicked.connect(self.limpiarPer)
        #self factorial
        self.botonCalcularFactorial.clicked.connect(self.metodoFactorial)
        self.botonLimpiarFactorial.clicked.connect(self.limpiarFac)
        #self combinacion
        self.botonCalcularCombinacion.clicked.connect(self.metodoCombinacion)
        self.botonLimpiarCombinacion.clicked.connect(self.limpiarComb)
        #self union
        self.botonCalcularUnion.clicked.connect(self.metodoUnion)
        self.botonLimpiarUnion.clicked.connect(self.limpiarUni)
        #self interseccion
        self.botonCalcularInterseccion.clicked.connect(self.metodoInterseccion)
        self.botonLimpiarInterseccion.clicked.connect(self.limpiarInt)
        #self diferencia
        self.botonCalcularDiferencia.clicked.connect(self.metodoDiferencia)
        self.botonLimpiarDiferencia.clicked.connect(self.limpiarDif)
        #self potencia
        self.botonCalcularPotencia.clicked.connect(self.metodoPotencia)
        self.botonLimpiarPotencia.clicked.connect(self.limpiarPot)
        #self binominal
        self.calcularBinominal.clicked.connect(self.metodoBinominal)
        self.botonLimpiarBinominal.clicked.connect(self.limpiarBin)
        #self geometrica
        self.botonCalcularGeometrica.clicked.connect(self.metodoGeometrica)
        self.botonLimpiarGeometrica.clicked.connect(self.limpiarGeo)
        #self poisson
        self.botonCalcularPoisson.clicked.connect(self.metodoPoisson)
        self.botonLimpiarPoisson.clicked.connect(self.limpiarPoi)
        
        
        
    def metodoPermutacion(self):
        entradaList = [self.dato1Perm.text(), self.dato2Perm.text(), self.dato3Perm.text()]
        entrada = list(entradaList)
        salidaStr = permutacion(entrada)
        salida = str(salidaStr)
        #print(salida)
        self.resultadoPermutacion.setText(salida)
        
    def limpiarPer(self):
        self.dato1Perm.clear(), self.dato2Perm.clear(), self.dato3Perm.clear(), self.dato4Perm.clear(), self.dato5Perm.clear()
        self.resultadoPermutacion.clear()
        
    def metodoFactorial(self):
        entradaInt = self.datoFact.text()
        entrada = int(entradaInt)
        salidaStr = factorial(entrada)
        salida = str(salidaStr)
        #print(salida)
        self.resultadoFactorial.setText(salida)
        
    def limpiarFac(self):
        self.datoFact.clear()
        self.resultadoFactorial.clear()
        
    def metodoCombinacion(self):
        entradaList = [self.dato1Comb.text(), self.dato2Comb.text(), self.dato3Comb.text(), self.dato4Comb.text(), self.dato5Comb.text()]
        entrada = list(entradaList)
        salidaStr = combinacion(entrada)
        salida = str(salidaStr)
        #print(salida)
        self.resultadoCombinacion.setText(salida)
        
    def limpiarComb(self):
        self.dato1Comb.clear(), self.dato2Comb.clear(), self.dato3Comb.clear(), self.dato4Comb.clear(), self.dato5Comb.clear()
        self.resultadoCombinacion.clear()
        
    def metodoUnion(self):
        entrada1List = [self.lista1Dato1Union.text(), self.lista1Dato2Union.text(), self.lista1Dato3Union.text(), self.lista1Dato4Union.text(), self.lista1Dato5Union.text()]
        entrada1 = list(entrada1List)
        entrada2List = [self.lista2Dato1Union.text(), self.lista2Dato2Union.text(), self.lista2Dato3Union.text(), self.lista2Dato4Union.text(), self.lista2Dato5Union.text()]
        entrada2 = list(entrada2List)
        salidaStr = union(entrada1List, entrada2List)
        salida = str(salidaStr)
        #print(salida)
        self.resultadoUnion.setText(salida)
        
    def limpiarUni(self):
        self.lista1Dato1Union.clear(), self.lista1Dato2Union.clear(), self.lista1Dato3Union.clear(), self.lista1Dato4Union.clear(), self.lista1Dato5Union.clear()
        self.lista2Dato1Union.clear(), self.lista2Dato2Union.clear(), self.lista2Dato3Union.clear(), self.lista2Dato4Union.clear(), self.lista2Dato5Union.clear()
        self.resultadoUnion.clear()
        
    def metodoInterseccion(self):
        entrada1List = [self.lista1Dato1Intersec.text(), self.lista1Dato2Intersec.text(), self.lista1Dato3Intersec.text(), self.lista1Dato4Intersec.text(), self.lista1Dato5Intersec.text()]
        entrada1 = list(entrada1List)
        entrada2List = [self.lista2Dato1Intersec.text(), self.lista2Dato2Intersec.text(), self.lista2Dato3Intersec.text(), self.lista2Dato4Intersec.text(), self.lista2Dato5Intersec.text()]
        entrada2 = list(entrada2List)
        salidaStr = interseccion(entrada1, entrada2)
        salida = str(salidaStr)
        self.resultadoInterseccion.setText(salida)
        
    def limpiarInt(self):
        self.lista1Dato1Intersec.clear(), self.lista1Dato2Intersec.clear(), self.lista1Dato3Intersec.clear(), self.lista1Dato4Intersec.clear(), self.lista1Dato5Intersec.clear()
        self.lista2Dato1Intersec.clear(), self.lista2Dato2Intersec.clear(), self.lista2Dato3Intersec.clear(), self.lista2Dato4Intersec.clear(), self.lista2Dato5Intersec.clear()
        self.resultadoInterseccion.clear()
        
    def metodoDiferencia(self):
        entrada1 = list([self.lista1Dato1Difer.text(), self.lista1Dato2Difer.text(), self.lista1Dato3Difer.text(), self.lista1Dato4Difer.text(), self.lista1Dato5Difer.text()])
        entrada2 = list([self.lista2Dato1Difer.text(), self.lista2Dato2Difer.text(), self.lista2Dato3Difer.text(), self.lista2Dato4Difer.text(), self.lista2Dato5Difer.text()])
        salida = str(diferencia(entrada1, entrada2))
        self.resultadoDiferencia.setText(salida)
        
    def limpiarDif(self):
        self.lista1Dato1Difer.clear(), self.lista1Dato2Difer.clear(), self.lista1Dato3Difer.clear(), self.lista1Dato4Difer.clear(), self.lista1Dato5Difer.clear()
        self.lista2Dato1Difer.clear(), self.lista2Dato2Difer.clear(), self.lista2Dato3Difer.clear(), self.lista2Dato4Difer.clear(), self.lista2Dato5Difer.clear()
        self.resultadoDiferencia.clear()
        
    def metodoPotencia(self):
        entrada1Int = int(self.dato1Potencia.text())
        entrada2Int = int(self.dato2Poteencia.text())
        salida = str(potencia(entrada1Int, entrada2Int))
        self.resultadoPotencia.setText(salida)
        
    def limpiarPot(self):
        self.dato1Potencia.clear(), self.dato2Poteencia.clear()
        self.resultadoPotencia.clear()
        
    def metodoBinominal(self):
        entradaN = int(self.nDatoBinominal.text())
        entradaX = int(self.rDatoBinominal.text())
        entradaP = float(self.pDatoBinominal.text())
        salida = str(binominal(entradaN, entradaX, entradaP))
        self.resultado2Binominal.setText(salida)
        self.resultado1Binominal.setText(salida) #Inicio del Diagrama
        self.proceso1n.setText((str(entradaN)).rjust(4," ")), self.proceso1x.setText(str(entradaX).rjust(4," "))
        self.proceso1p.setText((str(entradaP)).rjust(4," "))
        self.proceso2x.setText((str(entradaX)).rjust(4," "))
        self.proceso2p.setText(str(entradaP))
        self.proceso2n.setText((str(entradaN)).rjust(4," ")), self.proceso3x.setText((str(entradaX)).rjust(4," "))
        
        
    def limpiarBin(self):
        self.nDatoBinominal.clear(), self.rDatoBinominal.clear(), self.pDatoBinominal.clear()
        self.resultado1Binominal.clear(), self.resultado2Binominal.clear()
        self.proceso1n.clear(), self.proceso2n.clear()
        self.proceso1x.clear(), self.proceso2x.clear(), self.proceso3x.clear()
        self.proceso1p.clear(), self.proceso2p.clear()
        
    def metodoGeometrica(self):
        entradaX = int(self.datoXGeometrica.text())
        entradaP = float(self.datoPGeometrica.text())
        salida =str(geometrica(entradaX, entradaP))
        self.resultadoGeometrica.setText(salida)
        
    def limpiarGeo(self):
        self.datoXGeometrica.clear()
        self.datoPGeometrica.clear()
        self.resultadoGeometrica.clear()
        
    def metodoPoisson(self):
        entradaM = float(self.datoMPoisson.text())
        entradaN = int(self.datoNPoisson.text())
        salida = str(poisson(entradaM, entradaN))
        self.resultadoPoisson.setText(salida)
        
    def limpiarPoi(self):
        self.datoMPoisson.clear()
        self.datoNPoisson.clear()
        self.resultadoPoisson.clear()
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()