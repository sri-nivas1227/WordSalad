"""
Test script for WordSalad API
Tests the parsing and Wikipedia integration without requiring OpenAI API key
"""

import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import parse_input, get_wikipedia_summary


def test_parse_input():
    """Test input parsing functionality"""
    print("Testing parse_input function...")
    
    # Test valid inputs
    test_cases = [
        ("moon30", "moon", 30),
        ("python50", "python", 50),
        ("artificial intelligence100", "artificial intelligence", 100),
        ("earth25", "earth", 25),
    ]
    
    for input_str, expected_topic, expected_count in test_cases:
        topic, count = parse_input(input_str)
        assert topic == expected_topic, f"Expected topic '{expected_topic}', got '{topic}'"
        assert count == expected_count, f"Expected count {expected_count}, got {count}"
        print(f"  ✓ '{input_str}' -> topic='{topic}', count={count}")
    
    # Test invalid inputs
    invalid_cases = ["moon", "30", "", "123abc"]
    for input_str in invalid_cases:
        topic, count = parse_input(input_str)
        assert topic is None and count is None, f"Expected None for '{input_str}', got topic='{topic}', count={count}"
        print(f"  ✓ Invalid input '{input_str}' correctly returned None")
    
    print("✅ All parse_input tests passed!\n")


def test_wikipedia_summary():
    """Test Wikipedia API integration"""
    print("Testing get_wikipedia_summary function...")
    
    # Test valid topics
    topics = ["Moon", "Python programming language", "Earth"]
    
    for topic in topics:
        summary = get_wikipedia_summary(topic)
        if summary:
            print(f"  ✓ Found Wikipedia summary for '{topic}'")
            print(f"    Summary preview: {summary[:100]}...")
        else:
            print(f"  ✗ No Wikipedia summary found for '{topic}'")
    
    # Test invalid topic
    invalid_topic = "ThisTopicDefinitelyDoesNotExistOnWikipedia12345"
    summary = get_wikipedia_summary(invalid_topic)
    assert summary is None, f"Expected None for invalid topic, got summary"
    print(f"  ✓ Invalid topic '{invalid_topic}' correctly returned None")
    
    print("✅ All Wikipedia tests passed!\n")


def main():
    print("=" * 60)
    print("WordSalad API - Component Tests")
    print("=" * 60)
    print()
    
    try:
        test_parse_input()
        test_wikipedia_summary()
        
        print("=" * 60)
        print("🎉 All tests passed successfully!")
        print("=" * 60)
        print()
        print("To test the full API with LLM generation:")
        print("1. Set your OpenAI API key in .env file")
        print("2. Run: python app.py")
        print("3. In another terminal, run: curl -X POST http://localhost:5000/generate -H 'Content-Type: application/json' -d '{\"input\":\"moon30\"}'")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
