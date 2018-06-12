var app = angular.module('rulesApp', ['ngRoute']).config(config);

function config($locationProvider, $routeProvider) {
    $locationProvider.hashPrefix('');
    $routeProvider
        .when('/', {
            templateUrl: '/angular-app/home/home.html',
            controller: homeController,
            controllerAs: 'vm'
        })
        .when('/part-numbers', {
            templateUrl: '/angular-app/part-numbers/part_numbers.html',
            controller: partNumbersController,
            controllerAs: 'vm'
        })
        .when('/categories', {
            templateUrl: '/angular-app/categories/categories.html',
            controller: categoriesController,
            controllerAs: 'vm'
        })
        .when('/locations', {
            templateUrl:'/angular-app/locations/locations.html',
            controller: locationsController,
            controllerAs: 'vm'
        })
        .when('/components', {
            templateUrl: '/angular-app/components/components.html',
            controller: componentsController,
            controllerAs: 'vm'
        })
        .when('/rules', {
            templateUrl: '/angular-app/rules/rules.html',
            controller: rulesController,
            controllerAs: 'vm'
        })
        .otherwise({
            redirectTo:'/'})
}