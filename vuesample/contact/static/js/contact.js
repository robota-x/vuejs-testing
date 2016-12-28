'use strict';
console.log('contact loaded');

// gmaps callback
function initMap() {
    var myPosition = {lat: 42, lng: 42};
    var map = new google.maps.Map(document.getElementById('office-map'), {
        zoom: 4,
        center: myPosition
    });
    var marker = new google.maps.Marker({
        position: myPosition,
        map: map
    });
}


// vue.js
window.onload = function() {
    var message = 'Hello Vue!';

    var officeList = new Vue({
        el: '#office-list',
        data: {
            message: message
        },
        methods: {
            getOffices: getOffices
        }
    });

    function getOffices() {
        var requestHandler = $.get( "/offices")
          .done(function(res) {
              officeList.message = res;
          })
          .fail(function() {
              officeList.message = 'loading failed'
          })
    }
};

