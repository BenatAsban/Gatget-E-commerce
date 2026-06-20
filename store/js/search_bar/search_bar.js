
  // Wait for the DOM to be fully loaded
  document.addEventListener('DOMContentLoaded', function() {
    // Get elements
    const searchInput = document.querySelector('.search-input');
    const searchButton = document.querySelector('.search-button');

    // Check if elements exist before adding event listener
    if (searchInput && searchButton) {
      // Event listener for search button click
      searchButton.addEventListener('click', function() {
        const query = searchInput.value.trim(); // Trim any leading or trailing whitespace
        if (query) {
          // Here you can handle what happens when the search button is clicked
          console.log('Search query:', query);
          // You can perform further actions such as displaying search results or navigating to a search results page
        } else {
          console.log('Please enter a search query');
          // You can display a message or perform another action if the search query is empty
        }
      });
    } else {
      console.error('Search input or search button not found');
    }
  });

