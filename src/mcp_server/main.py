"""
Main entry point for the MCP server application.
"""
import os

from dotenv import load_dotenv
from fastmcp import FastMCP

from mcp_server.tools.datetime_tools import register_datetime_tools
from mcp_server.tools.math_tools import register_math_tools
from mcp_server.tools.text_tools import register_text_tools
from mcp_server.tools.utility import register_utility_tools
from mcp_server.utils.logging import setup_logging

# Load environment variables
load_dotenv()

# Configure logging
logger = setup_logging()

# Initialize MCP server
app_name = os.getenv("APP_NAME", "mcp_server")
mcp = FastMCP(app_name)

# Register the hello_world tool
@mcp.tool("hello-world")
def hello_world(name: str = "World") -> str:
    """
    Returns a greeting message.

    Args:
        name (str): The name to greet. Defaults to "World".

    Returns:
        str: A greeting message.
    """
    logger.info(f"Hello World tool called with name: {name}")
    return f"Hello, {name}!"


# Register all tool modules
register_utility_tools(mcp)
register_math_tools(mcp)
register_text_tools(mcp)
register_datetime_tools(mcp)

# Log server initialization
logger.info(f"MCP server '{app_name}' initialized and ready to start")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")

