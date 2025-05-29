"""
General utility tools for the MCP server.

This module contains general utility tools that can be used by MCP clients.
"""
from typing import Dict, Any

from mcp.server import FastMCP


def register_utility_tools(mcp_instance: FastMCP):
    """
    Register all utility tools with the MCP server instance.

    Args:
        mcp_instance: The FastMCP instance to register tools with
    """

    @mcp_instance.tool("Echo Message")
    def echo(message: str) -> str:
        """
        Echo back the received message.

        Args:
            message: The message to echo back

        Returns:
            The same message that was received
        """
        return message

    @mcp_instance.tool("Get Server Info")
    def server_info() -> Dict[str, Any]:
        """
        Get information about the MCP server.

        Returns:
            Dictionary with server information
        """
        return {
            "name": "MCP Server Template",
            "version": "0.1.0",
            "description": "A starter template for building MCP servers in Python"
        }

    @mcp_instance.tool("Ping")
    def ping() -> str:
        """
        Simple ping tool to check if the server is responsive.

        Returns:
            "pong" message
        """
        return "pong"
