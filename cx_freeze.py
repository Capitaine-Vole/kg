from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "kg.py",
    version = "1",
    description = "je ne dirais rien O_o",
    executables = [Executable("thekg.py")],
)