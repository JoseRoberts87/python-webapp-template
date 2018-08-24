app.controller('partNumbersController', partNumbersController);

function partNumbersController(dataFactory) {

    var vm = this;
    vm.title = 'Part Numbers';

    dataFactory.partNumbers().then(function (response) {

        console.log(response);
        vm.partNumbers = response[0];

    })

}

