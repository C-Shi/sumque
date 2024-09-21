from setuptools import setup, find_packages

setup(
    name="SummaQueue",
    version="0.1.0",
    description="A Python package for AI/ML-based text summarization of files and directories.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Cheng Shi",
    author_email="mr.cheng.shi@gmail.com", 
    url="https://github.com/C-Shi/sumque",
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        "transformers>=4.0.0",
        "PyPDF2>=1.26.0",
        "python-docx>=0.8.10",
        "tqdm>=4.50.0",
        "torch>=1.7.0",
    ],
    entry_points={
        'console_scripts': [
            'summaqueue=summaqueue.summarizer:main',  # This makes it a command-line tool
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.6',  # Minimum Python version
)
