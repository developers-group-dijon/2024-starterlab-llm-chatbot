# IMPORTING LIBRARIES
from transformers import AutoTokenizer, pipeline, AutoModelForSequenceClassification, AutoModel
from transformers import Trainer, TrainingArguments
from datasets import load_dataset, DatasetDict
from utils.args import init_train_args


def tokenize_function(examples: DatasetDict) -> AutoTokenizer:
  return tokenizer(examples["sentence"], padding="max_length", truncation=True)


def init_data(dataset_name: str) -> DatasetDict:
  # load data
  dataset_ = load_dataset(dataset_name)

  # Prepare the dataset
  dataset_ = dataset_.map(tokenize_function, batched=True)

  return dataset_


def init_trainer(ds: DatasetDict, model: AutoModel) -> Trainer:
  # instantiate the training loop
  training_args = TrainingArguments(output_dir="./results")
  trainer_ = Trainer(model=model, args=training_args, train_dataset=ds["train"], eval_dataset=ds["test"])

  return trainer_


if __name__ == "__main__":
  # Get arguments from CLI
  args = init_train_args()

  # Instantiate the models
  raw_model = AutoModel.from_pretrained(args.raw_model_name)
  tokenizer = AutoTokenizer.from_pretrained(args.raw_model_name)

  # Get the data to train the model upon with
  dataset = init_data(args.dataset_name)

  # train and save
  trainer = init_trainer(dataset, raw_model)
  trainer.train()
  trainer.save_model(f"models/fine-tuned-{args.raw_model_name}")

  # evaluate the model
  classifier = pipeline(task="text-classification", model=f"models/fine-tuned-{args.raw_model_name}")
  classifier(dataset["test"]["sentence"])
