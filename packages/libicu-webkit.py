class ICUPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'libicu', '4.5.2',
			source_dir_name = 'icu/source',
			sources = [
				'http://download.icu-project.org/files/icu4c/%{version}/icu4c-4_5_2-src.tgz'
			]

		)

		if Package.profile.name == 'darwin':
			configure_flags = ([
				'--disable-renaming'
			])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (1, len (self.sources)):
				self.sh ('patch -p0 < "%{sources[' + str (p) + ']}"')

ICUPackage()
