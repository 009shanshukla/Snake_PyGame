import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:/Python36/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = "C:/Python36/tcl/tk8.6"

executables = [cx_Freeze.Executable("init.py")]
cx_Freeze.setup(
    name = "Snake Py_Game",
    options = {"build_exe":{"packages":["pygame"],"include_files":["snakeHead.jpg","apple1.jpg","Body.jpg"]}},
    description = "Snake Py_Game Tut",
    executables = executables

    )
