import matplotlib.pyplot as plt
import matplotlib_venn as venn

# Crear los conjuntos
bolsa_empleo = 300
prestando_servicios = 235 
otras_situaciones = 30
nunca_prestado = 35
interinos_fuera = 30
no_cumplen_requisitos = 5

# Calcular intersecciones
prestando_servicios_bolsa = prestando_servicios - interinos_fuera
otras_situaciones_bolsa = otras_situaciones
nunca_prestado_bolsa = nunca_prestado
interinos_fuera_cumplen = interinos_fuera - no_cumplen_requisitos
interinos_fuera_no_cumplen = no_cumplen_requisitos

# Crear figura con 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))

# Crear diagrama de Venn en subplot 1
v1 = venn.venn3(subsets=(prestando_servicios_bolsa, nunca_prestado_bolsa, interinos_fuera_cumplen, 
                        otras_situaciones_bolsa, 0, interinos_fuera_no_cumplen, 0),
               set_labels=('Prestando Servicios', 'Nunca han Prestado', 'Interinos Fuera'), ax=ax1)
v1.get_label_by_id('100').set_text(bolsa_empleo)
v1.get_label_by_id('010').set_text(nunca_prestado)
v1.get_label_by_id('001').set_text(interinos_fuera)
ax1.set_title('Diagrama de Venn - Bolsa de Empleo')

# Crear diagrama de Venn en subplot 2 
v2 = venn.venn3(subsets=(interinos_fuera_cumplen, 0, interinos_fuera_no_cumplen, 0),
               set_labels=('No cumplen requisitos', 'Interinos Fuera'), ax=ax2)
v2.get_label_by_id('100').set_text(bolsa_empleo)
v2.get_label_by_id('010').set_text(nunca_prestado)
v2.get_label_by_id('001').set_text(interinos_fuera)
ax2.set_title('Diagrama de Venn - Bolsa de Empleo')

# Ajustar layout y mostrar diagramas
fig.tight_layout()
plt.show()