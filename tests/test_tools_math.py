"""
Tests for math tools.
"""
import math

import pytest

from mcp_server.tools.math_tools import register_math_tools


class TestMathTools:
    """Test cases for math tools."""

    def setup_method(self) -> None:
        """Set up a mock MCP instance and capture registered tools."""
        self.tools: dict = {}

        def tool_decorator(name: str):  # type: ignore[return]
            def decorator(func):  # type: ignore[return]
                self.tools[name] = func
                return func

            return decorator

        mock_mcp = type("MockMCP", (), {"tool": staticmethod(tool_decorator)})()
        register_math_tools(mock_mcp)

    def test_add(self) -> None:
        add = self.tools["Add Numbers"]
        assert add(2, 3) == 5
        assert add(0, 0) == 0
        assert add(-1, 1) == 0
        assert add(1.5, 2.5) == 4.0

    def test_subtract(self) -> None:
        subtract = self.tools["Subtract Numbers"]
        assert subtract(10, 3) == 7
        assert subtract(0, 5) == -5

    def test_multiply(self) -> None:
        multiply = self.tools["Multiply Numbers"]
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10

    def test_divide(self) -> None:
        divide = self.tools["Divide Numbers"]
        assert divide(10, 2) == 5.0
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self) -> None:
        divide = self.tools["Divide Numbers"]
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_power(self) -> None:
        power = self.tools["Power"]
        assert power(2, 10) == 1024
        assert power(3, 0) == 1

    def test_square_root(self) -> None:
        sqrt = self.tools["Square Root"]
        assert sqrt(4) == 2.0
        assert sqrt(0) == 0.0
        assert math.isclose(sqrt(2), math.sqrt(2))

    def test_square_root_negative(self) -> None:
        sqrt = self.tools["Square Root"]
        with pytest.raises(ValueError, match="negative"):
            sqrt(-1)

    def test_factorial(self) -> None:
        factorial = self.tools["Factorial"]
        assert factorial(0) == 1
        assert factorial(5) == 120
        assert factorial(10) == 3628800

    def test_factorial_negative(self) -> None:
        factorial = self.tools["Factorial"]
        with pytest.raises(ValueError, match="negative"):
            factorial(-3)
