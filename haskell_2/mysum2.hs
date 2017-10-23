mysum :: Int -> [Int] -> Int
mysum acc []     = acc
mysum acc (x:xs) = mysum (acc+x) xs

main = print $ mysum 0 $ take 1000000 $ [1..]
