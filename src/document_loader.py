import logging
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Logger configuration

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def load_document(file_path: str):
    """
    Load a PDF document and returns a list of document objects.
    each Document contains the text of a page and its metadata.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
    List of Documents with page_content and metadata.
    """   
    
    path = Path(file_path)

    # Check if the file exists
    if not path.exists():
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if path.suffix.lower() != ".pdf": 
        logger.error(f"Unsupported file type: {path.suffix}. Only PDF files are supported.")
        raise ValueError(f"Unsupported file type: {path.suffix}. Only PDF files are supported.")
    
    logger.info(f"Loading document from: {path.name}")

    loader = PyPDFLoader(str(path))
    pages = loader.load()

    logger.info(f"✅ Successfully loaded document: {path.name} with {len(pages)} pages.")

    return pages

def split_documents(pages: list) -> list:
    """
    Split the content of each page into smaller chunks using RecursiveCharacterTextSplitter.

    Args:
        pages (list): List of Document objects, each containing page_content and metadata.

    Returns:
        List of Document objects with split content.
    """
    logger.info(f"Splitting documents into smaller chunks...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks = splitter.split_documents(pages)

    logger.info(f"✅ Successfully split documents into {len(chunks)} chunks.")

    return chunks


def log_chunks_metadata(chunks: list) -> None: 
    """
    Log the metadata of each chunk for debugging purposes.

    Args:
        chunks (list): List of Document objects with split content.
    """
    logger.info("--- Logging metadata of each chunk ---")
    for i, chunk in enumerate(chunks):
        source = chunk.metadata.get("source", "Unknown Source")
        page = chunk.metadata.get("page", "?")
        size = len(chunk.page_content)
        
        logger.info(f"Chunk {i+1} | Source: {source}, Page: {page} |Size: {size} chars ")
