from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bir-ph-jmit",
    version="1.0.0",
    author="JMIT",
    author_email="support@jmit.ph",
    description="Standard Bureau of Internal Revenue (BIR) Philippines Reports for ERPNext v15 CAS Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/bir-ph-jmit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Frappe",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "frappe>=14.0",
        "erpnext>=15.0",
    ],
)
