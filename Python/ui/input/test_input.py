import sys
import os

# Add parent directory to path so imports work correctly
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame
pygame.init()

from input import VirtualInput
import string


def test_initialization():
    """Test default and custom initialization."""
    # Default
    vi = VirtualInput()
    assert vi.message == ""
    assert vi.hidden == False
    assert vi.current_string == ""
    assert vi._cursor == 0
    print("  Default initialization: OK")

    # Custom
    vi = VirtualInput(message="Name:", password=True, value="test")
    assert vi.message == "Name:"
    assert vi.hidden == True
    assert vi.current_string == "test"
    print("  Custom initialization: OK")


def test_text_properties():
    """Test text getter/setter properties."""
    vi = VirtualInput(value="hello")

    assert vi.current_text == "hello"
    assert vi.text == "hello"

    vi.text = "world"
    assert vi.current_string == "world"
    print("  Text properties: OK")


def test_cursor_movement():
    """Test cursor movement methods."""
    vi = VirtualInput(value="hello world")
    vi._cursor = 5

    vi.move_in_string(3)
    assert vi._cursor == 8

    vi.move_in_string(-5)
    assert vi._cursor == 3

    # Test clamping
    vi.move_in_string(-100)
    assert vi._cursor == 0

    vi.move_in_string(100)
    assert vi._cursor == 11
    print("  Cursor movement: OK")


def test_get_character():
    """Test getting character at cursor position."""
    vi = VirtualInput(value="hello")

    vi._cursor = 0
    assert vi.get_character() == "h"

    vi._cursor = 2
    assert vi.get_character() == "l"

    vi._cursor = 5  # End of string
    assert vi.get_character() == ""
    print("  Get character: OK")


def test_insert_character():
    """Test character insertion."""
    vi = VirtualInput()
    vi.current_string = "hllo"
    vi._cursor = 1
    vi.insert_character("e")
    assert vi.current_string == "hello"
    assert vi._cursor == 2

    # Insert at end
    vi.current_string = "hell"
    vi._cursor = 4
    vi.insert_character("o")
    assert vi.current_string == "hello"
    assert vi._cursor == 5
    print("  Insert character: OK")


def test_remove_character():
    """Test character removal."""
    vi = VirtualInput()
    vi.current_string = "heello"
    vi._cursor = 3
    vi.remove_character()
    assert vi.current_string == "hello"
    assert vi._cursor == 2

    # Remove at start does nothing
    vi._cursor = 0
    vi.remove_character()
    assert vi.current_string == "hello"
    print("  Remove character: OK")


def test_clear():
    """Test clearing input."""
    vi = VirtualInput(value="hello")
    vi._cursor = 3
    vi.clear()
    assert vi.current_string == ""
    assert vi._cursor == 0
    print("  Clear: OK")


def test_whitelist_toggles():
    """Test whitelist toggle methods."""
    vi = VirtualInput()

    vi.toggle_input_to_letters()
    assert set(vi.whitelisted_characters) == set(string.ascii_letters)

    vi.toggle_input_to_digits()
    assert set(vi.whitelisted_characters) == set(string.digits)

    vi.toggle_input_to_digits(negative=True, decimal=True)
    assert "-" in vi.whitelisted_characters
    assert "." in vi.whitelisted_characters

    vi.toggle_input_to_custom("abc123")
    assert vi.whitelisted_characters == ['a', 'b', 'c', '1', '2', '3']
    print("  Whitelist toggles: OK")


def test_character_limit():
    """Test character limit property."""
    vi = VirtualInput(value="hello")

    vi.maximum_message_length = -1
    assert vi.is_at_character_limit == False

    vi.maximum_message_length = 10
    assert vi.is_at_character_limit == False

    vi.maximum_message_length = 5
    assert vi.is_at_character_limit == True
    print("  Character limit: OK")


def test_speak_word():
    """Test speak_word helper."""
    vi = VirtualInput(value="hello world test")

    assert vi.speak_word(0) == "hello"
    assert vi.speak_word(6) == "world"
    assert vi.speak_word(12) == "test"
    print("  Speak word: OK")


def test_speak_line():
    """Test speak_line helper."""
    vi = VirtualInput()
    vi.current_string = "line1\nline2\nline3"

    assert vi.speak_line(0) == "line1"
    assert vi.speak_line(6) == "line2"
    assert vi.speak_line(12) == "line3"
    print("  Speak line: OK")


def run_all_tests():
    """Run all tests."""
    print("Running VirtualInput tests...\n")

    tests = [
        ("Initialization", test_initialization),
        ("Text Properties", test_text_properties),
        ("Cursor Movement", test_cursor_movement),
        ("Get Character", test_get_character),
        ("Insert Character", test_insert_character),
        ("Remove Character", test_remove_character),
        ("Clear", test_clear),
        ("Whitelist Toggles", test_whitelist_toggles),
        ("Character Limit", test_character_limit),
        ("Speak Word", test_speak_word),
        ("Speak Line", test_speak_line),
    ]

    passed = 0
    failed = 0

    for name, test_func in tests:
        try:
            print(f"Testing {name}...")
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"  FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            failed += 1

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    print(f"{'='*40}")


if __name__ == "__main__":
    run_all_tests()
