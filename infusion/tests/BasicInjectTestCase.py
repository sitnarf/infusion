from unittest import TestCase
from infusion.Context import Context


class BasicInjectTestCase(TestCase):

    def test_inject(self):

        context = Context({
            "param1": "param1",
            "param3": "param3",
        })

        @context.inject("param1", c="param3")
        def test_function(a, b, c):
            return "%s %s %s" % (a, b, c)

        self.assertEqual(
            test_function(b="param2"),
            "param1 param2 param3"
        )

    def test_update(self):

        context = Context({
            "param1": "param1",
            "param2": "param2",
        })

        context.update({
            "param2": "change",
        })

        @context.inject("param1", "param2")
        def test_function(a, b):
            return "%s %s" % (a, b)

        self.assertEqual(
            test_function(),
            "param1 change"
        )
