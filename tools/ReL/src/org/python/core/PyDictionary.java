/*
 * Copyright (c) Corporation for National Research Initiatives
 * Copyright (c) Jython Developers
 */
package org.python.core;

import java.util.AbstractSet;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.concurrent.ConcurrentMap;
import java.util.concurrent.ConcurrentHashMap;

import org.python.expose.ExposedClassMethod;
import org.python.expose.ExposedMethod;
import org.python.expose.ExposedNew;
import org.python.expose.ExposedType;
import org.python.expose.MethodType;
import org.python.util.Generic;


/**
 * A builtin python dictionary.
 */
@ExposedType(name = "dict", doc = BuiltinDocs.dict_doc)
public class PyDictionary extends PyObject implements ConcurrentMap {

    public static final PyType TYPE = PyType.fromClass(PyDictionary.class);

    private final ConcurrentMap<PyObject, PyObject> map;

    public ConcurrentMap<PyObject, PyObject> getMap() {
        return map;
    }

    /**
     * Create an empty dictionary.
     */
    public PyDictionary() {
        this(TYPE);
    }

    /**
     * Create a dictionary of type with the specified initial capacity.
     */
    public PyDictionary(PyType type, int capacity) {
        super(type);
        map = new ConcurrentHashMap<PyObject, PyObject>(capacity, Generic.CHM_LOAD_FACTOR,
                                                          Generic.CHM_CONCURRENCY_LEVEL);
    }

    /**
     * For derived types
     */
    public PyDictionary(PyType type) {
        super(type);
        map = Generic.concurrentMap();
    }

    /**
     * Create a new dictionary which is based on given map.
     */
    public PyDictionary(Map<PyObject, PyObject> map) {
        this(TYPE, map);
    }

    /**
     * Create a new dictionary which is populated with entries the given map.
     */
    public PyDictionary(PyType type, Map<PyObject, PyObject> map) {
        this(type, Math.max((int) (map.size() / Generic.CHM_LOAD_FACTOR) + 1,
                            Generic.CHM_INITIAL_CAPACITY));
        this.map.putAll(map);
    }

    /**
     * Create a new dictionary without initializing table. Used for dictionary
     * factories, with different backing maps, at the cost that it prevents us from making table be final.
     */
    // TODO we may want to revisit this API, but our chain calling of super makes this tough
    protected PyDictionary(PyType type, boolean initializeBacking) {
        super(type);
        if (initializeBacking) {
            map = Generic.concurrentMap();
        } else {
            map = null; // for later initialization
        }
    }

    /**
     * Create a new dictionary with the element as content.
     *
     * @param elements
     *            The initial elements that is inserted in the dictionary. Even numbered elements
     *            are keys, odd numbered elements are values.
     */
    public PyDictionary(PyObject elements[]) {
        this();
        for (int i = 0; i < elements.length; i += 2) {
            map.put(elements[i], elements[i + 1]);
        }
    }

    @ExposedMethod(doc = BuiltinDocs.dict___init___doc)
    @ExposedNew
    protected final void dict___init__(PyObject[] args, String[] keywords) {
        updateCommon(args, keywords, "dict");
    }

    public static PyObject fromkeys(PyObject keys) {
        return fromkeys(keys, Py.None);
    }

    public static PyObject fromkeys(PyObject keys, PyObject value) {
        return dict_fromkeys(TYPE, keys, value);
    }

    @ExposedClassMethod(defaults = "Py.None", doc = BuiltinDocs.dict_fromkeys_doc)
    static PyObject dict_fromkeys(PyType type, PyObject keys, PyObject value) {
        PyObject d = type.__call__();
        for (PyObject o : keys.asIterable()) {
            d.__setitem__(o, value);
        }
        return d;
    }

    @Override
    public int __len__() {
        return dict___len__();
    }

    @ExposedMethod(doc = BuiltinDocs.dict___len___doc)
    final int dict___len__() {
        return getMap().size();
    }

