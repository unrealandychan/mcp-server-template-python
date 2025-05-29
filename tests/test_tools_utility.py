"""
Tests for utility tools.
"""
import pytest
from unittest.mock import MagicMock, patch

from src.mcp_server.tools.utility import register_utility_tools


class TestUtilityTools:
    """Test cases for utility tools."""

    def setup_method(self):
        """Set up test environment before each test."""
        # Create a mock FastMCP instance with a tool decorator that captures functions
        self.mock_mcp = MagicMock()
        self.tools = {}

        # Create a custom decorator that captures the decorated function
        def tool_decorator(name):
            def decorator(func):
                self.tools[name] = func
                return func
            return decorator

        # Replace the mock's tool method with our decorator factory
        self.mock_mcp.tool = tool_decorator

        # Register the utility tools with the mock
        register_utility_tools(self.mock_mcp)

    def test_echo_tool(self):
        """Test the echo tool functionality."""
        # Find the echo function
        echo_func = None
        for name, func in self.tools.items():
            if name == "Echo Message":
                echo_func = func
                break

        # If we found the function, test it
        if echo_func:
            assert echo_func("hello") == "hello"
            assert echo_func("test message") == "test message"
        else:
            pytest.fail("Echo tool not registered correctly")

    def test_server_info_tool(self):
        """Test the server_info tool functionality."""
        # Find the server_info function
        server_info_func = None
        for name, func in self.tools.items():
            if name == "Get Server Info":
                server_info_func = func
                break

        # If we found the function, test it
        if server_info_func:
            result = server_info_func()
            assert isinstance(result, dict)
            assert "name" in result
            assert "version" in result
            assert "description" in result
            assert result["name"] == "MCP Server Template"
        else:
            pytest.fail("Server info tool not registered correctly")

    def test_ping_tool(self):
        """Test the ping tool functionality."""
        # Find the ping function
        ping_func = None
        for name, func in self.tools.items():
            if name == "Ping":
                ping_func = func
                break

        # If we found the function, test it
        if ping_func:
            assert ping_func() == "pong"
        else:
            pytest.fail("Ping tool not registered correctly")
