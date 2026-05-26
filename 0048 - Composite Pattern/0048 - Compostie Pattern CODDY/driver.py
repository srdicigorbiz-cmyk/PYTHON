# Import all necessary classes
from file_system import FileSystem
from directory import Directory
from file import File

# Comprehensive test case handler
test_case = input()

if test_case == "basic_file_test":
    file = File("test.txt", 100)
    print(f"Name: {file.name}")
    print(f"Size: {file.get_size()} KB")
    print(file.display())

elif test_case == "basic_directory_test":
    documents = Directory("Documents")
    file1 = File("resume.pdf", 250)
    file2 = File("cover_letter.doc", 180)
    documents.add(file1)
    documents.add(file2)
    print(f"Total size: {documents.get_size()} KB")
    print(documents.display())

elif test_case == "file_system_basic_test":
    fs = FileSystem()
    readme = File("README.md", 50)
    fs.add_to_path("/", readme)
    print(fs.display())
    print(f"Total system size: {fs.get_total_size()} KB")

elif test_case == "nested_directory_test":
    fs = FileSystem()
    docs = Directory("Documents")
    projects = Directory("Projects")
    
    fs.add_to_path("/", docs)
    fs.add_to_path("/Documents", projects)
    
    project_file = File("main.py", 300)
    readme = File("README.md", 75)
    
    fs.add_to_path("/Documents/Projects", project_file)
    fs.add_to_path("/Documents/Projects", readme)
    
    print(fs.display())

elif test_case == "path_operations_test":
    fs = FileSystem()
    
    # Create directory structure
    docs = Directory("Documents")
    projects = Directory("Projects")
    fs.add_to_path("/", docs)
    fs.add_to_path("/Documents", projects)
    
    # Add files
    file1 = File("notes.txt", 120)
    file2 = File("project1.py", 450)
    fs.add_to_path("/Documents", file1)
    fs.add_to_path("/Documents/Projects", file2)
    
    # Test path operations
    retrieved_docs = fs.get_from_path("/Documents")
    retrieved_file = fs.get_from_path("/Documents/Projects/project1.py")
    
    print(f"Documents directory size: {retrieved_docs.get_size()} KB")
    print(f"Retrieved file: {retrieved_file.name} ({retrieved_file.get_size()} KB)")

elif test_case == "file_validation_test":
    try:
        invalid_file = File("negative.txt", -50)
        print("Validation failed - should have raised ValueError")
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    # Test NotImplementedError operations
    valid_file = File("test.txt", 100)
    try:
        valid_file.add(File("other.txt", 50))
    except NotImplementedError as e:
        print(f"Add operation error: {e}")
    
    try:
        valid_file.get_component("nonexistent")
    except NotImplementedError as e:
        print(f"Get component error: {e}")

elif test_case == "directory_duplicate_test":
    directory = Directory("TestDir")
    file1 = File("duplicate.txt", 100)
    file2 = File("duplicate.txt", 200)
    
    directory.add(file1)
    print("First file added successfully")
    
    try:
        directory.add(file2)
        print("Duplicate check failed")
    except ValueError as e:
        print(f"Caught expected duplicate error: {e}")

elif test_case == "component_removal_test":
    directory = Directory("TestDir")
    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 150)
    file3 = File("file3.txt", 200)
    
    directory.add(file1)
    directory.add(file2)
    directory.add(file3)
    
    print("Initial state:")
    print(directory.display())
    
    directory.remove(file2)
    print("\nAfter removing file2.txt:")
    print(directory.display())
    
    try:
        nonexistent = File("ghost.txt", 50)
        directory.remove(nonexistent)
    except ValueError as e:
        print(f"\nRemoval error: {e}")

elif test_case == "recursive_search_test":
    root_dir = Directory("root")
    subdir1 = Directory("subdir1")
    subdir2 = Directory("subdir2")
    
    file1 = File("target.txt", 100)
    file2 = File("other.txt", 150)
    file3 = File("deep.txt", 200)
    
    root_dir.add(subdir1)
    subdir1.add(subdir2)
    subdir1.add(file1)
    subdir2.add(file3)
    root_dir.add(file2)
    
    # Search for existing files
    found1 = root_dir.find_component_recursive("target.txt")
    found2 = root_dir.find_component_recursive("deep.txt")
    not_found = root_dir.find_component_recursive("missing.txt")
    
    print(f"Found target.txt: {found1.name if found1 else 'Not found'}")
    print(f"Found deep.txt: {found2.name if found2 else 'Not found'}")
    print(f"Found missing.txt: {not_found.name if not_found else 'Not found'}")

