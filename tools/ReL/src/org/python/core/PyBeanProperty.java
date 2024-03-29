// Copyright (c) Corporation for National Research Initiatives
package org.python.core;
import java.lang.reflect.*;

public class PyBeanProperty extends PyReflectedField {
    public Method getMethod, setMethod;
    public Class<?> myType;
    String __name__;

    public PyBeanProperty(String name, Class<?> myType, Method getMethod, Method setMethod) {
        __name__ = name;
        this.getMethod = getMethod;
        this.setMethod = setMethod;
        this.myType = myType;
    }

    @Override
    public PyObject _doget(PyObject self) {
        if (self == null) {
            if (field != null) {
                return super._doget(null);
            }
            throw Py.AttributeError("instance attr: "+__name__);
        }

        if (getMethod == null) {
            throw Py.AttributeError("write-only attr: "+__name__);
        }

        Object iself = Py.tojava(self, getMethod.getDeclaringClass());

        try {
            Object value = getMethod.invoke(iself, (Object[])Py.EmptyObjects);
            return Py.java2py(value);
        } catch (Exception e) {
            throw Py.JavaError(e);
        }
    }

    @Override
    public boolean _doset(PyObject self, PyObject value) {
        if (self == null) {
            if (field != null) {
                return super._doset(null, value);
            }
            throw Py.AttributeError("instance attr: "+__name__);
        }

        if (setMethod == null) {
            throw Py.AttributeError("read-only attr: "+__name__);
        }

        Object iself = Py.tojava(self, setMethod.getDeclaringClass());

        // Special handling of tuples - try to call a class constructor
        if (value instanceof PyTuple) {
            try {
                value = Py.java2py(myType).__call__(((PyTuple)value).getArray());
            } catch (Throwable t) {
                throw Py.JavaError(t);
            }
        }
        Object jvalue = Py.tojava(value, myType);

        try {
            setMethod.invoke(iself, jvalue);
        } catch (Exception e) {
            throw Py.JavaError(e);
        }
        return true;
    }

    public PyBeanProperty copy() {
        return new PyBeanProperty(__name__, myType, getMethod, setMethod);
    }

    @Override
    public String toString() {
        String typeName = "unknown";
        if (myType != null) {
            typeName = myType.getName();
        }
        return "<beanProperty "+__name__+" type: "+typeName+" "+
            Py.idstr(this)+">";
    }
}

