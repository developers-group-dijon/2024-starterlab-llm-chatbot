from transformers import AutoTokenizer, pipeline, AutoModelForSequenceClassification, AutoModel
from transformers import Trainer, TrainingArguments
from datasets import load_dataset, DatasetDict
from utils.args import init_train_args


# TODO: - 001 : Instantiate the LLM and the tokenizer model
#       - 002 : Load the dataset from HuggingFace
#       - 003 : Train and save the Supervised fine-tuned model
#       - 004 : Evaluate the model
#       - 005 : Complete the function init_data to load data
#       - 006 : Complete the init_trainer function to instantiate the trainer object
def tokenize_function(examples: DatasetDict) -> AutoTokenizer:
  return tokenizer(examples["sentence"], padding="max_length", truncation=True)


def init_data(dataset_name: str) -> DatasetDict:
  # load data
  # TODO 005 - Tips : Use load_dataset from the datasets library
  dataset = ...

  # Prepare the dataset
  dataset = dataset.map(tokenize_function, batched=True)

  return dataset

def init_trainer(dataset: DatasetDict, model: AutoModel) -> Trainer:

  # instantiate the training loop
  # TODO 006 - Tips : Use TrainingArguments and Trainer from the transformers library
  training_args = ...(...)
  trainer = Trainer(...=...,
                    ...=...,
                    ...=...,
                    ...=...)

  return trainer


if __name__ == "__main__":
  # Get arguments from CLI
  args = init_train_args()

  # Instantiate the models
  # TODO 001 - Tips : Use the classes AutoModelForSequenceClassification and AutoTokenizer
  model = xxx.xxx(args.raw_model_name)
  tokenizer = xxx.xxx(args.raw_model_name)

  # Get the data to train the model upon with
  # TODO 002 - Tips : use the init_data function
  dataset = ...(args.dataset_name)

  # train and save
  # TODO 003
  trainer.xxx()
  trainer.xxx(...)

  # evaluate the model
  # TODO 004 - Tips : create a pipeline and deploy it on the test split of the dataset
  classifier = ...(...=..., ...=...)
  classifier(...[...][...])
