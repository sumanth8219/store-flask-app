docker run \
    -d \
    --network host
    -v $(pwd)/neo4j/data:/data \
    -v $(pwd)/neo4j/logs:/logs \
    -v $(pwd)/neo4j/import:/var/lib/neo4j/import \
    -v $(pwd)/neo4j/plugins:/plugins \
    --env NEO4J_AUTH=neo4j/test \
    neo4j:latest
