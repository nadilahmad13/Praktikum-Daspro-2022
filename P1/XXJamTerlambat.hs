-- NIM   : 16521516
-- Nama  : Ahmad Nadil
-- Judul : Jam Terlambat

-- Definisi dan Spesifikasi
module JamTerlambat where

-- Realisasi
jamTerlambat :: Int -> Int -> Int -> (Int,Int,Int,Bool,Int)
detik :: Int -> Int -> Int -> Int

detik x y z = (x*3600 + y*60 + z)*10
jamTerlambat j m d
    | (j < 8) || (j == 8 && m < 30) =        --Kondisi Tidak Telat
        if j == 8 then (0,30-m,d,False,0)
        else if m > 30 then (8-j-1,90-m,d,False,0)
        else (8-j,30-m,d,False,0)
    |j == 8 && m == 30 && d == 0 = (0,0,0,False,0)
    | otherwise =
        if j == 8 then (0,m-30,d,True,detik 0 (m-30) d)
        else if m < 30 then (j-8-1,m+30,d,True,detik (j-8-1) (m+30) d)
        else if m > 30 then (j-8,m-30,d,True,detik (j-8) (m-30) d)
        else (j-8,0,d,True,detik (j-8) 0 d)

-- Aplikasi
    -- jamTerlambat 10 0 01