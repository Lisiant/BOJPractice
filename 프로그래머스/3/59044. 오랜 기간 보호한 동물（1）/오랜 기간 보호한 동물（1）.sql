-- 코드를 입력하세요

# in에는 남아 있고 out에는 없는 애들 중 날짜순 오름차순 3순위

SELECT NAME, DATETIME
FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN (SELECT I.ANIMAL_ID
                        FROM ANIMAL_INS I 
                        JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID)
ORDER BY DATETIME
LIMIT 3;