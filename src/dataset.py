import pandas as pd

data = {
    "question": ["What is AI?", "What is ML?", "Explain neural networks."],
    "answer": [
        "AI stands for Artificial Intelligence.",
        "ML stands for Machine Learning.",
        "Neural networks are a series of algorithms that mimic the operations of a human brain."
    ]
}

df = pd.DataFrame(data)
