""" Example pylib functions"""


def numbers_and_nulls(resource, doc, env, *args, **kwargs):
    """ A generator that produces a dataset that intermixes numbers and nulls

    """

    yield 'float int'.split()

    for i in range(10):
        if i%2 == 0:
            yield [float(i*1.1), int(i)]
        else:
            yield [None, None]
            

