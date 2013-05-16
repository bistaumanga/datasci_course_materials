SELECT sum(A.count * B.count)
FROM frequency as A, frequency as B
WHERE A.term = B.term and A.docid = '10080_txt_crude' and B.docid = '17035_txt_earn'
GROUP BY A.docid, B.docid;