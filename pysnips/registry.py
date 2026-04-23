# pysnips/registry.py

SNIPPETS = {
    # 🔰 BASIC (15)
    "for": {
        "description": "Standard for loop over a range or iterable",
        "category": "BASIC",
        "template": """for {{item}} in {{iterable}}:
    {{# Action to perform}}
    print({{item}})"""
    },
    "while": {
        "description": "Standard while loop with a condition",
        "category": "BASIC",
        "template": """while {{condition}}:
    {{# Action to perform}}
    pass"""
    },
    "if": {
        "description": "Simple if statement",
        "category": "BASIC",
        "template": """if {{condition}}:
    {{# Action to perform}}
    pass"""
    },
    "ifelse": {
        "description": "If-else conditional block",
        "category": "BASIC",
        "template": """if {{condition}}:
    {{# Action if true}}
    pass
else:
    {{# Action if false}}
    pass"""
    },
    "elif": {
        "description": "If-elif-else conditional block",
        "category": "BASIC",
        "template": """if {{condition1}}:
    pass
elif {{condition2}}:
    pass
else:
    pass"""
    },
    "try": {
        "description": "Basic try-except block",
        "category": "BASIC",
        "template": """try:
    {{# Risky operation}}
    pass
except {{Exception}} as e:
    print(f"An error occurred: {e}")"""
    },
    "tryfull": {
        "description": "Full try-except-else-finally block",
        "category": "BASIC",
        "template": """try:
    {{# Risky operation}}
    pass
except {{Exception}} as e:
    print(f"Error: {e}")
else:
    {{# Runs if no exception}}
    pass
finally:
    {{# Always runs}}
    pass"""
    },
    "func": {
        "description": "Standard function definition",
        "category": "BASIC",
        "template": '''def {{name}}({{args}}):
    """{{docstring}}"""
    {{# Implementation}}
    pass'''
    },
    "rfunc": {
        "description": "Function with a return value",
        "category": "BASIC",
        "template": '''def {{name}}({{args}}) -> {{return_type}}:
    """{{docstring}}"""
    return {{value}}'''
    },
    "listcomp": {
        "description": "List comprehension",
        "category": "BASIC",
        "template": "[{{expression}} for {{item}} in {{iterable}} if {{condition}}]"
    },
    "dictcomp": {
        "description": "Dictionary comprehension",
        "category": "BASIC",
        "template": "{ {{key}}: {{value}} for {{item}} in {{iterable}} if {{condition}} }"
    },
    "setcomp": {
        "description": "Set comprehension",
        "category": "BASIC",
        "template": "{ {{item}} for {{item}} in {{iterable}} if {{condition}} }"
    },
    "lambda": {
        "description": "Anonymous lambda function",
        "category": "BASIC",
        "template": "{{name}} = lambda {{args}}: {{expression}}"
    },
    "maincheck": {
        "description": "Standard if __name__ == '__main__': block",
        "category": "BASIC",
        "template": """if __name__ == "__main__":
    {{# Entry point}}
    main()"""
    },
    "printfmt": {
        "description": "F-string formatted print",
        "category": "BASIC",
        "template": 'print(f"{{variable_name}} is { {{variable_name}} }")'
    },

    # 🤖 MACHINE LEARNING (10)
    "linear-reg": {
        "description": "Linear Regression using Scikit-Learn",
        "category": "MACHINE LEARNING",
        "template": """from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)"""
    },
    "logistic-reg": {
        "description": "Logistic Regression for classification",
        "category": "MACHINE LEARNING",
        "template": """from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)"""
    },
    "knn": {
        "description": "K-Nearest Neighbors classifier",
        "category": "MACHINE LEARNING",
        "template": """from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors={{n}})
model.fit(X_train, y_train)
y_pred = model.predict(X_test)"""
    },
    "svm": {
        "description": "Support Vector Machine classifier",
        "category": "MACHINE LEARNING",
        "template": """from sklearn.svm import SVC

model = SVC(kernel='{{kernel}}')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)"""
    },
    "decision-tree": {
        "description": "Decision Tree classifier",
        "category": "MACHINE LEARNING",
        "template": """from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)"""
    },
    "random-forest": {
        "description": "Random Forest classifier",
        "category": "MACHINE LEARNING",
        "template": """from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators={{n_estimators}})
model.fit(X_train, y_train)
y_pred = model.predict(X_test)"""
    },
    "naive-bayes": {
        "description": "Gaussian Naive Bayes classifier",
        "category": "MACHINE LEARNING",
        "template": """from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)"""
    },
    "kmeans": {
        "description": "K-Means clustering algorithm",
        "category": "MACHINE LEARNING",
        "template": """from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters={{clusters}}, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_"""
    },
    "pca": {
        "description": "Principal Component Analysis for dimensionality reduction",
        "category": "MACHINE LEARNING",
        "template": """from sklearn.decomposition import PCA

pca = PCA(n_components={{n}})
X_pca = pca.fit_transform(X)"""
    },
    "model-eval": {
        "description": "Classification report and confusion matrix",
        "category": "MACHINE LEARNING",
        "template": """from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))"""
    },

    # 🧠 DEEP LEARNING (10)
    "nn-basic": {
        "description": "Basic Keras Sequential model",
        "category": "DEEP LEARNING",
        "template": """from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense({{units}}, activation='relu', input_shape=({{input_shape}},)),
    Dense(1, activation='sigmoid')
])"""
    },
    "nn-compile": {
        "description": "Compile a Keras model",
        "category": "DEEP LEARNING",
        "template": """model.compile(
    optimizer='{{optimizer}}',
    loss='{{loss}}',
    metrics=['accuracy']
)"""
    },
    "nn-train": {
        "description": "Train a Keras model",
        "category": "DEEP LEARNING",
        "template": """history = model.fit(
    X_train, y_train,
    epochs={{epochs}},
    batch_size={{batch_size}},
    validation_split=0.2
)"""
    },
    "cnn-basic": {
        "description": "Simple Convolutional Neural Network",
        "category": "DEEP LEARNING",
        "template": """from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=({{input_shape}})))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())"""
    },
    "cnn-image": {
        "description": "CNN for image classification",
        "category": "DEEP LEARNING",
        "template": """from tensorflow.keras import layers, models

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=({{shape}})),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense({{num_classes}}, activation='softmax')
])"""
    },
    "rnn-basic": {
        "description": "Simple Recurrent Neural Network",
        "category": "DEEP LEARNING",
        "template": """from tensorflow.keras.layers import SimpleRNN

model.add(SimpleRNN({{units}}, input_shape=({{timesteps}}, {{features}})))"""
    },
    "lstm": {
        "description": "Long Short-Term Memory (LSTM) layer",
        "category": "DEEP LEARNING",
        "template": """from tensorflow.keras.layers import LSTM

model.add(LSTM({{units}}, return_sequences=False))"""
    },
    "dropout": {
        "description": "Dropout layer for regularization",
        "category": "DEEP LEARNING",
        "template": """from tensorflow.keras.layers import Dropout

model.add(Dropout({{rate}}))"""
    },
    "predict": {
        "description": "Model prediction boilerplate",
        "category": "DEEP LEARNING",
        "template": """predictions = model.predict({{X_new}})
y_pred = (predictions > 0.5).astype("int32")"""
    },
    "save-load-dl": {
        "description": "Save and load Keras models",
        "category": "DEEP LEARNING",
        "template": """model.save('{{model_path}}')
# To load:
# from tensorflow.keras.models import load_model
# model = load_model('{{model_path}}')"""
    },

    # 🔄 ML PIPELINE (5)
    "data-load": {
        "description": "Load CSV data using Pandas",
        "category": "ML PIPELINE",
        "template": """import pandas as pd

df = pd.read_csv('{{path}}')
print(df.head())"""
    },
    "data-clean": {
        "description": "Handle missing values and drop duplicates",
        "category": "ML PIPELINE",
        "template": """# Drop duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna(df.mean(), inplace=True)"""
    },
    "train-test": {
        "description": "Split data into training and testing sets",
        "category": "ML PIPELINE",
        "template": """from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size={{test_size}}, random_state=42
)"""
    },
    "scaler": {
        "description": "Scale features using StandardScaler",
        "category": "ML PIPELINE",
        "template": """from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)"""
    },
    "pipeline": {
        "description": "Scikit-Learn Pipeline for automation",
        "category": "ML PIPELINE",
        "template": """from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier())
])
pipeline.fit(X_train, y_train)"""
    },

    # 🌐 AI FULL-STACK (10)
    "fastapi-app": {
        "description": "Minimal FastAPI application",
        "category": "AI FULL-STACK",
        "template": """from fastapi import FastAPI

app = FastAPI(title="{{title}}")

@app.get("/")
def read_root():
    return {"message": "Welcome to {{title}} API"}"""
    },
    "route-get": {
        "description": "FastAPI GET route",
        "category": "AI FULL-STACK",
        "template": """@app.get("/{{path}}/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}"""
    },
    "route-post": {
        "description": "FastAPI POST route with Pydantic model",
        "category": "AI FULL-STACK",
        "template": """from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item"""
    },
    "ml-api": {
        "description": "FastAPI endpoint for ML prediction",
        "category": "AI FULL-STACK",
        "template": """@app.post("/predict")
def predict(data: dict):
    # Perform prediction logic here
    prediction = model.predict([data['features']])
    return {"prediction": prediction.tolist()}"""
    },
    "file-upload": {
        "description": "FastAPI file upload handler",
        "category": "AI FULL-STACK",
        "template": """from fastapi import UploadFile, File

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}"""
    },
    "json-response": {
        "description": "Explicit JSONResponse in FastAPI",
        "category": "AI FULL-STACK",
        "template": """from fastapi.responses import JSONResponse

@app.get("/custom")
def custom_json():
    return JSONResponse(content={"status": "ok"}, status_code=200)"""
    },
    "async-api": {
        "description": "Asynchronous API call with httpx",
        "category": "AI FULL-STACK",
        "template": """import httpx

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()"""
    },
    "db-connect": {
        "description": "SQLAlchemy database connection boilerplate",
        "category": "AI FULL-STACK",
        "template": """from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)"""
    },
    "save-predict": {
        "description": "Store results to database after prediction",
        "category": "AI FULL-STACK",
        "template": """def save_prediction(db, prediction_result):
    # Logic to save to DB
    new_entry = PredictionResult(value=prediction_result)
    db.add(new_entry)
    db.commit()"""
    },
    "logger": {
        "description": "Structured logging configuration",
        "category": "AI FULL-STACK",
        "template": """import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("{{name}}")

logger.info("Application started")"""
    },
}
