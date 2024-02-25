#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self._value = value

  @property 
  def value(self):
    return self._value

  @value.setter 
  def value(self, new_value):
    if not isinstance(new_value, str):
      print("The value must be a string.")
    else: 
      self._value = new_value

  def is_sentence(self):
    return self._value.endswith('.')
  
  def is_question(self):
    return self._value.endswith('?')
  
  def is_exclamation(self):
    return self._value.endswith('!')
  
  def count_sentences(self):
    cleaned_value = self._value.replace('?!', '.').replace('!!', '.').replace('?','.').replace('!', '.')
    sentences = cleaned_value.split('.')
    non_empty_sent = [sentence for sentence in sentences if sentence]
   
    return len(non_empty_sent)