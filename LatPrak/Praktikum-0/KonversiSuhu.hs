{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
module KonversiSuhu where
    konversiSuhu :: Double -> Char -> Double
    konversiSuhu t s
        | s == 'R' = 4/5 * t
        | s == 'F' = (9/5 * t) + 32
        | s == 'K' = -t + 273.15