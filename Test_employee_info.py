import employee_info

# --- Tests for get_employees_by_age_range ---

def test_get_employees_by_age_range_normal():
    result = employee_info.get_employees_by_age_range(20, 30)
    assert len(result) == 2

def test_get_employees_by_age_range_no_match():
    result = employee_info.get_employees_by_age_range(50, 60)
    assert result == []

def test_get_employees_by_age_range_all():
    result = employee_info.get_employees_by_age_range(20, 50)
    assert len(result) == 6

# --- Tests for calculate_average_salary ---

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    expected = (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6
    assert result == expected

# --- Tests for get_employees_by_dept ---

def test_get_employees_by_dept_sales():
    result = employee_info.get_employees_by_dept("Sales")
    assert len(result) == 2

def test_get_employees_by_dept_marketing():
    result = employee_info.get_employees_by_dept("Marketing")
    assert len(result) == 2

def test_get_employees_by_dept_engineering():
    result = employee_info.get_employees_by_dept("Engineering")
    assert len(result) == 2

def test_get_employees_by_dept_no_match():
    result = employee_info.get_employees_by_dept("Finance")
    assert result == []