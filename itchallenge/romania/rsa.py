import base64
from pyasn1.codec.der import encoder
from pyasn1.type import univ


def recover_key(p, q, e, output_file):

    # Extended Euclidean Algorithm
    def egcd(a, b):
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
        return gcd, x, y

    def modinv(a, m):
        gcd, x, y = egcd(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m

    def pempriv(n, e, d, p, q, dP, dQ, qInv):
        template = '-----BEGIN RSA PRIVATE KEY-----\n{}-----END RSA PRIVATE KEY-----\n'
        seq = univ.Sequence()
        for x in [0, n, e, d, p, q, dP, dQ, qInv]:
            seq.setComponentByPosition(len(seq), univ.Integer(x))
        der = encoder.encode(seq)
        return template.format(base64.encodestring(der).decode('ascii'))

    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    dp = modinv(e, (p - 1))
    dq = modinv(e, (q - 1))
    qi = modinv(q, p)

    key = pempriv(n, e, d, p, q, dp, dq, qi)

    f = open(output_file, "w")
    f.write(key)
    f.close()


# Obtained from pub key modulus
e = 65537

# Obtained with n / q
p = 57248512388615138300979959427360676128469

# known
q = 1094782941871623486260250734009229761

recover_key(p, q, e, "id_rsa.key")

# ASN1 Public key decrypted
# 62674694810582163977646464092292439405182466161502960359408571447710174165909
# 65537

# cat data | openssl rsautl -decrypt -inkey id_rsa.key
