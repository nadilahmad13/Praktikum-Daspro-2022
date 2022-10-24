setDiff :: [Int] -> [Int] -> [Int]
setDiff l1 l2
    | null l1 = []
    | otherwise = 
        if isElmt (head l1) l2 then setDiff (tail l1) l2 
        else [head l1] ++ setDiff (tail l1) l2

isElmt :: Int -> [Int] -> Bool
isElmt n l2 
    | null l2 = False
    | otherwise = 
        if n == head l2 then True
        else isElmt n (tail l2)