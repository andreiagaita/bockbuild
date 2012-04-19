class LibgcryptPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'libgcrypt', '1.5.0')

		if Package.profile.name == 'darwin' and Package.profile.os_x_minor >= 7:
			self.version = '1.5.0'
			self.configure_flags.extend(['--disable-asm'])

		# 1.5.0 does not compile with Xcode 3.x on Snow Leopard and Xcode4 is Lion only
		if Package.profile.name == 'darwin' and Package.profile.os_x_minor == 6:
			self.version = '1.4.6'
		
		self.sources = ['ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2']
		self.sources.extend (['patches/libgcrypt-asm.patch'])

        def prep (self):
                Package.prep (self)
                if Package.profile.name == 'darwin':
                        for p in range (1, len (self.sources)):
                                self.sh ('patch -p0 < "%{sources[' + str (p) + ']}"')				
LibgcryptPackage ()
