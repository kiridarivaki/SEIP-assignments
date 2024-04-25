import pytest
import sys
from io import StringIO
from argparse import ArgumentParser
from src.main.python.main import *  # Adjust the import path to your script

# Test for main function to verify correct parsing of arguments and initial outputs
def test_main_initial_output(monkeypatch, capsys):
    # Simulate user input and arguments
    user_inputs = iter([
        "create_list",  # Command chosen
        "G",            # List type (goal)
        "My First Goal", # List name
        "2024-12-31",   # Goal date
    ])
    
    monkeypatch.setattr('builtins.input', lambda _: next(user_inputs))
    monkeypatch.setattr(sys, 'argv', ['skillsync', '--help'])  # Simulate script run with --help
    
    main()  # Run the main function
    
    # Capture output to check expected output
    captured = capsys.readouterr()
    
    # Check if expected output contains specific text
    assert "Welcome to SkillSync!" in captured.out
    assert "create_list" in captured.out  # Check if command is listed
    assert "Creating skills list" in captured.out  # Check if list creation message is displayed

# Test for invalid command input
def test_invalid_command(monkeypatch, capsys):
    # Simulate invalid command input
    user_inputs = iter([
        "invalid_command",  # Invalid command
        "quit",  # Quits after invalid input
    ])
    
    monkeypatch.setattr('builtins.input', lambda _: next(user_inputs))
    
    main()  # Run the main function
    
    captured = capsys.readouterr()
    
    # Check if user is prompted for a valid command
    assert "Please enter a valid command" in captured.out
    assert "See you soon!" in captured.out  # Ensure exit message is displayed
