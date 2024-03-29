// Copyright (c) Corporation for National Research Initiatives
package org.python.modules;

import java.io.File;

import com.kenai.constantine.platform.Errno;
import org.python.core.Py;
import org.python.core.PyList;
import org.python.core.PyString;
import org.python.core.PySystemState;

public class _py_compile {
    public static PyList __all__ = new PyList(new PyString[] { new PyString("compile") });

    public static boolean compile(String filename, String cfile, String dfile) {
        // Resolve relative path names. dfile is only used for error messages and should not be
        // resolved
        PySystemState sys = Py.getSystemState();
        filename = sys.getPath(filename);
        cfile = sys.getPath(cfile);

        File file = new File(filename);
        if (!file.exists()) {
            throw Py.IOError(Errno.ENOENT, filename);
        }
        String name = getModuleName(file);

        byte[] bytes = org.python.core.imp.compileSource(name, file, dfile, cfile);
        org.python.core.imp.cacheCompiledSource(filename, cfile, bytes);

        return bytes.length > 0;
    }

    public static final String getModuleName(File f) {
        String name = f.getName();
        int dot = name.lastIndexOf('.');
        if (dot != -1) {
            name = name.substring(0, dot);
        }

        // name the __init__ module after its package
        File dir = f.getParentFile();
        if (name.equals("__init__")) {
            name = dir.getName();
            dir = dir.getParentFile();
        }

        // Make the compiled classfile's name fully qualified with a package by walking up the
        // directory tree looking for __init__.py files. Don't check for __init__$py.class since
        // we're compiling source here and the existence of a class file without corresponding
        // source probably doesn't indicate a package.
        while (dir != null && (new File(dir, "__init__.py").exists())) {
            name = dir.getName() + "." + name;
            dir = dir.getParentFile();
        }
        return name;
    }
}
