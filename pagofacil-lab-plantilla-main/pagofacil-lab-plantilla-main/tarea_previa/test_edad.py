from edad import es_mayor_de_edad


def test_adulto_claro():
    assert es_mayor_de_edad(30) is True


def test_menor_claro():
    assert es_mayor_de_edad(10) is False


def test_justo_18_es_mayor_de_edad():
    assert es_mayor_de_edad(18) is True