    @Override
    public boolean __nonzero__() {
        return getMap().size() != 0;
    }

    @Override
    public PyObject __finditem__(int index) {
        throw Py.TypeError("loop over non-sequence");
    }

    @Override
    public PyObject __finditem__(PyObject key) {
        return getMap().get(key);
    }

    @ExposedMethod(doc = BuiltinDocs.dict___getitem___doc)
    protected final PyObject dict___getitem__(PyObject key) {
        PyObject result = getMap().get(key);
        if (result != null) {
            return result;
        }

        // Look up __missing__ method if we're a subclass.
        PyType type = getType();
        if (type != TYPE) {
            PyObject missing = type.lookup("__missing__");
            if (missing != null) {
                return missing.__get__(this, type).__call__(key);
            }
        }
        throw Py.KeyError(key);
    }

    @Override
    public void __setitem__(PyObject key, PyObject value) {
        dict___setitem__(key, value);
    }

    @ExposedMethod(doc = BuiltinDocs.dict___setitem___doc)
    final void dict___setitem__(PyObject key, PyObject value)  {
        getMap().put(key, value);
    }

    @Override
    public void __delitem__(PyObject key) {
        dict___delitem__(key);
    }

    @ExposedMethod(doc = BuiltinDocs.dict___delitem___doc)
    final void dict___delitem__(PyObject key) {
        Object ret = getMap().remove(key);
        if (ret == null) {
            throw Py.KeyError(key.toString());
        }
    }

    @Override
    public PyObject __iter__() {
        return dict___iter__();
    }

    @ExposedMethod(doc = BuiltinDocs.dict___iter___doc)
    final PyObject dict___iter__() {
        return iterkeys();
    }

    @Override
    public String toString() {
        return dict_toString();
    }

    @ExposedMethod(names = {"__repr__", "__str__"}, doc = BuiltinDocs.dict___str___doc)
    final String dict_toString() {
        ThreadState ts = Py.getThreadState();
        if (!ts.enterRepr(this)) {
            return "{...}";
        }

        StringBuilder buf = new StringBuilder("{");
        for (Entry<PyObject, PyObject> entry : getMap().entrySet()) {
            buf.append((entry.getKey()).__repr__().toString());
            buf.append(": ");
            buf.append((entry.getValue()).__repr__().toString());
            buf.append(", ");
        }
        if (buf.length() > 1) {
            buf.delete(buf.length() - 2, buf.length());
        }
        buf.append("}");

        ts.exitRepr(this);
        return buf.toString();
    }

    @Override
    public PyObject __eq__(PyObject otherObj) {
        return dict___eq__(otherObj);
    }

    @ExposedMethod(type = MethodType.BINARY, doc = BuiltinDocs.dict___eq___doc)
    final PyObject dict___eq__(PyObject otherObj) {
        PyType thisType = getType();
        PyType otherType = otherObj.getType();
        if (otherType != thisType && !thisType.isSubType(otherType)
                && !otherType.isSubType(thisType)) {
            return null;
        }
        PyDictionary other = (PyDictionary)otherObj;
        int an = getMap().size();
        int bn = other.getMap().size();
        if (an != bn) {
            return Py.False;
        }

        PyList akeys = keys();
        for (int i = 0; i < an; i++) {
            PyObject akey = akeys.pyget(i);
            PyObject bvalue = other.__finditem__(akey);
            if (bvalue == null) {
                return Py.False;
            }
            PyObject avalue = __finditem__(akey);
            if (!avalue._eq(bvalue).__nonzero__()) {
                return Py.False;
            }
        }
        return Py.True;
    }

    @Override
    public PyObject __ne__(PyObject otherObj) {
        return dict___ne__(otherObj);
    }

