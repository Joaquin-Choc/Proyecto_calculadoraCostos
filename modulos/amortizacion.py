from utils.helpers import Helpers

class TablaAmortizacion:
    def __init__(self):
        self.helpers = Helpers()
    
    def ejecutar(self):
        print("\n--- TABLA DE AMORTIZACIÓN - INTERÉS COMPUESTO ---")
        
        try:
            capital = float(input("Capital inicial ($): "))
            tasa_anual = float(input("Tasa de interés anual (%): ")) / 100
            años = int(input("Número de años: "))
            opcion = self.helpers.obtener_capitalizacion()
            
            frecuencia = self.helpers.frecuencias[opcion]
            tasa_periodica = tasa_anual / frecuencia
            periodos_totales = años * frecuencia
            
            print(f"\nTABLA DE AMORTIZACIÓN - {self.helpers.tipos_capitalizacion[opcion].upper()}")
            print("="*80)
            print(f"{'Periodo':<10} {'Capital Inicial':<15} {'Interés':<15} {'Capital Final':<15}")
            print("-"*80)
            
            capital_actual = capital
            for periodo in range(1, periodos_totales + 1):
                interes_periodo = capital_actual * tasa_periodica
                capital_final = capital_actual + interes_periodo
                
                print(f"{periodo:<10} ${capital_actual:<14.2f} ${interes_periodo:<14.2f} ${capital_final:<14.2f}")
                
                capital_actual = capital_final
            
            print("="*80)
            interes_total = capital_actual - capital
            print(f"Capital final total: ${capital_actual:,.2f}")
            print(f"Interés total generado: ${interes_total:,.2f}")
            
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")