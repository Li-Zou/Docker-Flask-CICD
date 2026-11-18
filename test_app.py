from app import app

def test_home():
    """Test that the home page renders correctly"""
    response = app.test_client().get("/")

    # 1. 状态码应该是 200 (OK)
    assert response.status_code == 200
    
    # 2. 页面里应该包含计算器的标题或关键元素，而不再是 "Hello World!"
    assert b"Flask Calculator" in response.data
    assert b"Calculate" in response.data


def test_calculate_addition():
    """Test the addition operation"""
    response = app.test_client().post(
        "/calculate", 
        json={"a": 5, "b": 3, "op": "add"}
    )
    
    assert response.status_code == 200
    assert response.json == {"result": 8}


def test_calculate_division():
    """Test the division operation"""
    response = app.test_client().post(
        "/calculate", 
        json={"a": 10, "b": 2, "op": "div"}
    )
    
    assert response.status_code == 200
    assert response.json == {"result": 5}


def test_divide_by_zero():
    """Test division by zero error handling"""
    response = app.test_client().post(
        "/calculate", 
        json={"a": 10, "b": 0, "op": "div"}
    )
    
    # 应该返回 400 Bad Request
    assert response.status_code == 400
    assert response.json == {"error": "Cannot divide by zero"}


def test_invalid_input():
    """Test invalid number input"""
    response = app.test_client().post(
        "/calculate", 
        json={"a": "abc", "b": 5, "op": "add"}
    )
    
    assert response.status_code == 400
    assert response.json == {"error": "Please enter valid numbers"}