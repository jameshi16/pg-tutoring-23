-- Queue.hs - hurrdurr own implementation of queue
module Queue where

data Queue a = Q { front :: [a], back :: [a]} deriving (Show)

empty :: Queue a
empty = Q [] []

queue :: a -> Queue a -> Queue a
queue x q = Q (front q) (x : back q)

dequeue :: Queue a -> (Queue a, a)
dequeue (Q f b)
  | length f == 0 = case length b of 0 -> error "oops"
                                     _ -> dequeue $ moveBack
  | otherwise = (Q (tail f) (b), head f)
  where moveBack = Q (reverse $ b) ([])

{--
Try:
  empty
  queue 2 empty
  queue 4 $ queue 3 $ queue 2 empty
  dequeue $ queue 4 $ queue 3 $ queue 2 empty
--}
