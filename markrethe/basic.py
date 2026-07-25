from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class BasicSyntax(ABC):
    """Mixin class providing basic Markdown syntax methods."""

    @abstractmethod
    def _write(self, content: str) -> None:
        """Write content to the output."""
        ...

    def heading(self, text: str, level: int = 1, id: Optional[str] = None) -> None:
        """Write a heading element.

        Args:
            text: The heading text content.
            level: Heading level from 1 to 6. Defaults to 1.
            id: Optional custom heading ID for anchor links.

        Raises:
            ValueError: If level is not between 1 and 6.
        """
        if level < 1 or level > 6:
            raise ValueError("Heading level should be between 1 and 6")
        if id:
            self._write(f"{'#' * level} {text} {{#{id}}}\n\n")
        else:
            self._write(f"{'#' * level} {text}\n\n")

    def paragraph(self, text: str) -> None:
        """Write a paragraph element.

        Args:
            text: The paragraph text content.
        """
        self._write(f"{text}\n\n")

    def line_break(self) -> None:
        """Write a line break element."""
        self._write("  \n")

    def horizontal_rule(self) -> None:
        """Write a horizontal rule element."""
        self._write("\n---\n\n")

    def bold(self, text: str) -> None:
        """Write bold text.

        Args:
            text: The text to make bold.
        """
        self._write(f"**{text}**\n\n")

    def italic(self, text: str) -> None:
        """Write italic text.

        Args:
            text: The text to make italic.
        """
        self._write(f"*{text}*\n\n")

    def bold_italic(self, text: str) -> None:
        """Write bold and italic text.

        Args:
            text: The text to make bold and italic.
        """
        self._write(f"***{text}***\n\n")

    def blockquote(self, text: str) -> None:
        """Write a blockquote element.

        Args:
            text: The blockquote text content.
        """
        self._write(f"> {text}\n\n")

    def blockquote_multi(self, texts: list[str]) -> None:
        """Write a multi-paragraph blockquote.

        Args:
            texts: List of paragraph texts for the blockquote.
        """
        for text in texts:
            self._write(f"> {text}\n>\n")
        self._write("\n")

    def blockquote_nested(self, texts: list[str]) -> None:
        """Write a nested blockquote.

        Args:
            texts: List of texts, each nested one level deeper.
        """
        for depth, text in enumerate(texts):
            self._write(f"{'>' * (depth + 1)} {text}\n")
        self._write("\n")

    def blockquote_element(self, text: str, element: Optional[str] = None) -> None:
        """Write a blockquote containing a specific element type.

        Args:
            text: The content text.
            element: Element type - 'heading', 'list', 'bold',
                'italic', 'code', or 'link'. Defaults to plain text.
        """
        if element == "heading":
            self._write(f"> #### {text}\n>\n")
        elif element == "list":
            self._write(f"> - {text}\n>\n")
        elif element == "bold":
            self._write(f"> **{text}**\n>\n")
        elif element == "italic":
            self._write(f"> *{text}**\n>\n")
        elif element == "code":
            self._write(f"> `{text}`\n>\n")
        elif element == "link":
            self._write(f"> {text}\n>\n")
        else:
            self._write(f"> {text}\n>\n")

    def ordered_list(self, items: list[str]) -> None:
        """Write an ordered list.

        Args:
            items: List of item texts.
        """
        for i, item in enumerate(items):
            self._write(f"{i}. {item}\n")
        self._write("\n")

    def ordered_list_start(self, items: list[str], start: int = 1) -> None:
        """Write an ordered list starting from a specific number.

        Args:
            items: List of item texts.
            start: Starting number for the list. Defaults to 1.
        """
        for i, item in enumerate(items):
            self._write(f"{start + i}. {item}\n")
        self._write("\n")

    def unordered_list(self, items: list[str], marker: str = "-") -> None:
        """Write an unordered list.

        Args:
            items: List of item texts.
            marker: List marker - '-', '*', or '+'. Defaults to '-'.
        """
        for item in items:
            self._write(f"{marker} {item}\n")
        self._write("\n")

    def nested_ordered_list(self, items: list[str], indent: int = 1) -> None:
        """Write a nested ordered list.

        Args:
            items: List of item texts.
            indent: Indentation level. Defaults to 1.
        """
        for i, item in enumerate(items):
            self._write(f"{'    ' * indent}{i + 1}. {item}\n")
        self._write("\n")

    def nested_unordered_list(self, items: list[str], indent: int = 1) -> None:
        """Write a nested unordered list.

        Args:
            items: List of item texts.
            indent: Indentation level. Defaults to 1.
        """
        for item in items:
            self._write(f"{'    ' * indent}- {item}\n")
        self._write("\n")

    def list_with_paragraph(self, items: list[str | tuple[str, str]]) -> None:
        """Write a list where items can contain sub-paragraphs.

        Args:
            items: List of strings or tuples (item, paragraph_text).
        """
        for item in items:
            if isinstance(item, tuple):
                self._write(f"- {item[0]}\n\n    {item[1]}\n\n")
            else:
                self._write(f"- {item}\n")
        self._write("\n")

    def list_with_blockquote(self, items: list[str | tuple[str, str]]) -> None:
        """Write a list where items can contain blockquotes.

        Args:
            items: List of strings or tuples (item, blockquote_text).
        """
        for item in items:
            if isinstance(item, tuple):
                self._write(f"- {item[0]}\n\n    > {item[1]}\n\n")
            else:
                self._write(f"- {item}\n")
        self._write("\n")

    def list_with_code(self, items: list[str | tuple[str, str]]) -> None:
        """Write a list where items can contain code blocks.

        Args:
            items: List of strings or tuples (item, code_text).
        """
        for item in items:
            if isinstance(item, tuple):
                self._write(f"- {item[0]}\n\n        {item[1]}\n\n")
            else:
                self._write(f"- {item}\n")
        self._write("\n")

    def inline_code(self, text: str) -> None:
        """Write inline code.

        Args:
            text: The code text to inline.
        """
        self._write(f"`{text}`\n\n")

    def code_block(self, code: str, indent: int = 4) -> None:
        """Write an indented code block.

        Args:
            code: The code content.
            indent: Number of spaces for indentation. Defaults to 4.
        """
        for line in code.split("\n"):
            self._write(f"{' ' * indent}{line}\n")
        self._write("\n")

    def link(self, text: str, url: str, title: Optional[str] = None) -> None:
        """Write a hyperlink.

        Args:
            text: The link text.
            url: The URL to link to.
            title: Optional tooltip title text.
        """
        if title:
            self._write(f'[{text}]({url} "{title}")\n\n')
        else:
            self._write(f"[{text}]({url})\n\n")

    def link_bold(self, text: str, url: str) -> None:
        """Write a bold hyperlink.

        Args:
            text: The link text.
            url: The URL to link to.
        """
        self._write(f"**[{text}]({url})**\n\n")

    def link_italic(self, text: str, url: str) -> None:
        """Write an italic hyperlink.

        Args:
            text: The link text.
            url: The URL to link to.
        """
        self._write(f"*[{text}]({url})*\n\n")

    def link_code(self, text: str, url: str) -> None:
        """Write a code-formatted hyperlink.

        Args:
            text: The link text.
            url: The URL to link to.
        """
        self._write(f"[`{text}`]({url})\n\n")

    def reference_link(self, text: str, label: str) -> None:
        """Write a reference-style link (first part).

        Args:
            text: The link text.
            label: The reference label identifier.
        """
        self._write(f"[{text}][{label}]\n\n")

    def reference_definition(
        self, label: str, url: str, title: Optional[str] = None
    ) -> None:
        """Write a reference-style link definition (second part).

        Args:
            label: The reference label identifier.
            url: The URL to link to.
            title: Optional tooltip title text.
        """
        if title:
            self._write(f'[{label}]: <{url}> "{title}"\n\n')
        else:
            self._write(f"[{label}]: <{url}>\n\n")

    def image(self, alt: str, url: str, title: Optional[str] = None) -> None:
        """Write an image element.

        Args:
            alt: Alternative text for the image.
            url: The image URL or path.
            title: Optional tooltip title text.
        """
        if title:
            self._write(f'![{alt}]({url} "{title}")\n\n')
        else:
            self._write(f"![{alt}]({url})\n\n")

    def image_link(
        self,
        alt: str,
        img_url: str,
        link_url: str,
        title: Optional[str] = None,
    ) -> None:
        """Write an image wrapped in a hyperlink.

        Args:
            alt: Alternative text for the image.
            img_url: The image URL or path.
            link_url: The URL to link to.
            title: Optional tooltip title text.
        """
        if title:
            self._write(f'[![{alt}]({img_url} "{title}")]({link_url})\n\n')
        else:
            self._write(f"[![{alt}]({img_url})]({link_url})\n\n")

    def escape(self, char: str) -> str:
        """Escape a special Markdown character.

        Args:
            char: The character to escape.

        Returns:
            The escaped character with a backslash prefix.
        """
        return f"\\{char}"

    def auto_link(self, url: str) -> None:
        """Write an auto-link in angle brackets.

        Args:
            url: The URL to auto-link.
        """
        self._write(f"<{url}>\n\n")

    def escape_chars(self, text: str) -> str:
        """Escape all special Markdown characters in text.

        Args:
            text: The text to escape.

        Returns:
            Text with all special characters escaped.
        """
        chars = [
            "\\",
            "`",
            "*",
            "_",
            "{",
            "}",
            "[",
            "]",
            "<",
            ">",
            "(",
            ")",
            "#",
            "+",
            "-",
            ".",
            "!",
            "|",
        ]
        return "".join(f"\\{c}" if c in chars else c for c in text)
