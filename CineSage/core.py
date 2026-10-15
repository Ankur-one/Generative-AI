from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser


class Movie(BaseModel):
    title: str
    release_year : Optional[int]
    genre : List[str]
    director : Optional[str]
    cast : List[str]
    rating : Optional[float]
    summery : str

# ============================================================
# Load TinyLlama
# ============================================================

def load_model():

    llm = HuggingFacePipeline.from_model_id(
        model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        pipeline_kwargs={
            "max_new_tokens": 512,
            "do_sample": False,
            "repetition_penalty": 1.03,
        },
    )

    return ChatHuggingFace(llm=llm)


model = load_model()

parser = PydanticOutputParser(pydantic_object=Movie)
# ============================================================
# Information Extraction Prompt
# ============================================================

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are CineSage, an expert Information Extraction and
Summarization AI.

Your task is to analyze the paragraph provided by the user
and extract ALL useful information that is explicitly present
in the paragraph.

IMPORTANT RULES:

- Use ONLY information provided in the paragraph.
- Do NOT use outside knowledge.
- Do NOT guess or assume information.
- Do NOT add facts that are not present in the paragraph.
- If information is not available, write exactly:
  "Not mentioned in the paragraph."
- Keep the extracted information concise and accurate.
- Correct obvious spelling mistakes only when the intended
  information is clear from the paragraph.
- Do not add unnecessary explanations.

Extract the following information:

1. Name / Title
   Extract the name or title of the movie, book, person,
   event, product, or other main subject.

2. Type / Category
   Identify the type or category if mentioned.

3. Author / Director / Creator
   Extract the author, director, creator, or other creator
   mentioned in the paragraph.

4. Release / Publication Year
   Extract the release, publication, or creation year.

5. Main People / Cast
   Extract all important people, actors, characters, or
   individuals mentioned.

6. Roles of Important People
   Mention the role of each important person if explicitly
   provided.

7. Genre / Category
   Extract the genre or category mentioned.

8. Main Topic
   Identify the main subject or topic discussed.

9. Main Storyline / Description
   Give a concise description of the main story or subject
   based only on the paragraph.

10. Central Theme
    Extract the main theme or idea explicitly described.

11. Purpose / Objective
    Extract the purpose, objective, or goal if mentioned.

12. Important Locations
    Extract all important places, locations, planets, cities,
    countries, or other geographical locations mentioned.

13. Important Organizations
    Extract organizations, companies, institutions, agencies,
    or groups mentioned.

14. Important Events
    Extract important events described in the paragraph.

15. Important Dates
    Extract specific dates, years, or time periods mentioned.

16. Important Facts
    Extract the most important factual information from the
    paragraph.

17. Key Points
    List the most important points in concise bullet points.

18. Important Keywords
    Extract important keywords and concepts.

19. Quick Summary
    Provide a short 2–3 sentence summary of the paragraph.

OUTPUT FORMAT:

Name / Title:
...

Type / Category:
...

Author / Director / Creator:
...

Release / Publication Year:
...

Main People / Cast:
- ...
- ...

Roles of Important People:
- ...
- ...

Genre / Category:
...

Main Topic:
...

Main Storyline / Description:
...

Central Theme:
...

Purpose / Objective:
...

Important Locations:
- ...
- ...

Important Organizations:
- ...
- ...

Important Events:
- ...
- ...

Important Dates:
- ...
- ...

Important Facts:
- ...
- ...

Key Points:
- ...
- ...

Important Keywords:
- ...
- ...

Quick Summary:
...

Remember: Every answer must be based ONLY on the paragraph.
""",
        ),
        (
            "human",
            """
Analyze and extract all available information from this paragraph:

{paragraph}
""",
        ),
    ]
)


# ============================================================
# Information Extraction Function
# ============================================================

def extract_information(paragraph: str):

    final_prompt = prompt.invoke(
        {
            "paragraph": paragraph
        }
    )

    response = model.invoke(final_prompt)

    return response.content