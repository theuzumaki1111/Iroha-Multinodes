from iroha import IrohaCrypto, IrohaGrpc, Iroha
from iroha import primitive_pb2



def generate_peer_key():
    peer_key = IrohaCrypto.private_key()
    peer = primitive_pb2.Peer()
    public = IrohaCrypto.derive_public_key(peer_key)
    peer.peer_key = public

    return {
                "priv_key": peer_key, 
                "pub_key": public
           }

def generate_user_key():
    user_private_key = IrohaCrypto.private_key()
    user_public_key = IrohaCrypto.derive_public_key(user_private_key)
    
    return {
                "priv_key": user_private_key, 
                "pub_key": user_public_key
           }


peer = generate_peer_key()
user = generate_user_key()

print(peer)
print(user)