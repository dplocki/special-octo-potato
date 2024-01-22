import requests


# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def test_query_params(httpserver):
    httpserver.expect_request("/foo", query_string={"user": "user1", "group": "group1"}).respond_with_data("OK")

    assert requests.get(httpserver.url_for("/foo?user=user1&group=group1")).status_code == 200
    assert requests.get(httpserver.url_for("/foo?group=group1&user=user1")).status_code == 200
