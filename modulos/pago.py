from utils.helpers import Helpers

class CalculadoraPago:
    def __init__(self):
        self.helpers = Helpers()
    
    def ejecutar(self):
        """Calcula el pago periódico de un préstamo (función PAGO)"""
        print("\n--- CÁLCULO DEL PAGO PERIÓDICO (PAGO) ---")
        print("Calcula el pago periódico para un préstamo basado en pagos constantes y tasa constante")
        
        try:
            # Solicitar datos según la función PAGO de Excel
            print("\nParámetros de la función PAGO:")
            tasa = float(input("Tasa de interés por periodo (%): ")) / 100
            nper = int(input("Número total de pagos (periodos): "))
            va = float(input("Valor actual (monto del préstamo) ($): "))
            
            # Preguntar por valor futuro (opcional)
            vf_input = input("Valor futuro (opcional, presione Enter para 0): ")
            vf = float(vf_input) if vf_input else 0
            
            # Preguntar por tipo (opcional)
            tipo_input = input("Tipo (0 = fin de periodo, 1 = inicio de periodo, Enter para 0): ")
            tipo = int(tipo_input) if tipo_input else 0
            
            if tipo not in [0, 1]:
                print("Tipo no válido. Usando 0 (fin de periodo).")
                tipo = 0
            
            # Validar datos
            if tasa < 0:
                print("Error: La tasa no puede ser negativa")
                return
            
            if nper <= 0:
                print("Error: El número de periodos debe ser mayor a 0")
                return
            
            if va <= 0:
                print("Error: El valor actual debe ser mayor a 0")
                return
            
            # Calcular pago
            pago = self.calcular_pago(tasa, nper, va, vf, tipo)
            
            # Calcular total a pagar e intereses totales
            total_pagado = pago * nper
            intereses_totales = total_pagado - va + vf
            
            # Mostrar resultados
            print("\n" + "="*80)
            print("RESULTADOS - CÁLCULO DEL PAGO (PAGO)")
            print("="*80)
            print(f"Tasa por periodo: {tasa*100:.4f}%")
            print(f"Número de periodos: {nper}")
            print(f"Valor actual (préstamo): ${va:,.2f}")
            print(f"Valor futuro: ${vf:,.2f}")
            print(f"Tipo de pago: {'Inicio de periodo' if tipo == 1 else 'Fin de periodo'}")
            
            print(f"\n--- RESULTADOS PRINCIPALES ---")
            print(f"Pago periódico: ${pago:,.2f}")
            print(f"Total a pagar: ${total_pagado:,.2f}")
            print(f"Intereses totales: ${intereses_totales:,.2f}")
            print(f"Porcentaje de intereses: {(intereses_totales/va)*100:.2f}%")
            
            # Mostrar tabla de amortización simplificada
            self.mostrar_tabla_amortizacion(va, tasa, nper, pago, tipo)
            
            print("="*80)
            
            return pago
            
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")
        except ZeroDivisionError:
            print("Error: No se puede calcular con los parámetros proporcionados")
        except Exception as e:
            print(f"Error en el cálculo: {e}")
    
    def calcular_pago(self, tasa, nper, va, vf=0, tipo=0):
        """Calcula el pago periódico usando la fórmula de anualidades"""
        if tasa == 0:
            # Si tasa es 0, pago simple
            return (va - vf) / nper
        else:
            if tipo == 0:
                # Pago al final del periodo
                factor = (1 + tasa) ** nper
                pago = (va * tasa * factor) / (factor - 1) - (vf * tasa) / (factor - 1)
            else:
                # Pago al inicio del periodo
                factor = (1 + tasa) ** nper
                pago = (va * tasa * factor) / ((factor - 1) * (1 + tasa)) - (vf * tasa) / ((factor - 1) * (1 + tasa))
            
            return pago
    
    def mostrar_tabla_amortizacion(self, va, tasa, nper, pago, tipo):
        """Muestra una tabla de amortización simplificada"""
        print(f"\n--- TABLA DE AMORTIZACIÓN (PRIMEROS 5 PERIODOS) ---")
        print(f"{'Periodo':<8} {'Saldo Inicial':<15} {'Pago':<15} {'Interés':<15} {'Capital':<15} {'Saldo Final':<15}")
        print("-"*78)
        
        saldo = va
        periodos_a_mostrar = min(5, nper)
        
        for periodo in range(1, periodos_a_mostrar + 1):
            if tipo == 1 and periodo == 1:
                # Para pagos al inicio, el primer pago se aplica inmediatamente
                interes_periodo = 0
                capital_periodo = pago
                saldo_final = saldo - capital_periodo
            else:
                interes_periodo = saldo * tasa
                capital_periodo = pago - interes_periodo
                saldo_final = saldo - capital_periodo
            
            # Ajustar para evitar saldo negativo
            if saldo_final < 0:
                capital_periodo = saldo + interes_periodo
                pago_ajustado = capital_periodo
                saldo_final = 0
            else:
                pago_ajustado = pago
            
            print(f"{periodo:<8} ${saldo:<14.2f} ${pago_ajustado:<14.2f} ${interes_periodo:<14.2f} ${capital_periodo:<14.2f} ${saldo_final:<14.2f}")
            
            saldo = saldo_final
        
        # Mostrar información del último periodo si hay más de 5 periodos
        if nper > 5:
            print(f"...{'':<6} {'...':<14} {'...':<14} {'...':<14} {'...':<14} {'...':<14}")
            
            # Calcular último periodo
            saldo = va
            for periodo in range(1, nper):
                if tipo == 1 and periodo == 1:
                    capital_periodo = pago
                    saldo_final = saldo - capital_periodo
                else:
                    interes_periodo = saldo * tasa
                    capital_periodo = pago - interes_periodo
                    saldo_final = saldo - capital_periodo
                saldo = saldo_final
            
            # Último periodo
            interes_periodo = saldo * tasa
            capital_periodo = saldo
            pago_ajustado = interes_periodo + capital_periodo
            saldo_final = 0
            
            print(f"{nper:<8} ${saldo:<14.2f} ${pago_ajustado:<14.2f} ${interes_periodo:<14.2f} ${capital_periodo:<14.2f} ${saldo_final:<14.2f}")
    
    def calcular_plazo_alternativo(self, va, pago_maximo, tasa):
        """Calcula el plazo alternativo dado un pago máximo"""
        if tasa == 0:
            return va / pago_maximo
        else:
            # Fórmula: n = log(1 - (va * i) / pago) / log(1 + i)
            try:
                from math import log
                nper = log(1 - (va * tasa) / pago_maximo) / log(1 + tasa)
                return abs(nper)
            except (ValueError, ZeroDivisionError):
                return float('inf')