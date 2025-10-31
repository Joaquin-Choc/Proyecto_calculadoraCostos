from utils.helpers import Helpers

class InteresCompuesto:
    def __init__(self):
        self.helpers = Helpers()
    
    def ejecutar(self):
        print("\n--- INTERÉS COMPUESTO ---")
        capital, tasa_anual, tiempo = self.helpers.obtener_datos_comunes()
        
        if capital is None:
            return
        
        opcion = self.helpers.obtener_capitalizacion()
        frecuencia = self.helpers.frecuencias[opcion]
        tipo_cap = self.helpers.tipos_capitalizacion[opcion]
        
        tasa_periodica = tasa_anual / frecuencia
        periodos = frecuencia * tiempo
        
        monto_final = capital * (1 + tasa_periodica) ** periodos
        interes = monto_final - capital
        
        print("\n" + "="*50)
        print("RESULTADOS - INTERÉS COMPUESTO")
        print("="*50)
        print(f"Capital inicial: ${capital:,.2f}")
        print(f"Tasa anual: {tasa_anual*100:.2f}%")
        print(f"Tipo de capitalización: {tipo_cap}")
        print(f"Frecuencia: {frecuencia} veces por año")
        print(f"Tasa periódica: {tasa_periodica*100:.6f}%")
        print(f"Periodos totales: {periodos:.2f}")
        print(f"Interés generado: ${interes:,.2f}")
        print(f"Monto final: ${monto_final:,.2f}")
        print("="*50)
        
        return interes, monto_final