#To run the environment, use source .venv/bin/activate

#Load the pdf developer documentation
from pathlib import Path
from langchain.document_loaders import PyPDFLoader


#Load documents from data directory
def load_documents(pdf_dir: str):
    """Returns a list of page Documents from the data directory."""
    # Convert pdf_dir to Path objectß
    pdf_dir = Path(pdf_dir)
    # Initalise an empty list to hold the documents
    all_docs = []
    #Loop through all sorted pdf files in the directory
    for pdf in pdf_dir.glob("**/*.pdf"):
        #Load one pdf at a time
        doc_loader = PyPDFLoader(str(pdf))
        #Append the loaded pages to all_docs
        all_docs.extend(doc_loader.load())
        return all_docs

documents = load_documents("data")
        