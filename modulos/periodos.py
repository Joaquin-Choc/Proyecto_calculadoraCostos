import math
from datetime import datetime, timedelta
from utils.helpers import Helpers

class CalculoPeriodos:
    def __init__(self):
        self.helpers = Helpers()
    
    def ejecutar(self):
        print("\n--- CÁLCULO DEL NÚMERO DE PERIODOS ---")
        print("Calcula el tiempo necesario para que una inversión alcance un monto objetivo")
        
        try:
            capital_inicial = float(input("Capital inicial ($): "))
            monto_objetivo = float(input("Monto objetivo ($): "))
            tasa_anual = float(input("Tasa de interés anual (%): ")) / 100
            
            opcion = self.helpers.obtener_capitalizacion()
            frecuencia = self.helpers.frecuencias[opcion]
            tipo_cap = self.helpers.tipos_capitalizacion[opcion]
            
            if capital_inicial <= 0:
                print("Error: El capital inicial debe ser mayor a 0")
                return
            
            if monto_objetivo <= capital_inicial:
                print("Error: El monto objetivo debe ser mayor al capital inicial")
                return
            
            tasa_periodica = tasa_anual / frecuencia
            periodos_compuesto = math.log(monto_objetivo / capital_inicial) / math.log(1 + tasa_periodica)
            años_compuesto = periodos_compuesto / frecuencia
            
            if tasa_anual > 0:
                años_simple = (monto_objetivo - capital_inicial) / (capital_inicial * tasa_anual)
                periodos_simple = años_simple * frecuencia
            else:
                años_simple = float('inf')
                periodos_simple = float('inf')
            
            print("\n" + "="*70)
            print("RESULTADOS - NÚMERO DE PERIODOS")
            print("="*70)
            print(f"Capital inicial: ${capital_inicial:,.2f}")
            print(f"Monto objetivo: ${monto_objetivo:,.2f}")
            print(f"Tasa anual: {tasa_anual*100:.2f}%")
            print(f"Capitalización: {tipo_cap}")
            print(f"Tasa periódica: {tasa_periodica*100:.6f}%")
            
            print("\n--- INTERÉS COMPUESTO ---")
            print(f"Periodos necesarios: {periodos_compuesto:.2f}")
            print(f"Tiempo necesario: {años_compuesto:.2f} años")
            
            if años_simple != float('inf'):
                print("\n--- INTERÉS SIMPLE ---")
                print(f"Periodos necesarios: {periodos_simple:.2f}")
                print(f"Tiempo necesario: {años_simple:.2f} años")
                
                diferencia_años = años_simple - años_compuesto
                if diferencia_años > 0:
                    print(f"\nEl interés compuesto es {diferencia_años:.2f} años más rápido")
                else:
                    print(f"\nEl interés simple es {-diferencia_años:.2f} años más rápido")
            else:
                print("\nCon interés simple, nunca se alcanzaría el monto objetivo")
            
            meses_compuesto = años_compuesto * 12
            dias_compuesto = años_compuesto * 360
            
            print("\n--- EQUIVALENCIAS DE TIEMPO ---")
            print(f"{años_compuesto:.2f} años = {meses_compuesto:.2f} meses = {dias_compuesto:.2f} días")
            
            fecha_actual = datetime.now()
            fecha_futura = fecha_actual + timedelta(days=dias_compuesto)
            print(f"Fecha aproximada para alcanzar el objetivo: {fecha_futura.strftime('%d/%m/%Y')}")
            
            print("="*70)
            
            return periodos_compuesto, años_compuesto
            
        except ValueError as e:
            print(f"Error: Ingrese valores numéricos válidos - {e}")
        except ZeroDivisionError:
            print("Error: La tasa de interés no puede ser 0% para este cálculo")
        except Exception as e:
            print(f"Error inesperado: {e}")