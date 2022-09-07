from sklearn import datasets
import spacy_sentence_bert


try: 
    iris = datasets.load_iris()
    print('Iris redo')
    digits = datasets.load_digits()
    print('Digits redo')
    diabetes = datasets.load_diabetes()
    print('Diabetes redo')
    images = datasets.load_sample_images()
    print('Images redo')
    breast_cancer = datasets.load_breast_cancer()
    print('Breast cancer redo')

    datasets.fetch_20newsgroups()
    print('fetch_20newsgroups redo')
    datasets.fetch_20newsgroups_vectorized()
    print('fetch_20newsgroups_vectorized redo')
    datasets.fetch_california_housing()
    print('fetch_california_housing redo')
    datasets.fetch_covtype()
    print('fetch_covtype redo')
    datasets.fetch_kddcup99()
    print('fetch_kddcup99 redo')
    datasets.fetch_lfw_pairs()
    print('fetch_lfw_pairs redo')
    datasets.fetch_lfw_people()
    print('fetch_lfw_people redo')
    datasets.fetch_olivetti_faces()
    print('fetch_olivetti_faces redo')
    datasets.fetch_rcv1()
    print('fetch_rcv1 redo')
    datasets.fetch_species_distributions()
    print('fetch_species_distributions redo')

    nlp = spacy_sentence_bert.load_model('en_stsb_distilbert_base')
    print('en_stsb_distilbert_base redo')
    nlp = spacy_sentence_bert.load_model('en_stsb_roberta_large')
    print('en_stsb_roberta_large redo')
    print('Nu är du redo!')
except Exception as e:
    print(e)


