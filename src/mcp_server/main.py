"""
Main entry point for the MCP server application.
"""
import os
from dotenv import load_dotenv
from fastmcp import FastMCP

# Import utility modules
from src.mcp_server.utils.logging import setup_logging
from src.mcp_server.tools.utility import register_utility_tools

# Load environment variables
load_dotenv()

# Configure logging
logger = setup_logging()

# Initialize MCP server
app_name = os.getenv("APP_NAME", "mcp_server")
mcp = FastMCP(app_name,
    log_level = "DEBUG",
    )

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

# # Register all utility tools
register_utility_tools(mcp)

# Log server initialization
logger.info(f"MCP server '{app_name}' initialized and ready to start")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")

