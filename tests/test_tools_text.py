"""
Tests for text tools.
"""
import pytest

from mcp_server.tools.text_tools import register_text_tools


class TestTextTools:
    """Test cases for text tools."""

    def setup_method(self) -> None:
        """Set up a mock MCP instance and capture registered tools."""
        self.tools: dict = {}

        def tool_decorator(name: str):  # type: ignore[return]
            def decorator(func):  # type: ignore[return]
                self.tools[name] = func
                return func

            return decorator

        mock_mcp = type("MockMCP", (), {"tool": staticmethod(tool_decorator)})()
        register_text_tools(mock_mcp)

    def test_to_uppercase(self) -> None:
        fn = self.tools["Uppercase Text"]
        assert fn("hello") == "HELLO"
        assert fn("Hello World") == "HELLO WORLD"

    def test_to_lowercase(self) -> None:
        fn = self.tools["Lowercase Text"]
        assert fn("HELLO") == "hello"
        assert fn("Hello World") == "hello world"

    def test_reverse_text(self) -> None:
        fn = self.tools["Reverse Text"]
        assert fn("abc") == "cba"
        assert fn("") == ""

    def test_count_words(self) -> None:
        fn = self.tools["Count Words"]
        assert fn("hello world") == 2
        assert fn("one") == 1
        assert fn("") == 0

    def test_count_characters_with_spaces(self) -> None:
        fn = self.tools["Count Characters"]
        assert fn("hello world", include_spaces=True) == 11

    def test_count_characters_without_spaces(self) -> None:
        fn = self.tools["Count Characters"]
        assert fn("hello world", include_spaces=False) == 10

    def test_title_case(self) -> None:
        fn = self.tools["Title Case"]
        assert fn("hello world") == "Hello World"

    def test_split_text(self) -> None:
        fn = self.tools["Split Text"]
        assert fn("a,b,c", delimiter=",") == ["a", "b", "c"]
        assert fn("hello world") == ["hello", "world"]

    def test_replace_text(self) -> None:
        fn = self.tools["Replace Text"]
        assert fn("foo bar foo", "foo", "baz") == "baz bar baz"

    def test_trim_text(self) -> None:
        fn = self.tools["Trim Text"]
        assert fn("  hello  ") == "hello"
        assert fn("no spaces") == "no spaces"

    def test_extract_emails(self) -> None:
        fn = self.tools["Extract Emails"]
        text = "Contact us at support@example.com or admin@test.org for help."
        result = fn(text)
        assert "support@example.com" in result
        assert "admin@test.org" in result

    def test_extract_emails_none_found(self) -> None:
        fn = self.tools["Extract Emails"]
        assert fn("No emails here!") == []
