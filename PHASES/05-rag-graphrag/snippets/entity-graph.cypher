// A tiny example graph: one service, one team, one incident.
MERGE (svc:Service {name: "invoice-worker"})
MERGE (team:Team {name: "billing-platform"})
MERGE (incident:Incident {id: "INC-42"})
MERGE (svc)-[:OWNED_BY]->(team)
MERGE (svc)-[:IMPACTED_BY]->(incident)
