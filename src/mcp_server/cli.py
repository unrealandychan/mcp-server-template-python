"""
Command-line interface for the MCP server.

This module provides a CLI for starting and managing the MCP server.
"""
import os
import sys

import typer
from dotenv import load_dotenv

from mcp_server.utils.logging import setup_logging

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
    transport: str = typer.Option(os.getenv("TRANSPORT", "streamable-http"), "--transport", "-t", help="Transport protocol (stdio, streamable-http, sse)"),
) -> None:
    """
    Start the MCP server with the specified configuration.
    """
    try:
        from mcp_server.main import mcp

        logger.info(f"Starting MCP server on {host}:{port} (transport={transport}, debug={debug})")
        logger.info(f"Log level set to {log_level}")

        if transport == "stdio":
            mcp.run(transport="stdio")
        else:
            mcp.run(transport=transport, host=host, port=port)
    except ImportError as exc:
        logger.error(f"Failed to import the MCP server module: {exc}")
        sys.exit(1)
    except Exception as exc:
        logger.error(f"Failed to start MCP server: {exc}")
        if debug:
            logger.exception("Detailed error:")
        sys.exit(1)


@app.command()
def version() -> None:
    """
    Display the current version of the MCP server.
    """
    from mcp_server import __version__

    typer.echo(f"MCP Server Template v{__version__}")


def main() -> None:
    """
    Main entry point for the CLI.
    """
    app()


if __name__ == "__main__":
    main()
