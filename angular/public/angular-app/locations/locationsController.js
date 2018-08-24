app.controller('locationsController', locationsController);

function locationsController(dataFactory) {
    var vm = this;
    vm.title = 'Locations'

    dataFactory.locations().then(function (response) {
        console.log(response);

        vm.locations = response[0];
    })
}