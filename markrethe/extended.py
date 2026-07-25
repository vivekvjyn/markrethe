from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class ExtendedSyntax(ABC):
    """Mixin class providing extended Markdown syntax methods."""

    @abstractmethod
    def _write(self, content: str) -> None:
        """Write content to the output."""
        ...

    def table(
        self,
        headers: list[str],
        rows: list[list[str]],
        alignments: Optional[list[str]] = None,
    ) -> None:
        """Write a table element.

        Args:
            headers: List of column header texts.
            rows: List of row data (each row is a list of cell values).
            alignments: Optional list of alignment strings ('left', 'center', 'right').
        """
        if not headers or not rows:
            return
        if alignments is None:
            alignments = ["left"] * len(headers)

        header_line = "| " + " | ".join(headers) + " |"
        self._write(header_line + "\n")

        separator_parts = []
        for i, align in enumerate(alignments):
            if i < len(headers):
                width = max(len(headers[i]), 3)
                if align == "center":
                    separator_parts.append(f":{'-' * width}:")
                elif align == "right":
                    separator_parts.append(f"{'-' * width}:")
                else:
                    separator_parts.append(f"{'-' * width}")
        self._write("| " + " | ".join(separator_parts) + " |\n")

        for row in rows:
            self._write("| " + " | ".join(str(cell) for cell in row) + " |\n")
        self._write("\n")

    def fenced_code(self, code: str, language: Optional[str] = None) -> None:
        """Write a fenced code block.

        Args:
            code: The code content.
            language: Optional language for syntax highlighting.
        """
        if language:
            self._write(f"```{language}\n{code}\n```\n\n")
        else:
            self._write(f"```\n{code}\n```\n\n")

    def footnote_reference(self, id: str) -> None:
        """Write a footnote reference.

        Args:
            id: The footnote identifier.
        """
        self._write(f"[^{id}]")

    def footnote_definition(self, id: str, text: str) -> None:
        """Write a footnote definition.

        Args:
            id: The footnote identifier.
            text: The footnote content.
        """
        self._write(f"\n[^{id}]: {text}\n\n")

    def heading_with_id(
        self, text: str, level: int = 1, id: Optional[str] = None
    ) -> None:
        """Write a heading with a custom ID.

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

    def heading_link(self, text: str, id: str) -> None:
        """Write a link to a heading by ID.

        Args:
            text: The link text.
            id: The heading ID to link to.
        """
        self._write(f"[{text}](#{id})\n\n")

    def definition_list(self, terms: dict[str, str | list[str]]) -> None:
        """Write a definition list.

        Args:
            terms: Dictionary mapping terms to definitions.
                Values can be a string or list of strings.
        """
        for term, definitions in terms.items():
            self._write(f"{term}\n")
            if isinstance(definitions, str):
                self._write(f": {definitions}\n\n")
            else:
                for defn in definitions:
                    self._write(f": {defn}\n")
                self._write("\n")

    def strikethrough(self, text: str) -> None:
        """Write strikethrough text.

        Args:
            text: The text to strikethrough.
        """
        self._write(f"~~{text}~~\n\n")

    def highlight(self, text: str) -> None:
        """Write highlighted text.

        Args:
            text: The text to highlight.
        """
        self._write(f"=={text}==\n\n")

    def task_list(self, items: list[str | tuple[str, bool]]) -> None:
        """Write a task list with checkboxes.

        Args:
            items: List of strings or tuples (text, checked).
                Tuples with checked=True render as checked boxes.
        """
        for item in items:
            if isinstance(item, tuple):
                checked = "x" if item[1] else " "
                self._write(f"- [{checked}] {item[0]}\n")
            else:
                self._write(f"- [ ] {item}\n")
        self._write("\n")

    def auto_url(self, url: str) -> None:
        """Write an auto-linked URL.

        Args:
            url: The URL to auto-link.
        """
        self._write(f"{url}\n\n")

    def no_auto_url(self, url: str) -> None:
        """Write a URL as code to prevent auto-linking.

        Args:
            url: The URL to display as code.
        """
        self._write(f"`{url}`\n\n")
