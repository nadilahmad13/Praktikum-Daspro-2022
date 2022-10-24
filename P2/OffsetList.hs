-- Nama : Ahmad Nadil
-- NIM : 16521516
-- Judul : OffsetList

-- Definisi dan Spesifikasi
module OffsetList where 
offsetList :: [Int] -> (Int -> Int) -> [Int]
plus2 :: Int -> Int
minus1 :: Int -> Int
offKond :: Int -> Int

-- Realisasi
plus2 x = x+2
minus1 x = x-1
offKond i
    | i >= 0 && i <= 40 = 10
    | i >= 41 && i <= 60 = 5
    | i >= 61 && i <= 89 = 3
    | i > 89 = 1
    | otherwise = 0

offsetList li f
    | null li = []
    | otherwise = f (head li) : offsetList (tail li) f

-- Aplikasi
    -- offsetList [1,2,3] plus2
    -- offsetList [1,2,3] minus1
    -- offsetList [1,2,3] offKond