{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
module RollnMove where
    movePlayer :: Int -> Int -> Int 

    nextSpace :: Int -> Int

    movePlayer a n
        | n == 1 = nextSpace a
        | otherwise = movePlayer (nextSpace a) (n-1)
        
    nextSpace a
        | a == 40 = 1
        | otherwise = a+1