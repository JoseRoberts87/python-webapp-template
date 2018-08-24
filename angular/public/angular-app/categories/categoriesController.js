app.controller('categoriesController', categoriesController);

function categoriesController(dataFactory) {

    var vm = this;

    vm.title = 'Categories'

    dataFactory.categories().then(function (response) {
        console.log(response);
        vm.categories = response[0];

    })

}