from calculator import square
import os
os.system("cls")  # Limpiar la consola (en Windows)

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(0) == 0
    assert square(-2) == 4
    assert square(-3) == 9

# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("Test failed: square(2) should be 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("Test failed: square(3) should be 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("Test failed: square(0) should be 0")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("Test failed: square(-2) should be 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("Test failed: square(-3) should be 9")

# if __name__ == "__main__":
#     main()