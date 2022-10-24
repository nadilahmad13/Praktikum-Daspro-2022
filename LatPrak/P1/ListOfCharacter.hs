module ListOfCharacter where
makeUnique :: [Char] -> [Char]
makeUnique li
    | null li = []
    | otherwise =
        if counter (last li) li == 1 then makeUnique (init li) ++ [last li]
        else makeUnique (init li)

counter :: Char -> [Char] -> Int
counter x li
    | null li = 0
    | x == head li = 1 + counter x (tail li)
    | otherwise = counter x (tail li)
