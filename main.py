from fastapi import FastAPI
from random import choice

app = FastAPI()

# Aligned categories for adjectives and nouns
categories = {
    "intellectual": {
        "adjectives": ["brilliant", "wise", "knowledgeable", "insightful"],
        "nouns": ["genius", "thinker", "scholar", "intellectual"]
    },
    "emotional": {
        "adjectives": ["kind-hearted", "compassionate", "understanding", "empathetic"],
        "nouns": ["guardian", "nurturer", "empath", "mentor"]
    },
    "energetic": {
        "adjectives": ["dynamic", "vivacious", "spirited", "lively"],
        "nouns": ["energizer", "mover", "doer", "creator"]
    },
    "reliable": {
        "adjectives": ["dependable", "trustworthy", "steadfast", "loyal"],
        "nouns": ["pillar", "rock", "anchor", "supporter"]
    }
}

verbs = ["inspire", "uplift", "energize", "guide", "enlighten", "empower", "encourage", "motivate"]

# Sentence structures
structures = [
    "You embody the spirit of a {adjective} {noun}.",
    "Your ability to {verb} others is truly {adjective}.",
    "You are not just {adjective}, you are a {noun} in your own right.",
    "In a world of ordinary, you stand out as {adjective}."
]

def choose_pair(category):
    """Choose a paired adjective and noun."""
    adjective = choice(categories[category]["adjectives"])
    noun = choice(categories[category]["nouns"])
    return adjective, noun

@app.get("/compliment")
async def get_compliment():
    category = choice(list(categories.keys()))
    adjective, noun = choose_pair(category)
    verb = choice(verbs)
    structure = choice(structures)
    compliment = structure.format(adjective=adjective, noun=noun, verb=verb)
    return {"compliment": compliment}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
