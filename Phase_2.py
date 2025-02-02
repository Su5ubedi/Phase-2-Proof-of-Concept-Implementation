import heapq

class Product:
    """Class to represent a product in the inventory"""
    def __init__(self, sku, price, category, stock):
        self.sku = sku
        self.price = price
        self.category = category
        self.stock = stock
    
    def __lt__(self, other):
        """Comparator function for heap sorting by stock levels"""
        return self.stock < other.stock
    
    def __repr__(self):
        return f"Product(SKU: {self.sku}, Price: {self.price}, Category: {self.category}, Stock: {self.stock})"

class Inventory:
    """Dynamic inventory management system using multiple data structures"""
    def __init__(self):
        self.products = {}  # Hash Table
        self.price_tree = None  # BST for price-based sorting
        self.restock_queue = []  # FIFO Queue
        self.priority_heap = []  # Min-Heap for low-stock prioritization
    
    # Hash Table Operations
    def add_product(self, product):
        if product.sku not in self.products:
            self.products[product.sku] = product
            heapq.heappush(self.priority_heap, product)  # Add to heap
        else:
            raise ValueError("SKU already exists.")
    
    def get_product(self, sku):
        return self.products.get(sku, "Product not found")
    
    def remove_product(self, sku):
        if sku in self.products:
            del self.products[sku]
        else:
            print("Product not found.")
    
    # Queue Operations
    def enqueue_restock(self, product):
        self.restock_queue.append(product)
    
    def process_restock(self):
        if self.restock_queue:
            return self.restock_queue.pop(0)
        return "No products to restock."
    
    # Heap Operations
    def get_low_stock_product(self):
        if self.priority_heap:
            return heapq.heappop(self.priority_heap)
        return "No low-stock products."
    
    # Display all products
    def display_inventory(self):
        return list(self.products.values())

# ========== TESTING THE SYSTEM ==========

def test_inventory():
    inventory = Inventory()
    
    # Adding Products
    p1 = Product("A100", 20.5, "Electronics", 15)
    p2 = Product("B200", 10.0, "Groceries", 5)
    p3 = Product("C300", 50.0, "Clothing", 2)
    
    inventory.add_product(p1)
    inventory.add_product(p2)
    inventory.add_product(p3)
    
    print("Inventory after adding products:")
    print(inventory.display_inventory())
    
    # Get Product
    print("\nFetching product B200:")
    print(inventory.get_product("B200"))
    
    # Remove Product
    inventory.remove_product("A100")
    print("\nInventory after removing product A100:")
    print(inventory.display_inventory())
    
    # Restocking Process
    inventory.enqueue_restock(p2)
    print("\nProcessing Restock:")
    print(inventory.process_restock())
    
    # Low-stock priority
    print("\nProduct with lowest stock:")
    print(inventory.get_low_stock_product())

# Run test cases
test_inventory()
