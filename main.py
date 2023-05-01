import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc
import matplotlib.pyplot as plt
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Veri setini yükle
df_olumlu = pd.read_csv('olumlu.csv')
df_olumsuz = pd.read_csv('olumsuz.csv')

df = pd.concat([df_olumlu, df_olumsuz], ignore_index=True)

# Öznitelikler ve hedef değişken ayrılır
X = df['Yorum']
y = df['Duygu']

# Stop words tanımlanır
def remove_stopwords(df):
    # Türkçe stopword'leri dosyadan okuduk
    with open('turkce-stop-words.txt', 'r') as f:
        stopwords = f.read().split()

    # Yorumlardan stopwords'leri kaldırdık ve aynı sütunun üzerine yazdık
    for i, yorum in enumerate(df['Yorum']):
        # Yorumu kelime listesine ayırdık
        yorum_kelimeleri = yorum.split()
        # Stopwords'leri kaldırdık
        yorum_kelimeleri_no_stopwords = [kelime for kelime in yorum_kelimeleri if kelime not in stopwords]
        # Kaldırılmış kelime listesini yorum sütununun üzerine yazdık
        df.loc[i, 'Yorum'] = ' '.join(yorum_kelimeleri_no_stopwords)

remove_stopwords(df)

# Veri seti eğitim ve test setlerine ayrılır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Metinleri vektörlere dönüştürmek için TfidfVectorizer kullanılır
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Logistic Regression modeli oluşturulur
model = LogisticRegression()

# Parametreler için arama yapılacak değerler belirlenir
param_grid = {'penalty': ['l2', 'none'], 'C': [0.1, 1, 10, 100]}
grid = GridSearchCV(model, param_grid, cv=5, n_jobs=-1, verbose=1, error_score='raise')


# Model eğitilir ve en iyi parametreler belirlenir
grid.fit(X_train_tfidf, y_train)
print("En iyi parametreler: ", grid.best_params_)

# Test seti üzerinde tahmin yapılır
y_pred = grid.predict(X_test_tfidf)

# Modelin doğruluğu hesaplanır
accuracy = accuracy_score(y_test, y_pred)
print("Model doğruluğu: ", accuracy)

# Örnek bir metin tanımı
text = "Bugün hava çok güzel."

# Metin, modelin anlayabileceği vektörlere dönüştürülür
text_tfidf = vectorizer.transform([text])

# Model, metnin duygusal yönünü tahmin eder
result = grid.predict(text_tfidf)

# Tahmin sonucunu yazdır
if result[0] == 1:
    print()
    print("------" ,text, "------")
    print()
    print("Örnek metin olumlu.")
else:
    print()
    print("------", text, "------")
    print()
    print("Örnek metin olumsuz.")


with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)