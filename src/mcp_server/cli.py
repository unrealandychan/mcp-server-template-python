"""
Command-line interface for the MCP server.

This module provides a CLI for starting and managing the MCP server.
"""
import os
import sys

import typer
from dotenv import load_dotenv

from src.mcp_server.utils.logging import setup_logging

# Load environment variables
load_dotenv()

# Create Typer app
app = typer.Typer(
    name="mcp-server",
    help="MCP Server CLI",
    add_completion=False,
)

# Configure logger
logger = setup_logging()


@app.command()
def start(
    host: str = typer.Option(os.getenv("HOST", "0.0.0.0"), "--host", "-h", help="Host to bind the server to"),
    port: int = typer.Option(int(os.getenv("PORT", "8000")), "--port", "-p", help="Port to bind the server to"),
    debug: bool = typer.Option(os.getenv("DEBUG", "").lower() == "true", "--debug", "-d", help="Enable debug mode"),
    log_level: str = typer.Option(os.getenv("LOG_LEVEL", "INFO"), "--log-level", "-l", help="Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)"),
):
    """
    Start the MCP server with the specified configuration.
    """
    try:
        # Dynamically import the MCP server to prevent circular imports
        from src.mcp_server.main import mcp

        # Apply CLI configuration
        logger.info(f"Starting MCP server on {host}:{port} with debug={debug}")
        logger.info(f"Log level set to {log_level}")

        # Start the MCP server
        mcp.start(host=host, port=port)
    except ImportError:
        logger.error("Failed to import the MCP server. Make sure the main module is correctly set up.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Failed to start MCP server: {e}")
        if debug:
            logger.exception("Detailed error:")
        sys.exit(1)


@app.command()
def version():
    """
    Display the version of the MCP server.
    """
    from src.mcp_server import __version__
    typer.echo(f"MCP Server Template v{__version__}")


def main():
    """
    Main entry point for the CLI.
    """
    app()


if __name__ == "__main__":
    main()
