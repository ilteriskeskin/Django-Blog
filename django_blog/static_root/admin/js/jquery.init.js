/*global django:true, js:false*/
/* Puts the included js into our own namespace using noConflict and passing
 * it 'true'. This ensures that the included js doesn't pollute the global
 * namespace (i.e. this preserves pre-existing values for both window.$ and
 * window.js).
 */
var django = django || {};
django.jQuery = jQuery.noConflict(true);
