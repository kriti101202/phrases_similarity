
from .similarity_calculator import SimilarityCalculator

class OnTheFlySimilarityCalculator(SimilarityCalculator):
    def find_closest_match(self, input_phrase):
        raise NotImplementedError("Subclasses must implement this method.")
