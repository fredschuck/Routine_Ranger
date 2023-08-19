document.addEventListener("DOMContentLoaded", function() {
  var select = document.getElementById("multiSelect");

  // Add a click event listener to each option
  select.querySelectorAll("option").forEach(function(option) {
    option.addEventListener("click", function() {
      // Toggle the selected attribute of the clicked option
      this.toggleAttribute("selected");
    });
  });

  // Prevent the default behavior of selecting text when clicking on the option
  select.addEventListener("mousedown", function(e) {
    e.preventDefault();
  });
});