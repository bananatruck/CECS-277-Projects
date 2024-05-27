class Contact:
  def __init__(self, first_name, last_name, phone, address, city, zip_code):
    """Initializes a Contact object with the given first name, last name, phone number, address,
    city, and zip code."""
    self.first_name = first_name
    self.last_name = last_name
    self.phone = phone
    self.address = address
    self.city = city
    self.zip_code = zip_code

  def __lt__(self, other):
    """Compares two Contact objects based on their last name and first name."""
    if self.last_name != other.last_name:
        return self.last_name < other.last_name
    else:
        return self.first_name < other.first_name

  def __str__(self):
    """Returns a string representation of the Contact object to display."""
    return f"First Name: {self.first_name}, Last Name: {self.last_name}, Phone: {self.phone}, Address: {self.address}, City: {self.city}, Zip: {self.zip_code}"

  def __repr__(self):
    """Returns a string representation of the Contact object to write to file."""
    return f"{self.first_name},{self.last_name},{self.phone},{self.address},{self.city},{self.zip_code}"
