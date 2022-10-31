{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
module HitungIndeks where
hitungIndeks :: Float -> Float -> Float -> Int
hitungIndeks nilaiUTS nilaiUAS nilaiTubes
    | nilaiUTS == 0 || nilaiUAS == 0 || nilaiTubes == 0 = 0
    | nilaiUTS < 40 || nilaiUAS < 40  = 1
    | nilaiTubes >= 75 && nilaiUTS >= 75 && nilaiUAS >= 75 = 4
    | nilaiTubes < 40 && nilaiUTS >= 40 && nilaiUAS >= 40 = 2
    | nilaiUTS < 75 && nilaiUAS < 75 && nilaiTubes < 75 = 2
    | nilaiTubes >= 75 || nilaiUTS >= 75 || nilaiUAS >= 75 = 3