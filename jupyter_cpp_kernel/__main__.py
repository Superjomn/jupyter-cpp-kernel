from __future__ import absolute_import
from ipykernel.kernelapp import IPKernelApp
from .kernel import CppKernel
IPKernelApp.launch_instance(kernel_class=CppKernel)
