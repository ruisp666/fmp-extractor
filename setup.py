import setuptools

setuptools.setup(
    name='fmp_extractors',
    version='0.0.2',
    author="Rui Sa Pereira",
    description="A package to access Financial Modelling Prep API endpoints in a pandas-friendly way",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)