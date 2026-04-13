import flet
from flet import Page, Dropdown, Text, ElevatedButton, Row, Container

# Colores y sus valores para las bandas de resistencia
color_bandas = {
    "Negro": 0,
    "Marrón": 1,
    "Rojo": 2,
    "Naranja": 3,
    "Amarillo": 4,
    "Verde": 5,
    "Azul": 6,
    "Violeta": 7,
    "Gris": 8,
    "Blanco": 9,
}

color_multiplicador = {
    "Negro": 1,
    "Marrón": 10,
    "Rojo": 100,
    "Naranja": 1_000,
    "Amarillo": 10_000,
    "Verde": 100_000,
    "Azul": 1_000_000,
    "Violeta": 10_000_000,
    "Gris": 100_000_000,
    "Blanco": 1_000_000_000,
    "Dorado": 0.1,
    "Plateado": 0.01,
}

color_tolerancia = {
    "Marrón": "±1%",
    "Rojo": "±2%",
    "Dorado": "±5%",
    "Plateado": "±10%",
    "Sin color": "±20%",
}


def formato_resistencia(valor_ohmios: float) -> str:
    """Devuelve el valor de resistencia con unidad adecuada."""
    if valor_ohmios >= 1_000_000:
        return f"{valor_ohmios / 1_000_000:.2f} MΩ"
    elif valor_ohmios >= 1_000:
        return f"{valor_ohmios / 1_000:.2f} kΩ"
    else:
        return f"{valor_ohmios:.2f} Ω"


def main(page: Page):
    page.title = "Calculadora de Resistencias por Código de Colores"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_width = 500
    page.window_height = 350

    # Dropdowns para seleccionar colores

    banda1 = Dropdown(
        label="Primera banda (primer dígito)",
        width=300,
        options=[flet.dropdown.Option(c) for c in color_bandas.keys()],
        value="Negro",
    )
    banda2 = Dropdown(
        label="Segunda banda (segundo dígito)",
        width=300,
        options=[flet.dropdown.Option(c) for c in color_bandas.keys()],
        value="Negro",
    )
    multiplicador = Dropdown(
        label="Multiplicador",
        width=300,
        options=[flet.dropdown.Option(c) for c in color_multiplicador.keys()],
        value="Negro",
    )
    tolerancia = Dropdown(
        label="Tolerancia",
        width=300,
        options=[flet.dropdown.Option(c) for c in color_tolerancia.keys()],
        value="Marrón",
    )

    resultado = Text(size=20, weight="bold")

    def calcular_resistencia(e):
        try:
            d1 = color_bandas[banda1.value]
            d2 = color_bandas[banda2.value]
            multi = color_multiplicador[multiplicador.value]
            tol = color_tolerancia[tolerancia.value]

            valor = (d1 * 10 + d2) * multi
            valor_formateado = formato_resistencia(valor)

            resultado.value = f"Valor: {valor_formateado} {tol}"
            page.update()
        except Exception as ex:
            resultado.value = f"Error: {ex}"
            page.update()

    boton_calcular = ElevatedButton(content=Text("Calcular resistencia"), on_click=calcular_resistencia)

    page.add(
        banda1,
        banda2,
        multiplicador,
        tolerancia,
        boton_calcular,
        Container(content=resultado, padding=20),
    )


if __name__ == "__main__":
    flet.app(target=main)