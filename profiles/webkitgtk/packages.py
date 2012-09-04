import os
from bockbuild.darwinprofile import DarwinProfile
from bockbuild.gnomeprofile import GnomeProfile
from bockbuild.glickprofile import GlickProfile

class WebkitPackages:
	def __init__ (self):
		# Toolchain
		self.packages.extend ([
			'autoconf.py',
			'tar.py',
			'xz.py',
			'automake-1.11.3.py',
			'libtool.py',
			'gettext.py',
			'pkg-config.py',
		])

		# Base Libraries
		self.packages.extend ([
			'libpng.py',
			'libjpeg.py',
			'libxml2.py',
			'libffi.py',
			'libtiff.py',
			'freetype.py',
			'fontconfig.py',
			'pixman.py',
			'cairo.py',
			'glib-2.33.py',
			'libcroco.py',
			'pango.py',
			'atk.py',
			'intltool.py',
			'gdk-pixbuf.py',
			'gtk+.py',
			'gconf-dummy.py',
			'libgpg-error.py',
			'libgcrypt.py',
			'gmp.py',
			'nettle.py',
			'gnutls.py',
			'glib-networking.py',
			'libsoup-2.39.3.py',
			'sqlite.py',
		])

		# WebKit-gtk
		# TODO on darwin currently fails on the build stage
		# so don't include it on darwin for now
		#if not isinstance (self, DarwinProfile):
		self.packages.extend ([
		# WebKit-gtk dependencies
				'gperf.py',
				'enchant.py',
				'libicu-webkit.py',
				'zlib.py',
				'webkit.py'
			])

		# Theme
		self.packages.extend ([
			'librsvg.py',
			'icon-naming-utils.py',
			'hicolor-icon-theme.py',
			'tango-icon-theme.py',
			'murrine.py'
		])

		if isinstance (self, DarwinProfile):
			self.packages.extend ([
				'monomac.py',
				'gtk-mac-integration.py'
			])

		self.packages.append ('webkit.py')

		self.packages = [os.path.join ('..', '..', 'packages', p)
			for p in self.packages]
