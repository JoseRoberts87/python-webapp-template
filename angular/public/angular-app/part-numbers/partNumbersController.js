app.controller('partNumbersController', partNumbersController);

function partNumbersController(dataFactory) {

    var vm = this;
    vm.title = 'AR DE Part Numbers';
    console.log('controller activated 1');


    dataFactory.partNumbers().then(function (response) {

        console.log(response);
        console.log('controller activated 2');

        vm.partNumbers = response;

    })

}

