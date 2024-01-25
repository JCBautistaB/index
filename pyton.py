def calcular_pago_por_hora(tarifa_deseada, horas_diarias):
    dias_trabajados_por_semana = 5
    semanas_al_mes = 4
    horas_mensuales = horas_diarias * dias_trabajados_por_semana * semanas_al_mes
    pago_mensual = tarifa_deseada * horas_mensuales
    return pago_mensual

# Configuración
tarifa_deseada = float(input("Ingresa tu tarifa por hora en USD: "))
horas_diarias = float(input("Ingresa las horas que trabajarás diariamente: "))

# Calcular el pago mensual
pago_mensual = calcular_pago_por_hora(tarifa_deseada, horas_diarias)

print(f"Tu tarifa por hora es de ${tarifa_deseada} USD.")
print(f"Si trabajas {horas_diarias} horas al día, tu estimación de ingresos mensuales sería de ${pago_mensual:.2f} USD.")
