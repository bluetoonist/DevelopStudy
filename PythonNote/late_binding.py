from unittest import TestCase

value = "foo"


def strchecker_(x1, x2):
    return x1 == x2


assert TestCase.assertEquals(strchecker_("foo", "Foo") == "Hello")
