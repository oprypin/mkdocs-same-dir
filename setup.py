import setuptools

setuptools.setup(
    name="mkdocs-same-dir",
    install_requires=["mkdocs>=1"],
    packages=["mkdocs_same_dir"],
    entry_points={
        "mkdocs.plugins": ["same-dir = mkdocs_same_dir.plugin:SameDirPlugin"],
    },
)
