# jupyter-cpp-kernel
An kernel implementation for C++, it 

- treat each cell as a unique `c++ main` function.
- support many magic templates.
- support complex compile configuration, for example, you can use this for CUDA programming.

Each code cell will be compiled as a c++ file, so it is slow but stable, 
and this idea is different from the kernel for the well known [cling](https://github.com/root-project/cline) project.


This project is based on the code of [jupyter-c-kernel](https://github.com/brendan-rius/jupyter-c-kernel), great work!

## install
the requirements are

- g++ (that support c++11)
- python3
- jupyter

to install as follows

- `python3 setup.py install`
- `install_cpp_kernel`
- `ipython notebook`

## usage and magics

There are some special tokens that helps to auto insert some code.

### `includes`

```c++
//% includes: full
```
will insert some high frequency header fills, such as

- iostream
- vector
- map
- set

to include some specific header file, just `includes` its name
```c++
//% includes: algorithm

// is equal to #include <algorithm>
```

### `main`
Kernal will automatically add main function wrapper, so just insert code block as follows will get

```c++
//% includes: full

std::cout << "hello world" << endl;
```
works.

But sometimes, we might need to define some data structure, so better to define a seperate `main` function.

```c++
//% includes: full
//% main: no

struct Node {
  int v;
  Node* left, *right;
};

int main() {
  Node root;
  
  return 0;
}
```
