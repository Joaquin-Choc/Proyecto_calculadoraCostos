from utils.helpers import Helpers

class CalculadoraVNA:
    def __init__(self):
        self.helpers = Helpers()
    
    def ejecutar(self):
        print("\n--- VALOR NETO ACTUAL (VNA) ---")
        print("Calcula el valor presente neto de una serie de flujos de caja")
        
        try:
            inversion_inicial = float(input("Inversión inicial ($): "))
            num_flujos = int(input("Número de periodos de flujos de caja: "))
            tasa_descuento = float(input("Tasa de descuento anual (%): ")) / 100
            
            flujos = []
            for i in range(num_flujos):
                flujo = float(input(f"Flujo de caja periodo {i+1} ($): "))
                flujos.append(flujo)
            
            vna = self.helpers.calcular_van(inversion_inicial, flujos, tasa_descuento)
            periodo_recuperacion = self.helpers.calcular_periodo_recuperacion(inversion_inicial, flujos)
            
            print("\n" + "="*80)
            print("RESULTADOS - VALOR NETO ACTUAL (VNA)")
            print("="*80)
            print(f"Inversión inicial: ${inversion_inicial:,.2f}")
            print(f"Tasa de descuento: {tasa_descuento*100:.2f}%")
            print(f"Número de periodos: {num_flujos}")
            
            print(f"\n--- FLUJOS DE CAJA ---")
            print(f"{'Periodo':<10} {'Flujo':<15} {'Valor Presente':<15}")
            print("-"*45)
            
            for i, flujo in enumerate(flujos, 1):
                vp_flujo = flujo / ((1 + tasa_descuento) ** i)
                print(f"{i:<10} ${flujo:<14.2f} ${vp_flujo:<14.2f}")
            
            print("="*45)
            print(f"VALOR NETO ACTUAL (VNA): ${vna:,.2f}")
            
            print(f"\n--- ANÁLISIS DE VIABILIDAD ---")
            if vna > 0:
                print("✅ PROYECTO VIABLE - VNA positivo")
                print(f"El proyecto genera un valor adicional de ${vna:,.2f}")
            elif vna == 0:
                print("⚖️  PROYECTO NEUTRO - VNA cero")
                print("El proyecto recupera exactamente la inversión con la tasa de descuento")
            else:
                print("❌ PROYECTO NO VIABLE - VNA negativo")
                print(f"El proyecto destruye valor por ${-vna:,.2f}")
            
            print(f"\n--- PERIODO DE RECUPERACIÓN ---")
            if periodo_recuperacion != float('inf'):
                print(f"Periodo de recuperación: {periodo_recuperacion:.2f} años")
                if periodo_recuperacion <= num_flujos:
                    print("✅ La inversión se recupera dentro del horizonte del proyecto")
                else:
                    print("⚠️  La inversión NO se recupera dentro del horizonte del proyecto")
            else:
                print("❌ La inversión NO se recupera con los flujos proyectados")
            
            print(f"\n--- FLUJOS ACUMULADOS ---")
            acumulado = -inversion_inicial
            print(f"{'Periodo':<10} {'Flujo':<15} {'Acumulado':<15}")
            print("-"*45)
            print(f"{0:<10} ${-inversion_inicial:<14.2f} ${acumulado:<14.2f}")
            
            for i, flujo in enumerate(flujos, 1):
                acumulado += flujo
                print(f"{i:<10} ${flujo:<14.2f} ${acumulado:<14.2f}")
            
            print("="*80)
            
            return vna
            
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")