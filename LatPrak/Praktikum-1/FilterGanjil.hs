module FilterGanjil where
filterGanjil :: [Int] -> [Int]
filterGanjil li 
    | length li == 0 = []
    | mod (head li) 2 == 0 = filterGanjil (tail li)
    | otherwise = [head li] ++ filterGanjil (tail li)