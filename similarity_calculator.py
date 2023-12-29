
from word_embeddings.embeddings import WordEmbeddings
import pandas as pd

class SimilarityCalculator:
    def __init__(self, embeddings_model, phrases_path):
        self.embeddings_model = embeddings_model
        self.phrases = pd.read_csv("phrases.csv", encoding='utf-8')['phrase'].tolist()

    def calculate_similarity(self, output_path):
        raise NotImplementedError("Subclasses must implement this method.")
