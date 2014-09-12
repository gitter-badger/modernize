from utils import check_on_input


ZIP_CALL_NO_ARGS = ("""\
zip()
""", """\
from six.moves import zip
list(zip())
""")

ZIP_CALL_1_ARG = ("""\
zip(x)
""", """\
from six.moves import zip
list(zip(x))
""")

ZIP_CALL_2_ARGS = ("""\
zip(x, y)
zip(w, z)
""", """\
from six.moves import zip
list(zip(x, y))
list(zip(w, z))
""")

ZIP_CALL_STAR_ARGS = ("""\
zip(*args)
""", """\
from six.moves import zip
list(zip(*args))
""")

ZIP_KWARGS = ("""\
zip(arg1=[1])
""", """\
zip(arg1=[1])
""")

ZIP_ITERATOR_CONTEXT = ("""\
for a in zip(x):
    pass
""", """\
from six.moves import zip
for a in zip(x):
    pass
""")

ZIP_SIX_ALREADY = ("""\
from six.moves import zip
zip(x)
""", """\
from six.moves import zip
zip(x)
""")


def test_zip_call_no_args():
    check_on_input(*ZIP_CALL_NO_ARGS)

def test_zip_call_1_arg():
    check_on_input(*ZIP_CALL_1_ARG)

def test_zip_call_2_args():
    check_on_input(*ZIP_CALL_2_ARGS)

def test_zip_call_star_args():
    check_on_input(*ZIP_CALL_STAR_ARGS)

def test_zip_kwargs():
    check_on_input(*ZIP_KWARGS)

def test_zip_iterator_context():
    check_on_input(*ZIP_ITERATOR_CONTEXT)

def test_zip_six_already():
    check_on_input(*ZIP_SIX_ALREADY)
