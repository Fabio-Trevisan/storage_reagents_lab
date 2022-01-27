from segno import helpers
import segno

# generate qr code

qr_consumabili = segno.make('https://stramon1um.github.io/storage_reagents_lab/index.html')

qr_reagenti = segno.make('https://stramon1um.github.io/storage_reagents_lab/page_2.html')

qr_email = segno.helpers.make_email(to='mauro.maver@unibz.it', cc=None, bcc=None, subject='[Update] Storage K-1 and Lab 1.20', body=None)


# save qr code
qr_consumabili.save('qr_consumabili.svg', scale=3, dark='black', data_dark='#198259',data_light='white', quiet_zone="#198259")

qr_reagenti.save('qr_reagenti.svg', scale=3, dark='black', data_dark='#198259',data_light='white', quiet_zone="#198259")

qr_email.save('qr_lab_mail.svg', scale=3, dark='black', data_dark='#198259',data_light='white', quiet_zone="#198259")