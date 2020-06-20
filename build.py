from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.build_policy = "missing"
    builder.upload = ("https://api.bintray.com/conan/matkonnerth/cpprepo", False, "upload_repo")
    builder.add(settings={"arch": "x86_64", "build_type": "Debug"},
                options={}, env_vars={}, build_requires={})
    builder.add(settings={"arch": "x86_64", "build_type": "RelWithDebInfo"},
                options={}, env_vars={}, build_requires={})   
    builder.run()
