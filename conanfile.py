# noqa: D100

from conan import ConanFile
from conan.tools.scm import Git
from conan.tools.files import copy


class dkmRecipe(ConanFile):    # noqa: D101
    name = "dkm"
    user = "gtel"
    channel = "stable"
    license = "MIT"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/darcamo/conan-dkm"
    description = ("This is a k-means clustering algorithm written in C++, "
                   "intended to be used as a header-only library. Requires "
                   "C++11. See https://github.com/genbattle/dkm")
    topics = ("k-means", "clustering")
    no_copy_source: True
    homepage = "https://github.com/genbattle/dkm"

    package_type = "header-library"

    def source(self):  # noqa: D102
        git = Git(self)
        git.clone(self.homepage, target=".")
        git.checkout(self.conan_data['sources'][self.version])

    def package(self):  # noqa: D102
        # This will also copy the "include" folder
        copy(self, "*.hpp", self.source_folder, self.package_folder)

    def package_info(self):  # noqa: D102
        # For header-only packages, libdirs and bindirs are not used
        # so it's necessary to set those as empty.
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
