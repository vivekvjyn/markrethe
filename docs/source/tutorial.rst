Usage Examples
--------------

Basic Usage
^^^^^^^^^^^

.. code-block:: python

    from markrethe import Markrethe

    m = Markrethe("./logs")
    m.heading("Experiment 1")
    m.paragraph("This is the start of my experiment.")
    m.bold("Important finding:")
    m.italic("The results were significant.")

The instance can also be called directly as a function to write a paragraph:

.. code-block:: python

    m("This writes a paragraph directly.")

Text Structure
^^^^^^^^^^^^^^

Headings
""""""""

.. code-block:: python

    m.heading("Title", level=1)       # # Title
    m.heading("Subtitle", level=2)    # ## Subtitle
    m.heading("Custom", level=1, id="my-custom-id")  # # Title {#my-custom-id}

Paragraphs and Line Breaks
""""""""""""""""""""""""""

.. code-block:: python

    m.paragraph("This is a paragraph.")
    m.line_break()  # Two trailing spaces for <br>
    m.horizontal_rule()  # ---

Emphasis
""""""""

.. code-block:: python

    m.bold("bold text")       # **bold text**
    m.italic("italic text")   # *italic text*
    m.bold_italic("both")     # ***both***

Blockquotes
"""""""""""

.. code-block:: python

    m.blockquote("Simple quote")
    m.blockquote_multi(["First paragraph", "Second paragraph"])
    m.blockquote_nested(["Level 1", "Level 2", "Level 3"])

Lists
"""""

.. code-block:: python

    m.ordered_list(["First", "Second", "Third"])
    m.ordered_list_start(["Fifth", "Sixth"], start=5)
    m.unordered_list(["Item", "Item"])
    m.unordered_list(["Item"], marker="*")   # asterisks
    m.unordered_list(["Item"], marker="+")   # plus signs
    m.nested_ordered_list(["Nested item"])
    m.nested_unordered_list(["Nested item"])

Lists with other elements:

.. code-block:: python

    m.list_with_paragraph([
        ("Item 1", "Sub-paragraph text"),
        "Item 2"
    ])
    m.list_with_blockquote([
        ("Item", "This is a blockquote inside a list")
    ])
    m.list_with_code([
        ("Open the file", "cat file.txt")
    ])

Code
""""

.. code-block:: python

    m.inline_code("variable_name")  # `variable_name`
    m.code_block("line 1\nline 2")  # Indented code block

Links and Images
""""""""""""""""

.. code-block:: python

    m.link("Google", "https://google.com")
    m.link("Google", "https://google.com", title="Search engine")
    m.link_bold("Bold link", "https://example.com")
    m.link_italic("Italic link", "https://example.com")
    m.link_code("Code link", "https://example.com")

Reference-style links:

.. code-block:: python

    m.reference_link("Click here", "my-label")
    m.reference_definition("my-label", "https://example.com", title="My Site")

Images:

.. code-block:: python

    m.image("Alt text", "/path/to/image.png")
    m.image("Alt text", "/path/to/image.png", title="Image title")
    m.image_link("Alt text", "img.png", "https://example.com")

Escaping Characters
"""""""""""""""""""

.. code-block:: python

    escaped = m.escape("*")        # \*
    safe_text = m.escape_chars("text with * and _")  # text with \* and \_

Extended Syntax
^^^^^^^^^^^^^^^

Tables
""""""

.. code-block:: python

    m.table(
        headers=["Name", "Age", "City"],
        rows=[["Alice", "30", "NYC"], ["Bob", "25", "LA"]],
        alignments=["left", "right", "center"]
    )

Fenced Code Blocks
""""""""""""""""""

.. code-block:: python

    m.fenced_code("x = 1\nprint(x)")  # No language
    m.fenced_code("x = 1", language="python")  # With syntax highlighting

Footnotes
"""""""""

.. code-block:: python

    m.paragraph("This has a footnote.")
    m.footnote_reference("1")
    m.footnote_definition("1", "This is the footnote content.")

Heading IDs and Links
"""""""""""""""""""""

.. code-block:: python

    m.heading_with_id("My Section", level=2, id="my-section")
    m.heading_link("Go to section", "my-section")

Definition Lists
""""""""""""""""

.. code-block:: python

    m.definition_list({
        "Term 1": "Definition for term 1",
        "Term 2": ["First definition", "Second definition"]
    })

Text Formatting
"""""""""""""""

.. code-block:: python

    m.strikethrough("deleted text")   # ~~deleted text~~
    m.highlight("important text")     # ==important text==

Task Lists
""""""""""

.. code-block:: python

    m.task_list([
        "Unchecked item",
        ("Checked item", True),
        ("Unchecked item", False)
    ])

Auto URL Linking
""""""""""""""""

.. code-block:: python

    m.auto_url("https://example.com")     # Auto-linked
    m.no_auto_url("https://example.com")  # Displayed as code

Carriage Return
"""""""""""""""

To remove the last written line:

.. code-block:: python

    m.paragraph("This will be removed")
    m.carriage_return()
