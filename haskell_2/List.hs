module List where

import Prelude hiding (Fractional, Functor, fmap)
import Functor

data List a = Nil | Cons a (List a) deriving (Read, Show)
data Fractional = Fraction Int Int
