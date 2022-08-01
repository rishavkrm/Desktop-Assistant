import wolframalpha
from respond import respond


def wolfram_function(text):
    question = text
    app_id = "6VQK5G-2Q6JYEEWVH"
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    respond("The answer is " + answer)
