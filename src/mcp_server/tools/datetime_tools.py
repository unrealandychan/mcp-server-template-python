"""
Datetime tools for the MCP server.

Provides date and time utilities for MCP clients.
"""
from datetime import date, datetime, timedelta, timezone
from typing import Optional
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from fastmcp import FastMCP


def register_datetime_tools(mcp_instance: FastMCP) -> None:
    """
    Register all datetime tools with the MCP server instance.

    Args:
        mcp_instance: The FastMCP instance to register tools with
    """

    @mcp_instance.tool("Current UTC Time")
    def current_utc_time() -> str:
        """
        Return the current UTC date and time in ISO 8601 format.

        Returns:
            Current UTC datetime as an ISO 8601 string
        """
        return datetime.now(tz=timezone.utc).isoformat()

    @mcp_instance.tool("Current Date")
    def current_date() -> str:
        """
        Return today's date (UTC) in ISO 8601 format (YYYY-MM-DD).

        Returns:
            Today's date as a string
        """
        return date.today().isoformat()

    @mcp_instance.tool("Time In Timezone")
    def time_in_timezone(tz_name: str) -> str:
        """
        Return the current date and time in the specified timezone.

        Args:
            tz_name: IANA timezone name, e.g. "America/New_York" or "Europe/London"

        Returns:
            Current datetime in the given timezone as an ISO 8601 string

        Raises:
            ValueError: If the timezone name is not recognised
        """
        try:
            tz = ZoneInfo(tz_name)
        except ZoneInfoNotFoundError:
            raise ValueError(f"Unknown timezone: '{tz_name}'. Use an IANA timezone name.")
        return datetime.now(tz=tz).isoformat()

    @mcp_instance.tool("Add Days To Date")
    def add_days_to_date(date_str: str, days: int) -> str:
        """
        Add (or subtract) a number of days to/from a date.

        Args:
            date_str: A date string in ISO 8601 format (YYYY-MM-DD)
            days: Number of days to add; use a negative value to subtract

        Returns:
            The resulting date as an ISO 8601 string

        Raises:
            ValueError: If date_str cannot be parsed
        """
        try:
            parsed = date.fromisoformat(date_str)
        except ValueError:
            raise ValueError(f"Invalid date format: '{date_str}'. Expected YYYY-MM-DD.")
        return (parsed + timedelta(days=days)).isoformat()

    @mcp_instance.tool("Days Between Dates")
    def days_between_dates(start_date: str, end_date: str) -> int:
        """
        Calculate the number of days between two dates.

        Args:
            start_date: Start date in ISO 8601 format (YYYY-MM-DD)
            end_date: End date in ISO 8601 format (YYYY-MM-DD)

        Returns:
            Number of days from start_date to end_date (can be negative)

        Raises:
            ValueError: If either date string cannot be parsed
        """
        try:
            start = date.fromisoformat(start_date)
            end = date.fromisoformat(end_date)
        except ValueError as exc:
            raise ValueError(f"Invalid date format. Expected YYYY-MM-DD. Detail: {exc}")
        return (end - start).days

    @mcp_instance.tool("Format Datetime")
    def format_datetime(datetime_str: str, fmt: Optional[str] = "%B %d, %Y %H:%M:%S") -> str:
        """
        Re-format an ISO 8601 datetime string using a strftime-style format.

        Args:
            datetime_str: An ISO 8601 datetime string
            fmt: A strftime format string (default: "%B %d, %Y %H:%M:%S")

        Returns:
            The formatted datetime string

        Raises:
            ValueError: If datetime_str cannot be parsed
        """
        fmt = fmt or "%B %d, %Y %H:%M:%S"
        try:
            parsed = datetime.fromisoformat(datetime_str)
        except ValueError:
            raise ValueError(f"Invalid datetime format: '{datetime_str}'. Expected ISO 8601.")
        return parsed.strftime(fmt)
