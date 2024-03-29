# Generated by h2py from /usr/include/sys/stropts.h

# Included from sys/feature_tests.h

# Included from sys/isa_defs.h
_CHAR_ALIGNMENT = 1
_SHORT_ALIGNMENT = 2
_INT_ALIGNMENT = 4
_LONG_ALIGNMENT = 8
_LONG_LONG_ALIGNMENT = 8
_DOUBLE_ALIGNMENT = 8
_LONG_DOUBLE_ALIGNMENT = 16
_POINTER_ALIGNMENT = 8
_MAX_ALIGNMENT = 16
_ALIGNMENT_REQUIRED = 1
_CHAR_ALIGNMENT = 1
_SHORT_ALIGNMENT = 2
_INT_ALIGNMENT = 4
_LONG_ALIGNMENT = 4
_LONG_LONG_ALIGNMENT = 4
_DOUBLE_ALIGNMENT = 4
_LONG_DOUBLE_ALIGNMENT = 4
_POINTER_ALIGNMENT = 4
_MAX_ALIGNMENT = 4
_ALIGNMENT_REQUIRED = 0
_CHAR_ALIGNMENT = 1
_SHORT_ALIGNMENT = 2
_INT_ALIGNMENT = 4
_LONG_LONG_ALIGNMENT = 8
_DOUBLE_ALIGNMENT = 8
_ALIGNMENT_REQUIRED = 1
_LONG_ALIGNMENT = 4
_LONG_DOUBLE_ALIGNMENT = 8
_POINTER_ALIGNMENT = 4
_MAX_ALIGNMENT = 8
_LONG_ALIGNMENT = 8
_LONG_DOUBLE_ALIGNMENT = 16
_POINTER_ALIGNMENT = 8
_MAX_ALIGNMENT = 16
_POSIX_C_SOURCE = 1
_LARGEFILE64_SOURCE = 1
_LARGEFILE_SOURCE = 1
_FILE_OFFSET_BITS = 64
_FILE_OFFSET_BITS = 32
_POSIX_C_SOURCE = 199506L
_POSIX_PTHREAD_SEMANTICS = 1
_XOPEN_VERSION = 500
_XOPEN_VERSION = 4
_XOPEN_VERSION = 3
from TYPES import *

# Included from sys/conf.h

# Included from sys/t_lock.h

# Included from sys/machlock.h
from TYPES import *
LOCK_HELD_VALUE = 0xff
def SPIN_LOCK(pl): return ((pl) > ipltospl(LOCK_LEVEL))

def LOCK_SAMPLE_INTERVAL(i): return (((i) & 0xff) == 0)

CLOCK_LEVEL = 10
LOCK_LEVEL = 10
DISP_LEVEL = (LOCK_LEVEL + 1)
PTR24_LSB = 5
PTR24_MSB = (PTR24_LSB + 24)
PTR24_ALIGN = 32
PTR24_BASE = 0xe0000000

# Included from sys/param.h
from TYPES import *
_POSIX_VDISABLE = 0
MAX_INPUT = 512
MAX_CANON = 256
UID_NOBODY = 60001
GID_NOBODY = UID_NOBODY
UID_NOACCESS = 60002
MAX_TASKID = 999999
MAX_MAXPID = 999999
DEFAULT_MAXPID = 999999
DEFAULT_JUMPPID = 100000
DEFAULT_MAXPID = 30000
DEFAULT_JUMPPID = 0
MAXUID = 2147483647
MAXPROJID = MAXUID
MAXLINK = 32767
NMOUNT = 40
CANBSIZ = 256
NOFILE = 20
NGROUPS_UMIN = 0
NGROUPS_UMAX = 32
NGROUPS_MAX_DEFAULT = 16
NZERO = 20
NULL = 0L
NULL = 0
CMASK = 022
CDLIMIT = (1L<<11)
NBPS = 0x20000
NBPSCTR = 512
UBSIZE = 512
SCTRSHFT = 9
SYSNAME = 9
PREMOTE = 39
MAXPATHLEN = 1024
MAXSYMLINKS = 20
MAXNAMELEN = 256
NADDR = 13
PIPE_BUF = 5120
PIPE_MAX = 5120
NBBY = 8
MAXBSIZE = 8192
DEV_BSIZE = 512
DEV_BSHIFT = 9
MAXFRAG = 8
MAXOFF32_T = 0x7fffffff
MAXOFF_T = 0x7fffffffffffffffl
MAXOFFSET_T = 0x7fffffffffffffffl
MAXOFF_T = 0x7fffffffl
MAXOFFSET_T = 0x7fffffff
def btodb(bytes): return   \

def dbtob(db): return   \

def lbtodb(bytes): return   \

def ldbtob(db): return   \

NCARGS32 = 0x100000
NCARGS64 = 0x200000
NCARGS = NCARGS64
NCARGS = NCARGS32
FSHIFT = 8
FSCALE = (1<<FSHIFT)
def DELAY(n): return drv_usecwait(n)

def mmu_ptob(x): return ((x) << MMU_PAGESHIFT)

def mmu_btop(x): return (((x)) >> MMU_PAGESHIFT)

def mmu_btopr(x): return ((((x) + MMU_PAGEOFFSET) >> MMU_PAGESHIFT))

def mmu_ptod(x): return ((x) << (MMU_PAGESHIFT - DEV_BSHIFT))

def ptod(x): return ((x) << (PAGESHIFT - DEV_BSHIFT))

def ptob(x): return ((x) << PAGESHIFT)

def btop(x): return (((x) >> PAGESHIFT))

def btopr(x): return ((((x) + PAGEOFFSET) >> PAGESHIFT))

def dtop(DD): return (((DD) + NDPP - 1) >> (PAGESHIFT - DEV_BSHIFT))

def dtopt(DD): return ((DD) >> (PAGESHIFT - DEV_BSHIFT))

_AIO_LISTIO_MAX = (4096)
_AIO_MAX = (-1)
_MQ_OPEN_MAX = (32)
_MQ_PRIO_MAX = (32)
_SEM_NSEMS_MAX = INT_MAX
_SEM_VALUE_MAX = INT_MAX

