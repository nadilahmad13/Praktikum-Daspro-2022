{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
module ListOfInteger where
setIntersect :: [Int] -> [Int] -> [Int]
setIntersect li1 li2
    | null li1 || null li2  = []
    | isElement (head li1) li2 = [head li1] ++ setIntersect (tail li1) li2

isElement :: Int -> [Int] -> Bool
isElement e li
    | null li = False
    | e == head li = True || isElement e (tail li)
    | otherwise = isElement e (tail li)