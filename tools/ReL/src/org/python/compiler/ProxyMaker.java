// Copyright (c) Corporation for National Research Initiatives
package org.python.compiler;

import java.io.OutputStream;
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.Map;
import java.util.Set;

import org.objectweb.asm.Label;
import org.objectweb.asm.Opcodes;
import org.python.core.Py;
import org.python.core.PyMethod;
import org.python.core.PyObject;
import org.python.core.PyProxy;
import org.python.core.PyReflectedFunction;
import org.python.util.Generic;

public class ProxyMaker implements ClassConstants, Opcodes
{
    public static final int tBoolean=0;
    public static final int tByte=1;
    public static final int tShort=2;
    public static final int tInteger=3;
    public static final int tLong=4;
    public static final int tFloat=5;
    public static final int tDouble=6;
    public static final int tCharacter=7;
    public static final int tVoid=8;
    public static final int tOther=9;
    public static final int tNone=10;

    public static Map<Class<?>, Integer> types = fillTypes();

    public static Map<Class<?>, Integer> fillTypes() {
        Map<Class<?>, Integer> typeMap = Generic.map();
        typeMap.put(Boolean.TYPE, tBoolean);
        typeMap.put(Byte.TYPE, tByte);
        typeMap.put(Short.TYPE, tShort);
        typeMap.put(Integer.TYPE, tInteger);
        typeMap.put(Long.TYPE, tLong);
        typeMap.put(Float.TYPE, tFloat);
        typeMap.put(Double.TYPE, tDouble);
        typeMap.put(Character.TYPE, tCharacter);
        typeMap.put(Void.TYPE, tVoid);
        return typeMap;
    }

    public static int getType(Class<?> c) {
        if (c == null) {
            return tNone;
        }
        Object i = types.get(c);
        if (i == null) {
            return tOther;
        } else {
            return ((Integer)i);
        }
    }

    /**
     * Retrieves <code>name</code> from the PyObject in <code>proxy</code> if it's defined in
     * Python.  This is a specialized helper function for internal PyProxy use.
     */
    public static PyObject findPython(PyProxy proxy, String name) {
        PyObject o = proxy._getPyInstance();
        if (o == null) {
            proxy.__initProxy__(new Object[0]);
            o = proxy._getPyInstance();
        }
        PyObject ret = o.__findattr__(name);
        if (ret instanceof PyMethod) {
            PyMethod meth = ((PyMethod)ret);
            if (meth.im_func instanceof PyReflectedFunction) {
                PyReflectedFunction func = (PyReflectedFunction)meth.im_func;
                if (func.nargs > 0 && proxy.getClass() == func.argslist[0].declaringClass) {
                    // This function is the default return for the proxy type if the Python instance
                    // hasn't returned something of its own from __findattr__, so do the standard
                    // Java call on this
                    return null;
                }
            }
        }
        Py.setSystemState(proxy._getPySystemState());
        return ret;
    }

    Class<?> superclass;
    Class<?>[] interfaces;
    Set<String> names;
    Set<String> supernames = Generic.set();
    public ClassFile classfile;
    /** The name of the class to build. */
    public String myClass;

    /**
     * Creates a proxy class maker that produces classes named
     * <code>org.python.proxies.(superclassName)</code> with <code>superclass</code> as an
     * implemented interface or extended class, depending on the its type.
     *
     * @deprecated - Use {@link ProxyMaker#ProxyMaker(String, Class, Class[])

     */
    @Deprecated
    public ProxyMaker(String superclassName, Class<?> superclass) {
        this("org.python.proxies." + superclassName,
            superclass.isInterface() ? Object.class : superclass,
            superclass.isInterface() ? new Class<?>[] { superclass} : new Class<?>[0]);

    }

    /**
     * Creates a proxy class maker that produces classes named <code>proxyClassName</code> that
     * extends <code>superclass</code> and implements the interfaces in <code>interfaces</code>.
     */
    public ProxyMaker(String proxyClassName, Class<?> superclass, Class<?>... interfaces) {
        this.myClass = proxyClassName;
        if (superclass == null) {
            superclass = Object.class;
        }
        if (superclass.isInterface()) {
            throw new IllegalArgumentException("Given an interface,  " + superclass.getName()
                    + ", for a proxy superclass");
        }
        this.superclass = superclass;
        if (interfaces == null) {
            interfaces = new Class[0];
        }
        for (Class<?> interfac : interfaces) {
            if (!interfac.isInterface()) {
                throw new IllegalArgumentException(
                    "All classes in the interfaces array must be interfaces, unlike "
                            + interfac.getName());
            }
        }
        this.interfaces = interfaces;
    }