# Included from sys/unistd.h
_CS_PATH = 65
_CS_LFS_CFLAGS = 68
_CS_LFS_LDFLAGS = 69
_CS_LFS_LIBS = 70
_CS_LFS_LINTFLAGS = 71
_CS_LFS64_CFLAGS = 72
_CS_LFS64_LDFLAGS = 73
_CS_LFS64_LIBS = 74
_CS_LFS64_LINTFLAGS = 75
_CS_XBS5_ILP32_OFF32_CFLAGS = 700
_CS_XBS5_ILP32_OFF32_LDFLAGS = 701
_CS_XBS5_ILP32_OFF32_LIBS = 702
_CS_XBS5_ILP32_OFF32_LINTFLAGS = 703
_CS_XBS5_ILP32_OFFBIG_CFLAGS = 705
_CS_XBS5_ILP32_OFFBIG_LDFLAGS = 706
_CS_XBS5_ILP32_OFFBIG_LIBS = 707
_CS_XBS5_ILP32_OFFBIG_LINTFLAGS = 708
_CS_XBS5_LP64_OFF64_CFLAGS = 709
_CS_XBS5_LP64_OFF64_LDFLAGS = 710
_CS_XBS5_LP64_OFF64_LIBS = 711
_CS_XBS5_LP64_OFF64_LINTFLAGS = 712
_CS_XBS5_LPBIG_OFFBIG_CFLAGS = 713
_CS_XBS5_LPBIG_OFFBIG_LDFLAGS = 714
_CS_XBS5_LPBIG_OFFBIG_LIBS = 715
_CS_XBS5_LPBIG_OFFBIG_LINTFLAGS = 716
_SC_ARG_MAX = 1
_SC_CHILD_MAX = 2
_SC_CLK_TCK = 3
_SC_NGROUPS_MAX = 4
_SC_OPEN_MAX = 5
_SC_JOB_CONTROL = 6
_SC_SAVED_IDS = 7
_SC_VERSION = 8
_SC_PASS_MAX = 9
_SC_LOGNAME_MAX = 10
_SC_PAGESIZE = 11
_SC_XOPEN_VERSION = 12
_SC_NPROCESSORS_CONF = 14
_SC_NPROCESSORS_ONLN = 15
_SC_STREAM_MAX = 16
_SC_TZNAME_MAX = 17
_SC_AIO_LISTIO_MAX = 18
_SC_AIO_MAX = 19
_SC_AIO_PRIO_DELTA_MAX = 20
_SC_ASYNCHRONOUS_IO = 21
_SC_DELAYTIMER_MAX = 22
_SC_FSYNC = 23
_SC_MAPPED_FILES = 24
_SC_MEMLOCK = 25
_SC_MEMLOCK_RANGE = 26
_SC_MEMORY_PROTECTION = 27
_SC_MESSAGE_PASSING = 28
_SC_MQ_OPEN_MAX = 29
_SC_MQ_PRIO_MAX = 30
_SC_PRIORITIZED_IO = 31
_SC_PRIORITY_SCHEDULING = 32
_SC_REALTIME_SIGNALS = 33
_SC_RTSIG_MAX = 34
_SC_SEMAPHORES = 35
_SC_SEM_NSEMS_MAX = 36
_SC_SEM_VALUE_MAX = 37
_SC_SHARED_MEMORY_OBJECTS = 38
_SC_SIGQUEUE_MAX = 39
_SC_SIGRT_MIN = 40
_SC_SIGRT_MAX = 41
_SC_SYNCHRONIZED_IO = 42
_SC_TIMERS = 43
_SC_TIMER_MAX = 44
_SC_2_C_BIND = 45
_SC_2_C_DEV = 46
_SC_2_C_VERSION = 47
_SC_2_FORT_DEV = 48
_SC_2_FORT_RUN = 49
_SC_2_LOCALEDEF = 50
_SC_2_SW_DEV = 51
_SC_2_UPE = 52
_SC_2_VERSION = 53
_SC_BC_BASE_MAX = 54
_SC_BC_DIM_MAX = 55
_SC_BC_SCALE_MAX = 56
_SC_BC_STRING_MAX = 57
_SC_COLL_WEIGHTS_MAX = 58
_SC_EXPR_NEST_MAX = 59
_SC_LINE_MAX = 60
_SC_RE_DUP_MAX = 61
_SC_XOPEN_CRYPT = 62
_SC_XOPEN_ENH_I18N = 63
_SC_XOPEN_SHM = 64
_SC_2_CHAR_TERM = 66
_SC_XOPEN_XCU_VERSION = 67
_SC_ATEXIT_MAX = 76
_SC_IOV_MAX = 77
_SC_XOPEN_UNIX = 78
_SC_PAGE_SIZE = _SC_PAGESIZE
_SC_T_IOV_MAX = 79
_SC_PHYS_PAGES = 500
_SC_AVPHYS_PAGES = 501
_SC_COHER_BLKSZ = 503
_SC_SPLIT_CACHE = 504
_SC_ICACHE_SZ = 505
_SC_DCACHE_SZ = 506
_SC_ICACHE_LINESZ = 507
_SC_DCACHE_LINESZ = 508
_SC_ICACHE_BLKSZ = 509
_SC_DCACHE_BLKSZ = 510
_SC_DCACHE_TBLKSZ = 511
_SC_ICACHE_ASSOC = 512
_SC_DCACHE_ASSOC = 513
_SC_MAXPID = 514
_SC_STACK_PROT = 515
_SC_THREAD_DESTRUCTOR_ITERATIONS = 568
_SC_GETGR_R_SIZE_MAX = 569
_SC_GETPW_R_SIZE_MAX = 570
_SC_LOGIN_NAME_MAX = 571
_SC_THREAD_KEYS_MAX = 572
_SC_THREAD_STACK_MIN = 573
_SC_THREAD_THREADS_MAX = 574
_SC_TTY_NAME_MAX = 575
_SC_THREADS = 576
_SC_THREAD_ATTR_STACKADDR = 577
_SC_THREAD_ATTR_STACKSIZE = 578
_SC_THREAD_PRIORITY_SCHEDULING = 579
_SC_THREAD_PRIO_INHERIT = 580
_SC_THREAD_PRIO_PROTECT = 581
_SC_THREAD_PROCESS_SHARED = 582
_SC_THREAD_SAFE_FUNCTIONS = 583
_SC_XOPEN_LEGACY = 717
_SC_XOPEN_REALTIME = 718
_SC_XOPEN_REALTIME_THREADS = 719
_SC_XBS5_ILP32_OFF32 = 720
_SC_XBS5_ILP32_OFFBIG = 721
_SC_XBS5_LP64_OFF64 = 722
_SC_XBS5_LPBIG_OFFBIG = 723
_PC_LINK_MAX = 1
_PC_MAX_CANON = 2
_PC_MAX_INPUT = 3
_PC_NAME_MAX = 4
_PC_PATH_MAX = 5
_PC_PIPE_BUF = 6
_PC_NO_TRUNC = 7
_PC_VDISABLE = 8
_PC_CHOWN_RESTRICTED = 9
_PC_ASYNC_IO = 10
_PC_PRIO_IO = 11
_PC_SYNC_IO = 12
_PC_FILESIZEBITS = 67
_PC_LAST = 67
_POSIX_VERSION = 199506L
_POSIX2_VERSION = 199209L
_POSIX2_C_VERSION = 199209L
_XOPEN_XCU_VERSION = 4
_XOPEN_REALTIME = 1
_XOPEN_ENH_I18N = 1
_XOPEN_SHM = 1
_POSIX2_C_BIND = 1
_POSIX2_CHAR_TERM = 1
_POSIX2_LOCALEDEF = 1
_POSIX2_C_DEV = 1
_POSIX2_SW_DEV = 1
_POSIX2_UPE = 1

# Included from sys/mutex.h
from TYPES import *
def MUTEX_HELD(x): return (mutex_owned(x))


# Included from sys/rwlock.h
from TYPES import *
def RW_READ_HELD(x): return (rw_read_held((x)))

def RW_WRITE_HELD(x): return (rw_write_held((x)))

def RW_LOCK_HELD(x): return (rw_lock_held((x)))

def RW_ISWRITER(x): return (rw_iswriter(x))


# Included from sys/semaphore.h

# Included from sys/thread.h
from TYPES import *

# Included from sys/klwp.h
from TYPES import *

# Included from sys/condvar.h
from TYPES import *

# Included from sys/time.h

# Included from sys/types32.h

# Included from sys/int_types.h
TIME32_MAX = INT32_MAX
TIME32_MIN = INT32_MIN
def TIMEVAL_OVERFLOW(tv): return \

from TYPES import *
DST_NONE = 0
DST_USA = 1
DST_AUST = 2
DST_WET = 3
DST_MET = 4
DST_EET = 5
DST_CAN = 6
DST_GB = 7
DST_RUM = 8
DST_TUR = 9
DST_AUSTALT = 10
ITIMER_REAL = 0
ITIMER_VIRTUAL = 1
ITIMER_PROF = 2
ITIMER_REALPROF = 3
def ITIMERVAL_OVERFLOW(itv): return \

SEC = 1
MILLISEC = 1000
MICROSEC = 1000000
NANOSEC = 1000000000

# Included from sys/time_impl.h
def TIMESPEC_OVERFLOW(ts): return \

def ITIMERSPEC_OVERFLOW(it): return \

__CLOCK_REALTIME0 = 0
CLOCK_VIRTUAL = 1
CLOCK_PROF = 2
__CLOCK_REALTIME3 = 3
CLOCK_HIGHRES = 4
CLOCK_MAX = 5
CLOCK_REALTIME = __CLOCK_REALTIME3
CLOCK_REALTIME = __CLOCK_REALTIME0
TIMER_RELTIME = 0x0
TIMER_ABSTIME = 0x1
def TICK_TO_SEC(tick): return ((tick) / hz)

def SEC_TO_TICK(sec): return ((sec) * hz)

def TICK_TO_MSEC(tick): return \

def MSEC_TO_TICK(msec): return \

def MSEC_TO_TICK_ROUNDUP(msec): return \

def TICK_TO_USEC(tick): return ((tick) * usec_per_tick)

def USEC_TO_TICK(usec): return ((usec) / usec_per_tick)

def USEC_TO_TICK_ROUNDUP(usec): return \

def TICK_TO_NSEC(tick): return ((tick) * nsec_per_tick)

def NSEC_TO_TICK(nsec): return ((nsec) / nsec_per_tick)

def NSEC_TO_TICK_ROUNDUP(nsec): return \

def TIMEVAL_TO_TICK(tvp): return \

def TIMESTRUC_TO_TICK(tsp): return \


# Included from time.h
from TYPES import *

# Included from iso/time_iso.h
NULL = 0L
NULL = 0
CLOCKS_PER_SEC = 1000000

