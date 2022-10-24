module ListOfInteger where

maxList :: [Int] -> Int 
maxList li
    | length li == 1 = head li
    | otherwise =
        if head li < head (tail li) then maxList (tail li)
        else maxList ([head li] ++ tail(tail li)) 

{- testList :: Int -> [Int] -> Bool 

maxList li 
    | length li == 1 = head li
    | testList (head li) li = head li
    | otherwise = maxList (tail li) 

testList x li
    | length li == 0 = True
    | x > head li = testList x (tail li)
    | otherwise = False -}