    public static String mapClass(Class<?> c) {
        String name = c.getName();
        int index = name.indexOf(".");
        if (index == -1) {
            return name;
        }
        StringBuffer buf = new StringBuffer(name.length());
        int last_index = 0;
        while (index != -1) {
            buf.append(name.substring(last_index, index));
            buf.append("/");
            last_index = index+1;
            index = name.indexOf(".", last_index);
        }
        buf.append(name.substring(last_index, name.length()));
        return buf.toString();
    }

    public static String mapType(Class<?> type) {
        if (type.isArray())
            return "["+mapType(type.getComponentType());

        switch (getType(type)) {
        case tByte: return "B";
        case tCharacter:  return "C";
        case tDouble:  return "D";
        case tFloat:  return "F";
        case tInteger:  return "I";
        case tLong:  return "J";
        case tShort:  return "S";
        case tBoolean:  return "Z";
        case tVoid:  return "V";
        default:
            return "L"+mapClass(type)+";";
        }
    }

    public static String makeSig(Class<?> ret, Class<?>... sig) {
        String[] mapped = new String[sig.length];
        for (int i = 0; i < mapped.length; i++) {
            mapped[i] = mapType(sig[i]);
        }
        return makeSig(mapType(ret), mapped);
    }

    public static String makeSig(String returnType, String... parameterTypes) {
        StringBuilder buf = new StringBuilder("(");
        for (String param : parameterTypes) {
            buf.append(param);
        }
        return buf.append(')').append(returnType).toString();
    }


    public void doConstants() throws Exception {
        Code code = classfile.addMethod("<clinit>", makeSig("V"), Modifier.STATIC);
        code.return_();
    }

    public static void doReturn(Code code, Class<?> type) throws Exception {
        switch (getType(type)) {
        case tNone:
            break;
        case tCharacter:
        case tBoolean:
        case tByte:
        case tShort:
        case tInteger:
            code.ireturn();
            break;
        case tLong:
            code.lreturn();
            break;
        case tFloat:
            code.freturn();
            break;
        case tDouble:
            code.dreturn();
            break;
        case tVoid:
            code.return_();
            break;
        default:
            code.areturn();
            break;
        }
    }

    public static void doNullReturn(Code code, Class<?> type) throws Exception {
        switch (getType(type)) {
        case tNone:
            break;
        case tCharacter:
        case tBoolean:
        case tByte:
        case tShort:
        case tInteger:
            code.iconst_0();
            code.ireturn();
            break;
        case tLong:
            code.lconst_0();
            code.lreturn();
            break;
        case tFloat:
            code.fconst_0();
            code.freturn();
            break;
        case tDouble:
            code.dconst_0();
            code.dreturn();
            break;
        case tVoid:
            code.return_();
            break;
        default:
            code.aconst_null();
            code.areturn();
            break;
        }
    }

    public void callSuper(Code code,
                          String name,
                          String superclass,
                          Class<?>[] parameters,
                          Class<?> ret,
                          String sig) throws Exception {

        code.aload(0);
        int local_index;
        int i;
        for (i=0, local_index=1; i<parameters.length; i++) {
            switch(getType(parameters[i])) {
            case tCharacter:
            case tBoolean:
            case tByte:
            case tShort:
            case tInteger:
                code.iload(local_index);
                local_index += 1;
                break;
            case tLong:
                code.lload(local_index);
                local_index += 2;
                break;
            case tFloat:
                code.fload(local_index);
                local_index += 1;
                break;
            case tDouble:
                code.dload(local_index);
                local_index += 2;
                break;
            default:
                code.aload(local_index);
                local_index += 1;
                break;
            }
        }
        code.invokespecial(superclass, name, sig);

        doReturn(code, ret);
    }

    public void doJavaCall(Code code, String name, String type,
                          String jcallName)
        throws Exception
    {
        code.invokevirtual("org/python/core/PyObject", jcallName, makeSig($pyObj, $objArr));
        code.invokestatic("org/python/core/Py", "py2"+name, makeSig(type, $pyObj));
    }


