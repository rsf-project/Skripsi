# from rasa.nlu.test import run_evaluation
# evaluation_results = run_evaluation("tests/test_intent.yml","models/20230520-221504.tar.gz")
# nilai_akurasi = evaluation_results['intent_evaluation']['accuracy']
# print("Nilai Akurasi: {:.2f}%".format(nilai_akurasi * 100))
import asyncio
from rasa.nlu.test import run_evaluation

async def evaluate():
    data_uji = "tests/test_intent.yml"
    direktori_model = "models/"
    evaluation_results = await run_evaluation(data_uji, direktori_model)
    nilai_akurasi = evaluation_results['intent_evaluation']['accuracy']
    print("Nilai Akurasi: {:.2f}%".format(nilai_akurasi * 100))

loop = asyncio.get_event_loop()
loop.run_until_complete(evaluate())