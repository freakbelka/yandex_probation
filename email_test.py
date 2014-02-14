# -*- coding: utf-8 -*-
# unittest for email validation module 
import validation.email
import unittest

class KnownValues(unittest.TestCase):
     known_values = ( 
          # hostname validation
          ('freakbelka@gma2il.com', True),
          ('freakbelka@gma1-il.com', True),
          ('freakbelka@gf.mg', True),
          ('freakbelka@gm_ail.com', True),
          ('freakbelka@gm12ail.com', True),
          ('freakbelka@@gmail.com', False),
          ('freakbelka@sd', False),
          ('freakbelka@sdfs"dsd', False),
          ('freakbelka@-gmail.com', False),
          ('freakbelka@gm2ail-.com', False),
          ('freakbelka@gm3ail.-com', False),
          ('freakbelka@gmail.com-', False),
          ('freakbelka@gm3ail.com.', False),

          # username validation
          ('freak"belka@gma2il.com', False),
          ('frealbel+ka@gma2il.com', False),
          ('@gma2il.com', False),
          ('freakb..elka@gma2il.com', False),
          ('freak!belka@gma2il.com', False),
          ('fre"a:"kb!"el:"ka@gmail.com', False),
          ('frea_k1342.be-lka@gma2il.com', True),
          ('freak"belka"@gma2il.com', True),
          ('freak"b:elka!"@gma2il.com', True),
          ('fre"a:"kb"!el:"ka@gmail.com', True)
          )
  
     def test_email_validation(self):
          # splitting должен вернуть известный результат на конкретное значение
          for input_email, value in self.known_values:
               result = validation.email.splitting(input_email)
               self.assertEqual(value, result)
               
if __name__ == '__main__':
     unittest.main()
