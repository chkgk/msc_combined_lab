(function () {
    "use strict";

    var a = document.createElement( "input" );

    a.setAttribute( "type", "number" );
    a.setAttribute( "value", 2319 );

    if ( "valueAsNumber" in a && a.value !== a.valueAsNumber ) {
        if ( "defineProperty" in Object && "getPrototypeOf" in Object ) {
            Object.defineProperty( Object.getPrototypeOf( a ), "valueAsNumber", {
                get: function () { return parseFloat( this.value, 10 ); }
            });
        }
    }

}());