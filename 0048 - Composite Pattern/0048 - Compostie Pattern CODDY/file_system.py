from directory import Directory

class FileSystem:
    """Represents the overall file system.
    
    This class serves as a facade for working with the file system components.
    """
    
    def __init__(self):
        # TODO: Create root directory with name "root"
        # TODO: Store it as self.root
        self.root = Directory("root")
    
    def _get_directory_from_path(self, path):
        """Helper method to navigate to a directory from a path."""
        # TODO: If path is empty or "/", return self.root
        # TODO: Split path by "/" and remove empty parts
        # TODO: Navigate through path parts starting from root
        # TODO: For each part except last, get component and verify it's a directory
        # TODO: Return (parent_directory, target_component) tuple
        # TODO: Raise ValueError if path not found or component is not directory
        if path == "" or path == "/":
            return (None, self.root)
        else:
            parts = [p for p in path.split("/") if p]
            
            # 1. Beállítjuk a kiindulópontot
            current_dir = self.root
            parent_dir = None
            
            # 2. Csak ezután indul a ciklus végig a szövegeken
            for p in parts:

                if not isinstance(current_dir, Directory):
                    raise ValueError("Component in path is not a directory")

                parent_dir = current_dir
                current_dir = current_dir.get_component(p)
                
                # Ha a keresett név nem létezik a mappában:
                if current_dir is None:
                    raise ValueError(f"Path not found: {path}")
            return (parent_dir, current_dir)
    
    def add_to_path(self, path, component):
        """Adds a component at the specified path."""
        # TODO: If path is empty or "/", add component to root directory
        # TODO: Otherwise, get parent directory from path
        # TODO: Add component to parent directory
        if path == "" or path == "/":
            self.root.add(component)
        else:
            parent, target = self._get_directory_from_path(path)
            target.add(component)
    
    def remove_from_path(self, path):
        """Removes a component at the specified path."""
        # TODO: Check if trying to remove root directory (raise ValueError)
        # TODO: Get parent directory and target component from path
        # TODO: If component exists, remove it from parent
        # TODO: Otherwise raise ValueError for path not found
        if path == "" or path == "/":
            raise ValueError("cannot remove root")
        else:
            parent, target = self._get_directory_from_path(path)

            parent.remove(target)

        
    
    def get_from_path(self, path):
        """Retrieves a component at the specified path."""
        # TODO: If path is empty or "/", return root directory
        # TODO: Otherwise, use _get_directory_from_path to get component
        # TODO: Return the component
        if path == "" or path == "/":
            return self.root
        else:
            parent, target = self._get_directory_from_path(path)
            return target

    
    def display(self):
        """Displays the entire file system."""
        # TODO: Return the result of calling display() on root directory
        return self.root.display()
    
    def get_total_size(self):
        """Returns the total size of all files in the system."""
        # TODO: Return the result of calling get_size() on root directory
        return self.root.get_size()