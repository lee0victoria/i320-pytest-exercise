def fix_phone_num(phone_num_to_fix):
  # given "5125555678". Split the parts, then recombine and return
  area_code = phone_num_to_fix[0:3] # 512 (first three digits)
  three_part = phone_num_to_fix[3:6] # 555 (next three digits)
  four_part = phone_num_to_fix[6:] # # 5678 (last four digits)
  
  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
  return fixed_num

def test_fix_phone_num_valid():
    assert fix_phone_num("555-442-9876") == "5554429876"
    
    # New assertions
    assert fix_phone_num("5554429876") == "5554429876"
    assert fix_phone_num("3216543333") == "3216543333"
    
def test_fix_phone_num_too_long_or_misformatted():
    import pytest
    # These should raise errors once function is fixed
    with pytest.raises(ValueError):
        fix_phone_num("555-442-98761")
    with pytest.raises(ValueError):
        fix_phone_num("(3213) 654 3333")
        
def test_fix_phone_num_non_digits():
    import pytest
    with pytest.raises(ValueError):
        fix_phone_num("334dfdee45")
    with pytest.raises(ValueError):
        fix_phone_num("abcdefghij")
        
def fix_phone_num(phone):
    """
    Fixed version: strips special characters, validates length and digits.
    """
    cleaned = phone.replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
    
    if len(cleaned) != 10:
        raise ValueError("Phone number must be 10 digits")
    if not cleaned.isdigit():
        raise ValueError("Phone number must contain only digits")
    
    return cleaned
