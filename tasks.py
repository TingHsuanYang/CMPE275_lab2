""" Task definitions for invoke command line utility for python bindings
    overview article.
"""
import cffi
import invoke
import pathlib
import sys
import os
import shutil
import re
import glob

on_win = sys.platform.startswith("win")


@invoke.task
def clean(c):
    """Remove any built objects"""
    for file_pattern in (
        "*.o",
        "*.so",
        "*.obj",
        "*.dll",
        "*.exp",
        "*.lib",
        "*.pyd",
        "cffi_example*",  # Is this a dir?
        "cython_wrapper.cpp",
    ):
        for file in glob.glob(file_pattern):
            os.remove(file)
    for dir_pattern in "Release":
        for dir in glob.glob(dir_pattern):
            shutil.rmtree(dir)


def print_banner(msg):
    print("==================================================")
    print("= {} ".format(msg))


@invoke.task()
def build_csort(c, path=None):
    """Build the shared library for the sample C code"""
    # Moving this type hint into signature causes an error (???)
    c: invoke.Context
    if on_win:
        if not path:
            print("Path is missing")
        else:
            # Using c.cd didn't work with paths that have spaces :/
            path = f'"{path}vcvars32.bat" x86'  # Enter the VS venv
            path += f'&& cd "{os.getcwd()}"'  # Change to current dir
            path += "&& cl /LD csort.c"  # Compile
            # Uncomment line below, to suppress stdout
            # path = path.replace("&&", " >nul &&") + " >nul"
            c.run(path)
    else:
        print_banner("Building C Library")
        cmd = "gcc -c -Wall -Werror -fpic csort.c -I /usr/include/python3.8"
        invoke.run(cmd)
        invoke.run("gcc -shared -o libcsort.so csort.o")
        print("* Complete")


@invoke.task()
def test_ctypes(c):
    """Run the script to test ctypes"""
    print_banner("Testing ctypes Module for C")
    # pty and python3 didn't work for me (win).
    if on_win:
        invoke.run("python ctypes_c_test.py")
    else:
        invoke.run("python3.8 ctypes_c_test.py", pty=True)


@invoke.task()
def test_ctypes_cpp(c):
    """Run the script to test ctypes"""
    print_banner("Testing ctypes Module for C++")
    # pty and python3 didn't work for me (win).
    if on_win:
        invoke.run("python ctypes_cpp_test.py")
    else:
        invoke.run("python3.8 ctypes_cpp_test.py", pty=True)


@invoke.task()
def build_cffi(c):
    """Build the CFFI Python bindings"""
    print_banner("Building CFFI Module")
    invoke.run("python3 build_cffi.py ")
    print("* Complete")


@invoke.task()
def test_cffi(c):
    """Run the script to test CFFI"""
    print_banner("Testing CFFI Module")
    invoke.run("python3 run_cffi.py")


@invoke.task()
def build_cppsort(c):
    """Build the shared library for the sample C++ code"""
    print_banner("Building C++ Library")
    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC cppsort.cpp "
        "-o libcppsort.so "
    )
    print("* Complete")


def compile_python_module(cpp_name, extension_name):
    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC "
        "`python3.8 -m pybind11 --includes` "
        "-I /usr/include/python3.8 -I .  "
        "{0} "
        "-o {1}`python3.8-config --extension-suffix` "
        "-L. -lcppsort -Wl,-rpath,.".format(cpp_name, extension_name)
    )


@invoke.task(build_cppsort)
def build_pybind11(c):
    """Build the pybind11 wrapper library"""
    print_banner("Building PyBind11 Module")
    compile_python_module("pybind11_wrapper.cpp", "pybind11_cppsort")
    print("* Complete")


@invoke.task()
def test_pybind11(c):
    """Run the script to test PyBind11"""
    print_banner("Testing PyBind11 Module")
    invoke.run("python3.8 pybind11_test.py", pty=True)


@invoke.task(build_cppsort)
def build_cython(c):
    """Build the cython extension module"""
    print_banner("Building Cython Module")
    # Run cython on the pyx file to create a .cpp file
    invoke.run("python3 sort_Test.pyx ")
    invoke.run("python3 setup.py build_ext --inplace")
    print("* Complete")


@invoke.task()
def test_cython(c):
    """Run the script to test Cython"""
    print_banner("Testing Cython Module")
    invoke.run("python3 run.py", pty=True)


@invoke.task(
    clean,
    build_csort,
    build_cppsort,
    test_ctypes,
    test_ctypes_cpp,
    build_cffi,
    test_cffi,
    build_pybind11,
    test_pybind11,
    build_cython,
    test_cython,
)
def all(c):
    """Build and run all tests"""
    pass
