import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CalculatorTest {

    Calculator calc = new Calculator();

    @Test
    public void testAdd() {
        assertEquals(7, calc.add(3, 4), "3 + 4 should equal 7");
    }
    
    @Test
    public void testAddWithAssertTrue() {
        assertTrue(calc.add(3, 4) == 7, "3 + 4 should equal 7");
    }

    @Test
    public void testSubtract() {
        assertEquals(5, calc.subtract(10, 5), "10 - 5 should equal 5");
    }

    @Test
    public void testSubtractWithAssertTrue() {
        assertTrue(calc.subtract(10, 5) == 5, "10 - 5 should equal 5");
    }

    @Test
    public void testMultiply() {
        assertEquals(20, calc.multiply(4, 5), "4 * 5 should equal 20");
    }

    @Test
    public void testMultiplyWithAssertTrue() {
        assertTrue(calc.multiply(4, 5) == 20, "4 * 5 should equal 20");
    }

    @Test
    public void testDivide() {
        assertEquals(2.5, calc.divide(5, 2), 0.0001, "5 / 2 should equal 2.5");
    }

    @Test
    public void testDivideWithAssertTrue() {
        assertTrue(Math.abs(calc.divide(5, 2) - 2.5) < 0.0001, "5 / 2 should equal 2.5");
    }

    @Test
    public void testDivideByZero() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            calc.divide(5, 0);
        });
        assertEquals("Cannot divide by zero.", exception.getMessage());
    }
}
