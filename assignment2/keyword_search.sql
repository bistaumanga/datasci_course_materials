SELECT max(sim_score) FROM(
	SELECT A.docid, sum(A.count * B.count) as sim_score
FROM frequency as A, (SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count) as B
WHERE A.term = B.term and B.docid = 'q'
GROUP BY A.docid, B.docid
ORDER BY sim_score DESC);