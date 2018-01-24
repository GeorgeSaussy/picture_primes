#!/usr/bin/python
import sys, math, random

def is_prime(n):
  ret = True
  max_guesses = 500
  d = n-1
  s = 0
  done = False
  while s % 2 == 0:
    s /= 2
    s += 1
  count = 0
  while count < max_guesses and ret:
    a = random.randrange(n-1)
    wit = pow(a, d, n)
    if wit != 1: # find if wit is a witness to n
      pow_iter = 0
      done = (wit != n-1)
      while not done:
        if pow_iter == d - 1:
          done = True
          ret = False
        else:
          pow_iter += 1
          wit = (wit**2)%n
    count += 1
  return ret

def get_max_guesses(n1, n2):
  ret = -1
  n = max(n1, n2)
  p = 1 / math.log(n)
  ret = math.log(0.99) / math.log(1-p)
  ret *= 2
  return ret


def prime_in_range(n1, n2):
  ret = -1
  max_guesses = get_max_guesses(n1, n2)
  num_tries = 0
  done = False
  while not done:
    guess = random.randrange(n1, n2)
    if is_prime(guess):
      ret = guess
      done = True
    else:
      num_tries += 1
      if num_tries >= max_guesses:
        done = True
  return ret

if __name__ == "__main__":
  n1 = int(sys.argv[1])
  n2 = int(sys.argv[2])
  possible_prime = prime_in_range(n1, n2)
  if possible_prime == -1:
    print("Could not find a prime.")
  else:
    print(str(possible_prime))