# Included from sys/select.h
FD_SETSIZE = 65536
FD_SETSIZE = 1024
_NBBY = 8
NBBY = _NBBY
def FD_ZERO(p): return bzero((p), sizeof (*(p)))


# Included from sys/signal.h

# Included from sys/iso/signal_iso.h
SIGHUP = 1
SIGINT = 2
SIGQUIT = 3
SIGILL = 4
SIGTRAP = 5
SIGIOT = 6
SIGABRT = 6
SIGEMT = 7
SIGFPE = 8
SIGKILL = 9
SIGBUS = 10
SIGSEGV = 11
SIGSYS = 12
SIGPIPE = 13
SIGALRM = 14
SIGTERM = 15
SIGUSR1 = 16
SIGUSR2 = 17
SIGCLD = 18
SIGCHLD = 18
SIGPWR = 19
SIGWINCH = 20
SIGURG = 21
SIGPOLL = 22
SIGIO = SIGPOLL
SIGSTOP = 23
SIGTSTP = 24
SIGCONT = 25
SIGTTIN = 26
SIGTTOU = 27
SIGVTALRM = 28
SIGPROF = 29
SIGXCPU = 30
SIGXFSZ = 31
SIGWAITING = 32
SIGLWP = 33
SIGFREEZE = 34
SIGTHAW = 35
SIGCANCEL = 36
SIGLOST = 37
_SIGRTMIN = 38
_SIGRTMAX = 45
SIG_BLOCK = 1
SIG_UNBLOCK = 2
SIG_SETMASK = 3
SIGNO_MASK = 0xFF
SIGDEFER = 0x100
SIGHOLD = 0x200
SIGRELSE = 0x400
SIGIGNORE = 0x800
SIGPAUSE = 0x1000

# Included from sys/siginfo.h
from TYPES import *
SIGEV_NONE = 1
SIGEV_SIGNAL = 2
SIGEV_THREAD = 3
SI_NOINFO = 32767
SI_USER = 0
SI_LWP = (-1)
SI_QUEUE = (-2)
SI_TIMER = (-3)
SI_ASYNCIO = (-4)
SI_MESGQ = (-5)

# Included from sys/machsig.h
ILL_ILLOPC = 1
ILL_ILLOPN = 2
ILL_ILLADR = 3
ILL_ILLTRP = 4
ILL_PRVOPC = 5
ILL_PRVREG = 6
ILL_COPROC = 7
ILL_BADSTK = 8
NSIGILL = 8
EMT_TAGOVF = 1
EMT_CPCOVF = 2
NSIGEMT = 2
FPE_INTDIV = 1
FPE_INTOVF = 2
FPE_FLTDIV = 3
FPE_FLTOVF = 4
FPE_FLTUND = 5
FPE_FLTRES = 6
FPE_FLTINV = 7
FPE_FLTSUB = 8
NSIGFPE = 8
SEGV_MAPERR = 1
SEGV_ACCERR = 2
NSIGSEGV = 2
BUS_ADRALN = 1
BUS_ADRERR = 2
BUS_OBJERR = 3
NSIGBUS = 3
TRAP_BRKPT = 1
TRAP_TRACE = 2
TRAP_RWATCH = 3
TRAP_WWATCH = 4
TRAP_XWATCH = 5
NSIGTRAP = 5
CLD_EXITED = 1
CLD_KILLED = 2
CLD_DUMPED = 3
CLD_TRAPPED = 4
CLD_STOPPED = 5
CLD_CONTINUED = 6
NSIGCLD = 6
POLL_IN = 1
POLL_OUT = 2
POLL_MSG = 3
POLL_ERR = 4
POLL_PRI = 5
POLL_HUP = 6
NSIGPOLL = 6
PROF_SIG = 1
NSIGPROF = 1
SI_MAXSZ = 256
SI_MAXSZ = 128

# Included from sys/time_std_impl.h
from TYPES import *
SI32_MAXSZ = 128
def SI_CANQUEUE(c): return ((c) <= SI_QUEUE)

SA_NOCLDSTOP = 0x00020000
SA_ONSTACK = 0x00000001
SA_RESETHAND = 0x00000002
SA_RESTART = 0x00000004
SA_SIGINFO = 0x00000008
SA_NODEFER = 0x00000010
SA_NOCLDWAIT = 0x00010000
SA_WAITSIG = 0x00010000
NSIG = 46
MAXSIG = 45
S_SIGNAL = 1
S_SIGSET = 2
S_SIGACTION = 3
S_NONE = 4
MINSIGSTKSZ = 2048
SIGSTKSZ = 8192
SS_ONSTACK = 0x00000001
SS_DISABLE = 0x00000002
SN_PROC = 1
SN_CANCEL = 2
SN_SEND = 3

# Included from sys/ucontext.h
from TYPES import *

# Included from sys/regset.h
REG_CCR = (0)
REG_PSR = (0)
REG_PSR = (0)
REG_PC = (1)
REG_nPC = (2)
REG_Y = (3)
REG_G1 = (4)
REG_G2 = (5)
REG_G3 = (6)
REG_G4 = (7)
REG_G5 = (8)
REG_G6 = (9)
REG_G7 = (10)
REG_O0 = (11)
REG_O1 = (12)
REG_O2 = (13)
REG_O3 = (14)
REG_O4 = (15)
REG_O5 = (16)
REG_O6 = (17)
REG_O7 = (18)
REG_ASI = (19)
REG_FPRS = (20)
REG_PS = REG_PSR
REG_SP = REG_O6
REG_R0 = REG_O0
REG_R1 = REG_O1
_NGREG = 21
_NGREG = 19
NGREG = _NGREG
_NGREG32 = 19
_NGREG64 = 21
SPARC_MAXREGWINDOW = 31
MAXFPQ = 16
XRS_ID = 0x78727300

# Included from v7/sys/privregs.h

# Included from v7/sys/psr.h
PSR_CWP = 0x0000001F
PSR_ET = 0x00000020
PSR_PS = 0x00000040
PSR_S = 0x00000080
PSR_PIL = 0x00000F00
PSR_EF = 0x00001000
PSR_EC = 0x00002000
PSR_RSV = 0x000FC000
PSR_ICC = 0x00F00000
PSR_C = 0x00100000
PSR_V = 0x00200000
PSR_Z = 0x00400000
PSR_N = 0x00800000
PSR_VER = 0x0F000000
PSR_IMPL = 0xF0000000
PSL_ALLCC = PSR_ICC
PSL_USER = (PSR_S)
PSL_USERMASK = (PSR_ICC)
PSL_UBITS = (PSR_ICC|PSR_EF)
def USERMODE(ps): return (((ps) & PSR_PS) == 0)


# Included from sys/fsr.h
FSR_CEXC = 0x0000001f
FSR_AEXC = 0x000003e0
FSR_FCC = 0x00000c00
FSR_PR = 0x00001000
FSR_QNE = 0x00002000
FSR_FTT = 0x0001c000
FSR_VER = 0x000e0000
FSR_TEM = 0x0f800000
FSR_RP = 0x30000000
FSR_RD = 0xc0000000
FSR_VER_SHIFT = 17
FSR_FCC1 = 0x00000003
FSR_FCC2 = 0x0000000C
FSR_FCC3 = 0x00000030
FSR_CEXC_NX = 0x00000001
FSR_CEXC_DZ = 0x00000002
FSR_CEXC_UF = 0x00000004
FSR_CEXC_OF = 0x00000008
FSR_CEXC_NV = 0x00000010
FSR_AEXC_NX = (0x1 << 5)
FSR_AEXC_DZ = (0x2 << 5)
FSR_AEXC_UF = (0x4 << 5)
FSR_AEXC_OF = (0x8 << 5)
FSR_AEXC_NV = (0x10 << 5)
FTT_NONE = 0
FTT_IEEE = 1
FTT_UNFIN = 2
FTT_UNIMP = 3
FTT_SEQ = 4
FTT_ALIGN = 5
FTT_DFAULT = 6
FSR_FTT_SHIFT = 14
FSR_FTT_IEEE = (FTT_IEEE   << FSR_FTT_SHIFT)
FSR_FTT_UNFIN = (FTT_UNFIN  << FSR_FTT_SHIFT)
FSR_FTT_UNIMP = (FTT_UNIMP  << FSR_FTT_SHIFT)
FSR_FTT_SEQ = (FTT_SEQ    << FSR_FTT_SHIFT)
FSR_FTT_ALIGN = (FTT_ALIGN  << FSR_FTT_SHIFT)
FSR_FTT_DFAULT = (FTT_DFAULT << FSR_FTT_SHIFT)
FSR_TEM_NX = (0x1 << 23)
FSR_TEM_DZ = (0x2 << 23)
FSR_TEM_UF = (0x4 << 23)
FSR_TEM_OF = (0x8 << 23)
FSR_TEM_NV = (0x10 << 23)
RP_DBLEXT = 0
RP_SINGLE = 1
RP_DOUBLE = 2
RP_RESERVED = 3
RD_NEAR = 0
RD_ZER0 = 1
RD_POSINF = 2
RD_NEGINF = 3
FPRS_DL = 0x1
FPRS_DU = 0x2
FPRS_FEF = 0x4
PIL_MAX = 0xf
def SAVE_GLOBALS(RP): return \

