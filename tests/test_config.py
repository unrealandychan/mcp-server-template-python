"""
Tests for configuration module.
"""
import os
import pytest
from unittest import mock

from src.mcp_server.config.config import (
    ServerConfig,
    LoggingConfig,
    SecurityConfig,
    AppConfig,
    load_config
)


class TestConfigModels:
    """Test cases for configuration models."""

    def test_server_config_defaults(self):
        """Test ServerConfig default values."""
        config = ServerConfig()
        assert config.host == "0.0.0.0"
        assert config.port == 8000
        assert config.debug is False

    def test_server_config_custom_values(self):
        """Test ServerConfig with custom values."""
        config = ServerConfig(host="127.0.0.1", port=9000, debug=True)
        assert config.host == "127.0.0.1"
        assert config.port == 9000
        assert config.debug is True

    def test_logging_config_defaults(self):
        """Test LoggingConfig default values."""
        config = LoggingConfig()
        assert config.level == "INFO"
        assert "%(asctime)s" in config.format
        assert config.file_enabled is True
        assert config.file_dir == "logs"

    def test_security_config_defaults(self):
        """Test SecurityConfig default values."""
        config = SecurityConfig()
        assert config.api_key_enabled is False
        assert config.api_key is None
        assert config.cors_enabled is True
        assert config.cors_origins == ["*"]

    def test_app_config_defaults(self):
        """Test AppConfig default values."""
        config = AppConfig()
        assert config.app_name == "mcp_server"
        assert isinstance(config.server, ServerConfig)
        assert isinstance(config.logging, LoggingConfig)
        assert isinstance(config.security, SecurityConfig)


class TestLoadConfig:
    """Test cases for load_config function."""

    @mock.patch.dict(os.environ, {
        "APP_NAME": "test_app",
        "HOST": "127.0.0.1",
        "PORT": "9000",
        "DEBUG": "true",
        "LOG_LEVEL": "DEBUG",
        "API_KEY_ENABLED": "true",
        "API_KEY": "test_key",
        "CORS_ORIGINS": "origin1.com,origin2.com"
    })
    def test_load_config_from_env(self):
        """Test loading configuration from environment variables."""
        config = load_config()

        # Check all configuration values
        assert config.app_name == "test_app"
        assert config.server.host == "127.0.0.1"
        assert config.server.port == 9000
        assert config.server.debug is True
        assert config.logging.level == "DEBUG"
        assert config.security.api_key_enabled is True
        assert config.security.api_key == "test_key"
        assert "origin1.com" in config.security.cors_origins
        assert "origin2.com" in config.security.cors_origins

    def test_load_config_with_defaults(self):
        """Test loading configuration with default values when env vars are not set."""
        # Use a context manager to temporarily clear any environment variables that might affect the test
        with mock.patch.dict(os.environ, {}, clear=True):
            config = load_config()

            # Check that default values are used
            assert config.app_name == "mcp_server"
            assert config.server.host == "0.0.0.0"
            assert config.server.port == 8000
            assert config.server.debug is False
            assert config.logging.level == "INFO"
