from sklearn import datasets
import spacy_sentence_bert


try: 
    iris = datasets.load_iris()
    digits = datasets.load_digits()
    diabetes = datasets.load_diabetes()
    images = datasets.load_sample_images()
    breast_cancer = datasets.load_breast_cancer()

    datasets.fetch_20newsgroups()
    datasets.fetch_20newsgroups_vectorized()
    datasets.fetch_california_housing()
    datasets.fetch_covtype()
    datasets.fetch_kddcup99()
    datasets.fetch_lfw_pairs()
    datasets.fetch_lfw_people()
    datasets.fetch_olivetti_faces()
    datasets.fetch_openml()
    datasets.fetch_rcv1()
    datasets.fetch_species_distributions()

    nlp = spacy_sentence_bert.load_model('en_stsb_distilbert_base')
    nlp = spacy_sentence_bert.load_model('en_stsb_roberta_large')
    print('Nu är du redo!')
except Exception as e:
    print(e.message)