def RESTORE_GLOBALS(RP): return \

def SAVE_OUTS(RP): return \

def RESTORE_OUTS(RP): return \

def SAVE_WINDOW(SBP): return \

def RESTORE_WINDOW(SBP): return \

def STORE_FPREGS(FP): return \

def LOAD_FPREGS(FP): return \

_SPARC_MAXREGWINDOW = 31
_XRS_ID = 0x78727300
GETCONTEXT = 0
SETCONTEXT = 1
UC_SIGMASK = 001
UC_STACK = 002
UC_CPU = 004
UC_MAU = 010
UC_FPU = UC_MAU
UC_INTR = 020
UC_ASR = 040
UC_MCONTEXT = (UC_CPU|UC_FPU|UC_ASR)
UC_ALL = (UC_SIGMASK|UC_STACK|UC_MCONTEXT)
_SIGQUEUE_MAX = 32
_SIGNOTIFY_MAX = 32

# Included from sys/pcb.h
INSTR_VALID = 0x02
NORMAL_STEP = 0x04
WATCH_STEP = 0x08
CPC_OVERFLOW = 0x10
ASYNC_HWERR = 0x20
STEP_NONE = 0
STEP_REQUESTED = 1
STEP_ACTIVE = 2
STEP_WASACTIVE = 3

# Included from sys/msacct.h
LMS_USER = 0
LMS_SYSTEM = 1
LMS_TRAP = 2
LMS_TFAULT = 3
LMS_DFAULT = 4
LMS_KFAULT = 5
LMS_USER_LOCK = 6
LMS_SLEEP = 7
LMS_WAIT_CPU = 8
LMS_STOPPED = 9
NMSTATES = 10

# Included from sys/lwp.h

# Included from sys/synch.h
from TYPES import *
USYNC_THREAD = 0x00
USYNC_PROCESS = 0x01
LOCK_NORMAL = 0x00
LOCK_ERRORCHECK = 0x02
LOCK_RECURSIVE = 0x04
USYNC_PROCESS_ROBUST = 0x08
LOCK_PRIO_NONE = 0x00
LOCK_PRIO_INHERIT = 0x10
LOCK_PRIO_PROTECT = 0x20
LOCK_STALL_NP = 0x00
LOCK_ROBUST_NP = 0x40
LOCK_OWNERDEAD = 0x1
LOCK_NOTRECOVERABLE = 0x2
LOCK_INITED = 0x4
LOCK_UNMAPPED = 0x8
LWP_DETACHED = 0x00000040
LWP_SUSPENDED = 0x00000080
__LWP_ASLWP = 0x00000100
MAXSYSARGS = 8
NORMALRETURN = 0
JUSTRETURN = 1
LWP_USER = 0x01
LWP_SYS = 0x02
TS_FREE = 0x00
TS_SLEEP = 0x01
TS_RUN = 0x02
TS_ONPROC = 0x04
TS_ZOMB = 0x08
TS_STOPPED = 0x10
T_INTR_THREAD = 0x0001
T_WAKEABLE = 0x0002
T_TOMASK = 0x0004
T_TALLOCSTK = 0x0008
T_WOULDBLOCK = 0x0020
T_DONTBLOCK = 0x0040
T_DONTPEND = 0x0080
T_SYS_PROF = 0x0100
T_WAITCVSEM = 0x0200
T_WATCHPT = 0x0400
T_PANIC = 0x0800
TP_HOLDLWP = 0x0002
TP_TWAIT = 0x0004
TP_LWPEXIT = 0x0008
TP_PRSTOP = 0x0010
TP_CHKPT = 0x0020
TP_EXITLWP = 0x0040
TP_PRVSTOP = 0x0080
TP_MSACCT = 0x0100
TP_STOPPING = 0x0200
TP_WATCHPT = 0x0400
TP_PAUSE = 0x0800
TP_CHANGEBIND = 0x1000
TS_LOAD = 0x0001
TS_DONT_SWAP = 0x0002
TS_SWAPENQ = 0x0004
TS_ON_SWAPQ = 0x0008
TS_CSTART = 0x0100
TS_UNPAUSE = 0x0200
TS_XSTART = 0x0400
TS_PSTART = 0x0800
TS_RESUME = 0x1000
TS_CREATE = 0x2000
TS_ALLSTART = \
        (TS_CSTART|TS_UNPAUSE|TS_XSTART|TS_PSTART|TS_RESUME|TS_CREATE)
def CPR_VSTOPPED(t): return \

def THREAD_TRANSITION(tp): return thread_transition(tp);

def THREAD_STOP(tp): return \

def THREAD_ZOMB(tp): return THREAD_SET_STATE(tp, TS_ZOMB, NULL)

def SEMA_HELD(x): return (sema_held((x)))

NO_LOCKS_HELD = 1
NO_COMPETING_THREADS = 1
FMNAMESZ = 8

# Included from sys/systm.h
from TYPES import *

# Included from sys/proc.h

# Included from sys/cred.h

# Included from sys/user.h
from TYPES import *

# Included from sys/resource.h
from TYPES import *
PRIO_PROCESS = 0
PRIO_PGRP = 1
PRIO_USER = 2
RLIMIT_CPU = 0
RLIMIT_FSIZE = 1
RLIMIT_DATA = 2
RLIMIT_STACK = 3
RLIMIT_CORE = 4
RLIMIT_NOFILE = 5
RLIMIT_VMEM = 6
RLIMIT_AS = RLIMIT_VMEM
RLIM_NLIMITS = 7
RLIM_INFINITY = (-3l)
RLIM_SAVED_MAX = (-2l)
RLIM_SAVED_CUR = (-1l)
RLIM_INFINITY = 0x7fffffff
RLIM_SAVED_MAX = 0x7ffffffe
RLIM_SAVED_CUR = 0x7ffffffd
RLIM32_INFINITY = 0x7fffffff
RLIM32_SAVED_MAX = 0x7ffffffe
RLIM32_SAVED_CUR = 0x7ffffffd

# Included from sys/model.h

# Included from sys/debug.h
def ASSERT64(x): return ASSERT(x)

def ASSERT32(x): return ASSERT(x)

DATAMODEL_MASK = 0x0FF00000
DATAMODEL_ILP32 = 0x00100000
DATAMODEL_LP64 = 0x00200000
DATAMODEL_NONE = 0
DATAMODEL_NATIVE = DATAMODEL_LP64
DATAMODEL_NATIVE = DATAMODEL_ILP32
def STRUCT_SIZE(handle): return \

def STRUCT_BUF(handle): return ((handle).ptr.m64)

def SIZEOF_PTR(umodel): return \

def STRUCT_SIZE(handle): return (sizeof (*(handle).ptr))

def STRUCT_BUF(handle): return ((handle).ptr)

def SIZEOF_PTR(umodel): return sizeof (caddr_t)

def lwp_getdatamodel(t): return DATAMODEL_ILP32

RUSAGE_SELF = 0
RUSAGE_CHILDREN = -1

# Included from sys/auxv.h
AT_NULL = 0
AT_IGNORE = 1
AT_EXECFD = 2
AT_PHDR = 3
AT_PHENT = 4
AT_PHNUM = 5
AT_PAGESZ = 6
AT_BASE = 7
AT_FLAGS = 8
AT_ENTRY = 9
AT_DCACHEBSIZE = 10
AT_ICACHEBSIZE = 11
AT_UCACHEBSIZE = 12
AT_SUN_UID = 2000
AT_SUN_RUID = 2001
AT_SUN_GID = 2002
AT_SUN_RGID = 2003
AT_SUN_LDELF = 2004
AT_SUN_LDSHDR = 2005
AT_SUN_LDNAME = 2006
AT_SUN_LPAGESZ = 2007
AT_SUN_PLATFORM = 2008
AT_SUN_HWCAP = 2009
AT_SUN_IFLUSH = 2010
AT_SUN_CPU = 2011
AT_SUN_EMUL_ENTRY = 2012
AT_SUN_EMUL_EXECFD = 2013
AT_SUN_EXECNAME = 2014
AT_SUN_MMU = 2015

