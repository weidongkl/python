import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weidong-gitee", 
    version="1.0.0",
    author="weidong",
    author_email="weidong@uniontech.com",
    description="a gitee utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/weidongkl",
    keywords='weidong utils',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[]
    # 包含数据
    include_package_data=True,
    python_requires='>=3.7',
)
