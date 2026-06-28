"""
Tiny test helper used by every exercise file.

Usage at the bottom of an exercise file:

    from testkit import check, report

    check("empty input", my_func([]), [])
    check("basic case", my_func([1, 2, 2]), [2])
    report()

Run the file directly:  python warmup/contains_duplicate.py
"""
_PASSED = 0
_FAILED = 0


def check(name, got, expected):
    """Compare `got` to `expected` and print a readable line."""
    global _PASSED, _FAILED
    if got == expected:
        _PASSED += 1
        print(f"  PASS  {name}")
    else:
        _FAILED += 1
        print(f"  FAIL  {name}")
        print(f"        expected: {expected!r}")
        print(f"        got:      {got!r}")


def report():
    """Print a summary line. Call once at the end of a file."""
    total = _PASSED + _FAILED
    print("-" * 40)
    if _FAILED == 0:
        print(f"All {total} tests passed.")
    else:
        print(f"{_PASSED}/{total} passed, {_FAILED} failed.")
    print()
