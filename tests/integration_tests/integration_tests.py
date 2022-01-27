import pytest


def test_index_with_registered_clubs(client, test_club_as_list, mocker_test_club_as_list):
    """
    checks that the route for index returns a success status code
    and displays the needed elements in template:
    - page title
    - points table for clubs
    """
    response = client.get('/')
    assert response.status_code == 200
    response_decode = response.data.decode()
    assert 'GUDLFT Registration Portal!' in response_decode
    assert 'Test Club' in response_decode
    assert '- 16' in response_decode


def test_index_with_no_clubs_registered(client, test_empty_list, mocker_test_empty_clubs_list):
    """
    checks that the route for index returns a success status code
    and displays that there is no club to display when clubs list in database is empty
    """
    response = client.get('/')
    assert response.status_code == 200
    response_decode = response.data.decode()
    assert 'GUDLFT Registration Portal!' in response_decode
    assert 'No clubs to display' in response_decode


def test_show_summary_with_registered_competitions(client, test_club, mocker_test_club_as_list,
                                                   mocker_test_competitions_as_list):
    """
    checks that the route for show summary returns a success status code
    and displays the list of registered competitions from database
    """
    response = client.post('/show_summary', data={'email': test_club['email']})
    response_decode = response.data.decode()
    assert response.status_code == 200
    assert 'Welcome, test@club.com' in response_decode
    assert 'Test Future Competition' in response_decode


def test_show_summary_with_no_registered_competitions(client, test_club, mocker_test_club_as_list,
                                                      mocker_test_empty_competitions_list):
    """
    checks that the route for show summary returns a success status code
    and displays that there is no competition to display when competitions list in database is empty
    """
    response = client.post('/show_summary', data={'email': test_club['email']})
    response_decode = response.data.decode()
    assert response.status_code == 200
    assert 'Welcome, test@club.com' in response_decode
    assert 'No competitions to display' in response_decode


def test_book(client, test_future_competition, test_club, mocker_test_club_as_list, mocker_test_competitions_as_list):
    """
    Integration test for book nominal case.
    checks that the whole function book works
    """
    competition_name = test_future_competition['name']
    club_name = test_club['name']
    response = client.get(f'/book/{competition_name}/{club_name}')
    response_decode = response.data.decode()
    assert response.status_code == 200
    assert 'places' in response_decode


def test_purchase_places(client, test_future_competition,
                         mocker_test_competitions_as_list, mocker_test_club_as_list, mocker_test_db_path,
                         test_club, test_required_places, mocker_test_database):
    """
    Integration test for purchase places nominal case.
    checks that the whole function purchase_places works
    """
    response = client.post('/purchase_places',
                           data={'competition_name': test_future_competition['name'],
                                 'club_name': test_club['name'],
                                 'places': test_required_places})
    response_decode = response.data.decode()
    assert response.status_code == 200
    assert 'Welcome, test@club.com' in response_decode
    assert f"Great-booking complete! :" \
           f" {test_required_places} places for {test_future_competition['name']}" \
           in response_decode


def test_purchase_places_number_places_not_ok(client, test_future_competition,
                                              mocker_test_competitions_as_list, mocker_test_club_as_list,
                                              mocker_test_db_path,
                                              test_club, test_required_places, mocker_test_database):
    """
    Integration test for purchase places error case.
    checks that the whole function purchase_places works
    """
    response = client.post('/purchase_places',
                           data={'competition_name': test_future_competition['name'],
                                 'club_name': test_club['name'],
                                 'places': ''})
    response_decode = response.data.decode()
    assert response.status_code == 200
    assert 'Welcome, test@club.com' in response_decode
    assert 'Please provide a positive number of places' in response_decode


def test_logout(client):
    """
    Integration test for logout nominal case.
    checks that the whole logout function works
    """
    response = client.get('/logout')
    response_decode = response.data.decode()

    assert response.status_code == 302
    assert 'redirected automatically to target URL: <a href="/">/</a>' in response_decode
