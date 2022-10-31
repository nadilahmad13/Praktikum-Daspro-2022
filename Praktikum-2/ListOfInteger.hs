-- NAMA  : Ahmad Nadil
-- NIM   : 16521516
-- Judul : List Of Integer

module ListOfInteger where
-- DEFINISI DAN SPESIFIKASI LIST
{- type List of Int: [ ] atau [e o List] atau [List o e]  
   Definisi type List of Int
   Basis: List of Int kosong adalah list of Int 
   Rekurens: 
   List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Int di awal 
   sebuah list atau
   dibuat dengan menambahkan sebuah elemen bertype Int di akhir sebuah list -}

-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Int -> [Int] -> [Int]
{- konso e li menghasilkan sebuah list of integer dari e (sebuah integer) dan li 
   (list of integer), dengan e sebagai elemen pertama: e o li -> li' -}
-- REALISASI
konso e li = [e] ++ li

konsDot :: [Int] -> Int -> [Int]
{- konsDot li e menghasilkan sebuah list of integer dari li (list of integer) dan 
   e (sebuah integer), dengan e sebagai elemen terakhir: li o e -> li' -}
-- REALISASI
konsDot li e = li ++ [e]

-- DEFINISI DAN SPESIFIKASI SELEKTOR
-- head :: [Int] -> Int
-- head l menghasilkan elemen pertama list l, l tidak kosong

-- tail :: [Int] -> [Int]
-- tail l menghasilkan list tanpa elemen pertama list l, l tidak kosong

-- last :: [Int] -> Int
-- last l menghasilkan elemen terakhir list l, l tidak kosong

-- init :: [Int] -> [Int]
-- init l menghasilkan list tanpa elemen terakhir list l, l tidak kosong

-- DEFINISI DAN SPESIFIKASI PREDIKAT
isEmpty :: [Int] -> Bool
-- isEmpty l  true jika list of integer l kosong
-- REALISASI
isEmpty l = null l

isOneElmt :: [Int] -> Bool
-- isOneElmt l true jika list of integer l hanya mempunyai satu elemen
-- REALISASI
isOneElmt l = (length l) == 1


--nbOcc
-- Definisi dan Spesifikasi
nbOcc :: [Int] -> Int -> Int

--Realisasi
nbOcc li e 
    | isEmpty li = 0
    | head li == e = 1 + nbOcc (tail li) e
    | otherwise = nbOcc (tail li) e

-- Aplikasi
   -- nbOcc [10,20,20] 20
      -- hasil = 2

--nbElmt
-- Definisi dan Spesifikasi
nbElmt :: [Int] -> Int

-- Realisasi
nbElmt l 
   | isEmpty l = 0
   | otherwise = 1 + nbElmt(tail l)

--Aplikasi
   -- nbElmt []
      -- hasil = 0
   -- nbElmt [1,2,3]
      -- hasil = 3
   
--elmtKeN
-- Definisi dan Spesifikasi
elmtKeN :: [Int] -> Int -> Int 

-- Realisasi
elmtKeN l n 
   | n == 1 = head l 
   | otherwise = elmtKeN (tail l) (n-1)

-- Aplikasi
   -- elmtKeN [10,20,30] 3
      -- hasil = 30

-- listPlus
-- Definisi dan Spesifikasi
listPlus :: [Int] -> [Int] -> [Int]

-- Realisasi
listPlus li1 li2 
   | isEmpty li1 = []
   | otherwise = konso (head li1 + head li2) (listPlus (tail li1) (tail li2))

-- Aplikasi
   -- listPlus [2,22,4,5] [4,0,-1,-1]
      -- hasil = [6,22,3,4]

--setDiff
-- Definisi dan Spesifikasi
setDiff :: [Int] -> [Int] -> [Int]
isElmt :: Int -> [Int] -> Bool

--Realisasi
setDiff l1 l2
    | null l1 = []
    | otherwise = 
        if isElmt (head l1) l2 then setDiff (tail l1) l2 
        else konso (head l1) (setDiff (tail l1) l2)

isElmt n l2 
    | null l2 = False
    | otherwise = 
        if n == head l2 then True
        else isElmt n (tail l2)