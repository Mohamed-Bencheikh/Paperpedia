from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import google.generativeai as genai
import arxiv
from config import pc_api_key, g_api_key
import warnings

warnings.filterwarnings("ignore")

embed_model = "all-mpnet-base-v2"
genai.configure(api_key=pc_api_key)
pc = Pinecone(api_key=pc_api_key)

def get_latest_papers(category, num_papers=3):
    search = arxiv.Search(
    query=category,
    max_results=num_papers,
    sort_by=arxiv.SortCriterion.SubmittedDate,
    sort_order=arxiv.SortOrder.Descending,
    )
    results = list(search.results())
    papers = []
    for res in results:
        papers.append({
            "title": res.title,
            "authors": [author.name for author in res.authors],
            "date": res.published.strftime("%d %m %Y"),
            "abstract": res.summary,
            "categories": res.categories,
            "journal": res.journal_ref,
            "url": res.pdf_url
        })
    return papers