# Included from sys/errno.h
EPERM = 1
ENOENT = 2
ESRCH = 3
EINTR = 4
EIO = 5
ENXIO = 6
E2BIG = 7
ENOEXEC = 8
EBADF = 9
ECHILD = 10
EAGAIN = 11
ENOMEM = 12
EACCES = 13
EFAULT = 14
ENOTBLK = 15
EBUSY = 16
EEXIST = 17
EXDEV = 18
ENODEV = 19
ENOTDIR = 20
EISDIR = 21
EINVAL = 22
ENFILE = 23
EMFILE = 24
ENOTTY = 25
ETXTBSY = 26
EFBIG = 27
ENOSPC = 28
ESPIPE = 29
EROFS = 30
EMLINK = 31
EPIPE = 32
EDOM = 33
ERANGE = 34
ENOMSG = 35
EIDRM = 36
ECHRNG = 37
EL2NSYNC = 38
EL3HLT = 39
EL3RST = 40
ELNRNG = 41
EUNATCH = 42
ENOCSI = 43
EL2HLT = 44
EDEADLK = 45
ENOLCK = 46
ECANCELED = 47
ENOTSUP = 48
EDQUOT = 49
EBADE = 50
EBADR = 51
EXFULL = 52
ENOANO = 53
EBADRQC = 54
EBADSLT = 55
EDEADLOCK = 56
EBFONT = 57
EOWNERDEAD = 58
ENOTRECOVERABLE = 59
ENOSTR = 60
ENODATA = 61
ETIME = 62
ENOSR = 63
ENONET = 64
ENOPKG = 65
EREMOTE = 66
ENOLINK = 67
EADV = 68
ESRMNT = 69
ECOMM = 70
EPROTO = 71
ELOCKUNMAPPED = 72
ENOTACTIVE = 73
EMULTIHOP = 74
EBADMSG = 77
ENAMETOOLONG = 78
EOVERFLOW = 79
ENOTUNIQ = 80
EBADFD = 81
EREMCHG = 82
ELIBACC = 83
ELIBBAD = 84
ELIBSCN = 85
ELIBMAX = 86
ELIBEXEC = 87
EILSEQ = 88
ENOSYS = 89
ELOOP = 90
ERESTART = 91
ESTRPIPE = 92
ENOTEMPTY = 93
EUSERS = 94
ENOTSOCK = 95
EDESTADDRREQ = 96
EMSGSIZE = 97
EPROTOTYPE = 98
ENOPROTOOPT = 99
EPROTONOSUPPORT = 120
ESOCKTNOSUPPORT = 121
EOPNOTSUPP = 122
EPFNOSUPPORT = 123
EAFNOSUPPORT = 124
EADDRINUSE = 125
EADDRNOTAVAIL = 126
ENETDOWN = 127
ENETUNREACH = 128
ENETRESET = 129
ECONNABORTED = 130
ECONNRESET = 131
ENOBUFS = 132
EISCONN = 133
ENOTCONN = 134
ESHUTDOWN = 143
ETOOMANYREFS = 144
ETIMEDOUT = 145
ECONNREFUSED = 146
EHOSTDOWN = 147
EHOSTUNREACH = 148
EWOULDBLOCK = EAGAIN
EALREADY = 149
EINPROGRESS = 150
ESTALE = 151
PSARGSZ = 80
PSCOMSIZ = 14
MAXCOMLEN = 16
__KERN_NAUXV_IMPL = 19
__KERN_NAUXV_IMPL = 21
__KERN_NAUXV_IMPL = 21
PSARGSZ = 80

# Included from sys/watchpoint.h
from TYPES import *

# Included from vm/seg_enum.h

# Included from sys/copyops.h
from TYPES import *

# Included from sys/buf.h

# Included from sys/kstat.h
from TYPES import *
KSTAT_STRLEN = 31
def KSTAT_ENTER(k): return \

def KSTAT_EXIT(k): return \

KSTAT_TYPE_RAW = 0
KSTAT_TYPE_NAMED = 1
KSTAT_TYPE_INTR = 2
KSTAT_TYPE_IO = 3
KSTAT_TYPE_TIMER = 4
KSTAT_NUM_TYPES = 5
KSTAT_FLAG_VIRTUAL = 0x01
KSTAT_FLAG_VAR_SIZE = 0x02
KSTAT_FLAG_WRITABLE = 0x04
KSTAT_FLAG_PERSISTENT = 0x08
KSTAT_FLAG_DORMANT = 0x10
KSTAT_FLAG_INVALID = 0x20
KSTAT_READ = 0
KSTAT_WRITE = 1
KSTAT_DATA_CHAR = 0
KSTAT_DATA_INT32 = 1
KSTAT_DATA_UINT32 = 2
KSTAT_DATA_INT64 = 3
KSTAT_DATA_UINT64 = 4
KSTAT_DATA_LONG = KSTAT_DATA_INT32
KSTAT_DATA_ULONG = KSTAT_DATA_UINT32
KSTAT_DATA_LONG = KSTAT_DATA_INT64
KSTAT_DATA_ULONG = KSTAT_DATA_UINT64
KSTAT_DATA_LONG = 7
KSTAT_DATA_ULONG = 8
KSTAT_DATA_LONGLONG = KSTAT_DATA_INT64
KSTAT_DATA_ULONGLONG = KSTAT_DATA_UINT64
KSTAT_DATA_FLOAT = 5
KSTAT_DATA_DOUBLE = 6
KSTAT_INTR_HARD = 0
KSTAT_INTR_SOFT = 1
KSTAT_INTR_WATCHDOG = 2
KSTAT_INTR_SPURIOUS = 3
KSTAT_INTR_MULTSVC = 4
KSTAT_NUM_INTRS = 5
B_BUSY = 0x0001
B_DONE = 0x0002
B_ERROR = 0x0004
B_PAGEIO = 0x0010
B_PHYS = 0x0020
B_READ = 0x0040
B_WRITE = 0x0100
B_KERNBUF = 0x0008
B_WANTED = 0x0080
B_AGE = 0x000200
B_ASYNC = 0x000400
B_DELWRI = 0x000800
B_STALE = 0x001000
B_DONTNEED = 0x002000
B_REMAPPED = 0x004000
B_FREE = 0x008000
B_INVAL = 0x010000
B_FORCE = 0x020000
B_HEAD = 0x040000
B_NOCACHE = 0x080000
B_TRUNC = 0x100000
B_SHADOW = 0x200000
B_RETRYWRI = 0x400000
def notavail(bp): return \

def BWRITE(bp): return \

def BWRITE2(bp): return \


# Included from sys/aio_req.h

# Included from sys/uio.h
from TYPES import *
WP_NOWATCH = 0x01
WP_SETPROT = 0x02

# Included from sys/timer.h
from TYPES import *
_TIMER_MAX = 32
ITLK_LOCKED = 0x01
ITLK_WANTED = 0x02
ITLK_REMOVE = 0x04
IT_PERLWP = 0x01
IT_SIGNAL = 0x02

# Included from sys/utrap.h
UT_INSTRUCTION_DISABLED = 1
UT_INSTRUCTION_ERROR = 2
UT_INSTRUCTION_PROTECTION = 3
UT_ILLTRAP_INSTRUCTION = 4
UT_ILLEGAL_INSTRUCTION = 5
UT_PRIVILEGED_OPCODE = 6
UT_FP_DISABLED = 7
UT_FP_EXCEPTION_IEEE_754 = 8
UT_FP_EXCEPTION_OTHER = 9
UT_TAG_OVERFLOW = 10
UT_DIVISION_BY_ZERO = 11
UT_DATA_EXCEPTION = 12
UT_DATA_ERROR = 13
UT_DATA_PROTECTION = 14
UT_MEM_ADDRESS_NOT_ALIGNED = 15
UT_PRIVILEGED_ACTION = 16
UT_ASYNC_DATA_ERROR = 17
UT_TRAP_INSTRUCTION_16 = 18
UT_TRAP_INSTRUCTION_17 = 19
UT_TRAP_INSTRUCTION_18 = 20
UT_TRAP_INSTRUCTION_19 = 21
UT_TRAP_INSTRUCTION_20 = 22
UT_TRAP_INSTRUCTION_21 = 23
UT_TRAP_INSTRUCTION_22 = 24
UT_TRAP_INSTRUCTION_23 = 25
UT_TRAP_INSTRUCTION_24 = 26
UT_TRAP_INSTRUCTION_25 = 27
UT_TRAP_INSTRUCTION_26 = 28
UT_TRAP_INSTRUCTION_27 = 29
UT_TRAP_INSTRUCTION_28 = 30
UT_TRAP_INSTRUCTION_29 = 31
UT_TRAP_INSTRUCTION_30 = 32
UT_TRAP_INSTRUCTION_31 = 33
UTRAP_V8P_FP_DISABLED = UT_FP_DISABLED
UTRAP_V8P_MEM_ADDRESS_NOT_ALIGNED = UT_MEM_ADDRESS_NOT_ALIGNED
UT_PRECISE_MAXTRAPS = 33

