#!/usr/bin/env python3
"""
Test script to verify all required packages are installed correctly.
Run this before running the main automation script.
"""

import sys
import importlib.util

def test_package(package_name, import_name=None):
    """Test if a package can be imported"""
    if import_name is None:
        import_name = package_name
    
    try:
        spec = importlib.util.find_spec(import_name)
        if spec is None:
            print(f"❌ {package_name}: Not installed")
            return False
        
        # Try to actually import it
        module = importlib.import_module(import_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"✅ {package_name}: Installed (version: {version})")
        return True
    except Exception as e:
        print(f"❌ {package_name}: Error importing - {e}")
        return False

def main():
    print("🔍 Testing required packages...\n")
    
    # Test Python version
    python_version = sys.version_info
    if python_version >= (3, 7):
        print(f"✅ Python: {python_version.major}.{python_version.minor}.{python_version.micro}")
    else:
        print(f"❌ Python: {python_version.major}.{python_version.minor}.{python_version.micro} (requires 3.7+)")
    
    print()
    
    # Test required packages
    packages = [
        ("selenium", "selenium"),
        ("PyPDF2", "PyPDF2"),
        ("requests", "requests"),
    ]
    
    all_good = True
    for package_name, import_name in packages:
        if not test_package(package_name, import_name):
            all_good = False
    
    print()
    
    # Test built-in modules
    print("🔍 Testing built-in modules...")
    builtin_modules = ["os", "time", "zipfile", "datetime"]
    
    for module in builtin_modules:
        test_package(module)
    
    print()
    
    if all_good:
        print("🎉 All packages are installed correctly!")
        print("📝 You can now run: python sensibull_screenshot_automation.py")
    else:
        print("❌ Some packages are missing. Please install them using:")
        print("   pip install -r requirements.txt")
    
    print("\n" + "="*50)
    print("📖 For setup instructions, see README.md")
    print("🤖 For Telegram bot setup, see the Telegram section in README.md")

if __name__ == "__main__":
    main()
