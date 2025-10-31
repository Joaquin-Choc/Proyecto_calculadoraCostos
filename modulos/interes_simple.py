from utils.helpers import Helpers

class InteresSimple:
    def __init__(self):
        self.helpers = Helpers()
    
    def ejecutar(self):
        print("\n--- INTERÉS SIMPLE ---")
        capital, tasa_anual, tiempo = self.helpers.obtener_datos_comunes()
        
        if capital is None:
            return
        
        interes = capital * tasa_anual * tiempo
        monto_final = capital + interes
        
        print("\n" + "="*40)
        print("RESULTADOS - INTERÉS SIMPLE")
        print("="*40)
        print(f"Capital inicial: ${capital:,.2f}")
        print(f"Tasa anual: {tasa_anual*100:.2f}%")
        print(f"Tiempo: {tiempo:.2f} años")
        print(f"Interés generado: ${interes:,.2f}")
        print(f"Monto final: ${monto_final:,.2f}")
        print("="*40)
        
        return interes, monto_final