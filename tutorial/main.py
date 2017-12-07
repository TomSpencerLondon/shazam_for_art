from skimage import io
from scripts.painting_processor import PaintingProcessor
from sklearn.externals import joblib

test_image = io.imread('./test_images/lowry_179.jpg')
clf = joblib.load('model.pkl')
print(clf.predict([PaintingProcessor(test_image).flatten()]))
