class LibsoupPackage (GnomeXzPackage):
	def __init__ (self):
		GnomePackage.__init__ (self, 'libsoup', '2.39', '3')
		self.configure_flags = [
			'--disable-gtk-doc',
			'--without-gnome'
		]

LibsoupPackage ()
