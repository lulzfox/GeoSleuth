function getLocation(callback) {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        callback({
          latitude: position.coords.latitude,
          longitude: position.coords.longitude
        });
      });
    } else {
      callback(null);
    }
  }
  