    @ExposedMethod(type = MethodType.BINARY, doc = BuiltinDocs.dict___ne___doc)
    final PyObject dict___ne__(PyObject otherObj) {
        PyObject eq_result = __eq__(otherObj);
        if (eq_result == null) {
            return null;
        }
        return eq_result.__not__();
    }

    @ExposedMethod(type = MethodType.BINARY, doc = BuiltinDocs.dict___lt___doc)
    final PyObject dict___lt__(PyObject otherObj) {
    	int result = __cmp__(otherObj);
    	if (result == -2) {
    		return null;
    	}
    	return result < 0 ? Py.True : Py.False;
    }

    @ExposedMethod(type = MethodType.BINARY, doc = BuiltinDocs.dict___gt___doc)
    final PyObject dict___gt__(PyObject otherObj) {
    	int result = __cmp__(otherObj);
    	if (result == -2) {
    		return null;
    	}
    	return result > 0 ? Py.True : Py.False;
    }

    @ExposedMethod(type = MethodType.BINARY, doc = BuiltinDocs.dict___le___doc)
    final PyObject dict___le__(PyObject otherObj) {
    	int result = __cmp__(otherObj);
    	if (result == -2) {
    		return null;
    	}
    	return result <= 0 ? Py.True : Py.False;
    }

    @ExposedMethod(type = MethodType.BINARY, doc = BuiltinDocs.dict___ge___doc)
    final PyObject dict___ge__(PyObject otherObj) {
    	int result = __cmp__(otherObj);
    	if (result == -2) {
    		return null;
    	}
    	return result >= 0 ? Py.True : Py.False;
    }

    @Override
    public int __cmp__(PyObject otherObj) {
        return dict___cmp__(otherObj);
    }

    @ExposedMethod(type = MethodType.CMP, doc = BuiltinDocs.dict___cmp___doc)
    final int dict___cmp__(PyObject otherObj) {
        PyType thisType = getType();
        PyType otherType = otherObj.getType();
        if (otherType != thisType && !thisType.isSubType(otherType)
                && !otherType.isSubType(thisType)) {
            return -2;
        }
        PyDictionary other = (PyDictionary)otherObj;
        int an = getMap().size();
        int bn = other.getMap().size();
        if (an < bn) {
            return -1;
        }
        if (an > bn) {
            return 1;
        }

        PyList akeys = keys();
        PyList bkeys = other.keys();

        akeys.sort();
        bkeys.sort();

        for (int i = 0; i < bn; i++) {
            PyObject akey = akeys.pyget(i);
            PyObject bkey = bkeys.pyget(i);
            int c = akey._cmp(bkey);
            if (c != 0) {
                return c;
            }

            PyObject avalue = __finditem__(akey);
            PyObject bvalue = other.__finditem__(bkey);
            if (avalue == null) {
                if (bvalue == null) {
                    continue;
                }
                return -3;
            } else if (bvalue == null) {
                return -3;
            }
            c = avalue._cmp(bvalue);
            if (c != 0) {
                return c;
            }
        }
        return 0;
    }

    /**
     * Return true if the key exist in the dictionary.
     */
    public boolean has_key(PyObject key) {
        return dict_has_key(key);
    }

    @ExposedMethod(doc = BuiltinDocs.dict_has_key_doc)
    final boolean dict_has_key(PyObject key) {
        return getMap().containsKey(key);
    }

    @Override
    public boolean __contains__(PyObject o) {
        return dict___contains__(o);
    }

    @ExposedMethod(doc = BuiltinDocs.dict___contains___doc)
    final boolean dict___contains__(PyObject o) {
        return dict_has_key(o);
    }

    /**
     * Return this[key] if the key exists in the mapping, defaultObj is returned
     * otherwise.
     *
     * @param key the key to lookup in the dictionary.
     * @param defaultObj the value to return if the key does not exists in the mapping.
     */
    public PyObject get(PyObject key, PyObject defaultObj) {
        return dict_get(key, defaultObj);
    }

