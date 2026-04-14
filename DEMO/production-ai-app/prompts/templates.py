"""Route-specific answer templates."""

ANSWER_TEMPLATES = {
    "rag": "Grounded answer using internal knowledge.",
    "code": "Code-focused answer grounded in repository context.",
    "web": "Web-style answer using curated external summaries.",
    "docs": "Documentation answer using guide and reference context.",
}
