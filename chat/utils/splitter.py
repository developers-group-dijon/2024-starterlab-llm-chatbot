from typing import List

from langchain_community.document_loaders import (
  PDFMinerLoader,
  TextLoader,
  UnstructuredHTMLLoader,
  UnstructuredMarkdownLoader,
)
from langchain_core.documents import Document
from langchain_text_splitters import (
  HTMLHeaderTextSplitter,
  MarkdownHeaderTextSplitter,
  RecursiveCharacterTextSplitter,
  TextSplitter,
)
from utils.args import SplitNamespace


def text_splitter(
  chunk_size: int = 1000,
  chunk_overlap: int = 100,
) -> TextSplitter:
  return RecursiveCharacterTextSplitter(
    separators=[" ", "."], chunk_size=chunk_size, chunk_overlap=chunk_overlap, add_start_index=True
  )


def html_splitter() -> HTMLHeaderTextSplitter:
  return HTMLHeaderTextSplitter(headers_to_split_on=[("h1", "Header 1"), ("h2", "Header 2"), ("h3", "Header 3")])


def markdown_splitter() -> MarkdownHeaderTextSplitter:
  return MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "Header 1"), ("##", "Header 2")])


def split_file(args: SplitNamespace) -> List[Document]:
  chunks = []
  match args.text_splitter:
    case "RecursiveCharacterTextSplitter":
      # Utilisation du loader adapté au type de contenu
      # pour pouvoir ensuite travailler (découper) sur du texte brut
      if args.file_path.endswith(".pdf"):
        loader_class = PDFMinerLoader
      elif args.file_path.endswith(".html"):
        loader_class = UnstructuredHTMLLoader
      elif args.file_path.endswith(".md"):
        loader_class = UnstructuredMarkdownLoader
      else:
        loader_class = TextLoader
      docs = loader_class(args.file_path).load()
      chunks = text_splitter(args.chunk_size, args.chunk_overlap).split_documents(docs)
    case "HTMLHeaderTextSplitter":
      chunks = html_splitter().split_text_from_file(args.file_path)
    case "MarkdownHeaderTextSplitter":
      docs = TextLoader(args.file_path).load()
      chunks = markdown_splitter().split_text(docs[0].page_content)
    case _:
      raise Exception(f"Splitter non valide : {args.text_splitter}")

  if args.apply_recursive_text_splitter and args.text_splitter != "RecursiveCharacterTextSplitter":
    chunks = text_splitter(args.chunk_size, args.chunk_overlap).split_documents(chunks)

  return chunks
