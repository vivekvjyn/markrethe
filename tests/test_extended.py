class TestTable:

    def test_table(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.table(["Name", "Age"], [["Alice", "30"], ["Bob", "25"]])
        content = read_log(tmpdir)
        assert "| Name | Age |" in content
        assert "| Alice | 30 |" in content

    def test_table_alignment(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.table(["Left", "Right"], [["a", "b"]], ["left", "right"])
        assert "----" in read_log(tmpdir)

    def test_table_empty(self, markrethe):
        m, _ = markrethe
        m.table([], [])

    def test_table_center_alignment(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.table(["Col"], [["val"]], ["center"])
        assert ":---:" in read_log(tmpdir)


class TestFencedCode:

    def test_fenced_code(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.fenced_code("x = 1")
        assert "```\nx = 1\n```\n\n" in read_log(tmpdir)

    def test_fenced_code_with_language(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.fenced_code("x = 1", language="python")
        assert "```python\nx = 1\n```\n\n" in read_log(tmpdir)


class TestFootnote:

    def test_footnote_reference(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.footnote_reference("1")
        assert "[^1]" == read_log(tmpdir)

    def test_footnote_definition(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.footnote_definition("1", "Note text")
        assert "\n[^1]: Note text\n\n" in read_log(tmpdir)


class TestHeadingId:

    def test_heading_with_id(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.heading_with_id("Title", level=2, id="custom")
        assert "## Title {#custom}\n\n" == read_log(tmpdir)

    def test_heading_with_id_no_id(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.heading_with_id("Title", level=2)
        assert "## Title\n\n" == read_log(tmpdir)

    def test_heading_with_id_invalid_level(self, markrethe):
        m, _ = markrethe
        import pytest

        with pytest.raises(ValueError):
            m.heading_with_id("Title", level=0)

    def test_heading_link(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.heading_link("Go to title", "my-title")
        assert "[Go to title](#my-title)\n\n" == read_log(tmpdir)


class TestDefinitionList:

    def test_definition_list(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.definition_list({"Term": "Definition"})
        content = read_log(tmpdir)
        assert "Term\n" in content
        assert ": Definition\n\n" in content

    def test_definition_list_multiple(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.definition_list({"Term": ["Def 1", "Def 2"]})
        content = read_log(tmpdir)
        assert ": Def 1\n" in content
        assert ": Def 2\n" in content


class TestTextFormatting:

    def test_strikethrough(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.strikethrough("deleted")
        assert "~~deleted~~\n\n" == read_log(tmpdir)

    def test_highlight(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.highlight("important")
        assert "==important==\n\n" == read_log(tmpdir)


class TestTaskList:

    def test_task_list(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.task_list(["Task 1", "Task 2"])
        content = read_log(tmpdir)
        assert "- [ ] Task 1\n" in content
        assert "- [ ] Task 2\n" in content

    def test_task_list_checked(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.task_list([("Task 1", True), ("Task 2", False)])
        content = read_log(tmpdir)
        assert "- [x] Task 1\n" in content
        assert "- [ ] Task 2\n" in content


class TestAutoUrl:

    def test_auto_url(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.auto_url("https://example.com")
        assert "https://example.com\n\n" == read_log(tmpdir)

    def test_no_auto_url(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.no_auto_url("https://example.com")
        assert "`https://example.com`\n\n" == read_log(tmpdir)
