import plot_utils


class Bar:
    def __init__(self, name, handmade_potatoes, crispy, soft_inside, potatoes_flavour, spicy_sauce, sauce_flavour,
                 sauce_density, price, quantity, qos):
        self.grades = {
            'Patatas caseras': handmade_potatoes,
            'Crujientes': crispy,
            'Blanditas dentro': soft_inside,
            'Sabor patatas': potatoes_flavour,
            'Salsa picante': spicy_sauce,
            'Sabor salsa': sauce_flavour,
            'Espesor salsa': sauce_density,
            'Precio': price,
            'Cantidad': quantity,
            'Atención': qos,
        }
        self.name = name
        for v in self.grades.values():
            if not 0 <= v <= 1:
                raise ValueError(f'{v} must be float and between [0, 1]')


# Gredos
GREDOS = Bar('Gredos', 1.0, 0.5, 1.0, 0.8,
             0.75, 0.85, 0.9, 1.0, 0.8, 0.9)

plot_utils.plot_pentagon(GREDOS.grades, GREDOS.name)

# Docamar
DOCAMAR = Bar('Docamar', 1.0, 0.0, 1.0, 0.5,
              0.5, 0.78, 0.68, 0.3, 0.5, 1.0)

plot_utils.plot_pentagon(DOCAMAR.grades, DOCAMAR.name)

# Puchero de quintana
PUCHERO_DE_QUINTANA = Bar('Puchero de Quitana', 1.0, 0.7, 1.0, 0.7,
                          0.8, 1.0, 0.9, 0.8, 0.9, 0.8)

plot_utils.plot_pentagon(PUCHERO_DE_QUINTANA.grades, PUCHERO_DE_QUINTANA.name)
