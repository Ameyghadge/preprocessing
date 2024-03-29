from preprocessing import utils  
__version__='0.0.1'

def get_wordcounts(x):
	return utils._get_wordcounts(x)
def _get_charcounts(x):
	return utils._get_charcounts(x)

def _get_avg_wordlength(x):
	return utils._get_avg_wordlength(x)
def _get_stopwords_counts(x):
	return utils._get_stopwords_counts(x)
def _get_hashtag_counts(x):
	return utils._get_hashtag_counts(x)
def _get_mentions_counts(x):
	return utils._get_mentions_counts(x)
def get_mentions_counts(x):
	return utils._get_mentions_counts(x)
def _get_digit_counts(x):
	return utils._get_digit_counts(x)
def _get_uppercase_counts(x):
	return utils._get_uppercase_counts(x)
def _remove_html_tags(x):
	return utils._remove_html_tags(x)
def _remove_accented_chars(x):
	return utils._remove_accented_chars(x)
def _remove_stopwords(x):
	return utils._remove_stopwords(X)
def make_base(x):
	return utils.make_base(x)
def _remove_rarewords(x,n=20):
	return utils._remove_rarewords(x,n=20)
def _spelling_correction(x):
	return utils._spelling_correction(x)
