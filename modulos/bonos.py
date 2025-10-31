from utils.helpers import Helpers

class CalculadoraBonos:
    def __init__(self):
        self.helpers = Helpers()
        self.tipos_bono = {
            '1': 'Bono Cupón Cero',
            '2': 'Bono Cupón Fijo',
            '3': 'Bono Amortizable',
            '4': 'Bono Perpetuo'
        }
    
    def mostrar_tipos_bono(self):
        print("\nTIPOS DE BONOS:")
        for key, value in self.tipos_bono.items():
            print(f"{key}. {value}")
    
    def ejecutar(self):
        print("\n--- CÁLCULO DE BONOS ---")
        self.mostrar_tipos_bono()
        
        try:
            opcion_bono = input("Seleccione el tipo de bono: ")
            
            if opcion_bono == '1':
                self.calcular_bono_cupon_cero()
            elif opcion_bono == '2':
                self.calcular_bono_cupon_fijo()
            elif opcion_bono == '3':
                self.calcular_bono_amortizable()
            elif opcion_bono == '4':
                self.calcular_bono_perpetuo()
            else:
                print("Opción no válida")
                
        except Exception as e:
            print(f"Error en el cálculo del bono: {e}")
    
    def calcular_bono_cupon_cero(self):
        print("\n--- BONO CUPÓN CERO ---")
        print("Bono que no paga intereses periódicos, se compra con descuento")
        
        try:
            valor_nominal = float(input("Valor nominal del bono ($): "))
            tasa_mercado = float(input("Tasa de mercado anual (%): ")) / 100
            tiempo = float(input("Tiempo hasta vencimiento (años): "))
            frecuencia = int(input("Frecuencia de capitalización (veces por año): "))
            
            periodos = frecuencia * tiempo
            tasa_periodica = tasa_mercado / frecuencia
            precio = valor_nominal / ((1 + tasa_periodica) ** periodos)
            descuento = valor_nominal - precio
            rendimiento = (valor_nominal / precio) ** (1/tiempo) - 1
            
            print("\n" + "="*60)
            print("RESULTADOS - BONO CUPÓN CERO")
            print("="*60)
            print(f"Valor nominal: ${valor_nominal:,.2f}")
            print(f"Tasa de mercado: {tasa_mercado*100:.2f}%")
            print(f"Tiempo hasta vencimiento: {tiempo:.2f} años")
            print(f"Frecuencia: {frecuencia} veces por año")
            print(f"Precio del bono: ${precio:,.2f}")
            print(f"Descuento: ${descuento:,.2f}")
            print(f"Rendimiento al vencimiento: {rendimiento*100:.2f}%")
            print(f"Descuento porcentual: {(descuento/valor_nominal)*100:.2f}%")
            print("="*60)
            
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")
    
    def calcular_bono_cupon_fijo(self):
        print("\n--- BONO CUPÓN FIJO ---")
        print("Bono que paga intereses periódicos fijos")
        
        try:
            valor_nominal = float(input("Valor nominal del bono ($): "))
            tasa_cupon = float(input("Tasa del cupón anual (%): ")) / 100
            tasa_mercado = float(input("Tasa de mercado anual (%): ")) / 100
            tiempo = float(input("Tiempo hasta vencimiento (años): "))
            frecuencia = int(input("Frecuencia de pagos por año: "))
            
            periodos = int(tiempo * frecuencia)
            tasa_periodica_mercado = tasa_mercado / frecuencia
            pago_cupon = (valor_nominal * tasa_cupon) / frecuencia
            
            precio = 0
            for t in range(1, periodos + 1):
                precio += pago_cupon / ((1 + tasa_periodica_mercado) ** t)
            
            precio += valor_nominal / ((1 + tasa_periodica_mercado) ** periodos)
            
            ingreso_anual = pago_cupon * frecuencia
            rendimiento_current = (ingreso_anual / precio) * 100
            prima_descuento = precio - valor_nominal
            
            print("\n" + "="*70)
            print("RESULTADOS - BONO CUPÓN FIJO")
            print("="*70)
            print(f"Valor nominal: ${valor_nominal:,.2f}")
            print(f"Tasa del cupón: {tasa_cupon*100:.2f}%")
            print(f"Tasa de mercado: {tasa_mercado*100:.2f}%")
            print(f"Tiempo hasta vencimiento: {tiempo:.2f} años")
            print(f"Frecuencia de pagos: {frecuencia} veces por año")
            print(f"Pago por cupón: ${pago_cupon:,.2f}")
            print(f"Precio del bono: ${precio:,.2f}")
            
            if prima_descuento > 0:
                print(f"Prima: ${prima_descuento:,.2f} ({prima_descuento/valor_nominal*100:.2f}%)")
            else:
                print(f"Descuento: ${-prima_descuento:,.2f} ({-prima_descuento/valor_nominal*100:.2f}%)")
            
            print(f"Rendimiento corriente: {rendimiento_current:.2f}%")
            print(f"Ingreso anual por cupones: ${ingreso_anual:,.2f}")
            
            print(f"\n--- PRIMEROS 5 PERIODOS ---")
            print(f"{'Periodo':<10} {'Flujo':<15} {'VP Flujo':<15}")
            print("-"*40)
            for t in range(1, min(6, periodos + 1)):
                if t == periodos:
                    flujo = pago_cupon + valor_nominal
                else:
                    flujo = pago_cupon
                vp_flujo = flujo / ((1 + tasa_periodica_mercado) ** t)
                print(f"{t:<10} ${flujo:<14.2f} ${vp_flujo:<14.2f}")
            
            print("="*70)
            
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")
    
    def calcular_bono_amortizable(self):
        print("\n--- BONO AMORTIZABLE ---")
        print("Bono que paga intereses y amortiza capital periódicamente")
        
        try:
            valor_nominal = float(input("Valor nominal del bono ($): "))
            tasa_cupon = float(input("Tasa del cupón anual (%): ")) / 100
            tasa_mercado = float(input("Tasa de mercado anual (%): ")) / 100
            tiempo = float(input("Plazo total (años): "))
            frecuencia = int(input("Frecuencia de pagos por año: "))
            
            periodos = int(tiempo * frecuencia)
            tasa_periodica_mercado = tasa_mercado / frecuencia
            amortizacion_periodo = valor_nominal / periodos
            
            saldo = valor_nominal
            precio = 0
            total_intereses = 0
            
            print(f"\nTABLA DE AMORTIZACIÓN DEL BONO")
            print("="*90)
            print(f"{'Periodo':<8} {'Saldo Inicial':<15} {'Interés':<15} {'Amortización':<15} {'Pago Total':<15} {'Saldo Final':<15}")
            print("-"*90)
            
            for t in range(1, periodos + 1):
                interes_periodo = saldo * tasa_cupon / frecuencia
                pago_total = interes_periodo + amortizacion_periodo
                saldo_final = saldo - amortizacion_periodo
                vp_flujo = pago_total / ((1 + tasa_periodica_mercado) ** t)
                precio += vp_flujo
                total_intereses += interes_periodo
                
                print(f"{t:<8} ${saldo:<14.2f} ${interes_periodo:<14.2f} ${amortizacion_periodo:<14.2f} ${pago_total:<14.2f} ${saldo_final:<14.2f}")
                
                saldo = saldo_final
            
            print("="*90)
            print(f"\nRESUMEN DEL BONO AMORTIZABLE")
            print(f"Precio teórico: ${precio:,.2f}")
            print(f"Total intereses pagados: ${total_intereses:,.2f}")
            print(f"Pago total (capital + intereses): ${valor_nominal + total_intereses:,.2f}")
            
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")
    
    def calcular_bono_perpetuo(self):
        print("\n--- BONO PERPETUO ---")
        print("Bono que paga intereses perpetuamente, sin fecha de vencimiento")
        
        try:
            valor_nominal = float(input("Valor nominal del bono ($): "))
            tasa_cupon = float(input("Tasa del cupón anual (%): ")) / 100
            tasa_mercado = float(input("Tasa de mercado anual (%): ")) / 100
            frecuencia = int(input("Frecuencia de pagos por año: "))
            
            pago_periodico = (valor_nominal * tasa_cupon) / frecuencia
            tasa_periodica_mercado = tasa_mercado / frecuencia
            precio = pago_periodico / tasa_periodica_mercado
            
            ingreso_anual = pago_periodico * frecuencia
            rendimiento = ingreso_anual / precio
            
            print("\n" + "="*60)
            print("RESULTADOS - BONO PERPETUO")
            print("="*60)
            print(f"Valor nominal: ${valor_nominal:,.2f}")
            print(f"Tasa del cupón: {tasa_cupon*100:.2f}%")
            print(f"Tasa de mercado: {tasa_mercado*100:.2f}%")
            print(f"Frecuencia de pagos: {frecuencia} veces por año")
            print(f"Pago periódico: ${pago_periodico:,.2f}")
            print(f"Precio del bono: ${precio:,.2f}")
            print(f"Rendimiento: {rendimiento*100:.2f}%")
            print(f"Ingreso anual: ${ingreso_anual:,.2f}")
            
            if precio > valor_nominal:
                print(f"PRIMA: ${precio - valor_nominal:,.2f}")
            else:
                print(f"DESCUENTO: ${valor_nominal - precio:,.2f}")
            print("="*60)
            
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")