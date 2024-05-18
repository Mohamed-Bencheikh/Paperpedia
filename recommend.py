from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import google.generativeai as genai
import arxiv
from config import pc_api_key, g_api_key
import warnings

warnings.filterwarnings("ignore")

embedding_model = SentenceTransformer("all-mpnet-base-v2") 
genai.configure(api_key=g_api_key)
pc = Pinecone(api_key=pc_api_key)
index = pc.Index("papers")

## RELEVANT PASSAGE
def get_relevant_passage(query, top_k=5):
    results = []
    q_emb = embedding_model.encode(query)
    res = index.query(vector=q_emb.tolist(), top_k=top_k, include_metadata=True).to_dict()
    ## get the titles and the urls
    for r in res['matches']:
        title = r['metadata']['title']
        url = r['metadata']['url']
        results.append({'title': title, 'url': url})
    return results 
   
def get_latest_papers(category, num_papers=5):
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
            "date": res.published.strftime("%d-%m-%Y"),
            "abstract": res.summary,
            "categories": res.categories,
            "journal": res.journal_ref,
            "url": res.pdf_url
        })
    return papers

