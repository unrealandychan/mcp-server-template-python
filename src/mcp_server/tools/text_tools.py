"""
Text tools for the MCP server.

Provides string manipulation and text analysis tools for MCP clients.
"""
import re
from typing import List

from fastmcp import FastMCP


def register_text_tools(mcp_instance: FastMCP) -> None:
    """
    Register all text tools with the MCP server instance.

    Args:
        mcp_instance: The FastMCP instance to register tools with
    """

    @mcp_instance.tool("Uppercase Text")
    def to_uppercase(text: str) -> str:
        """
        Convert text to uppercase.

        Args:
            text: The input string

        Returns:
            The uppercased string
        """
        return text.upper()

    @mcp_instance.tool("Lowercase Text")
    def to_lowercase(text: str) -> str:
        """
        Convert text to lowercase.

        Args:
            text: The input string

        Returns:
            The lowercased string
        """
        return text.lower()

    @mcp_instance.tool("Reverse Text")
    def reverse_text(text: str) -> str:
        """
        Reverse a string.

        Args:
            text: The input string

        Returns:
            The reversed string
        """
        return text[::-1]

    @mcp_instance.tool("Count Words")
    def count_words(text: str) -> int:
        """
        Count the number of words in a string.

        Args:
            text: The input string

        Returns:
            The word count
        """
        return len(text.split())

    @mcp_instance.tool("Count Characters")
    def count_characters(text: str, include_spaces: bool = True) -> int:
        """
        Count the number of characters in a string.

        Args:
            text: The input string
            include_spaces: Whether to include whitespace in the count (default True)

        Returns:
            The character count
        """
        if include_spaces:
            return len(text)
        return len(text.replace(" ", ""))

    @mcp_instance.tool("Title Case")
    def to_title_case(text: str) -> str:
        """
        Convert text to title case.

        Args:
            text: The input string

        Returns:
            The title-cased string
        """
        return text.title()

    @mcp_instance.tool("Split Text")
    def split_text(text: str, delimiter: str = " ") -> List[str]:
        """
        Split text by a delimiter.

        Args:
            text: The input string
            delimiter: The delimiter to split on (default: single space)

        Returns:
            A list of substrings
        """
        return text.split(delimiter)

    @mcp_instance.tool("Replace Text")
    def replace_text(text: str, old: str, new: str) -> str:
        """
        Replace all occurrences of old with new in text.

        Args:
            text: The input string
            old: The substring to find
            new: The replacement substring

        Returns:
            The modified string
        """
        return text.replace(old, new)

    @mcp_instance.tool("Trim Text")
    def trim_text(text: str) -> str:
        """
        Remove leading and trailing whitespace from text.

        Args:
            text: The input string

        Returns:
            The trimmed string
        """
        return text.strip()

    @mcp_instance.tool("Extract Emails")
    def extract_emails(text: str) -> List[str]:
        """
        Extract all email addresses found in a block of text.

        Args:
            text: The input string to search

        Returns:
            A list of email addresses found in the text
        """
        pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
        return re.findall(pattern, text)