    public void getArgs(Code code, Class<?>[] parameters) throws Exception {
        if (parameters.length == 0) {
            code.getstatic("org/python/core/Py", "EmptyObjects", $pyObjArr);
        } else {
            code.iconst(parameters.length);
            code.anewarray("java/lang/Object");

            int array = code.getLocal("[org/python/core/PyObject");
            code.astore(array);

            int local_index;
            int i;
            for (i=0, local_index=1; i<parameters.length; i++) {
                code.aload(array);
                code.iconst(i);

                switch (getType(parameters[i])) {
                case tBoolean:
                case tByte:
                case tShort:
                case tInteger:
                    code.iload(local_index);
                    local_index += 1;
                    code.invokestatic("org/python/core/Py", "newInteger", "(I)" + $pyInteger);
                    break;
                case tLong:
                    code.lload(local_index);
                    local_index += 2;
                    code.invokestatic("org/python/core/Py", "newInteger", "(J)" + $pyObj);
                    break;
                case tFloat:
                    code.fload(local_index);
                    local_index += 1;
                    code.invokestatic("org/python/core/Py", "newFloat", "(F)" + $pyFloat);
                    break;
                case tDouble:
                    code.dload(local_index);
                    local_index += 2;
                    code.invokestatic("org/python/core/Py", "newFloat", "(D)" + $pyFloat);
                    break;
                case tCharacter:
                    code.iload(local_index);
                    local_index += 1;
                    code.invokestatic("org/python/core/Py", "newString", "(C)" + $pyStr);
                    break;
                default:
                    code.aload(local_index);
                    local_index += 1;
                    break;
                }
                code.aastore();
            }
            code.aload(array);
        }
    }

    public void callMethod(Code code,
                           String name,
                           Class<?>[] parameters,
                           Class<?> ret,
                           Class<?>[] exceptions) throws Exception {
        Label start = null;
        Label end = null;

        String jcallName = "_jcall";
        int instLocal = 0;

        if (exceptions.length > 0) {
            start = new Label();
            end = new Label();
            jcallName = "_jcallexc";
            instLocal = code.getLocal("org/python/core/PyObject");
            code.astore(instLocal);
            code.label(start);
            code.aload(instLocal);
        }

        getArgs(code, parameters);

        switch (getType(ret)) {
        case tCharacter:
            doJavaCall(code, "char", "C", jcallName);
            break;
        case tBoolean:
            doJavaCall(code, "boolean", "Z", jcallName);
            break;
        case tByte:
        case tShort:
        case tInteger:
            doJavaCall(code, "int", "I", jcallName);
            break;
        case tLong:
            doJavaCall(code, "long", "J", jcallName);
            break;
        case tFloat:
            doJavaCall(code, "float", "F", jcallName);
            break;
        case tDouble:
            doJavaCall(code, "double", "D", jcallName);
            break;
        case tVoid:
            doJavaCall(code, "void", "V", jcallName);
            break;
        default:
            code.invokevirtual("org/python/core/PyObject", jcallName, makeSig($pyObj, $objArr));
            code.ldc(ret.getName());
            code.invokestatic("java/lang/Class","forName", makeSig($clss, $str));
            code.invokestatic("org/python/core/Py", "tojava", makeSig($obj, $pyObj, $clss));
            // I guess I need this checkcast to keep the verifier happy
            code.checkcast(mapClass(ret));
            break;
        }
        if (end != null) {
            code.label(end);
        }

        doReturn(code, ret);

        if (exceptions.length > 0) {
            boolean throwableFound = false;

            Label handlerStart = null;
            for (Class<?> exception : exceptions) {
                handlerStart = new Label();
                code.label(handlerStart);
                int excLocal = code.getLocal("java/lang/Throwable");
                code.astore(excLocal);

                code.aload(excLocal);
                code.athrow();

                code.visitTryCatchBlock(start, end, handlerStart, mapClass(exception));
                doNullReturn(code, ret);

                code.freeLocal(excLocal);
                if (exception == Throwable.class)
                    throwableFound = true;
            }

            if (!throwableFound) {
                // The final catch (Throwable)
                handlerStart = new Label();
                code.label(handlerStart);
                int excLocal = code.getLocal("java/lang/Throwable");
                code.astore(excLocal);
                code.aload(instLocal);
                code.aload(excLocal);

                code.invokevirtual("org/python/core/PyObject", "_jthrow", makeSig("V", $throwable));
                code.visitTryCatchBlock(start, end, handlerStart, "java/lang/Throwable");

                code.freeLocal(excLocal);
                doNullReturn(code, ret);
            }
            code.freeLocal(instLocal);
        }
    }


