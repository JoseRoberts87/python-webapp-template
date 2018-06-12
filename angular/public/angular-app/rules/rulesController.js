app.controller('rulesController', rulesController);

function rulesController(dataFactory) {
    var vm = this;
    vm.title = 'Audit Rules';

    dataFactory.rules().then(function (response) {
        console.log(response);

        vm.rules = response;
    })

}