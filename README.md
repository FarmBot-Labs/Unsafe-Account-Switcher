# Unsafe Account Switcher

### PROBLEM

 * You are a software developer writing tools for FarmBot.
 * You frequently switch between local and staging servers
 * WiFi reconfiguration is time consuming.

### SOLUTION

 * Use a farmware that switches between servers without re-configuration.

### CAVEATS

 * Not secure. Local development use only! Your password is transmitted over the network in plaintext.
 * Does not work on FBOS < 6.4.10 because of a hard requirement for crypto.