    public void addMethod(Method method, int access) throws Exception {
        boolean isAbstract = false;

        if (Modifier.isAbstract(access)) {
            access = access & ~Modifier.ABSTRACT;
            isAbstract = true;
        }

        Class<?>[] parameters = method.getParameterTypes();
        Class<?> ret = method.getReturnType();
        String sig = makeSig(ret, parameters);

        String name = method.getName();
        names.add(name);

        Code code = classfile.addMethod(name, sig, access);

        code.aload(0);
        code.ldc(name);

        if (!isAbstract) {
            int tmp = code.getLocal("org/python/core/PyObject");
            code.invokestatic("org/python/compiler/ProxyMaker", "findPython",
                makeSig($pyObj, $pyProxy, $str));
            code.astore(tmp);
            code.aload(tmp);

            Label callPython = new Label();
            code.ifnonnull(callPython);

            String superClass = mapClass(method.getDeclaringClass());

            callSuper(code, name, superClass, parameters, ret, sig);
            code.label(callPython);
            code.aload(tmp);
            callMethod(code, name, parameters, ret, method.getExceptionTypes());

            addSuperMethod("super__"+name, name, superClass, parameters,
                           ret, sig, access);
        } else {
            code.invokestatic("org/python/compiler/ProxyMaker", "findPython",
                makeSig($pyObj, $pyProxy, $str));
            code.dup();
            Label returnNull = new Label();
            code.ifnull(returnNull);
            callMethod(code, name, parameters, ret, method.getExceptionTypes());
            code.label(returnNull);
            code.pop();
            doNullReturn(code, ret);
        }
    }

    private String methodString(Method m) {
        StringBuffer buf = new StringBuffer(m.getName());
        buf.append(":");
        Class<?>[] params = m.getParameterTypes();
        for (Class<?> param : params) {
            buf.append(param.getName());
            buf.append(",");
        }
        return buf.toString();
    }

    protected void addMethods(Class<?> c, Set<String> t) throws Exception {
        Method[] methods = c.getDeclaredMethods();
        for (Method method : methods) {
            if (!t.add(methodString(method))) {
                continue;
            }

            int access = method.getModifiers();
            if (Modifier.isStatic(access) || Modifier.isPrivate(access)) {
                continue;
            }

            if (Modifier.isNative(access)) {
                access = access & ~Modifier.NATIVE;
            }

            if (Modifier.isProtected(access)) {
                access = (access & ~Modifier.PROTECTED) | Modifier.PUBLIC;
                if (Modifier.isFinal(access)) {
                    addSuperMethod(method, access);
                    continue;
                }
            } else if (Modifier.isFinal(access)) {
                continue;
            } else if (!Modifier.isPublic(access)) {
                continue; // package protected by process of elimination; we can't override
            }
            addMethod(method, access);
        }

        Class<?> sc = c.getSuperclass();
        if (sc != null) {
            addMethods(sc, t);
        }

        for (Class<?> iface : c.getInterfaces()) {
            addMethods(iface, t);
        }
    }

    public void addConstructor(String name,
                               Class<?>[] parameters,
                               Class<?> ret,
                               String sig,
                               int access) throws Exception {
        Code code = classfile.addMethod("<init>", sig, access);
        callSuper(code, "<init>", name, parameters, Void.TYPE, sig);
    }

    public void addConstructors(Class<?> c) throws Exception {
        Constructor<?>[] constructors = c.getDeclaredConstructors();
        String name = mapClass(c);
        for (Constructor<?> constructor : constructors) {
            int access = constructor.getModifiers();
            if (Modifier.isPrivate(access)) {
                continue;
            }
            if (Modifier.isNative(access)) {
                access = access & ~Modifier.NATIVE;
            }
            if (Modifier.isProtected(access)) {
                access = access & ~Modifier.PROTECTED | Modifier.PUBLIC;
            }
            Class<?>[] parameters = constructor.getParameterTypes();
            addConstructor(name, parameters, Void.TYPE, makeSig(Void.TYPE, parameters), access);
        }
    }

    // Super methods are added for the following three reasons:
    //
    //   1) for a protected non-final method add a public method with no
    //   super__ prefix.  This gives needed access to this method for
    //   subclasses
    //
    //   2) for protected final methods, add a public method with the
    //   super__ prefix.  This avoids the danger of trying to override a
    //   final method
    //
    //   3) For any other method that is overridden, add a method with the
    //   super__ prefix.  This gives access to super. version or the
    //   method.
    //
    public void addSuperMethod(Method method, int access) throws Exception {
        Class<?>[] parameters = method.getParameterTypes();
        Class<?> ret = method.getReturnType();
        String superClass = mapClass(method.getDeclaringClass());
        String superName = method.getName();
        String methodName = superName;
        if (Modifier.isFinal(access)) {
            methodName = "super__" + superName;
            access &= ~Modifier.FINAL;
        }
        addSuperMethod(methodName, superName, superClass, parameters,
                       ret, makeSig(ret, parameters), access);
    }

