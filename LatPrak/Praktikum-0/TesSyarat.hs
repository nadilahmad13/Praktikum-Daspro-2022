{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
module TesSyarat where
    tesSyarat :: Float -> Float -> Int
    tesSyarat ip pot
        |ip >= 3.5 = 4
        |pot < 1 && ip < 3.5 = 1
        |pot >= 1 && pot < 5 && ip < 3.5 && ip >= 2.0 = 3
        |pot >= 1 && pot < 5 && ip < 2 = 2
        |otherwise = 0