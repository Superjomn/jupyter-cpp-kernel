from setuptools import setup

setup(name='jupyter_cpp_kernel',
    version='0.0.2',
    description='c++ kernel for Jupyter',
    author='ChunweiYan',
    author_email='yanchunwei@outlook.com',
    packages=['jupyter_cpp_kernel'],
    scripts=['jupyter_cpp_kernel/install_cpp_kernel'],
    keywords=['jupyter', 'notebook', 'kernel', 'c++', 'cpp']
)
