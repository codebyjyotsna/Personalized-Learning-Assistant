def recommend_resources(learning_style):
    resources = {
        "visual": ["video1.mp4", "slides1.pptx"],
        "auditory": ["podcast1.mp3", "audiobook1.mp3"],
        "reading": ["book1.pdf", "article1.html"]
    }
    return resources.get(learning_style, [])
