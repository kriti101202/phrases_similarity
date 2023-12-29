
from word_embeddings.embeddings import WordEmbeddings
from phrases_similarity.batch_similarity_calculator import BatchSimilarityCalculator
from phrases_similarity.on_the_fly_similarity_calculator import OnTheFlySimilarityCalculator

def main():
    embeddings_model = WordEmbeddings("word2vec.bin")
    embeddings_model.save_as_flat_file("vectors.csv")

    batch_calculator = BatchSimilarityCalculator(embeddings_model, "phrases.csv")
    batch_calculator.calculate_similarity("batch_similarity_matrix.csv")

    on_the_fly_calculator = OnTheFlySimilarityCalculator(embeddings_model, "phrases.csv")
    result = on_the_fly_calculator.find_closest_match("user-input phrase")
    print(result)

if __name__ == "__main__":
    main()