# Included from sys/refstr.h

# Included from sys/task.h
from TYPES import *
TASK_NORMAL = 0x0
TASK_FINAL = 0x1
TASK_FINALITY = 0x1

# Included from sys/id_space.h
from TYPES import *

# Included from sys/vmem.h
from TYPES import *
VM_SLEEP = 0x00000000
VM_NOSLEEP = 0x00000001
VM_PANIC = 0x00000002
VM_KMFLAGS = 0x000000ff
VM_BESTFIT = 0x00000100
VMEM_ALLOC = 0x01
VMEM_FREE = 0x02
VMEM_SPAN = 0x10
ISP_NORMAL = 0x0
ISP_RESERVE = 0x1

# Included from sys/exacct_impl.h
from TYPES import *

# Included from sys/kmem.h
from TYPES import *
KM_SLEEP = 0x0000
KM_NOSLEEP = 0x0001
KM_PANIC = 0x0002
KM_VMFLAGS = 0x00ff
KM_FLAGS = 0xffff
KMC_NOTOUCH = 0x00010000
KMC_NODEBUG = 0x00020000
KMC_NOMAGAZINE = 0x00040000
KMC_NOHASH = 0x00080000
KMC_QCACHE = 0x00100000
_ISA_IA32 = 0
_ISA_IA64 = 1
SSLEEP = 1
SRUN = 2
SZOMB = 3
SSTOP = 4
SIDL = 5
SONPROC = 6
CLDPEND = 0x0001
CLDCONT = 0x0002
SSYS = 0x00000001
STRC = 0x00000002
SLOAD = 0x00000008
SLOCK = 0x00000010
SPREXEC = 0x00000020
SPROCTR = 0x00000040
SPRFORK = 0x00000080
SKILLED = 0x00000100
SULOAD = 0x00000200
SRUNLCL = 0x00000400
SBPTADJ = 0x00000800
SKILLCL = 0x00001000
SOWEUPC = 0x00002000
SEXECED = 0x00004000
SPASYNC = 0x00008000
SJCTL = 0x00010000
SNOWAIT = 0x00020000
SVFORK = 0x00040000
SVFWAIT = 0x00080000
EXITLWPS = 0x00100000
HOLDFORK = 0x00200000
SWAITSIG = 0x00400000
HOLDFORK1 = 0x00800000
COREDUMP = 0x01000000
SMSACCT = 0x02000000
ASLWP = 0x04000000
SPRLOCK = 0x08000000
NOCD = 0x10000000
HOLDWATCH = 0x20000000
SMSFORK = 0x40000000
SDOCORE = 0x80000000
FORREAL = 0
JUSTLOOKING = 1
SUSPEND_NORMAL = 0
SUSPEND_PAUSE = 1
NOCLASS = (-1)

# Included from sys/dditypes.h
DDI_DEVICE_ATTR_V0 = 0x0001
DDI_NEVERSWAP_ACC = 0x00
DDI_STRUCTURE_LE_ACC = 0x01
DDI_STRUCTURE_BE_ACC = 0x02
DDI_STRICTORDER_ACC = 0x00
DDI_UNORDERED_OK_ACC = 0x01
DDI_MERGING_OK_ACC = 0x02
DDI_LOADCACHING_OK_ACC = 0x03
DDI_STORECACHING_OK_ACC = 0x04
DDI_DATA_SZ01_ACC = 1
DDI_DATA_SZ02_ACC = 2
DDI_DATA_SZ04_ACC = 4
DDI_DATA_SZ08_ACC = 8
VERS_ACCHDL = 0x0001
DEVID_NONE = 0
DEVID_SCSI3_WWN = 1
DEVID_SCSI_SERIAL = 2
DEVID_FAB = 3
DEVID_ENCAP = 4
DEVID_MAXTYPE = 4

# Included from sys/varargs.h

# Included from sys/va_list.h
VA_ALIGN = 8
def _ARGSIZEOF(t): return ((sizeof (t) + VA_ALIGN - 1) & ~(VA_ALIGN - 1))

VA_ALIGN = 8
def _ARGSIZEOF(t): return ((sizeof (t) + VA_ALIGN - 1) & ~(VA_ALIGN - 1))

NSYSCALL = 256
SE_32RVAL1 = 0x0
SE_32RVAL2 = 0x1
SE_64RVAL = 0x2
SE_RVAL_MASK = 0x3
SE_LOADABLE = 0x08
SE_LOADED = 0x10
SE_NOUNLOAD = 0x20
SE_ARGC = 0x40

# Included from sys/devops.h
from TYPES import *

# Included from sys/poll.h
POLLIN = 0x0001
POLLPRI = 0x0002
POLLOUT = 0x0004
POLLRDNORM = 0x0040
POLLWRNORM = POLLOUT
POLLRDBAND = 0x0080
POLLWRBAND = 0x0100
POLLNORM = POLLRDNORM
POLLERR = 0x0008
POLLHUP = 0x0010
POLLNVAL = 0x0020
POLLREMOVE = 0x0800
POLLRDDATA = 0x0200
POLLNOERR = 0x0400
POLLCLOSED = 0x8000

# Included from vm/as.h

# Included from vm/seg.h

# Included from sys/vnode.h
from TYPES import *
VROOT = 0x01
VNOCACHE = 0x02
VNOMAP = 0x04
VDUP = 0x08
VNOSWAP = 0x10
VNOMOUNT = 0x20
VISSWAP = 0x40
VSWAPLIKE = 0x80
VVFSLOCK = 0x100
VVFSWAIT = 0x200
VVMLOCK = 0x400
VDIROPEN = 0x800
VVMEXEC = 0x1000
VPXFS = 0x2000
AT_TYPE = 0x0001
AT_MODE = 0x0002
AT_UID = 0x0004
AT_GID = 0x0008
AT_FSID = 0x0010
AT_NODEID = 0x0020
AT_NLINK = 0x0040
AT_SIZE = 0x0080
AT_ATIME = 0x0100
AT_MTIME = 0x0200
AT_CTIME = 0x0400
AT_RDEV = 0x0800
AT_BLKSIZE = 0x1000
AT_NBLOCKS = 0x2000
AT_VCODE = 0x4000
AT_ALL = (AT_TYPE|AT_MODE|AT_UID|AT_GID|AT_FSID|AT_NODEID|\
                        AT_NLINK|AT_SIZE|AT_ATIME|AT_MTIME|AT_CTIME|\
                        AT_RDEV|AT_BLKSIZE|AT_NBLOCKS|AT_VCODE)
AT_STAT = (AT_MODE|AT_UID|AT_GID|AT_FSID|AT_NODEID|AT_NLINK|\
                        AT_SIZE|AT_ATIME|AT_MTIME|AT_CTIME|AT_RDEV)
AT_TIMES = (AT_ATIME|AT_MTIME|AT_CTIME)
AT_NOSET = (AT_NLINK|AT_RDEV|AT_FSID|AT_NODEID|AT_TYPE|\
                        AT_BLKSIZE|AT_NBLOCKS|AT_VCODE)
VSUID = 04000
VSGID = 02000
VSVTX = 01000
VREAD = 00400
VWRITE = 00200
VEXEC = 00100
MODEMASK = 07777
PERMMASK = 00777
def MANDMODE(mode): return (((mode) & (VSGID|(VEXEC>>3))) == VSGID)

