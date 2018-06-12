app.factory('dataFactory', dataFactory);

var root = 'http://localhost:8761/api/';


function dataFactory($http) {
    return {
        home: home,
        part_numbers: part_numbers,
        categories: categories,
        login: login,
        register: register
    }

    function home() {
        return $http.get('api/').then(complete).catch(failed);
    }

    function part_numbers() {
        return $http.get('api/part_numbers').then(complete).catch(failed);
    }

    function categories() {
        return $http.get('api/categories/').then(complete).catch(failed);
    }

    function login() {
        return $http.get('api/login').then(complete).catch(failed);
    }

    function register() {
        return $http.get('api/register').then(complete).catch(failed);
    }

    function complete(response) {
        return response.data;
    }

    function failed(error) {
        console.log(error.statusText);
    }
}