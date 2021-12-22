from server import load_competitions, load_clubs, find_club

competitions = load_competitions()  # à retirer de la partie test plus tard ? à tester aussi ?
clubs = load_clubs()  # à retirer de la partie test plus tard ? à tester aussi ?


def test_load_clubs():
    """

    """
    pass


def test_load_competitions():
    """

    """
    pass


def test_index():
    """

    """
    pass


def test_show_summary_registered_user():
    """
    Checks that an email is registered
    """
    # si l'adresse est dans la base : OK
    # si l'adresse n'est pas dans la base : NOK

    email = "john@simplylift.co"
    registered_emails = [club['email'] for club in clubs]
    find_club(email)
    assert email in registered_emails


def test_show_summary_unregistered_user():
    """
    Checks that an email is not registered
    """

    email = 'unregistered_user@testclub.com'
    registered_emails = [club['email'] for club in clubs]
    find_club(email)
    assert email not in registered_emails


def test_show_summary_malformed_email_address():
    """

    """
    email = 'malformed_address@testclub.co'
    pass


def test_show_summary_not_an_email():
    """

    """
    email = 'hello_its_me'
    pass


def test_book():
    """
    TDD : When a place for a competition is bought, the number of points is deduced
    """
    pass


def test_purchase_places():
    """

    """
    pass


def test_display_points():
    """

    """
    pass


def test_logout():
    """

    """
    pass
