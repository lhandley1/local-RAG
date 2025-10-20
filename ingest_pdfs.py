#To run the environment, use source .venv/bin/activate

#Input the path to the pdf's directory
from pathlib import Path
#Import to load pdfs into documents
from langchain_community.document_loaders import PyPDFLoader
#Import to split text into chunks
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document



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

def split_documents(documents: list[Document]):
    """Splits documents into chunks of text."""
    #Implementation of the text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        length_function=len,
        separators=["\n\n", "\n", " ", ""], 
    )
    return text_splitter.split_documents(documents)

if __name__ == "__main__":
    documents = load_documents("data")
    #Quantity of documents loaded
    print(f"Loaded {len(documents)} documents")
    #Print the first document
    print(documents[0])
    #Split the documents into chunks
    chunks = split_documents(documents)
    #Print the first chunked document
    print(chunks[0])
    #Quantity of documents after splitting
    print(f"Split into {len(chunks)} chunks")