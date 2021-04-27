import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weidong-monitor",
    version="0.0.2",
    author="weidong",
    author_email="weidong@uniontech.com",
    description="A small test monitor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlabxxxx/monitor",
    keywords='monitor',
    entry_points={
        'console_scripts': ['weidong-monitor=monitor.main:main'],
    },
    packages=setuptools.find_packages(),
    install_requires=[
        'psutil'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