    @ExposedMethod(defaults = "Py.None", doc = BuiltinDocs.dict_get_doc)
    final PyObject dict_get(PyObject key, PyObject defaultObj) {
        PyObject o = getMap().get(key);
        return o == null ? defaultObj : o;
    }

    /**
     * Return this[key] if the key exists in the mapping, None
     * is returned otherwise.
     *
     * @param key  the key to lookup in the dictionary.
     */
    public PyObject get(PyObject key) {
        return dict_get(key, Py.None);
    }

    /**
     * Return a shallow copy of the dictionary.
     */
    public PyDictionary copy() {
        return dict_copy();
    }

    @ExposedMethod(doc = BuiltinDocs.dict_copy_doc)
    final PyDictionary dict_copy() {
        return new PyDictionary(getMap()); // no need to clone()
    }

    /**
     * Remove all items from the dictionary.
     */
    public void clear() {
        dict_clear();
    }

    @ExposedMethod(doc = BuiltinDocs.dict_clear_doc)
    final void dict_clear() {
        getMap().clear();
    }

    /**
     * Insert all the key:value pairs from <code>d</code> into
     * this dictionary.
     */
    public void update(PyObject other) {
        dict_update(new PyObject[] {other}, Py.NoKeywords);
    }

    @ExposedMethod(doc = BuiltinDocs.dict_update_doc)
    final void dict_update(PyObject[] args, String[] keywords) {
        updateCommon(args, keywords, "update");
    }

    private void updateCommon(PyObject[] args, String[] keywords, String methName) {
        int nargs = args.length - keywords.length;
        if (nargs > 1) {
            throw PyBuiltinCallable.DefaultInfo.unexpectedCall(nargs, false, methName, 0, 1);
        }
        if (nargs == 1) {
            PyObject arg = args[0];

            Object proxy = arg.getJavaProxy();
            if (proxy instanceof Map) {
                merge((Map)proxy);
            }
            else if (arg.__findattr__("keys") != null) {
                merge(arg);
            } else {
                mergeFromSeq(arg);
            }
        }
        for (int i = 0; i < keywords.length; i++) {
            dict___setitem__(Py.newString(keywords[i]), args[nargs + i]);
        }
    }

    private void merge(Map<Object, Object> other) {
        for (Entry<Object, Object> entry : other.entrySet()) {
            dict___setitem__(Py.java2py(entry.getKey()), Py.java2py(entry.getValue()));
        }
    }


    /**
     * Merge another PyObject that supports keys() with this
     * dict.
     *
     * @param other a PyObject with a keys() method
     */
    private void merge(PyObject other) {
        if (other instanceof PyDictionary) {
            getMap().putAll(((PyDictionary) other).getMap());
        } else if (other instanceof PyStringMap) {
            mergeFromKeys(other, ((PyStringMap)other).keys());
        } else {
            mergeFromKeys(other, other.invoke("keys"));
        }
    }

    /**
     * Merge another PyObject via its keys() method
     *
     * @param other a PyObject with a keys() method
     * @param keys the result of other's keys() method
     */
    private void mergeFromKeys(PyObject other, PyObject keys) {
        for (PyObject key : keys.asIterable()) {
            dict___setitem__(key, other.__getitem__(key));
        }
    }

    /**
     * Merge any iterable object producing iterable objects of length
     * 2 into this dict.
     *
     * @param other another PyObject
     */
    private void mergeFromSeq(PyObject other) {
        PyObject pairs = other.__iter__();
        PyObject pair;

        for (int i = 0; (pair = pairs.__iternext__()) != null; i++) {
            try {
                pair = PySequence.fastSequence(pair, "");
            } catch(PyException pye) {
                if (pye.match(Py.TypeError)) {
                    throw Py.TypeError(String.format("cannot convert dictionary update sequence "
                                                     + "element #%d to a sequence", i));
                }
                throw pye;
            }
            int n;
            if ((n = pair.__len__()) != 2) {
                throw Py.ValueError(String.format("dictionary update sequence element #%d "
                                                  + "has length %d; 2 is required", i, n));
            }
            dict___setitem__(pair.__getitem__(0), pair.__getitem__(1));
        }
    }

