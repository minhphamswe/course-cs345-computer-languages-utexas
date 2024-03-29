// Copyright (c) Corporation for National Research Initiatives
package org.python.core;

import java.io.OutputStream;

import org.python.core.util.StringUtil;

public class StdoutWrapper extends OutputStream {
    protected String name;

    public StdoutWrapper() {
        this.name = "stdout";
    }

    protected PyObject getObject(PySystemState ss) {
        return ss.stdout;
    }

    protected void setObject(PySystemState ss, PyObject obj) {
        ss.stdout = obj;
    }

    protected PyObject myFile() {
        PySystemState ss = Py.getSystemState();
        PyObject obj = getObject(ss);
        if (obj == null) {
            throw Py.AttributeError("missing sys." + this.name);
        }
        if (obj.getJavaProxy() != null) {
            PyFile f = null;

            Object tojava = obj.__tojava__(OutputStream.class);
            if (tojava != null && tojava != Py.NoConversion) {
                f = new PyFile((OutputStream)tojava);
            }
            if (f != null) {
                setObject(ss, f);
                return f;
            }
        }
        return obj;
    }

    @Override
    public void flush() {
        PyObject obj = myFile();
        if (obj instanceof PyFile) {
            ((PyFile) obj).flush();
        } else {
            try {
                obj.invoke("flush");
            } catch (PyException pye) {
                // ok
            }
        }
    }

    public void write(String s) {
        PyObject obj = myFile();

        if (obj instanceof PyFile) {
            ((PyFile) obj).write(s);
        } else {
            obj.invoke("write", new PyString(s));
        }
    }

    @Override
    public void write(int i) {
        write(new String(new char[] { (char) i }));
    }

    @Override
    public void write(byte[] data, int off, int len) {
        write(StringUtil.fromBytes(data, off, len));
    }

    public void flushLine() {
        PyObject obj = myFile();

        if (obj instanceof PyFile) {
            PyFile file = (PyFile) obj;
            if (file.softspace) {
                file.write("\n");
                file.flush();
            }
            file.softspace = false;
        } else {
            PyObject ss = obj.__findattr__("softspace");
            if (ss != null && ss.__nonzero__()) {
                obj.invoke("write", Py.Newline);
            }
            try {
                obj.invoke("flush");
            } catch (PyException pye) {
                // ok
            }
            obj.__setattr__("softspace", Py.Zero);
        }
    }

    public void print(PyObject o, boolean space, boolean newline) {
        PyObject obj = myFile();

        if (obj instanceof PyFile) {
            PyFile file = (PyFile)obj;
            if (file.softspace) {
                file.write(" ");
                file.softspace = false;
            }

            String s;
            if (o instanceof PyUnicode && file.encoding != null) {
                s = ((PyUnicode)o).encode(file.encoding, "strict");
            } else {
                s = o.__str__().toString();
            }
            file.write(s);

            if (o instanceof PyString) {
                int len = s.length();
                if (len == 0 || !Character.isWhitespace(s.charAt(len - 1))
                    || s.charAt(len - 1) == ' ') {
                    file.softspace = space;
                }
            } else {
                file.softspace = space;
            }

            if (newline) {
                file.write("\n");
                file.softspace = false;
            }
            file.flush();
        } else if (obj instanceof PyFileWriter) {
            PyFileWriter file = (PyFileWriter)obj;
            if (file.softspace) {
                file.write(" ");
                file.softspace = false;
            }

            // since we are outputting directly to a character stream,
            // avoid doing an encoding
            String s;
            if (o instanceof PyString) {
                s = ((PyString) o).getString();
            } else {
                s = o.toString();
            }
            file.write(s);

            if (o instanceof PyString) {
                int len = s.length();
                if (len == 0 || !Character.isWhitespace(s.charAt(len - 1))
                    || s.charAt(len - 1) == ' ') {
                    file.softspace = space;
                }
            } else {
                file.softspace = space;
            }

            if (newline) {
                file.write("\n");
                file.softspace = false;
            }
            file.flush();
        } else {
            PyObject ss = obj.__findattr__("softspace");
            if (ss != null && ss.__nonzero__()) {
                obj.invoke("write", Py.Space);
                obj.__setattr__("softspace", Py.Zero);
            }

            if (!(o instanceof PyUnicode)) {
                o = o.__str__();
            }
            obj.invoke("write", o);

            if (o instanceof PyString) {
                String s = o.toString();
                int len = s.length();
                if (len == 0 || !Character.isWhitespace(s.charAt(len - 1))
                    || s.charAt(len - 1) == ' ') {
                    obj.__setattr__("softspace", space ? Py.One : Py.Zero);
                }
            } else {
                obj.__setattr__("softspace", space ? Py.One : Py.Zero);
            }

            if (newline) {
                obj.invoke("write", Py.Newline);
                obj.__setattr__("softspace", Py.Zero);
            }
        }
    }

    public void print(String s) {
        print(new PyString(s), false, false);
    }

    public void println(String s) {
        print(new PyString(s), false, true);
    }

    public void print(PyObject o) {
        print(o, false, false);
    }

    public void printComma(PyObject o) {
        print(o, true, false);
    }

    public void println(PyObject o) {
        print(o, false, true);
    }

    public void println() {
        PyObject obj = myFile();

        if (obj instanceof PyFile) {
            PyFile file = (PyFile) obj;
            file.write("\n");
            file.flush();
            file.softspace = false;
        } else {
            obj.invoke("write", Py.Newline);
            obj.__setattr__("softspace", Py.Zero);
        }
    }
}
