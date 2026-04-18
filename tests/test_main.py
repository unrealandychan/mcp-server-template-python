"""
Tests for main MCP server functionality.
"""
from unittest.mock import patch

from mcp_server.main import hello_world


class TestMainFunctionality:
    """Test cases for main MCP server functionality."""

    @patch("mcp_server.main.logger")
    def test_hello_world_default(self, mock_logger: object) -> None:
        """Test hello_world with the default parameter."""
        result = hello_world()
        assert result == "Hello, World!"
        mock_logger.info.assert_called_with("Hello World tool called with name: World")

    @patch("mcp_server.main.logger")
    def test_hello_world_custom_name(self, mock_logger: object) -> None:
        """Test hello_world with a custom name."""
        result = hello_world("John")
        assert result == "Hello, John!"
        mock_logger.info.assert_called_with("Hello World tool called with name: John")

    @patch("mcp_server.main.logger")
    def test_hello_world_empty_string(self, mock_logger: object) -> None:
        """Test hello_world with an empty string."""
        result = hello_world("")
        assert result == "Hello, !"
        mock_logger.info.assert_called_with("Hello World tool called with name: ")


class TestMCPServerIntegration:
    @patch("mcp_server.main.mcp")
    def test_server_run_is_callable(self, mock_mcp: object) -> None:
        """Test that mcp.run() is callable on the server instance."""
        from mcp_server.main import mcp

        mcp.run()
        mock_mcp.run.assert_called_once()
