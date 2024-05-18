from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import google.generativeai as genai
import arxiv
from config import pc_api_key, g_api_key
import textwrap
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

def make_prompt(query, relevant_passage):
  escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
  prompt = textwrap.dedent(f"""You are a helpful Recommender System that recommend research papers from the list of articles proposed in the context below. \
  Be sure to suggest the most relevant one based on the QUERY, including all relevant background information. \
  Your response should look like this:\
  I recommend this article:\
  TITLE: the title of the article\
  URL: the url of the article\
  Reason: your reasoning for the recommendation\
  If the passage is irrelevant to the answer, you may ignore it.
  QUESTION: '{query}'
  PASSAGE: '{escaped}'
  ANSWER:
  """)
  return prompt

def get_chat_response(query):
  context = get_relevant_passage(query)
  passage = ""
  for i, res in enumerate(context):
    passage += f"result {i+1}:\n"
    passage += f"Title: {res['title']}\n"
    passage += f"Url: {res['url']}\n"
  prompt = make_prompt(query, passage)
  q_a_model = genai.GenerativeModel('gemini-1.5-pro-latest')
  response = q_a_model.generate_content(prompt)
  return response

