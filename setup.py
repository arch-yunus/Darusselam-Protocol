from setuptools import setup, find_packages

setup(
    name="darusselam",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
        "rich",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "dp-audit=scripts.dp_audit:main",
        ],
    },
    author="arch-yunus",
    description="Hanif Teknoloji Standartları ve Darusselam Protokolü Denetim Araçları",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
)
