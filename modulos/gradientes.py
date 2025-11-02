from utils.helpers import Helpers

class CalculadoraGradientes:
    def __init__(self):
        self.helpers = Helpers()
    
    def ejecutar(self):
        """Calcula el valor presente y futuro de series con gradiente aritmético y geométrico"""
        print("\n--- CÁLCULO DE GRADIENTES ---")
        print("Calcula el valor presente y futuro de series con crecimiento constante")
        
        try:
            print("\nSeleccione el tipo de gradiente:")
            print("1. Gradiente Aritmético (crecimiento lineal)")
            print("2. Gradiente Geométrico (crecimiento porcentual)")
            print("3. Comparar Ambos Tipos")
            tipo_gradiente = input("Seleccione (1/2/3): ")
            
            if tipo_gradiente == "1":
                return self.calcular_gradiente_aritmetico()
            elif tipo_gradiente == "2":
                return self.calcular_gradiente_geometrico()
            elif tipo_gradiente == "3":
                return self.comparar_gradientes()
            else:
                print("Opción no válida")
                return None, None
                
        except Exception as e:
            print(f"Error en el cálculo: {e}")
            return None, None
    
    def calcular_gradiente_aritmetico(self):
        """Calcula gradiente aritmético (crecimiento lineal)"""
        print("\n--- GRADIENTE ARITMÉTICO ---")
        print("Serie con crecimiento constante en cantidad fija por periodo")
        
        try:
            # Solicitar datos
            primer_pago = float(input("Primer pago o ingreso ($): "))
            gradiente = float(input("Gradiente (crecimiento por periodo) ($): "))
            n_periodos = int(input("Número de periodos: "))
            tasa = float(input("Tasa de interés por periodo (%): ")) / 100
            tipo_serie = input("¿La serie es anticipada? (s/n, Enter para no): ").lower()
            es_anticipada = tipo_serie == 's'
            
            # Validar datos
            if n_periodos <= 0:
                print("Error: El número de periodos debe ser mayor a 0")
                return None, None
            
            # Calcular flujos de caja
            flujos = []
            for i in range(n_periodos):
                if es_anticipada:
                    flujo = primer_pago + (i * gradiente)
                else:
                    flujo = primer_pago + ((i) * gradiente)  # Corregido: i en lugar de i+1
                flujos.append(flujo)
            
            # Calcular valor presente
            vp = 0
            for i, flujo in enumerate(flujos):
                if es_anticipada:
                    vp += flujo / ((1 + tasa) ** i)
                else:
                    vp += flujo / ((1 + tasa) ** (i + 1))
            
            # Calcular valor futuro
            vf = vp * ((1 + tasa) ** n_periodos)
            
            # Calcular usando fórmulas directas de gradiente aritmético
            # VP = A * (P/A,i,n) + G * (P/G,i,n)
            if tasa == 0:
                vp_formula = sum(flujos)
                vf_formula = vp_formula
            else:
                # Para serie uniforme
                factor_p_a = (1 - (1 + tasa) ** -n_periodos) / tasa
                # Para gradiente aritmético
                factor_p_g = (1 / (tasa ** 2)) * (1 - (1 + tasa) ** -n_periodos) - (n_periodos / (tasa * (1 + tasa) ** n_periodos))
                
                if es_anticipada:
                    vp_formula = primer_pago * factor_p_a * (1 + tasa) + gradiente * factor_p_g * (1 + tasa)
                else:
                    vp_formula = primer_pago * factor_p_a + gradiente * factor_p_g
                
                vf_formula = vp_formula * ((1 + tasa) ** n_periodos)
            
            # Mostrar resultados
            print("\n" + "="*80)
            print("RESULTADOS - GRADIENTE ARITMÉTICO")
            print("="*80)
            print(f"Primer pago: ${primer_pago:,.2f}")
            print(f"Gradiente: ${gradiente:,.2f} por periodo")
            print(f"Número de periodos: {n_periodos}")
            print(f"Tasa de interés: {tasa*100:.2f}% por periodo")
            print(f"Tipo de serie: {'Anticipada' if es_anticipada else 'Vencida'}")
            
            print(f"\n--- FLUJOS DE CAJA ---")
            print(f"{'Periodo':<8} {'Flujo':<15} {'Acumulado':<15}")
            print("-"*38)
            acumulado = 0
            for i, flujo in enumerate(flujos):
                periodo = i if es_anticipada else i + 1
                acumulado += flujo
                print(f"{periodo:<8} ${flujo:<14.2f} ${acumulado:<14.2f}")
            
            print(f"\n--- RESULTADOS ---")
            print(f"Valor Presente (VP): ${vp:,.2f}")
            print(f"Valor Futuro (VF): ${vf:,.2f}")
            print(f"Valor Presente (fórmula): ${vp_formula:,.2f}")
            print(f"Valor Futuro (fórmula): ${vf_formula:,.2f}")
            
            # Verificar diferencia entre métodos
            diferencia_vp = abs(vp - vp_formula)
            diferencia_vf = abs(vf - vf_formula)
            print(f"Diferencia en VP: ${diferencia_vp:.6f}")
            print(f"Diferencia en VF: ${diferencia_vf:.6f}")
            
            # Análisis adicional
            crecimiento_total = flujos[-1] - primer_pago
            print(f"\n--- ANÁLISIS ADICIONAL ---")
            print(f"Crecimiento total: ${crecimiento_total:,.2f}")
            print(f"Último pago: ${flujos[-1]:,.2f}")
            print(f"Promedio de pagos: ${sum(flujos)/len(flujos):,.2f}")
            print(f"Suma total de flujos: ${sum(flujos):,.2f}")
            
            # Análisis de crecimiento
            if primer_pago != 0:
                crecimiento_porcentual = ((flujos[-1] - primer_pago) / abs(primer_pago)) * 100
                print(f"Crecimiento porcentual total: {crecimiento_porcentual:.2f}%")
            
            print("="*80)
            
            return vp, vf
            
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")
            return None, None
        except Exception as e:
            print(f"Error en el cálculo: {e}")
            return None, None
    
    def calcular_gradiente_geometrico(self):
        """Calcula gradiente geométrico (crecimiento porcentual)"""
        print("\n--- GRADIENTE GEOMÉTRICO ---")
        print("Serie con crecimiento constante en porcentaje por periodo")
        
        try:
            # Solicitar datos
            primer_pago = float(input("Primer pago o ingreso ($): "))
            tasa_crecimiento = float(input("Tasa de crecimiento por periodo (%): ")) / 100
            n_periodos = int(input("Número de periodos: "))
            tasa_interes = float(input("Tasa de interés por periodo (%): ")) / 100
            tipo_serie = input("¿La serie es anticipada? (s/n, Enter para no): ").lower()
            es_anticipada = tipo_serie == 's'
            
            # Validar datos
            if n_periodos <= 0:
                print("Error: El número de periodos debe ser mayor a 0")
                return None, None
            
            # Calcular flujos de caja
            flujos = []
            for i in range(n_periodos):
                if es_anticipada:
                    flujo = primer_pago * ((1 + tasa_crecimiento) ** i)
                else:
                    flujo = primer_pago * ((1 + tasa_crecimiento) ** (i))
                flujos.append(flujo)
            
            # Calcular valor presente
            vp = 0
            for i, flujo in enumerate(flujos):
                if es_anticipada:
                    vp += flujo / ((1 + tasa_interes) ** i)
                else:
                    vp += flujo / ((1 + tasa_interes) ** (i + 1))
            
            # Calcular valor futuro
            vf = vp * ((1 + tasa_interes) ** n_periodos)
            
            # Calcular usando fórmula directa de gradiente geométrico
            if abs(tasa_interes - tasa_crecimiento) < 1e-10:  # Evitar comparación exacta con floats
                if es_anticipada:
                    vp_formula = primer_pago * n_periodos / (1 + tasa_interes)
                else:
                    vp_formula = primer_pago * n_periodos
            else:
                factor = (1 + tasa_crecimiento) / (1 + tasa_interes)
                if es_anticipada:
                    vp_formula = primer_pago * (1 - factor ** n_periodos) / (tasa_interes - tasa_crecimiento) * (1 + tasa_interes)
                else:
                    vp_formula = primer_pago * (1 - factor ** n_periodos) / (tasa_interes - tasa_crecimiento)
            
            vf_formula = vp_formula * ((1 + tasa_interes) ** n_periodos)
            
            # Mostrar resultados
            print("\n" + "="*80)
            print("RESULTADOS - GRADIENTE GEOMÉTRICO")
            print("="*80)
            print(f"Primer pago: ${primer_pago:,.2f}")
            print(f"Tasa de crecimiento: {tasa_crecimiento*100:.2f}% por periodo")
            print(f"Número de periodos: {n_periodos}")
            print(f"Tasa de interés: {tasa_interes*100:.2f}% por periodo")
            print(f"Tipo de serie: {'Anticipada' if es_anticipada else 'Vencida'}")
            
            print(f"\n--- FLUJOS DE CAJA ---")
            print(f"{'Periodo':<8} {'Flujo':<15} {'Crecimiento':<15} {'Acumulado':<15}")
            print("-"*53)
            acumulado = 0
            flujo_anterior = primer_pago
            for i, flujo in enumerate(flujos):
                periodo = i if es_anticipada else i + 1
                if i == 0:
                    crecimiento = 0
                else:
                    crecimiento = flujo - flujo_anterior
                acumulado += flujo
                print(f"{periodo:<8} ${flujo:<14.2f} ${crecimiento:<14.2f} ${acumulado:<14.2f}")
                flujo_anterior = flujo
            
            print(f"\n--- RESULTADOS ---")
            print(f"Valor Presente (VP): ${vp:,.2f}")
            print(f"Valor Futuro (VF): ${vf:,.2f}")
            print(f"Valor Presente (fórmula): ${vp_formula:,.2f}")
            print(f"Valor Futuro (fórmula): ${vf_formula:,.2f}")
            
            # Verificar diferencia entre métodos
            diferencia_vp = abs(vp - vp_formula)
            diferencia_vf = abs(vf - vf_formula)
            print(f"Diferencia en VP: ${diferencia_vp:.6f}")
            print(f"Diferencia en VF: ${diferencia_vf:.6f}")
            
            # Análisis adicional
            crecimiento_total = (flujos[-1] / primer_pago - 1) * 100
            print(f"\n--- ANÁLISIS ADICIONAL ---")
            print(f"Crecimiento total: {crecimiento_total:.2f}%")
            print(f"Último pago: ${flujos[-1]:,.2f}")
            print(f"Promedio de pagos: ${sum(flujos)/len(flujos):,.2f}")
            print(f"Tasa efectiva de crecimiento: {((flujos[-1]/primer_pago)**(1/n_periodos)-1)*100:.2f}% por periodo")
            
            # Comparación con crecimiento sin interés
            total_sin_interes = sum(flujos)
            print(f"Total sin intereses: ${total_sin_interes:,.2f}")
            print(f"Beneficio por intereses: ${vf - total_sin_interes:,.2f}")
            
            # Análisis de poder de crecimiento
            if tasa_crecimiento > tasa_interes:
                print("⚠️  La tasa de crecimiento supera la tasa de interés - crecimiento acelerado")
            elif tasa_crecimiento < tasa_interes:
                print("✅ La tasa de interés supera el crecimiento - buen rendimiento")
            else:
                print("⚖️  Tasas iguales - crecimiento neutral")
            
            print("="*80)
            
            return vp, vf
            
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")
            return None, None
        except ZeroDivisionError:
            print("Error: La tasa de interés no puede ser igual a la tasa de crecimiento para este cálculo")
            return None, None
        except Exception as e:
            print(f"Error en el cálculo: {e}")
            return None, None
    
    def comparar_gradientes(self):
        """Compara gradiente aritmético vs geométrico con los mismos parámetros base"""
        print("\n--- COMPARACIÓN DE GRADIENTES ---")
        print("Compara el comportamiento de gradiente aritmético vs geométrico")
        
        try:
            # Solicitar datos comunes
            primer_pago = float(input("Primer pago o ingreso ($): "))
            n_periodos = int(input("Número de periodos: "))
            tasa_interes = float(input("Tasa de interés por periodo (%): ")) / 100
            tipo_serie = input("¿La serie es anticipada? (s/n, Enter para no): ").lower()
            es_anticipada = tipo_serie == 's'
            
            # Para gradiente aritmético
            gradiente_aritmetico = float(input("Gradiente aritmético ($ por periodo): "))
            
            # Para gradiente geométrico - calcular tasa equivalente
            # Encontrar tasa geométrica que dé un crecimiento total similar
            crecimiento_total_aritmetico = gradiente_aritmetico * (n_periodos - 1)
            ultimo_pago_aritmetico = primer_pago + crecimiento_total_aritmetico
            
            # Calcular tasa geométrica equivalente
            if primer_pago > 0:
                tasa_geometrica_equivalente = (ultimo_pago_aritmetico / primer_pago) ** (1/(n_periodos-1)) - 1
            else:
                tasa_geometrica_equivalente = 0.05  # Valor por defecto 5%
            
            print(f"\nTasa geométrica equivalente calculada: {tasa_geometrica_equivalente*100:.2f}%")
            usar_calculada = input("¿Usar esta tasa? (s/n): ").lower()
            
            if usar_calculada != 's':
                tasa_geometrica_equivalente = float(input("Tasa de crecimiento geométrico (%): ")) / 100
            
            # Calcular ambos gradientes
            print("\n" + "="*90)
            print("COMPARACIÓN GRADIENTE ARITMÉTICO vs GEOMÉTRICO")
            print("="*90)
            
            # Gradiente aritmético
            vp_aritmetico, vf_aritmetico = self._calcular_gradiente_aritmetico_interno(
                primer_pago, gradiente_aritmetico, n_periodos, tasa_interes, es_anticipada)
            
            # Gradiente geométrico
            vp_geometrico, vf_geometrico = self._calcular_gradiente_geometrico_interno(
                primer_pago, tasa_geometrica_equivalente, n_periodos, tasa_interes, es_anticipada)
            
            # Mostrar comparación
            print(f"\n{'PARÁMETRO':<25} {'ARITMÉTICO':<20} {'GEOMÉTRICO':<20} {'DIFERENCIA':<20}")
            print("-"*85)
            
            print(f"{'Valor Presente (VP)':<25} ${vp_aritmetico:<19.2f} ${vp_geometrico:<19.2f} ${vp_geometrico - vp_aritmetico:<19.2f}")
            print(f"{'Valor Futuro (VF)':<25} ${vf_aritmetico:<19.2f} ${vf_geometrico:<19.2f} ${vf_geometrico - vf_aritmetico:<19.2f}")
            
            # Calcular últimos pagos
            ultimo_aritmetico = primer_pago + (gradiente_aritmetico * (n_periodos - 1))
            ultimo_geometrico = primer_pago * ((1 + tasa_geometrica_equivalente) ** (n_periodos - 1))
            
            print(f"{'Último Pago':<25} ${ultimo_aritmetico:<19.2f} ${ultimo_geometrico:<19.2f} ${ultimo_geometrico - ultimo_aritmetico:<19.2f}")
            
            # Totales sin interés
            total_aritmetico = (n_periodos / 2) * (2 * primer_pago + (n_periodos - 1) * gradiente_aritmetico)
            total_geometrico = primer_pago * (1 - (1 + tasa_geometrica_equivalente) ** n_periodos) / (1 - (1 + tasa_geometrica_equivalente))
            
            print(f"{'Total Flujos':<25} ${total_aritmetico:<19.2f} ${total_geometrico:<19.2f} ${total_geometrico - total_aritmetico:<19.2f}")
            
            # Análisis
            print(f"\n--- ANÁLISIS COMPARATIVO ---")
            if vf_geometrico > vf_aritmetico:
                diferencia = vf_geometrico - vf_aritmetico
                print(f"El gradiente GEOMÉTRICO genera ${diferencia:,.2f} más en valor futuro")
            else:
                diferencia = vf_aritmetico - vf_geometrico
                print(f"El gradiente ARITMÉTICO genera ${diferencia:,.2f} más en valor futuro")
            
            # Recomendación
            print(f"\n--- RECOMENDACIÓN ---")
            if tasa_geometrica_equivalente > tasa_interes:
                print("✅ Gradiente GEOMÉTRICO recomendado - crecimiento acelerado")
            elif gradiente_aritmetico > (primer_pago * tasa_interes):
                print("✅ Gradiente ARITMÉTICO recomendado - crecimiento constante sólido")
            else:
                print("⚖️  Ambos métodos son similares - considere otros factores")
            
            print("="*90)
            
            return (vp_aritmetico, vf_aritmetico), (vp_geometrico, vf_geometrico)
            
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")
            return None, None
        except Exception as e:
            print(f"Error en la comparación: {e}")
            return None, None
    
    def _calcular_gradiente_aritmetico_interno(self, primer_pago, gradiente, n_periodos, tasa, es_anticipada):
        """Cálculo interno para gradiente aritmético (usado en comparación)"""
        flujos = []
        for i in range(n_periodos):
            if es_anticipada:
                flujo = primer_pago + (i * gradiente)
            else:
                flujo = primer_pago + (i * gradiente)
            flujos.append(flujo)
        
        vp = 0
        for i, flujo in enumerate(flujos):
            if es_anticipada:
                vp += flujo / ((1 + tasa) ** i)
            else:
                vp += flujo / ((1 + tasa) ** (i + 1))
        
        vf = vp * ((1 + tasa) ** n_periodos)
        return vp, vf
    
    def _calcular_gradiente_geometrico_interno(self, primer_pago, tasa_crecimiento, n_periodos, tasa_interes, es_anticipada):
        """Cálculo interno para gradiente geométrico (usado en comparación)"""
        flujos = []
        for i in range(n_periodos):
            if es_anticipada:
                flujo = primer_pago * ((1 + tasa_crecimiento) ** i)
            else:
                flujo = primer_pago * ((1 + tasa_crecimiento) ** i)
            flujos.append(flujo)
        
        vp = 0
        for i, flujo in enumerate(flujos):
            if es_anticipada:
                vp += flujo / ((1 + tasa_interes) ** i)
            else:
                vp += flujo / ((1 + tasa_interes) ** (i + 1))
        
        vf = vp * ((1 + tasa_interes) ** n_periodos)
        return vp, vf