    public void addSuperMethod(String methodName,
                               String superName,
                               String declClass,
                               Class<?>[] parameters,
                               Class<?> ret,
                               String sig,
                               int access) throws Exception {
        if (methodName.startsWith("super__")) {
            /* rationale: JC java-class, P proxy-class subclassing JC
               in order to avoid infinite recursion P should define super__foo
               only if no class between P and JC in the hierarchy defines
               it yet; this means that the python class needing P is the
               first that redefines the JC method foo.
            */
            try {
                superclass.getMethod(methodName, parameters);
                return;
            } catch (NoSuchMethodException e) {
                // OK, no one else defines it, so we need to
            } catch (SecurityException e) {
                return;
            }
        }
        supernames.add(methodName);
        Code code = classfile.addMethod(methodName, sig, access);
        callSuper(code, superName, declClass, parameters, ret, sig);
    }

    public void addProxy() throws Exception {
        // implement PyProxy interface
        classfile.addField("__proxy", $pyObj, Modifier.PROTECTED);
        // setProxy methods
        Code code = classfile.addMethod("_setPyInstance", makeSig("V", $pyObj), Modifier.PUBLIC);
        code.aload(0);
        code.aload(1);
        code.putfield(classfile.name, "__proxy", $pyObj);
        code.return_();

        // getProxy method
        code = classfile.addMethod("_getPyInstance", makeSig($pyObj), Modifier.PUBLIC);
        code.aload(0);
        code.getfield(classfile.name, "__proxy", $pyObj);
        code.areturn();

        String pySys =  "Lorg/python/core/PySystemState;";
        // implement PyProxy interface
        classfile.addField("__systemState", pySys, Modifier.PROTECTED | Modifier.TRANSIENT);

        // setProxy method
        code = classfile.addMethod("_setPySystemState",
                                   makeSig("V", pySys),
                                   Modifier.PUBLIC);

        code.aload(0);
        code.aload(1);
        code.putfield(classfile.name, "__systemState", pySys);
        code.return_();

        // getProxy method
        code = classfile.addMethod("_getPySystemState", makeSig(pySys), Modifier.PUBLIC);
        code.aload(0);
        code.getfield(classfile.name, "__systemState", pySys);
        code.areturn();
    }

    public void addClassDictInit() throws Exception {
        // classDictInit method
        classfile.addInterface(mapClass(org.python.core.ClassDictInit.class));
        Code code = classfile.addMethod("classDictInit", makeSig("V", $pyObj),
            Modifier.PUBLIC | Modifier.STATIC);
        code.aload(0);
        code.ldc("__supernames__");

        int strArray = CodeCompiler.makeStrings(code, supernames);
        code.aload(strArray);
        code.freeLocal(strArray);
        code.invokestatic("org/python/core/Py", "java2py", makeSig($pyObj, $obj));
        code.invokevirtual("org/python/core/PyObject", "__setitem__", makeSig("V", $str, $pyObj));
        code.return_();
    }

    /**
     * Builds this proxy and writes its bytecode to <code>out</code>.
     */
    public void build(OutputStream out) throws Exception {
        build();
        classfile.write(out);
    }

    public void build() throws Exception {
        names = Generic.set();
        int access = superclass.getModifiers();
        if ((access & Modifier.FINAL) != 0) {
            throw new InstantiationException("can't subclass final class");
        }
        access = Modifier.PUBLIC | Modifier.SYNCHRONIZED;

        classfile = new ClassFile(myClass, mapClass(superclass), access);
        addProxy();
        addConstructors(superclass);
        classfile.addInterface("org/python/core/PyProxy");

        Set<String> seenmethods = Generic.set();
        addMethods(superclass, seenmethods);
        for (Class<?> iface : interfaces) {
            if (iface.isAssignableFrom(superclass)) {
                Py.writeWarning("compiler", "discarding redundant interface: " + iface.getName());
                continue;
            }
            classfile.addInterface(mapClass(iface));
            addMethods(iface, seenmethods);
        }
        doConstants();
        addClassDictInit();
    }
}
