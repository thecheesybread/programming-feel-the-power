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
    $.ajax({
      url: '/get_recipes',
      data: {ingredients: JSON.stringify(currentIngredients)}
    }).done(function(res) {
      $('#recipes_container').html('');
      recipes = JSON.parse(res);
      var max = Math.min(recipes.length, 30);
      for (var i = 0; i < max; i++) {
        var percentStr = '';
        if (recipes[i]['percent'] !== undefined) {
          percentStr = ' (' + recipes[i]['percent'] + '% of ingredients)';
        }
        var recipeLink = '<a href="' + recipes[i]['url'] + '">' +
          recipes[i]['title'] + '</a>' + percentStr + '<br>';
        $('#recipes_container').append(recipeLink);
      }
    });
  };

  var addIngredient = function() {
    var ingredient = $('#new_ingredient_field').val();
    if (currentIngredients.indexOf(ingredient) === -1) {
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
