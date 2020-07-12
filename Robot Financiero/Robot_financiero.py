import datetime
import pandas as pd
from numpy import nan



class Desembolso:
    def __init__(self,prestamo, fecha_inicio, monto, dia_corte, plazo, tipo_tasa, amortizacion, tasa_referencia = "", puntos = 0,):
        self.prestamo = prestamo
        self.fecha_inicio = fecha_inicio
        self.monto = monto
        self.dia_corte = dia_corte
        self.plazo = plazo
        self.tipo_tasa = tipo_tasa
        self.amortizacion = amortizacion
        self.tasa_referencia = tasa_referencia
        self.puntos = puntos
    
    def __str__(self):
        return "se ha creado el prestamo numero {} en la fecha {}".format(self.prestamo, self.fecha_inicio)
    
    def manejo_tasa(self):
        if self.tipo_tasa == "dinamica":
            path_file = "Tasas de Referencia.xlsx"
            hoja = "Tasas de Referencia"
            df = pd.read_excel(path_file,sheet_name=hoja)
            tasa_r = round(float((df[(df.EFFECTIVE_DATE == self.fecha_inicio) & (df.RATE_CODE == self.tasa_referencia)].INT_RATE)/100),5)
            tasa_spread = round(float(self.puntos/100),5)
            if self.tasa_referencia == "IBRTV":
                tasa_ea = round(((1+(tasa_r + tasa_spread)/4)**4)-1,5)
                return tasa_ea
    
    def calendario(self):
        pass


                
                 

#((1+(tasa_r + tasa_spread)/4)^4)-1       


ejemplo_1 = Desembolso("26730027633",datetime.datetime(2020,2,27), 32000000, 2, 72, "dinamica", "EMI", "IBRTV", 6.77)
print(ejemplo_1.manejo_tasa())

