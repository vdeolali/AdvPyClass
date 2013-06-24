#include "Python.h"
#include <stdio.h>

PyObject *
triple(PyObject *self, PyObject *x)
{
    long cx, result;

    cx = PyInt_AsLong(x);
    if (cx == -1) {
        if (PyErr_Occurred())
            return NULL;
    }
    result = cx * 3;
    if (cx >= 0 && result < cx || cx<0 && result > cx) {
        PyErr_SetString(PyExc_ValueError, "tripling overflowed");
        return NULL;
    }
    return PyInt_FromLong(result);
}

/*

def collatz(x):
    if x % 2 == 0:
        return x // 2
    else:
        return 3 * x + 1
*/

int
collatz(int x)
{
    if (x & 1)
        return 3 * x + 1;
    return x >> 1;
}

PyObject *
py_collatz(PyObject *self, PyObject *args)
{
    int x, y;

    if(!PyArg_ParseTuple(args, "i", &x))
        return NULL;
    y = collatz(x);
    return Py_BuildValue("i", y);
}

PyObject *
show(PyObject *self, PyObject *args)
{
    const char *s;

    if(!PyArg_ParseTuple(args, "s", &s))
        return NULL;
    printf("<<%s>>\n", s);
    return Py_BuildValue("");
}

static PyMethodDef demo_funcs[] = {
    {"triple", (PyCFunction)triple, METH_O, "Triple a value"},
    {"collatz", (PyCFunction)py_collatz, METH_VARARGS, "Verify the Collatz conjecture"},
    {"show", (PyCFunction)show,        METH_VARARGS, "Expose the printf() function from C"},
    {NULL}
};

void
initdemo(void)
{
    Py_InitModule3("demo", demo_funcs, "misc helper functions module");
}
