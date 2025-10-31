from utils.helpers import Helpers

class ComparacionIntereses:
    def __init__(self):
        self.helpers = Helpers()
    
    def ejecutar(self):
        print("\n--- COMPARACIÓN INTERÉS SIMPLE vs COMPUESTO ---")
        capital, tasa_anual, tiempo = self.helpers.obtener_datos_comunes()
        
        if capital is None:
            return
        
        interes_simple = capital * tasa_anual * tiempo
        monto_simple = capital + interes_simple
        
        monto_compuesto = capital * (1 + tasa_anual) ** tiempo
        interes_compuesto = monto_compuesto - capital
        
        diferencia = monto_compuesto - monto_simple
        
        print("\n" + "="*60)
        print("COMPARACIÓN INTERÉS SIMPLE vs COMPUESTO")
        print("="*60)
        print(f"Capital inicial: ${capital:,.2f}")
        print(f"Tasa anual: {tasa_anual*100:.2f}%")
        print(f"Tiempo: {tiempo:.2f} años")
        print("\n--- INTERÉS SIMPLE ---")
        print(f"Interés generado: ${interes_simple:,.2f}")
        print(f"Monto final: ${monto_simple:,.2f}")
        print("\n--- INTERÉS COMPUESTO (Anual) ---")
        print(f"Interés generado: ${interes_compuesto:,.2f}")
        print(f"Monto final: ${monto_compuesto:,.2f}")
        print("\n--- DIFERENCIA ---")
        print(f"Diferencia a favor del compuesto: ${diferencia:,.2f}")
        print(f"Ventaja del compuesto: {(diferencia/monto_simple)*100:.2f}%")
        print("="*60)