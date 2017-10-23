module Hands where

import Data.Function (on)
import Data.List (groupBy, sortBy)
import Data.Ord (comparing)

import Types

checkGroups :: [Card] -> (HandRank, [Card])
checkGroups h = (hr, cs)
  where groupedByRank = sortByLength $ groupBy ((==) `on` rank) $ sort h
        topFive = take 5 $ concat groupedByRank
        handRank = case map length groupedByRank of
                  (4:_)    -> Quads
                  (3:2:_)  -> FullHouse
                  (3:_)    -> Trips
                  (2:2:_)  -> TwoPair
                  (2:_)    -> Pair
                  _        -> HighCard

sortByLength :: Ord a => [[a]] -> [[a]]
sortByLength = reverse . sortBy (comparing length)
