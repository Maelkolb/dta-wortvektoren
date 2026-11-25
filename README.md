# Wortvektoren aus dem Deutschen Textarchiv

A small page for exploring a word2vec model trained on the Deutsches Textarchiv (DTA). Type a word to see its nearest neighbours, or calculate with words (`könig - mann + frau`).

Live: https://maelkolb.github.io/dta-wortvektoren/

Built for the class "KI in den Geisteswissenschaften" (Universität Passau, winter term 2026/27).

## Model

- word2vec skip-gram, 300 dimensions, window 5, min_count 20, 5 epochs (gensim 4.3.3)
- Corpus: all DTA texts (DTA komplett, 10 Feb 2026), 165.7 million tokens, lowercased, long s as s
- The page holds the 40,000 most frequent words (at least 205 occurrences), quantized to 8 bits per value. Cosine similarities differ from the full model by about 0.001.

`index.html` is self-contained (data embedded) and also works offline. `build/` holds the export and page scripts.

## License

Texts: Deutsches Textarchiv, Berlin-Brandenburgische Akademie der Wissenschaften, CC BY-SA 4.0. The vectors on this page are derived from them and shared under the same license.
