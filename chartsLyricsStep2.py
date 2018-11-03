from datetime import datetime, timedelta
import json
import pandas
from sklearn.feature_extraction.text import CountVectorizer

#  Analyse swiss charts data
#  from 7.10.2018 until 4.10.1998

data = []  # list of fetched data

def main():
    # read json data from file into pandas object
    path2data = 'data/charts_lyrics_1998-2018.json'
    data = pandas.read_json(path_or_buf=path2data, orient=None, typ='frame', dtype=True, convert_axes=True, convert_dates=True,
                     keep_default_dates=True, numpy=False, precise_float=False, date_unit=None, encoding='utf-8',
                     lines=False, chunksize=None, compression='infer')

    # process lyrics to word array
    # create dataframe with every word and its count - over whole time // per year

    vectorizer = CountVectorizer(stop_words='english')  # TODO: purge meaningless words like "and" "is" "in" - might be managed by scikit aka stopwords ? english yes, but what about the german ones ?
    X = vectorizer.fit_transform(data.lyrics)
    print(vectorizer.get_feature_names())
    print(vectorizer.get_stop_words())
    print(X.toarray())



if __name__ == '__main__':
    main()
