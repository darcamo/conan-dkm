from conans import CMake, ConanFile, tools


class DkmConan(ConanFile):
    name = "dkm"
    version = "2018-11-23-ea62d93"
    license = "MIT"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/darcamo/conan-dkm"
    description = ("This is a k-means clustering algorithm written in C++, "
                   "intended to be used as a header-only library. Requires "
                   "C++11. See https://github.com/genbattle/dkm")
    no_copy_source = True
    homepage = "https://github.com/genbattle/dkm"

    def source(self):
        git = tools.Git(folder="dkm")
        commit_sha1 = self.version.split("-")[-1]
        git.clone(self.homepage)
        git.checkout(commit_sha1)

    def package(self):
        self.copy("include/*.hpp", src="dkm")

    def package_id(self):
        self.info.header_only()