VSA_ACL = 0x0001
VSA_ACLCNT = 0x0002
VSA_DFACL = 0x0004
VSA_DFACLCNT = 0x0008
LOOKUP_DIR = 0x01
DUMP_ALLOC = 0
DUMP_FREE = 1
DUMP_SCAN = 2
ATTR_UTIME = 0x01
ATTR_EXEC = 0x02
ATTR_COMM = 0x04
ATTR_HINT = 0x08
ATTR_REAL = 0x10

# Included from vm/faultcode.h
FC_HWERR = 0x1
FC_ALIGN = 0x2
FC_OBJERR = 0x3
FC_PROT = 0x4
FC_NOMAP = 0x5
FC_NOSUPPORT = 0x6
def FC_MAKE_ERR(e): return (((e) << 8) | FC_OBJERR)

def FC_CODE(fc): return ((fc) & 0xff)

def FC_ERRNO(fc): return ((unsigned)(fc) >> 8)


# Included from vm/hat.h
from TYPES import *

# Included from vm/page.h
PAGE_HASHAVELEN = 4
PAGE_HASHVPSHIFT = 6
PG_EXCL = 0x0001
PG_WAIT = 0x0002
PG_PHYSCONTIG = 0x0004
PG_MATCH_COLOR = 0x0008
PG_NORELOC = 0x0010
PG_FREE_LIST = 1
PG_CACHE_LIST = 2
PG_LIST_TAIL = 0
PG_LIST_HEAD = 1
def page_next_raw(PP): return page_nextn_raw((PP), 1)

PAGE_IO_INUSE = 0x1
PAGE_IO_WANTED = 0x2
PGREL_NOTREL = 0x1
PGREL_CLEAN = 0x2
PGREL_MOD = 0x3
P_FREE = 0x80
P_NORELOC = 0x40
def PP_SETAGED(pp): return ASSERT(PP_ISAGED(pp))

HAT_FLAGS_RESV = 0xFF000000
HAT_LOAD = 0x00
HAT_LOAD_LOCK = 0x01
HAT_LOAD_ADV = 0x04
HAT_LOAD_CONTIG = 0x10
HAT_LOAD_NOCONSIST = 0x20
HAT_LOAD_SHARE = 0x40
HAT_LOAD_REMAP = 0x80
HAT_RELOAD_SHARE = 0x100
HAT_PLAT_ATTR_MASK = 0xF00000
HAT_PROT_MASK = 0x0F
HAT_NOFAULT = 0x10
HAT_NOSYNC = 0x20
HAT_STRICTORDER = 0x0000
HAT_UNORDERED_OK = 0x0100
HAT_MERGING_OK = 0x0200
HAT_LOADCACHING_OK = 0x0300
HAT_STORECACHING_OK = 0x0400
HAT_ORDER_MASK = 0x0700
HAT_NEVERSWAP = 0x0000
HAT_STRUCTURE_BE = 0x1000
HAT_STRUCTURE_LE = 0x2000
HAT_ENDIAN_MASK = 0x3000
HAT_COW = 0x0001
HAT_UNLOAD = 0x00
HAT_UNLOAD_NOSYNC = 0x02
HAT_UNLOAD_UNLOCK = 0x04
HAT_UNLOAD_OTHER = 0x08
HAT_UNLOAD_UNMAP = 0x10
HAT_SYNC_DONTZERO = 0x00
HAT_SYNC_ZERORM = 0x01
HAT_SYNC_STOPON_REF = 0x02
HAT_SYNC_STOPON_MOD = 0x04
HAT_SYNC_STOPON_RM = (HAT_SYNC_STOPON_REF | HAT_SYNC_STOPON_MOD)
HAT_DUP_ALL = 1
HAT_DUP_COW = 2
HAT_MAP = 0x00
HAT_ADV_PGUNLOAD = 0x00
HAT_FORCE_PGUNLOAD = 0x01
P_MOD = 0x1
P_REF = 0x2
P_RO = 0x4
def hat_ismod(pp): return (hat_page_getattr(pp, P_MOD))

def hat_isref(pp): return (hat_page_getattr(pp, P_REF))

def hat_isro(pp): return (hat_page_getattr(pp, P_RO))

def hat_setmod(pp): return (hat_page_setattr(pp, P_MOD))

def hat_setref(pp): return (hat_page_setattr(pp, P_REF))

def hat_setrefmod(pp): return (hat_page_setattr(pp, P_REF|P_MOD))

def hat_clrmod(pp): return (hat_page_clrattr(pp, P_MOD))

def hat_clrref(pp): return (hat_page_clrattr(pp, P_REF))

def hat_clrrefmod(pp): return (hat_page_clrattr(pp, P_REF|P_MOD))

def hat_page_is_mapped(pp): return (hat_page_getshare(pp))

HAT_DONTALLOC = 0
HAT_ALLOC = 1
HRM_SHIFT = 4
HRM_BYTES = (1 << HRM_SHIFT)
HRM_PAGES = ((HRM_BYTES * NBBY) / 2)
HRM_PGPERBYTE = (NBBY/2)
HRM_PGBYTEMASK = (HRM_PGPERBYTE-1)
HRM_HASHSIZE = 0x200
HRM_HASHMASK = (HRM_HASHSIZE - 1)
HRM_BLIST_INCR = 0x200
HRM_SWSMONID = 1
SSL_NLEVELS = 4
SSL_BFACTOR = 4
SSL_LOG2BF = 2
SEGP_ASYNC_FLUSH = 0x1
SEGP_FORCE_WIRED = 0x2
SEGP_SUCCESS = 0
SEGP_FAIL = 1
def seg_pages(seg): return \

IE_NOMEM = -1
AS_PAGLCK = 0x80
AS_CLAIMGAP = 0x40
AS_UNMAPWAIT = 0x20
def AS_TYPE_64BIT(as_): return \

AS_LREP_LINKEDLIST = 0
AS_LREP_SKIPLIST = 1
AS_MUTATION_THRESH = 225
AH_DIR = 0x1
AH_LO = 0x0
AH_HI = 0x1
AH_CONTAIN = 0x2

# Included from sys/ddidmareq.h
DMA_UNIT_8 = 1
DMA_UNIT_16 = 2
DMA_UNIT_32 = 4
DMALIM_VER0 = ((0x86000000) + 0)
DDI_DMA_FORCE_PHYSICAL = 0x0100
DMA_ATTR_V0 = 0
DMA_ATTR_VERSION = DMA_ATTR_V0
DDI_DMA_CALLBACK_RUNOUT = 0
DDI_DMA_CALLBACK_DONE = 1
DDI_DMA_WRITE = 0x0001
DDI_DMA_READ = 0x0002
DDI_DMA_RDWR = (DDI_DMA_READ | DDI_DMA_WRITE)
DDI_DMA_REDZONE = 0x0004
DDI_DMA_PARTIAL = 0x0008
DDI_DMA_CONSISTENT = 0x0010
DDI_DMA_EXCLUSIVE = 0x0020
DDI_DMA_STREAMING = 0x0040
DDI_DMA_SBUS_64BIT = 0x2000
DDI_DMA_MAPPED = 0
DDI_DMA_MAPOK = 0
DDI_DMA_PARTIAL_MAP = 1
DDI_DMA_DONE = 2
DDI_DMA_NORESOURCES = -1
DDI_DMA_NOMAPPING = -2
DDI_DMA_TOOBIG = -3
DDI_DMA_TOOSMALL = -4
DDI_DMA_LOCKED = -5
DDI_DMA_BADLIMITS = -6
DDI_DMA_STALE = -7
DDI_DMA_BADATTR = -8
DDI_DMA_INUSE = -9
DDI_DMA_SYNC_FORDEV = 0x0
DDI_DMA_SYNC_FORCPU = 0x1
DDI_DMA_SYNC_FORKERNEL = 0x2

# Included from sys/ddimapreq.h

