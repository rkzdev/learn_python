class TestClass:
    x = "hello"

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        assert hasattr(self, "x")
