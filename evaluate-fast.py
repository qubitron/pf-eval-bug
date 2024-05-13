# https://github.com/Azure-Samples/contoso-chat/blob/may-2024-updates/evaluations/evaluate-chat-flow-sdk.ipynb
import os
import json
from datetime import datetime
from promptflow.core import AzureOpenAIModelConfiguration
from promptflow.evals.evaluate import evaluate
from promptflow.evals.evaluators import RelevanceEvaluator, GroundednessEvaluator, FluencyEvaluator, CoherenceEvaluator

from dotenv import load_dotenv
load_dotenv()

class WriterEvaluator:
    def __init__(self, model_config):
        self.evaluators = [
            RelevanceEvaluator(model_config),
            FluencyEvaluator(model_config),
            CoherenceEvaluator(model_config),
            GroundednessEvaluator(model_config),
        ]

    def __call__(self, *, query: str, context: str, response: str, **kwargs):
        output = {}
        for evaluator in self.evaluators:
            result = evaluator(
                question=query,
                context=context,
                answer=response,
            )
            output.update(result)
        return output

def evaluate_local(model_config, data_path):
    data = []
    with open(data_path) as f:
        for line in f:
            data.append(json.loads(line))

    writer_evaluator = WriterEvaluator(model_config)

    results = []
    futures = []
    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for row in data:
            futures.append(executor.submit(writer_evaluator, query=row["query"], context=row["context"], response=row["response"]))
        for future in futures:
            results.append(future.result())

    return results

if __name__ == "__main__":
    import time

    # Initialize Azure OpenAI Connection
    model_config = AzureOpenAIModelConfiguration(
            azure_deployment=os.environ["AZURE_DEPLOYMENT_NAME"],
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
            api_version=os.environ["AZURE_OPENAI_API_VERSION"],
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"]
        )

    start=time.time()
    print(f"Starting evaluate...")

    eval_result = evaluate_local(model_config, data_path="eval_writer.jsonl")

    print(eval_result)
    end=time.time()
    print(f"Finished evaluate in {end - start}s")

