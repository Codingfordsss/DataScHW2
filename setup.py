from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz_game"
        ]
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple math quiz command-line game.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="<link-to-your-repository>",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
