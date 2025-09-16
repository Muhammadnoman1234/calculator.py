"""
All-in-One Demo - Shows how all calculator components work together
"""

def demo_calculator_connections():
    """Demonstrate how all calculator components are connected"""
    print("PYTHON CALCULATOR - ALL IN ONE DEMO")
    print("=" * 40)
    
    # 1. Show direct function usage
    print("\n1. DIRECT FUNCTION USAGE:")
    print("   from calculator import add")
    print("   result = add(10, 5)")
    
    from calculator import add
    result = add(10, 5)
    print(f"   Result: {result}")
    
    # 2. Show advanced calculator class
    print("\n2. ADVANCED CALCULATOR CLASS:")
    print("   from advanced_calculator import Calculator")
    print("   calc = Calculator()")
    print("   result = calc.power(2, 8)")
    
    from advanced_calculator import Calculator
    calc = Calculator()
    result = calc.power(2, 8)
    print(f"   Result: {result}")
    
    # 3. Show memory functions
    print("\n3. MEMORY FUNCTIONS:")
    print("   calc.memory_store(42)")
    print("   value = calc.memory_recall()")
    
    calc.memory_store(42)
    value = calc.memory_recall()
    print(f"   Stored value: {value}")
    
    # 4. Show history
    print("\n4. CALCULATION HISTORY:")
    print("   calc.show_history()")
    
    history = calc.show_history()
    print("   Recent calculations:")
    history_lines = history.split('\n')
    for line in history_lines[-3:]:  # Show last 3 entries
        if line.strip():
            print(f"   - {line}")
    
    # 5. Show file connections
    print("\n5. PROJECT STRUCTURE:")
    components = [
        "calculator.py - Basic functions",
        "advanced_calculator.py - Enhanced features", 
        "gui_calculator.py - Graphical interface",
        "calculator_launcher.py - Unified access point",
        "README.md - Documentation"
    ]
    
    for component in components:
        print(f"   ✓ {component}")

def show_usage_examples():
    """Show practical usage examples"""
    print("\n\nPRACTICAL USAGE EXAMPLES")
    print("=" * 25)
    
    examples = [
        "1. Quick calculations in code:",
        "   from calculator import multiply",
        "   total = multiply(15, 4)  # Returns 60",
        "",
        "2. Advanced math operations:",
        "   from advanced_calculator import Calculator",
        "   calc = Calculator()",
        "   result = calc.sqrt(144)  # Returns 12.0",
        "",
        "3. Using the GUI calculator:",
        "   Just run: python gui_calculator.py",
        "   Then click buttons to calculate",
        "",
        "4. Using the unified launcher:",
        "   Run: python calculator_launcher.py",
        "   Then select your preferred calculator"
    ]
    
    for line in examples:
        print(line)

def show_launch_options():
    """Show all available ways to launch the calculators"""
    print("\n\nLAUNCH OPTIONS")
    print("=" * 15)
    
    options = [
        "COMMAND LINE:",
        "- python calculator.py              (Basic calculator)",
        "- python advanced_calculator.py    (Advanced calculator)",
        "- python gui_calculator.py         (GUI calculator)",
        "- python calculator_launcher.py    (Unified launcher)",
        "",
        "WINDOWS BATCH FILES:",
        "- run_calculator.bat              (Basic calculator)",
        "- run_advanced_calculator.bat    (Advanced calculator)",
        "- run_gui_calculator.bat         (GUI calculator)",
        "- launch_calculator.bat          (Unified launcher)",
        "- demo_working.bat               (Demo showcase)"
    ]
    
    for line in options:
        print(line)

def main():
    """Main demo function"""
    demo_calculator_connections()
    show_usage_examples()
    show_launch_options()
    
    print("\n\n" + "=" * 50)
    print("All calculator components are now connected!")
    print("You can access any calculator through the unified launcher:")
    print("   python calculator_launcher.py")
    print("=" * 50)

if __name__ == "__main__":
    main()