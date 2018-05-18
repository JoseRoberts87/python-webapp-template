var app = angular.module('rulesApp', ['ngRoute']).config(config);

function config($LocationProvider, $routeProvider) {
    $LocationProvider.hashPrefic('');
    $routeProvider
        .when('/', {
            templateUrl: 'index',
            controller: homeController,
            controllerAs: 'vm'
        })
        .when('/create', {
            templateUrl: 'create',
            controller: createRuleController,
            controllerAs: 'vm'
        })
        .when('/results', {
            templateUrl: 'results',
            controller: resultsController,
            controllerAs: 'vm'
        })
        .when('/', {
            templateUrl:'',
            controller: someController,
            controllerAs: 'vm'
        })
        .otherwise({
            redirectTo:'/'})
}