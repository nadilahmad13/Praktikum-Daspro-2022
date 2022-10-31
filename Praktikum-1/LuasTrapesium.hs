module LuasTrapesium where 

-- DEFINISI DAN SPESIFIKASI
luasTrapesium :: Float -> Float -> Float -> Float
-- angka yang diinput berbentuk integer
-- Luas akan menghasilkan angka dalam bentuk float

-- REALISASI
luasTrapesium t s1 s2 =  0.5 *  t * ( s1 +  s2)