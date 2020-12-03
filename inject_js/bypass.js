
setTimeout(function() { // avoid java.lang.ClassNotFoundException

	Java.perform(function() {

		// Root detection bypass example

		// var hook = Java.use("com.target.utils.RootCheck");
		console.log("info: hooking target class");

		// hook.isRooted.overload().implementation = function() {
		// 	console.log("info: entered target method");
        //
		// 	// obtain old retval
		// 	var retval = this.isRooted.overload().call(this);
		// 	console.log("old ret value: " + retval);
        //
		// 	// set new retval
		// 	var retnew = false;
		// 	console.log("new ret value: " + retnew);
		// 	return retnew;
		// }

	});

}, 0);