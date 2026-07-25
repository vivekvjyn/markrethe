import pytest


class TestHeading:

    def test_heading(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.heading("Title")
        assert "# Title\n\n" == read_log(tmpdir)

    def test_heading_level(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.heading("Title", level=3)
        assert "### Title\n\n" == read_log(tmpdir)

    def test_heading_invalid_level(self, markrethe):
        m, _ = markrethe
        with pytest.raises(ValueError):
            m.heading("Title", level=7)

    def test_heading_with_id(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.heading("Title", id="custom")
        assert "# Title {#custom}\n\n" == read_log(tmpdir)


class TestParagraph:

    def test_paragraph(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.paragraph("Hello world")
        assert "Hello world\n\n" == read_log(tmpdir)

    def test_line_break(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.line_break()
        assert "  \n" == read_log(tmpdir)

    def test_horizontal_rule(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.horizontal_rule()
        assert "\n---\n\n" == read_log(tmpdir)


class TestEmphasis:

    def test_bold(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.bold("text")
        assert "**text**\n\n" == read_log(tmpdir)

    def test_italic(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.italic("text")
        assert "*text*\n\n" == read_log(tmpdir)

    def test_bold_italic(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.bold_italic("text")
        assert "***text***\n\n" == read_log(tmpdir)


class TestBlockquote:

    def test_blockquote(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.blockquote("quote")
        assert "> quote\n\n" == read_log(tmpdir)

    def test_blockquote_multi(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.blockquote_multi(["para 1", "para 2"])
        content = read_log(tmpdir)
        assert "> para 1\n>" in content
        assert "> para 2\n>" in content

    def test_blockquote_nested(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.blockquote_nested(["level 1", "level 2"])
        content = read_log(tmpdir)
        assert "> level 1\n" in content
        assert ">> level 2\n" in content

    def test_blockquote_element_heading(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.blockquote_element("text", element="heading")
        assert "> #### text\n>" in read_log(tmpdir)

    def test_blockquote_element_list(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.blockquote_element("text", element="list")
        assert "> - text\n>" in read_log(tmpdir)

    def test_blockquote_element_bold(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.blockquote_element("text", element="bold")
        assert "> **text**\n>" in read_log(tmpdir)

    def test_blockquote_element_italic(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.blockquote_element("text", element="italic")
        assert "> *text**\n>" in read_log(tmpdir)

    def test_blockquote_element_code(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.blockquote_element("text", element="code")
        assert "> `text`\n>" in read_log(tmpdir)

    def test_blockquote_element_link(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.blockquote_element("text", element="link")
        assert "> text\n>" in read_log(tmpdir)

    def test_blockquote_element_default(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.blockquote_element("text")
        assert "> text\n>" in read_log(tmpdir)


class TestList:

    def test_ordered_list(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.ordered_list(["a", "b", "c"])
        content = read_log(tmpdir)
        assert "0. a\n" in content
        assert "1. b\n" in content
        assert "2. c\n" in content

    def test_ordered_list_start(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.ordered_list_start(["a", "b"], start=5)
        content = read_log(tmpdir)
        assert "5. a\n" in content
        assert "6. b\n" in content

    def test_unordered_list(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.unordered_list(["x", "y"])
        content = read_log(tmpdir)
        assert "- x\n" in content
        assert "- y\n" in content

    def test_unordered_list_star(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.unordered_list(["x", "y"], marker="*")
        content = read_log(tmpdir)
        assert "* x\n" in content
        assert "* y\n" in content

    def test_unordered_list_plus(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.unordered_list(["x", "y"], marker="+")
        content = read_log(tmpdir)
        assert "+ x\n" in content
        assert "+ y\n" in content

    def test_nested_ordered_list(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.nested_ordered_list(["item"])
        assert "    1. item\n" in read_log(tmpdir)

    def test_nested_unordered_list(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.nested_unordered_list(["item"])
        assert "    - item\n" in read_log(tmpdir)

    def test_list_with_paragraph_tuple(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.list_with_paragraph([("Item", "Sub-paragraph")])
        content = read_log(tmpdir)
        assert "- Item\n" in content
        assert "    Sub-paragraph\n" in content

    def test_list_with_paragraph_string(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.list_with_paragraph(["Item"])
        assert "- Item\n" in read_log(tmpdir)

    def test_list_with_blockquote_tuple(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.list_with_blockquote([("Item", "Quote text")])
        content = read_log(tmpdir)
        assert "- Item\n" in content
        assert "    > Quote text\n" in content

    def test_list_with_blockquote_string(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.list_with_blockquote(["Item"])
        assert "- Item\n" in read_log(tmpdir)

    def test_list_with_code_tuple(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.list_with_code([("Item", "code")])
        content = read_log(tmpdir)
        assert "- Item\n" in content
        assert "        code\n" in content

    def test_list_with_code_string(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.list_with_code(["Item"])
        assert "- Item\n" in read_log(tmpdir)


class TestCode:

    def test_inline_code(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.inline_code("code")
        assert "`code`\n\n" == read_log(tmpdir)

    def test_code_block(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.code_block("line1\nline2")
        content = read_log(tmpdir)
        assert "    line1\n" in content
        assert "    line2\n" in content


class TestLink:

    def test_link(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.link("Google", "https://google.com")
        assert "[Google](https://google.com)\n\n" == read_log(tmpdir)

    def test_link_with_title(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.link("Google", "https://google.com", title="Search")
        assert '[Google](https://google.com "Search")\n\n' == read_log(tmpdir)

    def test_link_bold(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.link_bold("text", "https://example.com")
        assert "**[text](https://example.com)**\n\n" == read_log(tmpdir)

    def test_link_italic(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.link_italic("text", "https://example.com")
        assert "*[text](https://example.com)*\n\n" == read_log(tmpdir)

    def test_link_code(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.link_code("text", "https://example.com")
        assert "[`text`](https://example.com)\n\n" == read_log(tmpdir)

    def test_reference_link(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.reference_link("text", "label")
        assert "[text][label]\n\n" == read_log(tmpdir)

    def test_reference_definition(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.reference_definition("label", "https://example.com")
        assert "[label]: <https://example.com>\n\n" == read_log(tmpdir)

    def test_reference_definition_with_title(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.reference_definition("label", "https://example.com", title="Title")
        assert '[label]: <https://example.com> "Title"\n\n' == read_log(tmpdir)


class TestImage:

    def test_image(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.image("alt", "img.png")
        assert "![alt](img.png)\n\n" == read_log(tmpdir)

    def test_image_with_title(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.image("alt", "img.png", title="Title")
        assert '![alt](img.png "Title")\n\n' == read_log(tmpdir)

    def test_image_link(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.image_link("alt", "img.png", "https://example.com")
        assert "[![alt](img.png)](https://example.com)\n\n" == read_log(tmpdir)

    def test_image_link_with_title(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.image_link("alt", "img.png", "https://example.com", title="Title")
        assert '[![alt](img.png "Title")](https://example.com)\n\n' == read_log(tmpdir)


class TestEscape:

    def test_auto_link(self, markrethe, read_log):
        m, tmpdir = markrethe
        m.auto_link("https://example.com")
        assert "<https://example.com>\n\n" == read_log(tmpdir)

    def test_escape(self, markrethe):
        m, _ = markrethe
        assert m.escape("*") == "\\*"

    def test_escape_chars(self, markrethe):
        m, _ = markrethe
        assert m.escape_chars("text with * and _") == "text with \\* and \\_"
