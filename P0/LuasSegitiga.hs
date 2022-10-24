module LuasSegitiga where
-- Menghitung luas segitiga

-- Definisi dan Spesifikasi
-- LuasSegitiga   Luas Segitiga(a, t)
-- a = alas segitiga, t = tinggi segitiga
-- asumsi :  a > 0, t > 0
luasSegitiga :: Float -> Float -> Float 
-- Realisasi
luasSegitiga a t = a * t * 0.5

-- Aplikasi
-- luasSegitiga 1 2