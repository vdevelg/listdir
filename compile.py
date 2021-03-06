def compile(source, tool="cx_Freeze"):
    if tool == "cx_Freeze":
        from cx_Freeze import setup, Executable
        options = {"build.exe" : {"includes" : ["os"]}}
        setup(
            name = "ListDir",
            version = "1.0",
            description = "Console utility",
            options = options,
            executables = [Executable("{0}".format(source))]
            )
    elif tool == "PyInstaller":
        import subprocess
        callstring = "pyinstaller {0} -F".format(source)
        subprocess.Popen(callstring, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

source = "listdir.py"
tool = "PyInstaller" # PyInstaller or cx_Freeze

compile(source, tool)
