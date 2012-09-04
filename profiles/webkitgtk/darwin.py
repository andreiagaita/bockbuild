#!/usr/bin/python -B

import os
import sys

sys.path.append ('../..')

from bockbuild.darwinprofile import DarwinProfile
from packages import WebkitPackages

class WebkitDarwinProfile (DarwinProfile, WebkitPackages):
	def __init__ (self):
		DarwinProfile.__init__ (self)

		# these flags interfere with ccache, take them out
		self.env.set ('CPPFLAGS',          '')
		self.env.compile()
		self.env.export()

		WebkitPackages.__init__ (self)

		self_dir = os.path.realpath (os.path.dirname (sys.argv[0]))
		self.bundle_skeleton_dir = os.path.join (self_dir, 'skeleton.darwin')
		self.bundle_output_dir = os.path.join (self_dir, 'bundle.darwin')

		self.bundle_from_build = [
			'bin/mono',
			'lib/mono/2.0/gmcs.exe',
			'lib/mono/gac/Mono.Addins.CecilReflector',
			'lib/pango',
			'lib/gtk-2.0/2.10.0/loaders',
			'lib/gtk-2.0/2.10.0/engines',
			'lib/gtk-2.0/2.10.0/immodules',
			'lib/gdk-pixbuf-2.0/2.10.0/loaders',
			'share/locale',
			'etc/mono/config',
			'etc/mono/1.0/machine.config',
			'etc/mono/2.0/machine.config',
			'etc/mono/2.0/settings.map'
		]

	def bundle (self):
		webkit_path = os.path.join (self.prefix, 'lib', 'webkitgtk')
		os.environ['MONO_PATH'] = ':'.join ([
			webkit_path
		])

		DarwinProfile.bundle (self)

		import shutil
		import glob

		bin_path = os.path.join (self.bundle_macos_dir, 'Webkit')
		shutil.move (os.path.join (self.bundle_res_dir, 'bin', 'webkitgtk'), bin_path)
		os.chmod (bin_path, 0755)


WebkitDarwinProfile ().build ()
