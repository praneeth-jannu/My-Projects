document.getElementById("recipe-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting

    const recipeName = document.getElementById("recipe-name").value;
    const recipeIngredients = document.getElementById("recipe-ingredients").value;
    const recipeInstructions = document.getElementById("recipe-instructions").value;

    addRecipe(recipeName, recipeIngredients, recipeInstructions);

    // Clear the form fields
    document.getElementById("recipe-name").value = "";
    document.getElementById("recipe-ingredients").value = "";
    document.getElementById("recipe-instructions").value = "";
});

// Initialize with sample recipes
const sampleRecipes = [
    {
        name: "Chocolate Chip Cookies",
        ingredients: "1 cup butter, 1 cup sugar, 2 cups flour, 2 cups chocolate chips, 1 tsp vanilla extract",
        instructions: "Preheat the oven to 350°F. In a bowl, mix butter and sugar. Add flour and chocolate chips. Bake for 10 minutes."
    },
    {
        name: "Spaghetti Carbonara",
        ingredients: "200g spaghetti, 100g pancetta, 2 eggs, 50g Parmesan cheese, pepper",
        instructions: "Cook spaghetti. In a pan, fry pancetta. Mix eggs and cheese. Combine with spaghetti and pancetta. Serve with pepper."
    },
    {
        name: "Caesar Salad",
        ingredients: "Romaine lettuce, croutons, Caesar dressing, Parmesan cheese",
        instructions: "Chop lettuce. Toss with croutons and dressing. Top with Parmesan cheese."
    }
];

// Function to add recipes to the list
function addRecipe(name, ingredients, instructions) {
    const recipesList = document.getElementById("recipes");
    const listItem = document.createElement("li");

    listItem.innerHTML = `
        <strong>${name}</strong><br>
        <em>Ingredients:</em> ${ingredients}<br>
        <em>Instructions:</em> ${instructions}
    `;
    recipesList.appendChild(listItem);
}

// Load sample recipes on page load
window.onload = function() {
    sampleRecipes.forEach(recipe => {
        addRecipe(recipe.name, recipe.ingredients, recipe.instructions);
    });
};
