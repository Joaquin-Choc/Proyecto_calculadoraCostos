from datetime import datetime, timedelta
import math

class Helpers:
    def __init__(self):
        self.tipos_capitalizacion = {
            '1': 'Anual',
            '2': 'Semestral',
            '3': 'Cuatrimestral',
            '4': 'Trimestral',
            '5': 'Bimestral',
            '6': 'Mensual',
            '7': 'Quincenal',
            '8': 'Diaria'
        }
        
        self.frecuencias = {
            '1': 1,    # Anual
            '2': 2,    # Semestral
            '3': 3,    # Cuatrimestral
            '4': 4,    # Trimestral
            '5': 6,    # Bimestral
            '6': 12,   # Mensual
            '7': 24,   # Quincenal
            '8': 360   # Diaria (convención comercial)
        }
    
    def mostrar_capitalizaciones(self):
        print("\nTIPOS DE CAPITALIZACIÓN:")
        for key, value in self.tipos_capitalizacion.items():
            print(f"{key}. {value}")
    
    def obtener_capitalizacion(self):
        self.mostrar_capitalizaciones()
        opcion = input("Seleccione el tipo de capitalización: ")
        
        if opcion not in self.frecuencias:
            print("Opción no válida. Usando capitalización anual por defecto.")
            opcion = '1'
        
        return opcion
    
    def obtener_datos_comunes(self):
        try:
            capital = float(input("Capital inicial ($): "))
            tasa_anual = float(input("Tasa de interés anual (%): ")) / 100
            tiempo = float(input("Tiempo: "))
            unidad_tiempo = input("Unidad de tiempo (años/meses/días): ").lower()
            
            if unidad_tiempo == "meses":
                tiempo = tiempo / 12
            elif unidad_tiempo == "días":
                tiempo = tiempo / 360
            
            return capital, tasa_anual, tiempo
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")
            return None, None, None
    
    def calcular_van(self, inversion_inicial, flujos, tasa_descuento):
        van = -inversion_inicial
        for i, flujo in enumerate(flujos, 1):
            van += flujo / ((1 + tasa_descuento) ** i)
        return van
    
    def calcular_tir_metodo(self, inversion_inicial, flujos, precision=0.0001, max_iter=1000):
        tasa_baja = 0.0
        tasa_alta = 1.0
        
        van_baja = self.calcular_van(inversion_inicial, flujos, tasa_baja)
        van_alta = self.calcular_van(inversion_inicial, flujos, tasa_alta)
        
        if van_baja * van_alta > 0:
            if van_baja > 0:
                return float('inf')
            else:
                return -1
        
        for _ in range(max_iter):
            tasa_media = (tasa_baja + tasa_alta) / 2
            van_media = self.calcular_van(inversion_inicial, flujos, tasa_media)
            
            if abs(van_media) < precision:
                return tasa_media
            
            if van_media > 0:
                tasa_baja = tasa_media
            else:
                tasa_alta = tasa_media
        
        return (tasa_baja + tasa_alta) / 2
    
    def calcular_periodo_recuperacion(self, inversion_inicial, flujos):
        acumulado = 0
        for i, flujo in enumerate(flujos, 1):
            acumulado += flujo
            if acumulado >= inversion_inicial:
                if i == 1:
                    return inversion_inicial / flujo
                else:
                    flujo_anterior = acumulado - flujo
                    return (i - 1) + (inversion_inicial - flujo_anterior) / flujo
        return float('inf')