app.controller('componentsController', componentsController);

function componentsController(dataFactory) {
    var vm = this;
    vm.title = 'AR DE Components';

    dataFactory.components().then(function (response) {
        console.log(response);
        vm.components = response;
    })
}