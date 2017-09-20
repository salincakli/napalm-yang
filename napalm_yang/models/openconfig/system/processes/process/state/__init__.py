
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/processes/process/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters related to monitored processes
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__pid','__name','__args','__start_time','__uptime','__cpu_usage_user','__cpu_usage_system','__cpu_utilization','__memory_usage','__memory_utilization',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__uptime = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)
    self.__cpu_utilization = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="cpu-utilization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    self.__start_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    self.__args = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="args", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    self.__pid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="pid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    self.__memory_utilization = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="memory-utilization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)
    self.__cpu_usage_system = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="cpu-usage-system", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)
    self.__cpu_usage_user = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="cpu-usage-user", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)
    self.__memory_usage = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="memory-usage", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'system', u'processes', u'process', u'state']

  def _get_pid(self):
    """
    Getter method for pid, mapped from YANG variable /system/processes/process/state/pid (uint64)

    YANG Description: The process pid
    """
    return self.__pid
      
  def _set_pid(self, v, load=False):
    """
    Setter method for pid, mapped from YANG variable /system/processes/process/state/pid (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pid() directly.

    YANG Description: The process pid
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="pid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pid must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="pid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)""",
        })

    self.__pid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pid(self):
    self.__pid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="pid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)


  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/processes/process/state/name (string)

    YANG Description: The process name
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/processes/process/state/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: The process name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)


  def _get_args(self):
    """
    Getter method for args, mapped from YANG variable /system/processes/process/state/args (string)

    YANG Description: Current process command line arguments.  Arguments with
a parameter (e.g., --option 10  or -option=10) should be
represented as a single element of the list with the
argument name and parameter together.  Flag arguments, i.e.,
those without a parameter should also be in their own list
element.
    """
    return self.__args
      
  def _set_args(self, v, load=False):
    """
    Setter method for args, mapped from YANG variable /system/processes/process/state/args (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_args is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_args() directly.

    YANG Description: Current process command line arguments.  Arguments with
a parameter (e.g., --option 10  or -option=10) should be
represented as a single element of the list with the
argument name and parameter together.  Flag arguments, i.e.,
those without a parameter should also be in their own list
element.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="args", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """args must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="args", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)""",
        })

    self.__args = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_args(self):
    self.__args = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="args", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)


  def _get_start_time(self):
    """
    Getter method for start_time, mapped from YANG variable /system/processes/process/state/start_time (uint64)

    YANG Description: The time at which this process started,
