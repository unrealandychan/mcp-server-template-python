"""
Tests for datetime tools.
"""
from datetime import date, datetime, timezone

import pytest

from mcp_server.tools.datetime_tools import register_datetime_tools


class TestDatetimeTools:
    """Test cases for datetime tools."""

    def setup_method(self) -> None:
        """Set up a mock MCP instance and capture registered tools."""
        self.tools: dict = {}

        def tool_decorator(name: str):  # type: ignore[return]
            def decorator(func):  # type: ignore[return]
                self.tools[name] = func
                return func

            return decorator

        mock_mcp = type("MockMCP", (), {"tool": staticmethod(tool_decorator)})()
        register_datetime_tools(mock_mcp)

    def test_current_utc_time_is_iso(self) -> None:
        fn = self.tools["Current UTC Time"]
        result = fn()
        # Should parse as a valid ISO 8601 datetime
        parsed = datetime.fromisoformat(result)
        assert parsed.tzinfo is not None

    def test_current_date_format(self) -> None:
        fn = self.tools["Current Date"]
        result = fn()
        # Should parse as a valid ISO 8601 date
        parsed = date.fromisoformat(result)
        assert isinstance(parsed, date)

    def test_time_in_timezone_valid(self) -> None:
        fn = self.tools["Time In Timezone"]
        result = fn("UTC")
        parsed = datetime.fromisoformat(result)
        assert parsed.tzinfo is not None

    def test_time_in_timezone_invalid(self) -> None:
        fn = self.tools["Time In Timezone"]
        with pytest.raises(ValueError, match="Unknown timezone"):
            fn("Invalid/Timezone")

    def test_add_days_to_date(self) -> None:
        fn = self.tools["Add Days To Date"]
        assert fn("2024-01-01", 10) == "2024-01-11"
        assert fn("2024-01-31", 1) == "2024-02-01"
        assert fn("2024-03-01", -1) == "2024-02-29"  # 2024 is a leap year

    def test_add_days_to_date_invalid(self) -> None:
        fn = self.tools["Add Days To Date"]
        with pytest.raises(ValueError, match="Invalid date format"):
            fn("not-a-date", 5)

    def test_days_between_dates(self) -> None:
        fn = self.tools["Days Between Dates"]
        assert fn("2024-01-01", "2024-01-11") == 10
        assert fn("2024-01-11", "2024-01-01") == -10

    def test_days_between_dates_same(self) -> None:
        fn = self.tools["Days Between Dates"]
        assert fn("2024-06-15", "2024-06-15") == 0

    def test_days_between_dates_invalid(self) -> None:
        fn = self.tools["Days Between Dates"]
        with pytest.raises(ValueError):
            fn("bad-date", "2024-01-01")

    def test_format_datetime(self) -> None:
        fn = self.tools["Format Datetime"]
        result = fn("2024-07-04T12:30:00", "%Y/%m/%d")
        assert result == "2024/07/04"

    def test_format_datetime_default_format(self) -> None:
        fn = self.tools["Format Datetime"]
        result = fn("2024-07-04T12:30:00")
        assert "2024" in result
        assert "July" in result or "07" in result

    def test_format_datetime_invalid(self) -> None:
        fn = self.tools["Format Datetime"]
        with pytest.raises(ValueError, match="Invalid datetime format"):
            fn("not-a-datetime")
