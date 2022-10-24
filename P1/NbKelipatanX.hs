-- NIM   : 16521516
-- Nama  : Ahmad Nadil
-- Judul : Kelipatan X

-- Definisi dan Spesifikasi
module NbKelipatanX where
nbKelipatanX :: Int -> Int -> Int -> Int

-- Realisasi
nbKelipatanX m n x
  | m == n = 
   if n `mod` x == 0 then 1
   else 0
  | n `mod` x == 0 = 1 + nbKelipatanX m (n-1) x
  | otherwise = nbKelipatanX m (n-1) x

-- Aplikasi
    -- nbKelipatanX 1 10 2