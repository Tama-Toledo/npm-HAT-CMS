#!/bin/bash

set -e

VENV_DIR=".venv"
REQUIREMENTS_FILE="python-requirements.txt"

if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

if [ ! -f "$VENV_DIR/.requirements_installed" ] || [ "$REQUIREMENTS_FILE" -nt "$VENV_DIR/.requirements_installed" ]; then
  python -m pip install --upgrade pip
  python -m pip install -r "$REQUIREMENTS_FILE"
  touch "$VENV_DIR/.requirements_installed"
fi

python main.py