    /**
     * Return this[key] if the key exist, otherwise insert key with
     * a None value and return None.
     *
     * @param key   the key to lookup in the dictionary.
     */
    public PyObject setdefault(PyObject key) {
        return dict_setdefault(key, Py.None);
    }

    /**
     * Return this[key] if the key exist, otherwise insert key with
     * the value of failobj and return failobj
     *
     * @param key     the key to lookup in the dictionary.
     * @param failobj the default value to insert in the dictionary
     *                if key does not already exist.
     */
    public PyObject setdefault(PyObject key, PyObject failobj) {
        return dict_setdefault(key, failobj);
    }

    @ExposedMethod(defaults = "Py.None", doc = BuiltinDocs.dict_setdefault_doc)
    final PyObject dict_setdefault(PyObject key, PyObject failobj) {
        PyObject oldValue = getMap().putIfAbsent(key, failobj);
        return oldValue == null ? failobj : oldValue;
    }

    // XXX: needs __doc__ but CPython does not define setifabsent
    @ExposedMethod(defaults = "Py.None")
    final PyObject dict_setifabsent(PyObject key, PyObject failobj) {
        PyObject oldValue = getMap().putIfAbsent(key, failobj);
        return oldValue == null ? Py.None : oldValue;
    }


    /**
     * Return a value based on key
     * from the dictionary.
     */
    public PyObject pop(PyObject key) {
        return dict_pop(key, null);
    }

    /**
     * Return a value based on key
     * from the dictionary or default if that key is not found.
     */
    public PyObject pop(PyObject key, PyObject defaultValue) {
        return dict_pop(key, defaultValue);
    }

    @ExposedMethod(defaults = "null", doc = BuiltinDocs.dict_pop_doc)
    final PyObject dict_pop(PyObject key, PyObject defaultValue) {
        if (!map.containsKey(key)) {
            if (defaultValue == null) {
                throw Py.KeyError("popitem(): dictionary is empty");
            }
            return defaultValue;
        }
        return getMap().remove(key);
    }


    /**
     * Return a random (key, value) tuple pair and remove the pair
     * from the dictionary.
     */
    public PyObject popitem() {
        return dict_popitem();
    }

    @ExposedMethod(doc = BuiltinDocs.dict_popitem_doc)
    final PyObject dict_popitem() {
        Iterator<Entry<PyObject, PyObject>> it = getMap().entrySet().iterator();
        if (!it.hasNext()) {
            throw Py.KeyError("popitem(): dictionary is empty");
        }
        Entry<PyObject, PyObject> entry = it.next();
        PyTuple tuple = new PyTuple(entry.getKey(), entry.getValue());
        it.remove();
        return tuple;
    }

    /**
     * Return a copy of the dictionary's list of (key, value) tuple
     * pairs.
     */
    public PyList items() {
        return dict_items();
    }

    @ExposedMethod(doc = BuiltinDocs.dict_items_doc)
    final PyList dict_items() {
        List<PyObject> list = new ArrayList<PyObject>(getMap().size());
        for (Entry<PyObject, PyObject> entry : getMap().entrySet()) {
            list.add(new PyTuple(entry.getKey(), entry.getValue()));
        }
        return PyList.fromList(list);
    }

    /**
     * Return a copy of the dictionary's list of keys.
     */
    public PyList keys() {
        return dict_keys();
    }

    @ExposedMethod(doc = BuiltinDocs.dict_keys_doc)
    final PyList dict_keys() {
        return PyList.fromList(new ArrayList<PyObject>(getMap().keySet()));
    }

