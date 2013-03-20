$(document).ready(function() {
  var allIngredients = [];
  $.getJSON('/static/all_ingredients.json', function(data) {
    allIngredients = data;
  });

  $('#new_ingredient_field').typeahead({
    source: function(query, process) {
      process(allIngredients);
    }
  });
});
