module TesKategori where
    tesKategori :: Int -> Int -> Int -> Bool
    tesKategori t b k 
        | (t > 0) && (t > 100) && (b > 0) && (b <= 150) && ((k == 2) || (k == 3)) = True 
        | (t > 0) && (t <= 100) && (b > 0) && (b <= 150) && (k == 2) = True
        | (t > 0) && (t <= 100) && (b > 30) && (b <= 150) && ((k == 1) || (k == 2))  = True
        | (t > 0) && (t <= 100) && (b > 150) && (k == 2) = True
        | (t > 100) && (t <= 200) && (b > 150) && ((k == 2) || (k == 3)) = True
        | k == 0 = True
        | otherwise = False