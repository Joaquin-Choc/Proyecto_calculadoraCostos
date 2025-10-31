from utils.helpers import Helpers

class CalculoTasaInteres:
    def __init__(self):
        self.helpers = Helpers()
    
    def ejecutar(self):
        print("\n--- CÁLCULO DE LA TASA DE INTERÉS ---")
        print("Calcula la tasa de interés necesaria para alcanzar un monto objetivo en un tiempo determinado")
        
        try:
            capital_inicial = float(input("Capital inicial ($): "))
            monto_objetivo = float(input("Monto objetivo ($): "))
            tiempo = float(input("Tiempo: "))
            unidad_tiempo = input("Unidad de tiempo (años/meses/días): ").lower()
            
            if unidad_tiempo == "meses":
                tiempo = tiempo / 12
            elif unidad_tiempo == "días":
                tiempo = tiempo / 360
            
            opcion = self.helpers.obtener_capitalizacion()
            frecuencia = self.helpers.frecuencias[opcion]
            tipo_cap = self.helpers.tipos_capitalizacion[opcion]
            
            if capital_inicial <= 0:
                print("Error: El capital inicial debe ser mayor a 0")
                return
            
            if monto_objetivo <= capital_inicial:
                print("Error: El monto objetivo debe ser mayor al capital inicial")
                return
            
            if tiempo <= 0:
                print("Error: El tiempo debe ser mayor a 0")
                return
            
            periodos_totales = frecuencia * tiempo
            tasa_anual_compuesto = frecuencia * ((monto_objetivo / capital_inicial) ** (1 / periodos_totales) - 1)
            tasa_periodica_compuesto = tasa_anual_compuesto / frecuencia
            tasa_anual_simple = (monto_objetivo / capital_inicial - 1) / tiempo
            
            print("\n" + "="*70)
            print("RESULTADOS - TASA DE INTERÉS REQUERIDA")
            print("="*70)
            print(f"Capital inicial: ${capital_inicial:,.2f}")
            print(f"Monto objetivo: ${monto_objetivo:,.2f}")
            print(f"Tiempo: {tiempo:.2f} años")
            print(f"Capitalización: {tipo_cap}")
            print(f"Frecuencia: {frecuencia} veces por año")
            print(f"Periodos totales: {periodos_totales:.2f}")
            
            print("\n--- INTERÉS COMPUESTO ---")
            print(f"Tasa periódica requerida: {tasa_periodica_compuesto*100:.6f}%")
            print(f"Tasa anual efectiva requerida: {tasa_anual_compuesto*100:.4f}%")
            print(f"Tasa anual nominal requerida: {tasa_anual_compuesto*100:.4f}%")
            
            print("\n--- INTERÉS SIMPLE ---")
            print(f"Tasa anual requerida: {tasa_anual_simple*100:.4f}%")
            
            diferencia_tasa = tasa_anual_simple - tasa_anual_compuesto
            print(f"\n--- COMPARACIÓN ---")
            print(f"El interés compuesto requiere {diferencia_tasa*100:.4f}% menos de tasa anual")
            
            print(f"\n--- ANÁLISIS DE VIABILIDAD ---")
            if tasa_anual_compuesto <= 0.50:
                print("✅ Tasa requerida: RAZONABLE (≤ 50% anual)")
            elif tasa_anual_compuesto <= 1.00:
                print("⚠️  Tasa requerida: ALTA (50% - 100% anual)")
            else:
                print("❌ Tasa requerida: MUY ALTA (> 100% anual) - Puede no ser realista")
            
            print("="*70)
            
            return tasa_anual_compuesto, tasa_anual_simple
            
        except ValueError as e:
            print(f"Error: Ingrese valores numéricos válidos - {e}")
        except ZeroDivisionError:
            print("Error: El tiempo no puede ser 0")
        except Exception as e:
            print(f"Error inesperado: {e}")