{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
module KonversiJam where
konversiJam :: Int -> Int -> Int -> (Bool, Int, Int, Int)
konversiJam j m d =
    if j-7 < 0 then (True, 24-7+j, m, d)
    else (False, j-7, m, d)