reported as nanoseconds since the UNIX epoch.  The
system must be synchronized such that the start-time
can be reported accurately, otherwise it should not be
reported.
    """
    return self.__start_time
      
  def _set_start_time(self, v, load=False):
    """
    Setter method for start_time, mapped from YANG variable /system/processes/process/state/start_time (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_start_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_start_time() directly.

    YANG Description: The time at which this process started,
reported as nanoseconds since the UNIX epoch.  The
system must be synchronized such that the start-time
can be reported accurately, otherwise it should not be
reported.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """start_time must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)""",
        })

    self.__start_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_start_time(self):
    self.__start_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)


  def _get_uptime(self):
    """
    Getter method for uptime, mapped from YANG variable /system/processes/process/state/uptime (oc-types:timeticks64)

    YANG Description: Amount of time elapsed since this process started.
    """
    return self.__uptime
      
  def _set_uptime(self, v, load=False):
    """
    Setter method for uptime, mapped from YANG variable /system/processes/process/state/uptime (oc-types:timeticks64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_uptime is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_uptime() directly.

    YANG Description: Amount of time elapsed since this process started.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """uptime must be of a type compatible with oc-types:timeticks64""",
          'defined-type': "oc-types:timeticks64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)""",
        })

    self.__uptime = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_uptime(self):
    self.__uptime = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)


  def _get_cpu_usage_user(self):
    """
    Getter method for cpu_usage_user, mapped from YANG variable /system/processes/process/state/cpu_usage_user (oc-types:timeticks64)

    YANG Description: CPU time consumed by this process in user mode.
    """
    return self.__cpu_usage_user
      
  def _set_cpu_usage_user(self, v, load=False):
    """
    Setter method for cpu_usage_user, mapped from YANG variable /system/processes/process/state/cpu_usage_user (oc-types:timeticks64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cpu_usage_user is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cpu_usage_user() directly.

    YANG Description: CPU time consumed by this process in user mode.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="cpu-usage-user", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cpu_usage_user must be of a type compatible with oc-types:timeticks64""",
          'defined-type': "oc-types:timeticks64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="cpu-usage-user", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)""",
        })

    self.__cpu_usage_user = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cpu_usage_user(self):
    self.__cpu_usage_user = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="cpu-usage-user", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)


  def _get_cpu_usage_system(self):
    """
    Getter method for cpu_usage_system, mapped from YANG variable /system/processes/process/state/cpu_usage_system (oc-types:timeticks64)

    YANG Description: CPU time consumed by this process in kernel mode.
    """
    return self.__cpu_usage_system
      
  def _set_cpu_usage_system(self, v, load=False):
    """
    Setter method for cpu_usage_system, mapped from YANG variable /system/processes/process/state/cpu_usage_system (oc-types:timeticks64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cpu_usage_system is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cpu_usage_system() directly.

    YANG Description: CPU time consumed by this process in kernel mode.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="cpu-usage-system", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cpu_usage_system must be of a type compatible with oc-types:timeticks64""",
          'defined-type': "oc-types:timeticks64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="cpu-usage-system", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)""",
        })

    self.__cpu_usage_system = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cpu_usage_system(self):
    self.__cpu_usage_system = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="cpu-usage-system", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)


  def _get_cpu_utilization(self):
    """
    Getter method for cpu_utilization, mapped from YANG variable /system/processes/process/state/cpu_utilization (oc-types:percentage)

    YANG Description: The percentage of CPU that is being used by the process.
    """
    return self.__cpu_utilization
      
  def _set_cpu_utilization(self, v, load=False):
    """
    Setter method for cpu_utilization, mapped from YANG variable /system/processes/process/state/cpu_utilization (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cpu_utilization is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cpu_utilization() directly.

    YANG Description: The percentage of CPU that is being used by the process.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="cpu-utilization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cpu_utilization must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="cpu-utilization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__cpu_utilization = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cpu_utilization(self):
    self.__cpu_utilization = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="cpu-utilization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)


  def _get_memory_usage(self):
    """
    Getter method for memory_usage, mapped from YANG variable /system/processes/process/state/memory_usage (uint64)

    YANG Description: Bytes allocated and still in use by the process
    """
    return self.__memory_usage
      
  def _set_memory_usage(self, v, load=False):
    """
    Setter method for memory_usage, mapped from YANG variable /system/processes/process/state/memory_usage (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_memory_usage is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_memory_usage() directly.

    YANG Description: Bytes allocated and still in use by the process
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="memory-usage", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """memory_usage must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="memory-usage", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)""",
        })

    self.__memory_usage = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_memory_usage(self):
    self.__memory_usage = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="memory-usage", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)


  def _get_memory_utilization(self):
    """
    Getter method for memory_utilization, mapped from YANG variable /system/processes/process/state/memory_utilization (oc-types:percentage)

    YANG Description: The percentage of RAM that is being used by the process.
    """
    return self.__memory_utilization
      
  def _set_memory_utilization(self, v, load=False):
    """
    Setter method for memory_utilization, mapped from YANG variable /system/processes/process/state/memory_utilization (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_memory_utilization is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_memory_utilization() directly.

    YANG Description: The percentage of RAM that is being used by the process.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="memory-utilization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """memory_utilization must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="memory-utilization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__memory_utilization = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_memory_utilization(self):
    self.__memory_utilization = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="memory-utilization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)

  pid = __builtin__.property(_get_pid)
  name = __builtin__.property(_get_name)
  args = __builtin__.property(_get_args)
  start_time = __builtin__.property(_get_start_time)
  uptime = __builtin__.property(_get_uptime)
  cpu_usage_user = __builtin__.property(_get_cpu_usage_user)
  cpu_usage_system = __builtin__.property(_get_cpu_usage_system)
  cpu_utilization = __builtin__.property(_get_cpu_utilization)
  memory_usage = __builtin__.property(_get_memory_usage)
  memory_utilization = __builtin__.property(_get_memory_utilization)


  _pyangbind_elements = {'pid': pid, 'name': name, 'args': args, 'start_time': start_time, 'uptime': uptime, 'cpu_usage_user': cpu_usage_user, 'cpu_usage_system': cpu_usage_system, 'cpu_utilization': cpu_utilization, 'memory_usage': memory_usage, 'memory_utilization': memory_utilization, }

