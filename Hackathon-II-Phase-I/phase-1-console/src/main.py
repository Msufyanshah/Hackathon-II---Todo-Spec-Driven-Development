"""
Main module for the Phase I Console Todo Application.
"""
from cli import TodoCLI

def main():
    """
    Main entry point for the application.
    """
    app = TodoCLI()
    app.run()

if __name__ == "__main__":
    main()