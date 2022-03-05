# Flight deal finder

Conectamos nuestra hoja de excel en google drive, con la api de sheety

![](img/img0.JPG)

Conectamos con la hoja gracia a sheety en python y vemos su contenido

![](img/img1.JPG)

Con ayuda de la API tequila obtenemos los iataCode de las ciudades que tenemos en nuestro excel, los preparamos en un archivo json.

![](img/img2.JPG)

Los insertamos via put en nuestro excel, ahora luce así. 

![](img/img3.JPG)

Con ayuda de la API tequila y gracias al código de las ciudades obtenemos los precios a cada una de la ciudades que tenemos en el excel partiendo de Londres. Comparamos los precios en los proximos 6 meses a esas ciudades.

![](img/img4.JPG)

Nos notificamos via SMS con ayuda de twilio cuando se encuentre el menor precio.

![](img/im5.jpeg)

Del mismo modo sí se desea se pueden agregar clientes que desean recibir la información vía correo. Tal y como se ve en la imagen se le pedirán los datos y se enviaran a el excel users.

![](img/img5.jpeg)

Ahora comprobamos y observamos que se tienen esos datos en la hoja de excel

![](img/img6.JPG)

Finalmente tambien enviamos las ofertas via email

![](img/img7.JPG)
