from __future__ import annotations

import os


class Base:
    """Base class providing core write functionality for markdown files."""

    def __init__(self, log_dir: str) -> None:
        """Initialize the markdown log writer.

        Args:
            log_dir: Directory where the markdown log file will be stored.
        """
        self.dir = log_dir
        os.makedirs(self.dir, exist_ok=True)
        if os.path.exists(os.path.join(self.dir, "log.md")):
            os.remove(os.path.join(self.dir, "log.md"))

    def _write(self, content: str) -> None:
        """Write content to the markdown log file.

        Args:
            content: The string content to append to the log file.
        """
        with open(os.path.join(self.dir, "log.md"), "a") as f:
            f.write(content)

    def carriage_return(self) -> None:
        """Remove the last line from the markdown log file."""
        with open(os.path.join(self.dir, "log.md"), "rb+") as f:
            f.seek(0, 2)
            pos = f.tell() - 1
            f.seek(pos)
            if f.read(1) == b"\n":
                pos -= 1
            while pos > 0:
                f.seek(pos)
                if f.read(1) == b"\n":
                    break
                pos -= 1
            f.truncate(pos + 1 if pos > 0 else 0)
