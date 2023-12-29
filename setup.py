
from setuptools import setup, find_packages

setup(
    name="word_embeddings_pipeline",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "gensim",
        "pandas",
        "numpy",
        "tqdm"
    ],
)

  