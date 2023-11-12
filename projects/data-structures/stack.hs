-- Stack in Haskell
module Stack where

push :: a -> [a] -> [a]
push x xs = x:xs

peek :: [a] -> a
peek [] = error "uh oh"
peek (x:_) = x

pop :: [a] -> [a]
pop [] = error "uh oh"
pop (_:xs) = xs

{-
Try these commands:

  let stack = push 1 $ push 2 $ push 3 $ push 4 []
  push 5 stack
  peek stack
  new_stack = pop stack
-}
