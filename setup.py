import setuptools

setuptools.setup(
    name="mkdocs-same-dir",
    version="0.1.0",
    description="",
    keywords="mkdocs",
    url="https://github.com/oprypin/mkdocs-same-dir",
    author="Oleh Prypin",
    author_email="oleh@pryp.in",
    license="MIT",
    python_requires=">=3.6",
    install_requires=["mkdocs>=1"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=["mkdocs_same_dir"],
    entry_points={
        "mkdocs.plugins": ["same-dir = mkdocs_same_dir.plugin:SameDirPlugin"],
    },
)