# Included from sys/mman.h
PROT_READ = 0x1
PROT_WRITE = 0x2
PROT_EXEC = 0x4
PROT_USER = 0x8
PROT_ZFOD = (PROT_READ | PROT_WRITE | PROT_EXEC | PROT_USER)
PROT_ALL = (PROT_READ | PROT_WRITE | PROT_EXEC | PROT_USER)
PROT_NONE = 0x0
MAP_SHARED = 1
MAP_PRIVATE = 2
MAP_TYPE = 0xf
MAP_FIXED = 0x10
MAP_NORESERVE = 0x40
MAP_ANON = 0x100
MAP_ANONYMOUS = MAP_ANON
MAP_RENAME = 0x20
PROC_TEXT = (PROT_EXEC | PROT_READ)
PROC_DATA = (PROT_READ | PROT_WRITE | PROT_EXEC)
SHARED = 0x10
PRIVATE = 0x20
VALID_ATTR = (PROT_READ|PROT_WRITE|PROT_EXEC|SHARED|PRIVATE)
PROT_EXCL = 0x20
_MAP_LOW32 = 0x80
_MAP_NEW = 0x80000000
from TYPES import *
MADV_NORMAL = 0
MADV_RANDOM = 1
MADV_SEQUENTIAL = 2
MADV_WILLNEED = 3
MADV_DONTNEED = 4
MADV_FREE = 5
MS_OLDSYNC = 0x0
MS_SYNC = 0x4
MS_ASYNC = 0x1
MS_INVALIDATE = 0x2
MC_SYNC = 1
MC_LOCK = 2
MC_UNLOCK = 3
MC_ADVISE = 4
MC_LOCKAS = 5
MC_UNLOCKAS = 6
MCL_CURRENT = 0x1
MCL_FUTURE = 0x2
DDI_MAP_VERSION = 0x0001
DDI_MF_USER_MAPPING = 0x1
DDI_MF_KERNEL_MAPPING = 0x2
DDI_MF_DEVICE_MAPPING = 0x4
DDI_ME_GENERIC = (-1)
DDI_ME_UNIMPLEMENTED = (-2)
DDI_ME_NORESOURCES = (-3)
DDI_ME_UNSUPPORTED = (-4)
DDI_ME_REGSPEC_RANGE = (-5)
DDI_ME_RNUMBER_RANGE = (-6)
DDI_ME_INVAL = (-7)

# Included from sys/ddipropdefs.h
def CELLS_1275_TO_BYTES(n): return ((n) * PROP_1275_CELL_SIZE)

def BYTES_TO_1275_CELLS(n): return ((n) / PROP_1275_CELL_SIZE)

PH_FROM_PROM = 0x01
DDI_PROP_SUCCESS = 0
DDI_PROP_NOT_FOUND = 1
DDI_PROP_UNDEFINED = 2
DDI_PROP_NO_MEMORY = 3
DDI_PROP_INVAL_ARG = 4
DDI_PROP_BUF_TOO_SMALL = 5
DDI_PROP_CANNOT_DECODE = 6
DDI_PROP_CANNOT_ENCODE = 7
DDI_PROP_END_OF_DATA = 8
DDI_PROP_FOUND_1275 = 255
PROP_1275_INT_SIZE = 4
DDI_PROP_DONTPASS = 0x0001
DDI_PROP_CANSLEEP = 0x0002
DDI_PROP_SYSTEM_DEF = 0x0004
DDI_PROP_NOTPROM = 0x0008
DDI_PROP_DONTSLEEP = 0x0010
DDI_PROP_STACK_CREATE = 0x0020
DDI_PROP_UNDEF_IT = 0x0040
DDI_PROP_HW_DEF = 0x0080
DDI_PROP_TYPE_INT = 0x0100
DDI_PROP_TYPE_STRING = 0x0200
DDI_PROP_TYPE_BYTE = 0x0400
DDI_PROP_TYPE_COMPOSITE = 0x0800
DDI_PROP_TYPE_ANY = (DDI_PROP_TYPE_INT  |       \
                                        DDI_PROP_TYPE_STRING    |       \
                                        DDI_PROP_TYPE_BYTE      |       \
                                        DDI_PROP_TYPE_COMPOSITE)
DDI_PROP_TYPE_MASK = (DDI_PROP_TYPE_INT |       \
                                        DDI_PROP_TYPE_STRING    |       \
                                        DDI_PROP_TYPE_BYTE      |       \
                                        DDI_PROP_TYPE_COMPOSITE)
DDI_RELATIVE_ADDRESSING = "relative-addressing"
DDI_GENERIC_ADDRESSING = "generic-addressing"

# Included from sys/ddidevmap.h
KMEM_PAGEABLE = 0x100
KMEM_NON_PAGEABLE = 0x200
UMEM_LOCKED = 0x400
UMEM_TRASH = 0x800
DEVMAP_OPS_REV = 1
DEVMAP_DEFAULTS = 0x00
DEVMAP_MAPPING_INVALID = 0x01
DEVMAP_ALLOW_REMAP = 0x02
DEVMAP_USE_PAGESIZE = 0x04
DEVMAP_SETUP_FLAGS = \
        (DEVMAP_MAPPING_INVALID | DEVMAP_ALLOW_REMAP | DEVMAP_USE_PAGESIZE)
DEVMAP_SETUP_DONE = 0x100
DEVMAP_LOCK_INITED = 0x200
DEVMAP_FAULTING = 0x400
DEVMAP_LOCKED = 0x800
DEVMAP_FLAG_LARGE = 0x1000
DDI_UMEM_SLEEP = 0x0
DDI_UMEM_NOSLEEP = 0x01
DDI_UMEM_PAGEABLE = 0x02
DDI_UMEM_TRASH = 0x04
DDI_UMEMLOCK_READ = 0x01
DDI_UMEMLOCK_WRITE = 0x02

# Included from sys/nexusdefs.h

# Included from sys/nexusintr.h
BUSO_REV = 4
BUSO_REV_3 = 3
BUSO_REV_4 = 4
DEVO_REV = 3
CB_REV = 1
DDI_IDENTIFIED = (0)
DDI_NOT_IDENTIFIED = (-1)
DDI_PROBE_FAILURE = ENXIO
DDI_PROBE_DONTCARE = 0
DDI_PROBE_PARTIAL = 1
DDI_PROBE_SUCCESS = 2
MAPDEV_REV = 1
from TYPES import *
D_NEW = 0x00
_D_OLD = 0x01
D_TAPE = 0x08
D_MTSAFE = 0x0020
_D_QNEXTLESS = 0x0040
_D_MTOCSHARED = 0x0080
D_MTOCEXCL = 0x0800
D_MTPUTSHARED = 0x1000
D_MTPERQ = 0x2000
D_MTQPAIR = 0x4000
D_MTPERMOD = 0x6000
D_MTOUTPERIM = 0x8000
_D_MTCBSHARED = 0x10000
D_MTINNER_MOD = (D_MTPUTSHARED|_D_MTOCSHARED|_D_MTCBSHARED)
D_MTOUTER_MOD = (D_MTOCEXCL)
D_MP = D_MTSAFE
D_64BIT = 0x200
D_SYNCSTR = 0x400
D_DEVMAP = 0x100
D_HOTPLUG = 0x4
SNDZERO = 0x001
SNDPIPE = 0x002
RNORM = 0x000
RMSGD = 0x001
RMSGN = 0x002
RMODEMASK = 0x003
RPROTDAT = 0x004
RPROTDIS = 0x008
RPROTNORM = 0x010
RPROTMASK = 0x01c
RFLUSHMASK = 0x020
RFLUSHPCPROT = 0x020
RERRNORM = 0x001
RERRNONPERSIST = 0x002
RERRMASK = (RERRNORM|RERRNONPERSIST)
WERRNORM = 0x004
WERRNONPERSIST = 0x008
WERRMASK = (WERRNORM|WERRNONPERSIST)
FLUSHR = 0x01
FLUSHW = 0x02
FLUSHRW = 0x03
FLUSHBAND = 0x04
MAPINOK = 0x01
NOMAPIN = 0x02
REMAPOK = 0x04
NOREMAP = 0x08
S_INPUT = 0x0001
S_HIPRI = 0x0002
S_OUTPUT = 0x0004
S_MSG = 0x0008
S_ERROR = 0x0010
S_HANGUP = 0x0020
S_RDNORM = 0x0040
S_WRNORM = S_OUTPUT
S_RDBAND = 0x0080
S_WRBAND = 0x0100
S_BANDURG = 0x0200
RS_HIPRI = 0x01
STRUIO_POSTPONE = 0x08
STRUIO_MAPIN = 0x10
MSG_HIPRI = 0x01
MSG_ANY = 0x02
MSG_BAND = 0x04
MSG_XPG4 = 0x08
MSG_IPEEK = 0x10
MSG_DISCARDTAIL = 0x20
MSG_HOLDSIG = 0x40
MSG_IGNERROR = 0x80
MSG_DELAYERROR = 0x100
MSG_IGNFLOW = 0x200
MSG_NOMARK = 0x400
MORECTL = 1
MOREDATA = 2
MUXID_ALL = (-1)
ANYMARK = 0x01
LASTMARK = 0x02
_INFTIM = -1
INFTIM = _INFTIM
