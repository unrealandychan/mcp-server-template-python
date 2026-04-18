"""
General utility tools for the MCP server.

This module contains general-purpose utility tools that MCP clients can invoke.
"""
from typing import Any, Dict

from fastmcp import FastMCP

from mcp_server import __version__


def register_utility_tools(mcp_instance: FastMCP) -> None:
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
            Dictionary with server name, version and description
        """
        return {
            "name": "MCP Server Template",
            "version": __version__,
            "description": "A production-ready starter template for building MCP servers in Python",
        }

    @mcp_instance.tool("Ping")
    def ping() -> str:
        """
        Simple ping tool to check whether the server is responsive.

        Returns:
            "pong" message
        """
        return "pong"
