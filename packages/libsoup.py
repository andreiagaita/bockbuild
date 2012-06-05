class LibsoupPackage (GnomeXzPackage):
	def __init__ (self):
		GnomePackage.__init__ (self, 'libsoup', '2.38', '1')
		self.configure_flags = [
			'--disable-gtk-doc',
			'--without-gnome'
		]

LibsoupPackage ()
