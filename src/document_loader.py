import logging
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

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

