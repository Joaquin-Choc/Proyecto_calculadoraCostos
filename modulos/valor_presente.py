from utils.helpers import Helpers

class ValorPresente:
    def __init__(self):
        self.helpers = Helpers()
    
    def ejecutar(self):
        print("\n--- CÁLCULO DEL VALOR PRESENTE ---")
        print("Calcula el valor actual de un monto futuro descontado a una tasa específica")
        
        try:
            valor_futuro = float(input("Valor futuro ($): "))
            tasa_descuento = float(input("Tasa de descuento anual (%): ")) / 100
            tiempo = float(input("Tiempo hasta el flujo: "))
            unidad_tiempo = input("Unidad de tiempo (años/meses/días): ").lower()
            
            if unidad_tiempo == "meses":
                tiempo = tiempo / 12
            elif unidad_tiempo == "días":
                tiempo = tiempo / 360
            
            print("\n¿Desea usar capitalización simple o compuesta?")
            print("1. Capitalización Simple")
            print("2. Capitalización Compuesta")
            tipo_interes = input("Seleccione (1/2): ")
            
            if tipo_interes == "1":
                valor_presente = valor_futuro / (1 + tasa_descuento * tiempo)
                formula_usada = "VP = VF / (1 + i * n)"
            else:
                valor_presente = valor_futuro / ((1 + tasa_descuento) ** tiempo)
                formula_usada = "VP = VF / (1 + i)^n"
            
            descuento_total = valor_futuro - valor_presente
            tasa_descuento_efectiva = (descuento_total / valor_presente) / tiempo * 100
            
            print("\n" + "="*60)
            print("RESULTADOS - VALOR PRESENTE")
            print("="*60)
            print(f"Valor futuro: ${valor_futuro:,.2f}")
            print(f"Tasa de descuento: {tasa_descuento*100:.2f}% anual")
            print(f"Tiempo: {tiempo:.2f} años")
            print(f"Tipo de interés: {'Simple' if tipo_interes == '1' else 'Compuesto'}")
            print(f"Fórmula utilizada: {formula_usada}")
            print(f"Valor presente: ${valor_presente:,.2f}")
            print(f"Descuento total: ${descuento_total:,.2f}")
            print(f"Tasa de descuento efectiva: {tasa_descuento_efectiva:.2f}%")
            print(f"Relación VP/VF: {(valor_presente/valor_futuro)*100:.2f}%")
            print("="*60)
            
            return valor_presente
            
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")
        except ZeroDivisionError:
            print("Error: El tiempo no puede ser 0")