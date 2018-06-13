app.factory('dataFactory', dataFactory);

var root = 'http://127.0.0.1:5000/';

function dataFactory($http) {
    return {
        homePage: homePage,
        partNumbers: partNumbers,
        categories: categories,
        components:components,
        locations:locations,
        rules:rules,
        login: login,
        register: register
    }

    function homePage() {
        return $http.get(root).then(complete).catch(failed);
    }

    function partNumbers() {
        return $http.get(root + 'part-numbers').then(complete).catch(failed);
    }

    function categories() {
        return $http.get(root + 'categories').then(complete).catch(failed);
    }

    function components() {
        return $http.get(root + 'components').then(complete).catch(failed);
    }

    function locations() {
        return $http.get(root + 'locations').then(complete).catch(failed);
    }

    function rules() {
        return $http.get(root + 'rules').then(complete).catch(failed);
    }

    function login() {
        return $http.get(root + 'login').then(complete).catch(failed);
    }

    function register() {
        return $http.get(root + 'register').then(complete).catch(failed);
    }

    function complete(response) {
        return response.data;
    }

    function failed(error) {
        console.log(error.statusText);
    }
}