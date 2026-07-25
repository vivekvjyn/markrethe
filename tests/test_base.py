import os

from markrethe import Markrethe


class TestBase:

    def test_callable(self, markrethe, read_log):
        m, tmpdir = markrethe
        m("Hello")
        assert "Hello\n\n" == read_log(tmpdir)

    def test_carriage_return(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.paragraph("First")
        m.carriage_return()
        m.paragraph("Second")
        assert "Second" in read_log(tmpdir)

    def test_carriage_return_multiline(self, markrethe, read_log):
        m, tmpdir = markrethe
        path = os.path.join(tmpdir, "log.md")
        with open(path, "w") as f:
            f.write("line1\nline2\n")
        m.carriage_return()
        with open(path) as f:
            content = f.read()
        assert "line1\n" in content
        assert "line2" not in content

    def test_log_file_created(self, markrethe):
        m, tmpdir = markrethe
        m.paragraph("test")
        assert os.path.exists(os.path.join(tmpdir, "log.md"))

    def test_log_file_cleared_on_init(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.paragraph("test")
        m2 = Markrethe(tmpdir)
        m2.paragraph("new")
        content = read_log(tmpdir)
        assert "test" not in content
        assert "new" in content
