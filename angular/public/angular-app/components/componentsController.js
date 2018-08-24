app.controller('componentsController', componentsController);

function componentsController(dataFactory) {
    var vm = this;
    vm.title = 'Components';

    dataFactory.components().then(function (response) {
        console.log(response);
        vm.components = response[0];
    })
}