{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
-- NIM   : 16521516
-- Nama  : Ahmad Nadil
-- Judul : Klasifikasi Komputer

-- Definisi dan Spesifikasi
module KlasifikasiKomputer where
klasifikasi :: Int -> Int -> Int -> Int

-- Realisasi
klasifikasi c g h 
    | c < 2 || g < 2 || h < 2 = 1
    | c < 5 || g < 5 = 2
    | c <= 7 && g <= 7 && h <= 7 = 3
    | c <= 7 || g <= 7 || h <= 7 = 4
    | c > 7 && g > 7 && h > 7 = 5

-- Aplikasi
    -- klasifikasi 6 10 1