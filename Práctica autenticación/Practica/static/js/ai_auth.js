/*
* Form customization
*/

$("input").on('focus', function() {
  $("body").css('background', '#81b754');
});

$("input").on('focusout', function() {
  $("body").css('background', '#aeff70');
});

// Enviar el formulario pulsando INTRO
$(document).ready(function() {
    $('#target').keydown(function(event) {
        if (event.keyCode == 13) {
            this.form.submit();
            return false;
         }
    });
});

/*
* Events code
*/

eventos = [];
tiempo_vuelo = [];
eventos_pulsar = [];
tiempo_presionado = [];

$("#target").keydown(function(event) {
  // console.log(event);
  eventos_pulsar.push(event);
  if (event.which == 13) {
    event.preventDefault();
  }
});

$("#target").keyup(function(event) {
  // console.log(event);
  eventos_pulsar.push(event);
  if (event.which == 13) {
    event.preventDefault();
  }

  if (eventos.length > 0) {
    var i;

    // Calculo del tiempo de vuelo
    for (i = eventos.length - 1; i > 0; i--) {
      tiempo_vuelo.push(eventos[i].timeStamp - eventos[i - 1].timeStamp);
    }
    // Del array con los distintos valores para el tiempo de vuelo calculamos la media
    if (tiempo_vuelo.length > 0) {
      var suma = 0,
        media = 0;
      for (i = 0; i < tiempo_vuelo.length; i++) {
        suma += tiempo_vuelo[i];
      }
      media = suma / tiempo_vuelo.length;
      $("#vuelo").val(media);
      console.log("La media de tiempo de vuelo es de " + media);
    }

    // Calculo del tiempo que mantiene pulsadas las teclas
    for (i = eventos_pulsar.length - 1; i > 0; i--) {
      tiempo_presionado.push(eventos_pulsar[i].timeStamp - eventos_pulsar[i - 1].timeStamp);
    }
    // Media del tiempo que mantiene pulsadas las teclas
    if (tiempo_presionado.length > 0) {
      var suma = 0,
        media = 0;
      for (i = 0; i < tiempo_presionado.length; i++) {
        suma += tiempo_presionado[i];
      }
      media = suma / tiempo_presionado.length;
      $("#presionado").val(media);
      console.log("La media de tiempo pulsado es de " + media);
    }

  }
});

$("#target").keypress(function(event) {
  // console.log(event);
  eventos.push(event);
  if (event.which == 13) {
    event.preventDefault();
  }
  $("#key").val(event.timeStamp);
});
