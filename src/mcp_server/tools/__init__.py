"""
Tools package for the MCP server.

Add your tool modules here and import their register functions in main.py.
"""

from mcp_server.tools.datetime_tools import register_datetime_tools
from mcp_server.tools.math_tools import register_math_tools
from mcp_server.tools.text_tools import register_text_tools
from mcp_server.tools.utility import register_utility_tools

__all__ = [
    "register_utility_tools",
    "register_math_tools",
    "register_text_tools",
    "register_datetime_tools",
]
