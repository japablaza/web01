# Apache

## Ubuntu

- Disable ServerTokens
  - `/etc/apache2/conf-available/security.conf`
    - `ServerTokens Prod`
    - `service apache2 reload`
- Disable .htaccess files
  - `/etc/apache2/apache2.conf`
    - `AllowOverride None`
- Prevent DoS Attacks
  - Enable mod_reqtimeout
    - `mod_reqtimeout`
    - Add the following configuration to `/etc/apache2/apache2.conf`
    - `RequestReadTimeout header=10-20,MinRate=500 body=20,MinRate=500`
## More Information

- <https://help.dreamhost.com/hc/en-us/articles/226327268-The-most-important-steps-to-take-to-make-an-Apache-server-more-secure>