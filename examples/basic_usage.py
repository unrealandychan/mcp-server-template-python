"""
Example: basic usage of the MCP Server Template.

This script shows the minimal setup needed to start the MCP server
programmatically with the default (HTTP) transport.

Run from the repository root:
    python examples/basic_usage.py
"""
from mcp_server.main import mcp

if __name__ == "__main__":
    # Start with streamable-HTTP transport on 0.0.0.0:8000
    mcp.run(transport="streamable-http")

