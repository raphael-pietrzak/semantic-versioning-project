from src.main import Main


def test_add_numbers():
    """Test de la fonction add_numbers de la classe Main."""
    # Arrange
    main = Main()

    # Act
    result1 = main.add_numbers(2, 3)
    result2 = main.add_numbers(-1, 1)
    result3 = main.add_numbers(0, 0)

    # Assert
    assert result1 == 5
    assert result2 == 0
    assert result3 == 0


def test_main_initialization():
    """Test de l'initialisation de la classe Main."""
    main = Main()
    assert main.name == "Main"
    assert main.version == "1.0.0"
