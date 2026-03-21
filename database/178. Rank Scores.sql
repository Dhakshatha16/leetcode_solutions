select score, DENSE_RANK() OVER (ORDER BY  Score DESC)  AS 'rank'
from Scores;