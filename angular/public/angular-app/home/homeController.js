app.controller('homeController', homeController);

function homeController(dataFactory) {
    var vm = this;
    vm.title = 'Home';


    // dataFactory.homePage().then(function (response) {
    //     console.log(response);
    //     vm.home = response;

    // })

    dataFactory.components().then(function (response) {
        console.log(response);
        vm.components = response[0];
    })
    dataFactory.locations().then(function (response) {
        console.log(response);
        vm.locations = response[0];
    })

}