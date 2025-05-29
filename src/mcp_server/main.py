from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os

load_dotenv()
mcp = FastMCP(os.getenv("APP_NAME", "mcp_server"),)

@mcp.tool("Hello World")
def hello_world(name: str = "World") -> str:
    """
    Returns a greeting message.

    Args:
        name (str): The name to greet. Defaults to "World".

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"
