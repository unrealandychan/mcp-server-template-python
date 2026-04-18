"""
Math tools for the MCP server.

Provides basic arithmetic and mathematical helper tools for MCP clients.
"""
import math
from typing import Union

from fastmcp import FastMCP

Number = Union[int, float]


def register_math_tools(mcp_instance: FastMCP) -> None:
    """
    Register all math tools with the MCP server instance.

    Args:
        mcp_instance: The FastMCP instance to register tools with
    """

    @mcp_instance.tool("Add Numbers")
    def add(a: Number, b: Number) -> Number:
        """
        Add two numbers together.

        Args:
            a: First operand
            b: Second operand

        Returns:
            The sum of a and b
        """
        return a + b

    @mcp_instance.tool("Subtract Numbers")
    def subtract(a: Number, b: Number) -> Number:
        """
        Subtract b from a.

        Args:
            a: Minuend
            b: Subtrahend

        Returns:
            The result of a - b
        """
        return a - b

    @mcp_instance.tool("Multiply Numbers")
    def multiply(a: Number, b: Number) -> Number:
        """
        Multiply two numbers.

        Args:
            a: First factor
            b: Second factor

        Returns:
            The product of a and b
        """
        return a * b

    @mcp_instance.tool("Divide Numbers")
    def divide(a: Number, b: Number) -> float:
        """
        Divide a by b.

        Args:
            a: Dividend
            b: Divisor (must not be zero)

        Returns:
            The result of a / b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @mcp_instance.tool("Power")
    def power(base: Number, exponent: Number) -> Number:
        """
        Raise base to the power of exponent.

        Args:
            base: The base value
            exponent: The exponent value

        Returns:
            base raised to the power of exponent
        """
        return base**exponent

    @mcp_instance.tool("Square Root")
    def square_root(value: Number) -> float:
        """
        Calculate the square root of a non-negative number.

        Args:
            value: A non-negative number

        Returns:
            The square root of value

        Raises:
            ValueError: If value is negative
        """
        if value < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(value)

    @mcp_instance.tool("Factorial")
    def factorial(n: int) -> int:
        """
        Calculate the factorial of a non-negative integer.

        Args:
            n: A non-negative integer

        Returns:
            n! (n factorial)

        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative integers")
        return math.factorial(n)
