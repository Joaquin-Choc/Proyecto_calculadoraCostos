from utils.helpers import Helpers

class CalculadoraTIR:
    def __init__(self):
        self.helpers = Helpers()
    
    def ejecutar(self):
        print("\n--- TASA INTERNA DE RETORNO (TIR) ---")
        print("Calcula la tasa de descuento que hace el VNA igual a cero")
        
        try:
            inversion_inicial = float(input("Inversión inicial ($): "))
            num_flujos = int(input("Número de periodos de flujos de caja: "))
            
            flujos = []
            for i in range(num_flujos):
                flujo = float(input(f"Flujo de caja periodo {i+1} ($): "))
                flujos.append(flujo)
            
            tir = self.helpers.calcular_tir_metodo(inversion_inicial, flujos)
            
            print("\n" + "="*70)
            print("RESULTADOS - TASA INTERNA DE RETORNO (TIR)")
            print("="*70)
            print(f"Inversión inicial: ${inversion_inicial:,.2f}")
            print(f"Número de periodos: {num_flujos}")
            
            print(f"\n--- FLUJOS DE CAJA ---")
            print(f"{'Periodo':<10} {'Flujo':<15}")
            print("-"*25)
            print(f"{0:<10} ${-inversion_inicial:,.2f}")
            for i, flujo in enumerate(flujos, 1):
                print(f"{i:<10} ${flujo:,.2f}")
            
            print("="*25)
            
            if tir == float('inf'):
                print("TIR: INFINITA (proyecto extremadamente rentable)")
                print("Los flujos son tan grandes que no existe una tasa que haga VNA=0")
            elif tir == -1:
                print("TIR: NO EXISTE (proyecto no viable)")
                print("No existe una tasa real que haga VNA=0")
            else:
                print(f"TASA INTERNA DE RETORNO (TIR): {tir*100:.2f}%")
                
                print(f"\n--- ANÁLISIS DE VIABILIDAD ---")
                tasa_minima = float(input("Ingrese la tasa mínima aceptable (costo de capital) (%): ")) / 100
                
                vna_tasa_minima = self.helpers.calcular_van(inversion_inicial, flujos, tasa_minima)
                
                print(f"\nTasa mínima aceptable: {tasa_minima*100:.2f}%")
                print(f"VNA a tasa mínima: ${vna_tasa_minima:,.2f}")
                
                if tir > tasa_minima:
                    print("✅ PROYECTO VIABLE - TIR > Tasa mínima")
                    print(f"Margen de seguridad: {(tir - tasa_minima)*100:.2f}%")
                elif tir == tasa_minima:
                    print("⚖️  PROYECTO NEUTRO - TIR = Tasa mínima")
                else:
                    print("❌ PROYECTO NO VIABLE - TIR < Tasa mínima")
                    print(f"Déficit: {(tasa_minima - tir)*100:.2f}%")
                
                print(f"\n--- SENSIBILIDAD ---")
                print("VNA a diferentes tasas de descuento:")
                print(f"{'Tasa':<10} {'VNA':<15}")
                print("-"*25)
                
                for tasa_test in [tasa_minima/2, tasa_minima, tir, tasa_minima*1.5, tasa_minima*2]:
                    if tasa_test >= 0:
                        vna_test = self.helpers.calcular_van(inversion_inicial, flujos, tasa_test)
                        print(f"{tasa_test*100:<9.1f}% ${vna_test:<14.2f}")
            
            print("="*70)
            
            return tir
            
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")