    @ExposedMethod(doc = BuiltinDocs.dict_values_doc)
    final PyList dict_values() {
        return PyList.fromList(new ArrayList<PyObject>(getMap().values()));
    }

    /**
     * Returns an iterator over (key, value) pairs.
     */
    public PyObject iteritems() {
        return dict_iteritems();
    }

    @ExposedMethod(doc = BuiltinDocs.dict_iteritems_doc)
    final PyObject dict_iteritems() {
        return new ItemsIter(getMap().entrySet());
    }

    /**
     * Returns an iterator over the dictionary's keys.
     */
    public PyObject iterkeys() {
        return dict_iterkeys();
    }

    @ExposedMethod(doc = BuiltinDocs.dict_iterkeys_doc)
    final PyObject dict_iterkeys() {
        return new ValuesIter(getMap().keySet());
    }

    /**
     * Returns an iterator over the dictionary's values.
     */
    public PyObject itervalues() {
        return dict_itervalues();
    }

    @ExposedMethod(doc = BuiltinDocs.dict_itervalues_doc)
    final PyObject dict_itervalues() {
        return new ValuesIter(getMap().values());
    }

    @Override
    public int hashCode() {
        return dict___hash__();
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final PyDictionary other = (PyDictionary) obj;
        if (this.map != other.map && (this.map == null || !this.map.equals(other.map))) {
            return false;
        }
        return true;
    }

    @ExposedMethod(doc = BuiltinDocs.dict___hash___doc)
    final int dict___hash__() {
        throw Py.TypeError(String.format("unhashable type: '%.200s'", getType().fastGetName()));
    }

    @Override
    public boolean isMappingType() {
        return true;
    }

    @Override
    public boolean isSequenceType() {
        return false;
    }

    class ValuesIter extends PyIterator {

        private final Iterator<PyObject> iterator;

        private final int size;

        public ValuesIter(Collection<PyObject> values) {
            iterator = values.iterator();
            size = values.size();
        }

        @Override
        public PyObject __iternext__() {
            if (getMap().size() != size) {
                throw Py.RuntimeError("dictionary changed size during iteration");
            }
            if (!iterator.hasNext()) {
                return null;
            }
            return iterator.next();
        }
    }

    class ItemsIter extends PyIterator {

        private final Iterator<Entry<PyObject, PyObject>> iterator;

        private final int size;

        public ItemsIter(Set<Entry<PyObject, PyObject>> items) {
            iterator = items.iterator();
            size = items.size();
        }

        @Override
        public PyObject __iternext__() {
            if (getMap().size() != size) {
                throw Py.RuntimeError("dictionary changed size during iteration");
            }
            if (!iterator.hasNext()) {
                return null;
            }
            Entry<PyObject, PyObject> entry = iterator.next();
            return new PyTuple(entry.getKey(), entry.getValue());
        }
    }

    /*
     * The following methods implement the java.util.Map interface which allows PyDictionary to be
     * passed to java methods that take java.util.Map as a parameter. Basically, the Map methods are
     * a wrapper around the PyDictionary's Map container stored in member variable 'table'. These
     * methods convert java Object to PyObjects on insertion, and PyObject to Objects on retrieval.
     */
    /** @see java.util.Map#entrySet() */
    public Set entrySet() {
        return new PyMapEntrySet(getMap().entrySet());
    }

    /** @see java.util.Map#keySet() */
    public Set keySet() {
        return new PyMapKeyValSet(getMap().keySet());
    }

    /** @see java.util.Map#values() */
    public Collection values() {
        return new PyMapKeyValSet(getMap().values());
    }

    /** @see java.util.Map#putAll(Map map) */
    public void putAll(Map map) {
        for (Object o : map.entrySet()) {
            Entry entry = (Entry)o;
            getMap().put(Py.java2py(entry.getKey()), Py.java2py(entry.getValue()));
        }
    }

