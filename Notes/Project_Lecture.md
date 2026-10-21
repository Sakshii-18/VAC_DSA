**#Project Lecture 8-10-26**



* **Client-server architecture**
* **DNS internal working**
* **website flow : http(by default 80) vs https(by default 443, encrypts data by using hashing algo(SHA256) , need certificate : SSL),JWT,Token**
* **encrypt/decrypt :** 1\*\*.One way algo\*\* 2\*\*.Two way algo\*\*
we hash password and save it in DB [onced hashed it can't return to normal state],after logging in how db checks if password is same or not ?: hash the givenm pass and compare/... uses key for security.[internal working?0
* **Man in the Middle - Attack**
* **CDN(content delivery network) - Cloudflare**
* **Port Mapping**
* **Nginx(does port mapping) - reverse proxy**
* **rainbow table - (used by attacker) : its like a table where data (decrypted) is stored**
* **linux - kernel**
* &#x20;**ubantu : Os based on linux**
* **kali /**





**#Project Lecture 9-10-26**



* **blob storage**
* **CORS**
* **CICD - JINX,DOCKER**
* **API**
* **METHODS : get,post (create/add),put (update),patch(update),del -- put updates whole schema vs patch updates particular field/record**
* **Headers : Authentication \& Authorization**
* **when credentials are sent to server it returns token ( server request to db where data is is stored) 1.Access token 2.Refresh token (Session)**
* **Cookie \& its types**
* **localstorage(browers own strg) , Secure local storage**
* **TTL(Time to leave) - log out destroys this token**
* **status code : 200 - success, 500 related : server error, 300 related : resource redirection/locator, 400 related - not found \& other imps 429 : rate limiting(DOS \& DDOS)**
* **Nginx : does forward proxy . request ---> hides other implementation** 
* **ping <domainname>**
* **VPN**
* dos & ddos
* reverse / forward proxy

#16 OCT  

inspect --> network (request -> API -> header,payload(body)dpdpconsent?,response,cookies(JWT Token : sent in 2 format : 1.local storage(unsecured) 2. cookie Storage);
console - cookies(request cookie) :refresh token ,access token [some cycle goes on til that token expires? what cycle?what happens after expiry?] , token encodes which user has requested-->  ;
JWT ---> header[we fill data] , payload[we fill data ] , signature [we fill timestamp];[userid brofre comma somehwere]
Authetication vs Autherization vs Authenticated
authentication API = Public , Authenticated API = private
Authenticated API : passes through middleware , when backend asks u for identity? JWT access token requests authenticated API
login () : asks for email /pass -->checks if email exist or not --> db retuns true/false -->now it will send pass + take salt we saved in env -->run by decrypt/bcrypt smtg -->goes in db compares db ----> now makes to JWT --> secret key,password passed to jwt --> access token ---> one more jwt secret.username ---> refresh token
salt : additional security layer






