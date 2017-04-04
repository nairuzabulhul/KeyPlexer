from cx_Freeze import setup, Executable



buildOptions = dict(
    includes=[],
    packages=['email']
)

setup( name = "KeyPlexer" , version = "0.1" , description = "" ,
        options = dict(build_exe = buildOptions),
        executables = [Executable("KeyPlexer.py",base = "Win32GUI")] , )
