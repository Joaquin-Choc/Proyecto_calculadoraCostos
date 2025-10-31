from modulos.interes_simple import InteresSimple
from modulos.interes_compuesto import InteresCompuesto
from modulos.comparacion import ComparacionIntereses
from modulos.periodos import CalculoPeriodos
from modulos.tasa_interes import CalculoTasaInteres
from modulos.amortizacion import TablaAmortizacion
from modulos.bonos import CalculadoraBonos
from modulos.valor_presente import ValorPresente
from modulos.vna import CalculadoraVNA
from modulos.tir import CalculadoraTIR

class CalculadoraFinanciera:
    def __init__(self):
        self.modulos = {
            '1': InteresSimple(),
            '2': InteresCompuesto(),
            '3': ComparacionIntereses(),
            '4': CalculoPeriodos(),
            '5': CalculoTasaInteres(),
            '6': TablaAmortizacion(),
            '7': CalculadoraBonos(),
            '8': ValorPresente(),
            '9': CalculadoraVNA(),
            '10': CalculadoraTIR()
        }
    
    def mostrar_menu(self):
        print("\n" + "="*50)
        print("      CALCULADORA FINANCIERA COMPLETA")
        print("="*50)
        print("1. Interés Simple")
        print("2. Interés Compuesto")
        print("3. Comparar Simple vs Compuesto")
        print("4. Calcular Número de Periodos")
        print("5. Calcular Tasa de Interés")
        print("6. Tabla de Amortización")
        print("7. Cálculo de Bonos")
        print("8. Calcular Valor Presente")
        print("9. Calcular VNA (Valor Neto Actual)")
        print("10. Calcular TIR (Tasa Interna de Retorno)")
        print("11. Salir")
        print("="*50)
    
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            
            if opcion == "11":
                print("¡Gracias por usar la calculadora financiera!")
                break
            elif opcion in self.modulos:
                self.modulos[opcion].ejecutar()
            else:
                print("Opción no válida. Por favor, seleccione 1-11.")
            
            input("\nPresione Enter para continuar...")