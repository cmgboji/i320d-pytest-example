import pytest

def fix_phone_num(phone_num_to_fix):
  cleaned_phone_num = ''
  for num in phone_num_to_fix:
        if num.isdigit():
            cleaned_phone_num += num
            
  if len(cleaned_phone_num) != 10:
      raise ValueError("Invalid Phone Number Length")
        
  area_code = cleaned_phone_num[0:3] # 512 (first three digits)
  three_part = cleaned_phone_num[3:6] # 555 (next three digits)
  four_part = cleaned_phone_num[6:] # # 8823 (last four digits)
  
  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
  return fixed_num

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  assert fix_phone_num("5554429876") == '(555) 442 9876'
  assert fix_phone_num("3216543333") == '(321) 654 3333'

def test_error_phone_nums():
  assert fix_phone_num('555-442-98761') == '(555) 442 9876'
  assert fix_phone_num('(321) 654 3333') == '(321) 654 3333'
    
def test_value_error_check():
    with pytest.raises(ValueError):
        fix_phone_num('51')

def test_not_all_digits():
    with pytest.raises(ValueError):
        fix_phone_num("bjjlnvxyi")
