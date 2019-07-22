from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

file_list = ["Google headquarters is in California", "Steve Jobs was a great  man",
    "Steve Jobs has done great technology innovations"]

transformer = TfidfVectorizer().fit(file_list)
file_data = transformer.transform(file_list)
with open('transformer.pickle', 'wb') as handle:
    pickle.dump(transformer, handle, protocol=pickle.HIGHEST_PROTOCOL)
file_data = file_data.toarray()
with open('transformer.pickle', 'rb') as handle:
    transformer = pickle.load(handle)
transformed_file = transformer.transform([file_list[0]]).toarray(

print(file_data[0].shape)
# output: (14,)

print(transformed_file.shape)
# output: (1,14)

# why different output?
