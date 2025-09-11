# 1. Design an API to search through shout-outs and comments for Amazon




# ✅ Functional Requirements
#
# Full-text search on shout-outs and comments.
# Filters: user, date range, product, type (shout-out or comment).
# Ranking: results sorted by relevance (e.g., keyword match score).
# API endpoints: client should be able to hit an API like
# GET /search?q=...&filters=...
#
# ✅ Non-Functional Requirements
#
# Scalability → potentially millions of comments/shout-outs.
# Low latency search (sub-second response).
# Consistency → search index should reflect recent updates.
# Extensibility → allow adding new filters in the future (e.g., sentiment, tags).




# high-level components


# API Layer → handles incoming requests, parses query and filters.
# Search Service → main service that queries the search engine.
# Indexing Service → takes new shout-outs/comments and updates the index.
# Data Store → source of truth (e.g., RDS/Postgres).
# Search Index → optimized for text queries (e.g., Elasticsearch, Lucene).
