n <- 10

a <- 0
b <- 1

cat(a, b, " ")

for (i in 3:n) {
  c <- a + b
  cat(c, " ")
  a <- b
  b <- c
}
