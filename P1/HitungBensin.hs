-- NIM   : 16521516
-- Nama  : Ahmad Nadil
-- Judul : Hitung bensin

-- Definisi dan Spesifikasi
module HitungBensin where

-- Realisasi
hitungBensin :: Int -> Int -> Int
hitungBensin a b =
    let count x
            | x == 1 = 0
            | x `mod` 2 == 0 = 1 + count (x `div` 2)
            | otherwise = 1 + count (3*x + 1)
    in if a == b then count a
    else count a + hitungBensin (a+1) b

-- Aplikasi
    -- hitungBensin 11 11