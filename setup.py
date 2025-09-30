"""
Setup script for the Portfolio Flask Application
"""
import subprocess
import sys
import os

def install_requirements():
    """Install required Python packages"""
    try:
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 or higher is required")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def main():
    """Main setup function"""
    print("🚀 Setting up Portfolio Flask Application...")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    print("\nTo run the application:")
    print("  python app.py")
    print("\nThen open your browser and visit:")
    print("  http://localhost:5000")
    print("\nTo stop the server, press Ctrl+C")

if __name__ == "__main__":
    main()
