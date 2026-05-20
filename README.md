# Binary to Intel HEX Converter

Convert binary instructions to Intel `.hex` format files for initializing ROM components.

## Overview

This tool takes binary instruction data and outputs `.hex` files compatible with the Intel HEX format — ready to use for ROM initialization in digital circuit simulators and similar environments.

**Tested with:** [Digital](https://github.com/hneemann/digital) — an open-source digital logic simulator.

## Getting Started

An example is included in the `.py` file to help you get up and running quickly.

## Usage

### Option 1 — Google Colab (No installation required)

Run the script entirely in your browser — no local Python setup needed.

1. Open [Google Colab](https://colab.new/)
2. Copy the contents of the `.py` file into a new notebook cell
3. Modify the binary input to match your instructions
4. Run the cell — your Intel `.hex` file will be generated

---

### Option 2 — Run Locally

If you have Python installed on your machine:

**Requirements:**
- Python 3.x — download from [python.org](https://www.python.org/downloads/)

**Steps:**
1. Clone or download this repository
2. Open a terminal in the project folder
3. Run the script:
   ```bash
   python converter.py
   ```
4. The output `.hex` file will be saved in the same directory

> **Note:** No third-party libraries are required — the script uses Python's standard library only.
