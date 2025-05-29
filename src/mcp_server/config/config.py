"""
Configuration handling for the MCP server.

This module provides centralized configuration management for the MCP server.
"""
import os
from typing import Dict, Any, Optional

from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()


class ServerConfig(BaseModel):
    """Server configuration model."""
    host: str = Field(default="0.0.0.0", description="Host to bind the server to")
    port: int = Field(default=8000, description="Port to bind the server to")
    debug: bool = Field(default=False, description="Enable debug mode")


class LoggingConfig(BaseModel):
    """Logging configuration model."""
    level: str = Field(default="INFO", description="Log level")
    format: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        description="Log format"
    )
    file_enabled: bool = Field(default=True, description="Enable logging to file")
    file_dir: str = Field(default="logs", description="Directory for log files")


class SecurityConfig(BaseModel):
    """Security configuration model."""
    api_key_enabled: bool = Field(default=False, description="Enable API key authentication")
    api_key: Optional[str] = Field(default=None, description="API key for authentication")
    cors_enabled: bool = Field(default=True, description="Enable CORS")
    cors_origins: list[str] = Field(default=["*"], description="Allowed CORS origins")


class AppConfig(BaseModel):
    """Main application configuration model."""
    app_name: str = Field(default="mcp_server", description="Application name")
    server: ServerConfig = Field(default_factory=ServerConfig, description="Server configuration")
    logging: LoggingConfig = Field(default_factory=LoggingConfig, description="Logging configuration")
    security: SecurityConfig = Field(default_factory=SecurityConfig, description="Security configuration")


def load_config() -> AppConfig:
    """
    Load configuration from environment variables.

    Returns:
        AppConfig: Application configuration
    """
    # Server configuration
    server_config = ServerConfig(
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
        debug=os.getenv("DEBUG", "").lower() == "true",
    )

    # Logging configuration
    logging_config = LoggingConfig(
        level=os.getenv("LOG_LEVEL", "INFO"),
        format=os.getenv("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
        file_enabled=os.getenv("LOG_FILE_ENABLED", "true").lower() == "true",
        file_dir=os.getenv("LOG_FILE_DIR", "logs"),
    )

    # Security configuration
    security_config = SecurityConfig(
        api_key_enabled=os.getenv("API_KEY_ENABLED", "").lower() == "true",
        api_key=os.getenv("API_KEY"),
        cors_enabled=os.getenv("CORS_ENABLED", "true").lower() == "true",
        cors_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    )

    # Main application configuration
    app_config = AppConfig(
        app_name=os.getenv("APP_NAME", "mcp_server"),
        server=server_config,
        logging=logging_config,
        security=security_config,
    )

    return app_config


# Create a global config instance
config = load_config()
