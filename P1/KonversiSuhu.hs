{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
-- NIM   : 16521516
-- Nama  : Ahmad Nadil
-- Judul : Konversi Suhu

-- Definisi dan Spesifikasi
module KonversiSuhu where
    konversiSuhu :: Float -> Char -> Float

-- Realisasi
    konversiSuhu t s
        | s == 'R' = 4/5 * t
        | s == 'F' = (9/5 * t) + 32
        | s == 'K' = t + 273.15

-- Aplikasi
    -- konversiSuhu 25 'R'