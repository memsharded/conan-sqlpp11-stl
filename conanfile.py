from conans import ConanFile, tools
import os


class sqlpp11stlConan(ConanFile):
    name = "sqlpp11-stl"
    version = "0.4"
    license = "MIT"
    url = "https://github.com/memsharded/conan-sqlpp11"
    requires = "sqlpp11/0.38@memsharded/testing"
    # No settings/options are necessary, this is header only

    def source(self):
       self.run("git clone https://github.com/rbock/sqlpp11-connector-stl")
       self.run("cd sqlpp11-connector-stl && git checkout 0.4")

    def package(self):
        self.copy("*.h", dst="include", src="sqlpp11-connector-stl/include")
