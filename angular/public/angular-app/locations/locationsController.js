app.controller('locationsController', locationsController);

function locationsController(dataFactory) {
    var vm = this;
    vm.title = 'AR DE Locations'

    dataFactory.locations().then(function (response) {
        console.log(response);

        vm.locations = response;
    })
}