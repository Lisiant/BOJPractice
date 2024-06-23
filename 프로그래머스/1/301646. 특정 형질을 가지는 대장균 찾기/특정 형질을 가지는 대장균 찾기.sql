select count(*) as COUNT 
from ECOLI_DATA
where NOT(GENOTYPE & 2) AND ((GENOTYPE & 1) OR (GENOTYPE & 4) OR (GENOTYPE & 5)) ;