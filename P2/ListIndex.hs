-- Nama : Ahmad Nadil
-- NIM : 16521516
-- Judul : List of Index

module ListIndex where 

-- List Index
-- Definisi dan Spesifikasi
listIndex :: [Int] -> (Int -> Char) -> [Char]

-- Realisasi
listIndex l f
    | null l = []
    | otherwise = [f (head l)] ++ listIndex (tail l) f

f :: Int -> Char
f x
    | x >= 80 && x <= 100 = 'A'
    | x < 80 && x >= 70 = 'B'
    | x < 70 && x >= 65 = 'C'
    | x < 65 && x >= 55 = 'D'
    | otherwise = 'E'

-- Aplikasi
    -- listIndex [75, 90, 10, 20, 100] f = "BAEEA"