    /** @see java.util.Map#remove(Object key) */
    public Object remove(Object key) {
        return tojava(getMap().remove(Py.java2py(key)));
    }

    /** @see java.util.Map#put(Object key, Object value) */
    public Object put(Object key, Object value) {
        return tojava(getMap().put(Py.java2py(key), Py.java2py(value)));
    }

    /** @see java.util.Map#get(Object key) */
    public Object get(Object key) {
        return tojava(getMap().get(Py.java2py(key)));
    }

    /** @see java.util.Map#containsValue(Object key) */
    public boolean containsValue(Object value) {
        return getMap().containsValue(Py.java2py(value));
    }

    /** @see java.util.Map#containsValue(Object key) */
    public boolean containsKey(Object key) {
        return getMap().containsKey(Py.java2py(key));
    }

    /** @see java.util.Map#isEmpty() */
    public boolean isEmpty() {
        return getMap().isEmpty();
    }

    /** @see java.util.Map#size() */
    public int size() {
        return getMap().size();
    }

    /** Convert return values to java objects */
    static Object tojava(Object val) {
        return val == null ? null : ((PyObject)val).__tojava__(Object.class);
    }

    public Object putIfAbsent(Object key, Object value) {
        return tojava(getMap().putIfAbsent(Py.java2py(key), Py.java2py(value)));
    }

    public boolean remove(Object key, Object value) {
        return getMap().remove(Py.java2py(key), Py.java2py(value));
    }

    public boolean replace(Object key, Object oldValue, Object newValue) {
        return getMap().replace(Py.java2py(key), Py.java2py(oldValue), Py.java2py(newValue));
    }

    public Object replace(Object key, Object value) {
        return tojava(getMap().replace(Py.java2py(key), Py.java2py(value)));
    }

}

/** Basic implementation of Entry that just holds onto a key and value and returns them. */
class SimpleEntry implements Entry {

    protected Object key;

    protected Object value;

    public SimpleEntry(Object key, Object value) {
        this.key = key;
        this.value = value;
    }

    public Object getKey() {
        return key;
    }

    public Object getValue() {
        return value;
    }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof Map.Entry)) {
            return false;
        }
        Map.Entry e = (Map.Entry)o;
        return eq(key, e.getKey()) && eq(value, e.getValue());
    }

    private static boolean eq(Object o1, Object o2) {
        return o1 == null ? o2 == null : o1.equals(o2);
    }

    @Override
    public int hashCode() {
        return ((key == null) ? 0 : key.hashCode()) ^ ((value == null) ? 0 : value.hashCode());
    }

    @Override
    public String toString() {
        return key + "=" + value;
    }

    public Object setValue(Object val) {
        throw new UnsupportedOperationException("Not supported by this view");
    }
}

/**
 * Wrapper for a Entry object returned from the java.util.Set object which in turn is returned by
 * the entrySet method of java.util.Map. This is needed to correctly convert from PyObjects to java
 * Objects. Note that we take care in the equals and hashCode methods to make sure these methods are
 * consistent with Entry objects that contain java Objects for a value so that on the java side they
 * can be reliable compared.
 */
class PyToJavaMapEntry extends SimpleEntry {

    /** Create a copy of the Entry with Py.None converted to null */
    PyToJavaMapEntry(Entry entry) {
        super(entry.getKey(), entry.getValue());
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || !(o instanceof Entry)) {
            return false;
        }
        Entry me = new JavaToPyMapEntry((Entry)o);
        return o.equals(me);
    }

    // tojava is called in getKey and getValue so the raw key and value can be
    // used to create a new SimpleEntry in getEntry.
    @Override
    public Object getKey() {
        return PyDictionary.tojava(key);
    }

    @Override
    public Object getValue() {
        return PyDictionary.tojava(value);
    }

    /**
     * @return an entry that returns the original values given to this entry.
     */
    public Entry getEntry() {
        return new SimpleEntry(key, value);
    }

    @Override
    public int hashCode() {
        return ((key == null) ? 0 : key.hashCode()) ^ ((value == null) ? 0 : value.hashCode());
    }

}

