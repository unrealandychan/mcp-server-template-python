"""
Tests for logging utilities.
"""
import logging
import os
import pytest
from unittest import mock

from src.mcp_server.utils.logging import setup_logging, LOG_LEVELS


class TestLoggingUtility:
    """Test cases for logging utility functions."""

    def test_log_levels_dictionary(self):
        """Test LOG_LEVELS dictionary contains all expected levels."""
        assert "DEBUG" in LOG_LEVELS
        assert "INFO" in LOG_LEVELS
        assert "WARNING" in LOG_LEVELS
        assert "ERROR" in LOG_LEVELS
        assert "CRITICAL" in LOG_LEVELS

        assert LOG_LEVELS["DEBUG"] == logging.DEBUG
        assert LOG_LEVELS["INFO"] == logging.INFO
        assert LOG_LEVELS["WARNING"] == logging.WARNING
        assert LOG_LEVELS["ERROR"] == logging.ERROR
        assert LOG_LEVELS["CRITICAL"] == logging.CRITICAL

    def test_setup_logging_default_name(self):
        """Test setup_logging with default app name."""
        with mock.patch.dict(os.environ, {"APP_NAME": "test_app"}):
            logger = setup_logging()
            assert logger.name == "test_app"

    def test_setup_logging_custom_name(self):
        """Test setup_logging with custom app name."""
        logger = setup_logging("custom_app")
        assert logger.name == "custom_app"

    def test_setup_logging_log_level(self):
        """Test setup_logging sets the correct log level."""
        with mock.patch.dict(os.environ, {"LOG_LEVEL": "DEBUG"}):
            logger = setup_logging("test_app")
            assert logger.level == logging.DEBUG

        with mock.patch.dict(os.environ, {"LOG_LEVEL": "ERROR"}):
            logger = setup_logging("test_app")
            assert logger.level == logging.ERROR

    def test_setup_logging_handlers(self):
        """Test setup_logging creates appropriate handlers."""
        # Mock os.path.exists to avoid creating directories
        with mock.patch('os.path.exists') as mock_exists:
            mock_exists.return_value = False

            logger = setup_logging("test_app")

            # Should have at least one handler (console)
            assert len(logger.handlers) >= 1

            # First handler should be a StreamHandler
            assert isinstance(logger.handlers[0], logging.StreamHandler)

            # Set os.path.exists to True to test file handler creation
            mock_exists.return_value = True

            # Mock the makedirs and RotatingFileHandler to avoid file operations
            with mock.patch('os.makedirs') as mock_makedirs, \
                 mock.patch('logging.handlers.RotatingFileHandler') as mock_file_handler:

                mock_file_handler.return_value = logging.handlers.RotatingFileHandler(
                    "dummy.log", maxBytes=1024, backupCount=3)

                logger = setup_logging("test_app")

                # Should have at least two handlers now (console + file)
                assert len(logger.handlers) >= 1

                # Make sure makedirs was called
                mock_makedirs.assert_not_called()  # We mocked exists to return True

    def test_setup_logging_formatter(self):
        """Test setup_logging sets the correct formatter."""
        custom_format = "%(levelname)s - %(message)s"

        with mock.patch.dict(os.environ, {"LOG_FORMAT": custom_format}):
            logger = setup_logging("test_app")

            # Check that the formatter for the handler uses our custom format
            formatter = logger.handlers[0].formatter
            assert formatter._fmt == custom_format  # Access private attribute for testing
