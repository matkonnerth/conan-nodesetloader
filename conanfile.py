from conans import ConanFile, CMake, tools

class NodesetLoaderConan(ConanFile):
    name = "nodesetloader"
    version = "master"
    license = "Mozilla Public License v2.0"
    url = "https://github.com/matkonnerth/nodesetLoader"
    homepage = "https://github.com/matkonnerth/nodesetLoader"
    description = "open source C99 implementation for loading opc ua nodesets"
    topics = ("opcua", "open62541", "xmlimport")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = ("open62541/master@matkonnerth/testing", "libxml2/2.9.9")
    default_options = {"libxml2:shared": True}

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        self.run("git clone https://github.com/matkonnerth/nodesetLoader.git")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = "ON"
        cmake.definitions["ENABLE_BACKEND_OPEN62541"] = "ON"
        cmake.configure(source_folder="nodesetLoader")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        cmake.patch_config_paths()

    def package_info(self):
        self.cpp_info.libs = ["NodesetLoader"]
