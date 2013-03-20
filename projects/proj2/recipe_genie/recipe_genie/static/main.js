$(document).ready(function() {
  var allIngredients = [];
  var currentIngredients = [];
  $.getJSON('/static/all_ingredients.json', function(data) {
    allIngredients = data;
  });

  $('#new_ingredient_field').typeahead({
    source: function(query, process) {
      process(allIngredients);
    }
  });

  var populateRecipes = function() {
    console.log('TODO: populateRecipes');
  };

  var addIngredient = function() {
    var ingredient = $('#new_ingredient_field').val();
    if (allIngredients.indexOf(ingredient) !== -1 &&
        currentIngredients.indexOf(ingredient) === -1) {
      currentIngredients.push(ingredient);
      var ingredientSpan = '<span class="ingredient">' + ingredient +
        '<button class="close">&times;</button></span>';
      $('#ingredients_container').append(ingredientSpan);
      $('#new_ingredient_field').val('');
      populateRecipes();
    }
  };

  $('#new_ingredient_field').on("change", function(e) {
    if (!e.originalEvent) {
      addIngredient();
    }
  });

  $('#add_ingredient_form').submit(function(e) {
    e.preventDefault();
    addIngredient();
  });

  $('#ingredients_container').on('click', 'button', function(e) {
    var ingredientSpan = $(e.currentTarget).parent();
    var ingredient = ingredientSpan.text().slice(0, -1);
    var idx = currentIngredients.indexOf(ingredient);
    if (idx !== -1) {
      currentIngredients.splice(idx, 1);
    }
    ingredientSpan.remove();
    populateRecipes();
  });
});
