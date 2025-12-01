# 🌿 Leaf Stitching Tool

This tool takes overlapping microscopy images of leaf segments and stitches them into a single high-resolution montage.

---

## 📦 Prerequisites

- **Python 3.6+** installed on your system  
- A folder named **`leaf_segments`** containing your images (`.jpg`, `.png`, `.tif`) located in the same directory as the script

---

## 🔧 Installation & Setup

Follow the steps below for your operating system to set up the environment and run the tool.

---

## 🪟 Windows Setup

1. Open **Command Prompt** or **PowerShell** and navigate to the project folder.
2. Install `virtualenv`:

   ```bash
   pip install virtualenv
   ```

   ```bash
   pip install virtualenv
   ```
3. Create a virtual environment:

   ```bash
   virtualenv venv
   ```
4. Activate the virtual environment:

   ```bash
   .\venv\Scripts\activate
   ```
   You should see `(venv)` appear at the start of your command line.

5. Install requirements:

   ```bash
   pip install opencv-python
   ```

---

## 🐧 Linux / 🍏 macOS Setup

1. Open **Terminal** and navigate to the project folder.
2. Install `virtualenv`:

   ```bash
   pip install virtualenv
   ```
   > **Note:** On some Linux distributions, you may need to use `pip3` or install `virtualenv` via the system package manager (e.g., `sudo apt install python3-virtualenv`).

3. Create a virtual environment:

   ```bash
   virtualenv venv
   ```
4. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```
   You should see `(venv)` appear at the start of your command line.

5. Install requirements:

   ```bash
   pip install opencv-python
   ```

---

## ▶️ Usage

1. Place your overlapping leaf images inside the `leaf_segments` folder. For an example of how to structure your input data, refer to the `example` directory.
2. Run the script from your activated virtual environment:

   ```bash
   python leaf_stitcher.py
   ```
3. On success, the output will be saved as `full_leaf_montage.jpg`.