elif test_case == "size_calculation_test":
    fs = FileSystem()
    
    # Create complex structure
    docs = Directory("Documents")
    images = Directory("Images")
    
    fs.add_to_path("/", docs)
    fs.add_to_path("/", images)
    
    # Add files with known sizes
    doc1 = File("doc1.txt", 100)
    doc2 = File("doc2.txt", 200)
    img1 = File("img1.jpg", 500)
    img2 = File("img2.png", 300)
    
    fs.add_to_path("/Documents", doc1)
    fs.add_to_path("/Documents", doc2)
    fs.add_to_path("/Images", img1)
    fs.add_to_path("/Images", img2)
    
    # Calculate sizes
    docs_size = fs.get_from_path("/Documents").get_size()
    images_size = fs.get_from_path("/Images").get_size()
    total_size = fs.get_total_size()
    
    print(f"Documents size: {docs_size} KB")
    print(f"Images size: {images_size} KB")
    print(f"Total size: {total_size} KB")
    print(f"Sum verification: {docs_size + images_size == total_size}")

elif test_case == "display_formatting_test":
    root = Directory("root")
    level1 = Directory("level1")
    level2 = Directory("level2")
    
    file1 = File("root_file.txt", 100)
    file2 = File("level1_file.txt", 200)
    file3 = File("level2_file.txt", 300)
    
    root.add(file1)
    root.add(level1)
    level1.add(file2)
    level1.add(level2)
    level2.add(file3)
    
    print("Formatted directory structure:")
    print(root.display())

elif test_case == "file_system_path_test":
    fs = FileSystem()
    
    try:
        # Create structure
        fs.add_to_path("/", Directory("home"))
        fs.add_to_path("/home", Directory("user"))
        fs.add_to_path("/home/user", File("profile.txt", 150))
        
        # Test retrieval
        user_dir = fs.get_from_path("/home/user")
        profile = fs.get_from_path("/home/user/profile.txt")
        
        print(f"User directory: {user_dir.name}")
        print(f"Profile file: {profile.name}")
        
        # Test removal
        fs.remove_from_path("/home/user/profile.txt")
        print("Profile removed successfully")
        
        # Try to access removed file
        try:
            fs.get_from_path("/home/user/profile.txt")
        except ValueError as e:
            print(f"Expected error accessing removed file: {e}")
            
    except ValueError as e:
        print(f"Path operation error: {e}")

elif test_case == "empty_directory_test":
    empty_dir = Directory("Empty")
    
    print(f"Empty directory size: {empty_dir.get_size()} KB")
    print("Empty directory display:")
    print(empty_dir.display())
    
    result = empty_dir.get_component("nonexistent")
    print(f"Get nonexistent component: {result}")

elif test_case == "name_property_test":
    file = File("original.txt", 100)
    directory = Directory("OriginalDir")
    
    print(f"Original file name: {file.name}")
    print(f"Original directory name: {directory.name}")
    
    # Test setting valid names
    file.name = "renamed.txt"
    directory.name = "RenamedDir"
    
    print(f"Renamed file: {file.name}")
    print(f"Renamed directory: {directory.name}")
    
    # Test setting empty name
    try:
        file.name = ""
        print("Empty name validation failed")
    except ValueError as e:
        print(f"Empty name error: {e}")

elif test_case == "large_file_system_test":
    fs = FileSystem()
    
    # Create multiple directories and files
    directories = ["Documents", "Images", "Videos", "Music"]
    file_counts = [5, 3, 2, 4]
    base_sizes = [100, 500, 1000, 200]
    
    total_files = 0
    total_directories = len(directories)
    
    for i, dir_name in enumerate(directories):
        fs.add_to_path("/", Directory(dir_name))
        
        for j in range(file_counts[i]):
            file_name = f"file_{j+1}.ext"
            file_size = base_sizes[i] + (j * 50)
            fs.add_to_path(f"/{dir_name}", File(file_name, file_size))
            total_files += 1
    
    print(f"Created {total_directories} directories")
    print(f"Created {total_files} files")
    print(f"Total system size: {fs.get_total_size()} KB")
    print("\nSystem structure:")
    print(fs.display())

elif test_case == "edge_cases_test":
    # Test file with size 0
    zero_file = File("empty.txt", 0)
    print(f"Zero size file: {zero_file.get_size()} KB")
    
    # Test directory with very long name
    long_name = "A" * 100
    long_dir = Directory(long_name)
    print(f"Long directory name length: {len(long_dir.name)}")
    
    # Test deeply nested structure
    current = Directory("level0")
    root = current
    
    for i in range(1, 6):
        next_level = Directory(f"level{i}")
        current.add(next_level)
        current = next_level
    
    # Add file at deepest level
    deep_file = File("deep.txt", 100)
    current.add(deep_file)
    
    print("Deep nesting test:")
    print(root.display())
    
    # Test operations on empty structures
    empty = Directory("Empty")
    try:
        empty.remove(File("ghost.txt", 50))
    except ValueError as e:
        print(f"Empty structure removal error: {e}")