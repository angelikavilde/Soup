$(document).ready(function() {
  const autocompleteList = ["Salt", "Pepper", "Sugar", "Flour", "Butter", "Milk", "Eggs"];

  $("#ingredientInput").autocomplete({
    source: autocompleteList});

  $("#addIngredientBtn").on("click", function() {
    const ingredient = $("#ingredientInput").val().trim();
    if (ingredient) {
      $("#ingredientList").append("<li>" + ingredient + "</li>");
      $("#ingredientInput").val("");}  });

  $("#ingredientForm").submit(function(event) {
    event.preventDefault();

    // Get the selected ingredients from the list
    const selectedIngredients = $("#ingredientList li").map(function() {
      return $(this).text();}).get();

    // Redirect to the new page with the selected ingredients as query parameters
    const queryString = selectedIngredients.length > 0 ? "?ingredients=" + selectedIngredients.join(",") : "";
    window.location.href = "new-page.html" + queryString;
  });
});
