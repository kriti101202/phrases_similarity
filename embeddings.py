
from gensim.models import KeyedVectors

class WordEmbeddings:
    def __init__(self, embeddings_path, limit=1000000):
        self.embeddings_path = embeddings_path
        self.limit = limit
        self.model = self.load_embeddings()

    def load_embeddings(self):
        return KeyedVectors.load_word2vec_format(
            self.embeddings_path, binary=True, limit=self.limit
        )

    def save_as_flat_file(self, output_path):
        self.model.save_word2vec_format(output_path)