/**
 * MapEntry Object for java MapEntry objects passed to the java.util.Set interface which is returned
 * by the entrySet method of PyDictionary. Essentially like PyTojavaMapEntry, but going the other
 * way converting java Objects to PyObjects.
 */
class JavaToPyMapEntry extends SimpleEntry {

    public JavaToPyMapEntry(Entry entry) {
        super(Py.java2py(entry.getKey()), Py.java2py(entry.getValue()));
    }
}

/**
 * Wrapper collection class for the keySet and values methods of java.util.Map
 */
class PyMapKeyValSet extends PyMapSet {

    PyMapKeyValSet(Collection coll) {
        super(coll);
    }

    @Override
    Object toJava(Object o) {
        return PyDictionary.tojava(o);
    }

    @Override
    Object toPython(Object o) {
        return Py.java2py(o);
    }
}

/**
 * Set wrapper for the entrySet method. Entry objects are wrapped further in JavaToPyMapEntry and
 * PyToJavaMapEntry. Note - The set interface is reliable for standard objects like strings and
 * integers, but may be inconsistent for other types of objects since the equals method may return
 * false for Entry object that hold more elaborate PyObject types. However, we insure that this
 * interface works when the Entry object originates from a Set object retrieved from a PyDictionary.
 */
class PyMapEntrySet extends PyMapSet {

    PyMapEntrySet(Collection coll) {
        super(coll);
    }

    // We know that PyMapEntrySet will only contains entries, so if the object being passed in is
    // null or not an Entry, then return null which will match nothing for remove and contains
    // methods.
    @Override
    Object toPython(Object o) {
        if (o == null || !(o instanceof Entry)) {
            return null;
        }
        if (o instanceof PyToJavaMapEntry) {
            // Use the original entry from PyDictionary
            return ((PyToJavaMapEntry)o).getEntry();
        } else {
            return new JavaToPyMapEntry((Entry)o);
        }
    }

    @Override
    Object toJava(Object o) {
        return new PyToJavaMapEntry((Entry)o);
    }
}

/**
 * PyMapSet serves as a wrapper around Set Objects returned by the java.util.Map interface of
 * PyDictionary. entrySet, values and keySet methods return this type for the java.util.Map
 * implementation. This class is necessary as a wrapper to convert PyObjects to java Objects for
 * methods that return values, and convert Objects to PyObjects for methods that take values. The
 * translation is necessary to provide java access to jython dictionary objects. This wrapper also
 * provides the expected backing functionality such that changes to the wrapper set or reflected in
 * PyDictionary.
 */
abstract class PyMapSet extends AbstractSet {

    private final Collection coll;

    PyMapSet(Collection coll) {
        this.coll = coll;
    }

    abstract Object toJava(Object obj);

    abstract Object toPython(Object obj);

    @Override
    public int size() {
        return coll.size();
    }

    @Override
    public boolean contains(Object o) {
        return coll.contains(toPython(o));
    }

    @Override
     public boolean remove(Object o) {
         return coll.remove(toPython(o));
    }

    @Override
    public void clear() {
        coll.clear();
    }

    // Iterator wrapper class returned by the PyMapSet iterator
    // method. We need this wrapper to return PyToJavaMapEntry objects
    // for the 'next()' method.
    class PySetIter implements Iterator {
        Iterator itr;

        PySetIter(Iterator itr) {
            this.itr = itr;
        }

        public boolean hasNext() {
            return itr.hasNext();
        }

        public Object next() {
            return toJava(itr.next());
        }

        public void remove() {
            itr.remove();
        }
    }

    @Override
    public Iterator iterator() {
        return new PySetIter(coll.iterator());
    }
}
