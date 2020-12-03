console.log("Script loaded successfully ");
function test(){
    Java.perform(function () {
        console.log('hook starting ')
        var X509TrustManager = Java.use('javax.net.ssl.X509TrustManager');
        var SSLContext = Java.use('javax.net.ssl.SSLContext');

        // build fake trust manager
        var TrustManager = Java.registerClass({
            name: 'com.sensepost.test.TrustManager',
            implements: [X509TrustManager],
            methods: {
                checkClientTrusted: function (chain, authType) {
                },
                checkServerTrusted: function (chain, authType) {
                },
                getAcceptedIssuers: function () {
                    return [];
                }
            }
        });

        // pass our own custom trust manager through when requested
        var TrustManagers = [TrustManager.$new()];
        var SSLContext_init = SSLContext.init.overload(
            '[Ljavax.net.ssl.KeyManager;', '[Ljavax.net.ssl.TrustManager;', 'java.security.SecureRandom'
        );
        SSLContext_init.implementation = function (keyManager, trustManager, secureRandom) {
            console.log('! Intercepted trustmanager request');
            SSLContext_init.call(this, keyManager, TrustManagers, secureRandom);
        };
        console.log('* Setup custom trust manager');

        // var MainActivity = Java.use("com.icbc.im.utils.aj");
        // MainActivity.commonEncryUrl.overload("java.lang.String").implementation=function(s){
        //     console.log('args[0]'+s)
        //     var url = this.commonEncryUrl(s)
        //     console.log('resval:' + url)
        // }
        var clazz = Java.use("com.icbc.mims.thirdparty.filter.util.MimsDes");
        clazz.encrypt.implementation=function(a, b){
            console.log('args[0]:'+a+'\n' + b.join('==='));
            var resval = this.encrypt(a, b);
            console.log('result:'+resval);
            return resval
        }
        console.log('hook end ...')

    });
}
