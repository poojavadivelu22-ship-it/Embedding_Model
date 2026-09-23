# Sentence Embedding and Semantic Similarity

## Introduction

Natural Language Processing (NLP) helps computers understand and process human language. In this project, sentences are converted into numerical representations called **embeddings** using the Sentence Transformers model. These embeddings capture the meaning of the sentences.

The project uses the **all-MiniLM-L6-v2** model to generate sentence embeddings and **Cosine Similarity** to measure how similar two sentences are in meaning. This helps identify sentences that have similar meanings even when their words are different.

## Project Description

This project demonstrates how sentences can be converted into numerical vectors called **embeddings** and how the semantic similarity between sentences can be calculated.

The project uses the **Sentence Transformers** library with the `all-MiniLM-L6-v2` model to generate sentence embeddings. It uses **Cosine Similarity** to find how similar two sentences are in meaning.

## Technologies Used

* Python
* Sentence Transformers
* Scikit-learn
* Cosine Similarity
* `all-MiniLM-L6-v2` model

## Libraries Required

Install the required libraries using:

```bash
pip install sentence-transformers
pip install scikit-learn
```

## How the Project Works

1. Load the Sentence Transformer model.
2. Store a set of sentences.
3. Convert the sentences into embeddings.
4. Display the embeddings.
5. Calculate cosine similarity between the embeddings.
6. Display sentence pairs with similarity greater than `0.5`.

## Project Structure

```text
Sentence_Transformer/
│
└── embeddingapp.py
```

## How to Run

Open the terminal in the project folder and run:

```bash
py embeddingapp.py
```

Or:

```bash
python embeddingapp.py
```

## Example

The project can identify sentences with similar meanings, such as:

```text
Sentence 1: My favorite food is pizza.
Sentence 2: I love eating cheese pizza.
```

The program calculates a similarity score between the two sentences.

## Output

The program displays:

* Total number of sentences
* Embedding dimension
* Sentence embeddings
* Semantically similar sentence pairs
* Cosine similarity score

Example:

```text
Total number of sentences: 8
Embedding dimension: 384

--- Embeddings ---

Sentence: I like playing cricket.
Embedding: [...]

--- Semantic Similarity ---

Sentence 1: My favorite food is pizza.
Sentence 2: I love eating cheese pizza.
Similarity: 0.XXXX
```

## Applications

Sentence embeddings and semantic similarity can be used in:

* Text similarity
* Search engines
* Question answering systems
* Recommendation systems
* Document comparison
* Chatbots
* Natural Language Processing (NLP)

## Conclusion

This project shows how Sentence Transformers can understand the meaning of sentences by converting them into embeddings. Cosine Similarity is then used to measure the similarity between sentences. This technique is useful in many NLP applications where understanding the meaning of text is important.
