from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="realtimeregister",
    version="1.0.1",
    author="Makafeli",
    author_email="info@yasin.nu",
    description="Python SDK for Realtime Register API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/makafeli/Python-library-Realtime-Register",
    packages=find_packages(include=["realtimeregister", "realtimeregister.*"]),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "python-dateutil>=2.8.0"
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.0.0",
            "black>=21.0.0",
            "isort>=5.0.0",
            "mypy>=0.900",
            "types-requests>=2.25.0",
            "types-python-dateutil>=2.8.0"
        ]
    }
)