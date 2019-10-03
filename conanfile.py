from conans import ConanFile, CMake, tools
import os

class mklDynamic(ConanFile):
    name = "nanoflann"
    version = "1.3.0"
    url = "https://github.com/jlblancoc/nanoflann"
    homepage = "https://github.com/jlblancoc/nanoflann"
    author = "Michael Gardner <mhgardner@berkeley.edu>"
    license = "BSD 2-Clause"   
    settings = {"os": None, "arch": ["x86_64"]}
    description = "A C++11 header-only library for Nearest Neighbor (NN) search with KD-trees"
    no_copy_source = True
    build_policy = "missing"
    
    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = ""
        if self.settings.os == "Windows":
            source_url = ("https://github.com/jlblancoc/nanoflann/archive/v1.3.0.zip")
        elif self.settings.os == "Macos":
            source_url = ("https://github.com/jlblancoc/nanoflann/archive/v1.3.0.tar.gz")
        elif self.settings.os == "Linux":
            source_url = ("https://github.com/jlblancoc/nanoflann/archive/v1.3.0.tar.gz")
        else:
            raise Exception("Binary does not exist for these settings")
        
        tools.get(source_url, destination=self._source_subfolder)        
        
    def package(self):
        include_folder = os.path.join(self._source_subfolder, "nanoflann-1.3.0/include")
        self.copy("LICENSE.txt", dst="licenses", src=self._source_subfolder + "/info")        
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
