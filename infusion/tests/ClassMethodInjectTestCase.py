from unittest import TestCase
from infusion.Context import Context


class ClassMethodInjectTestCase(TestCase):

    def test_inject(self):

        context = Context({
            "param1": "x",
            "param2": "y",
        })

        class TestClass:
            @context.inject_method("param1", "param2")
            def test_function(self, a, b):
                return "%s %s" % (a, b)


        instance = TestClass()
        self.assertEqual(
            instance.test_function(),
            "x y"
        )
