
# coding=utf-8


def application(env, start_response):
    """
    :param env: test
    :param start_response: test
    :return: test
    """
    start_response('200, OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]  # python3
