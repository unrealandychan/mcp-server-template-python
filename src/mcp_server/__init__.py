"""
MCP Server Template for Python
"""

from mcp_server.config.config import AppConfig, load_config
from mcp_server.utils.logging import setup_logging

__version__ = "0.1.0"
__all__ = ["__version__", "load_config", "AppConfig", "setup_logging"]
