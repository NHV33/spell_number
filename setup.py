from setuptools import setup, find_packages

setup(
    name="spell_number",
    version="0.1",
    packages=find_packages(),
    install_requires=[
    ],
    extras_require={
        'dev': ['pytest'],  # development dependency
    },
    entry_points={
        'console_scripts': [
            'spell-number=spell_number.spell_number:main',
        ],
    },
    author="Noel H. Vincent",
    author_email="noelvincent@me.com",
    description="A package to convert numbers to words",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/NHV33/spell_number",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
