
from .similarity_calculator import SimilarityCalculator
import numpy as np
from tqdm import tqdm

class BatchSimilarityCalculator(SimilarityCalculator):
    def calculate_similarity(self, output_path):
        num_phrases = len(self.phrases)
        similarity_matrix = np.zeros((num_phrases, num_phrases))

        for i in tqdm(range(num_phrases)):
            for j in range(num_phrases):
                similarity_matrix[i, j] = self.calculate_phrase_similarity(
                    self.phrases[i], self.phrases[j]
                )

        np.savetxt(output_path, similarity_matrix, delimiter=",")

    def calculate_phrase_similarity(self, phrase1, phrase2):
        raise NotImplementedError("Subclasses must implement this method.")
