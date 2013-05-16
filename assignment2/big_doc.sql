SELECT count(docid) FROM (SELECT DISTINCT docid 
	FROM (SELECT docid,sum(count) as "tot_terms"
FROM frequency
GROUP by docid)
WHERE tot_terms >300) x;