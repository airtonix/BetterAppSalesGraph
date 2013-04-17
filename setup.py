import os
import glob
from platform import platform

from distutils.core import setup
import matplotlib


PLATFORM = platform().lower()
HERE_DIR = os.path.abspath(os.path.dirname(__file__))
IS_LINUX = 'linux' in PLATFORM
IS_WINDOWS = 'windows' in PLATFORM
IS_MACOSX = 'macosx' in PLATFORM
APP = None
WINDOWS = None
OPTIONS = {}
SETUP_REQUIRES = [
    	'matplotlib',
    ]

def asset(path):
	if not isinstance(path, [list, set, tuple]):
		path = [path, ]
	return os.sep.join(['assets', ] + path_list ),

if IS_WINDOWS:
	import py2exe
	SETUP_REQUIRES.append('py2exe')
	OPTIONS['py2exe'] = {
			'packages' : ['matplotlib', 'pytz'],
			"dll_excludes": [
				"iconv.dll","intl.dll","libatk-1.0-0.dll",
				"libgdk_pixbuf-2.0-0.dll","libgdk-win32-2.0-0.dll",
				"libglib-2.0-0.dll","libgmodule-2.0-0.dll",
				"libgobject-2.0-0.dll","libgthread-2.0-0.dll",
				"libgtk-win32-2.0-0.dll","libpango-1.0-0.dll",
				"libpangowin32-1.0-0.dll"],
				"dist_dir" : 'dist_win',
			}
	WINDOWS = [
        {"script": "salesgraph.py",
        "icon_resources": [(1, "key.ico")]
        }
    ]

if IS_MACOSX:
	APP = [ 'salesgraph.py', ]
	SETUP_REQUIRES.append('py2app')
	OPTIONS['py2app']={
		'argv_emulation': True,
		'iconfile': asset(['icons','key.icns']),
	}

setup(
	name = "SalesGraph",
    version = app.__version__,
    description = "Software Sales Plotting Tool",
    app=APP,
    data_files=matplotlib.get_py2exe_datafiles() + (
		asset('images'),
		glob.glob(asset(['images','*.*'])),
		asset('sounds'),
		glob.glob(asset(['sounds','*.*'])),
		asset('icons'),
		glob.glob(asset(['icons','*.*'])),
		asset('keys'),
		glob.glob(asset(['keys','*.*'])),
	),
    options=OPTIONS,
    windows = WINDOWS,
    app = APP
    setup_requires=SETUP_REQUIRES,
)
