from file_system_component import FileSystemComponent

class Directory(FileSystemComponent):
    """Represents a directory in the file system.
    
    This class serves as the 'Composite' in the Composite pattern.
    """
    
    def __init__(self, name):
        # TODO: Call parent constructor with name using super()
        # TODO: Initialize empty list _components to store child components
        super().__init__(name)
        self._components = []
    
    def get_size(self):
        # TODO: Return the sum of sizes of all components in _components
        # TODO: Use sum() with generator expression: component.get_size() for each component
        return sum(component.get_size() for component in self._components)
    
    def display(self, indent=0):
        # TODO: Create result list starting with directory header
        # TODO: Header format: " " * indent + f"Directory: {self.name} ({self.get_size()} KB)"
        # TODO: For each component in _components, add component.display(indent + 2) to result
        # TODO: Join all result strings with "\n" and return
        result = []
        header=" " * indent + f"Directory: {self.name} ({self.get_size()} KB)"
        result.append(header)
        for component in self._components:
            result.append(component.display(indent + 2))
        return "\n".join(result)
    
    def add(self, component):
        # TODO: Check if any component in _components has the same name as the new component
        # TODO: If duplicate name found, raise ValueError: f"Component with name '{component.name}' already exists"
        # TODO: If no duplicate, append component to _components list
        for comp in self._components:
            if comp.name == component.name:
                raise ValueError(f"Component with name '{component.name}' already exists")
            
        self._components.append(component)
    
    def remove(self, component):
        # TODO: Check if component exists in _components list
        # TODO: If found, remove it from _components
        # TODO: If not found, raise ValueError: f"Component {component.name} not found"
        if component in self._components:
                self._components.remove(component)
        else:
            raise ValueError(f"Component {component.name} not found")
    
    def get_component(self, name):
        # TODO: Iterate through _components list
        # TODO: For each component, check if component.name equals the search name
        # TODO: Return the component if found, otherwise return None
        for comp in self._components:
            if comp.name == name:
                return comp
            
        return None
    
    def find_component_recursive(self, name):
        """Recursively searches for a component with the given name."""
        # TODO: First check direct children using get_component(name)
        # TODO: If component found, return it
        # TODO: Then check in subdirectories: iterate through _components
        # TODO: For each component that is isinstance(component, Directory):
        # TODO:   Call component.find_component_recursive(name)
        # TODO:   If found (not None), return the found component
        # TODO: Return None if not found anywhere
        found = self.get_component(name)
        if found is not None:
            return found
        else:
            for comp in self._components:
                if isinstance(comp, Directory):
                    sub_found = comp.find_component_recursive(name)
                    if sub_found is not None:
                        return sub_found
        return None

