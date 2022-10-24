-- NIM   : 16521516
-- Nama  : Ahmad Nadil
-- Judul : Menghitung Digit Angka

-- Definisi dan Spesifikasi
module SumOfDigits where
sumOfDigits :: Int -> Int

-- Realisasi
sumOfDigits n 
    | n `mod` 10 == n = n
    | otherwise = sumOfDigits (n `div` 10) + (n `mod` 10)

-- Aplikasi
    -- sumOfDigits 234