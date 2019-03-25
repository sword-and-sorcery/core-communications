from conans import ConanFile, CMake

class CoreCommunications(ConanFile):
    name = "core-communications"
    version = "0.0"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    generators = "cmake"

    scm = {"type": "git",
           "url": "auto",
           "revision": "auto"}

    def requirements(self):
        self.requires("core-messages/0.0@sword/sorcery")
        self.requires("grpc/1.17.2@inexorgame/stable", private=True)  # Privacy depends on shared/static

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["communications",]
