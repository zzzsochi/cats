from setuptools import setup, find_packages

setup(
    name='cats',
    description='More cats to your life!',
    version='0.1.1',
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development",
    ],
    url='https://github.com/zzzsochi/cats',
    keywords=['cats', 'development'],
    packages=find_packages(),
    package_data={'cats.database': ['*.json']},
    install_requires=[],
    extras_require={'parse': ['aiohttp', 'beautifulsoup4', 'colorama']},
    entry_points={
        'console_scripts': [
            'cats = cats.__main__:main',
        ],
    },
)
