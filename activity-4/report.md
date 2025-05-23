### Mutation Testing Report for is_leap_year(year)

**Original Function:**
Standard leap year check based on divisibility by 4, 100, and 400.

**Test Cases Used:**
[2019, 2024, 2000, 1900, 2100, 2400, 2023, 1996]

**Mutants Introduced:**

| Mutant | Description                     | Fault Introduced                     |
|--------|----------------------------------|---------------------------------------|
| M1     | Changed `year % 4 == 0` to `!=` | Reverses leap year base condition     |
| M2     | Changed `year % 100 == 0` to `!=`| Breaks century year check             |
| M3     | Changed `year % 400 == 0` to `!=`| Breaks 400-year leap condition        |
| M4     | Replaced body with `return True`| Ignores leap year logic               |

**Mutation Results:**

| Mutant | Killed By Test Case(s)  | Status   |
|--------|--------------------------|----------|
| M1     | 2024, 1996, 2023         | Killed   |
| M2     | 1900, 2100               | Killed   |
| M3     | 2000, 2400               | Killed   |
| M4     | 2019, 1900, 2100, 2023   | Killed   |

**Mutation Score: 100%**

All mutants were successfully detected and killed by the test suite.
