from p2p_node import P2PNode
from network_manager import NetworkManager
from file_chunker import FileChunker
import threading
import time

if __name__ == "__main__":

    local_ip = "172.20.10.6"
    local_port = 5000

    node_id = f"node_{local_ip}:{local_port}"
    node = P2PNode(node_id, local_ip, local_port)
    network = NetworkManager(local_ip, local_port)


    server_thread = threading.Thread(target=network.start_server, args=(node,))
    server_thread.daemon = True
    server_thread.start()

    node.add_peer("172.20.10.4", 5001)

    chunker = FileChunker("farouqfile.txt")
    chunks = chunker.file_chunker()

    for chunk in chunks:
        for peer_ip, peer_port in node.peers:
            node.upload_file_chunk(peer_ip, peer_port, chunk)

    time.sleep(10)

    network.reassemble_received_chunks("reassembled_file.txt")

    threading.Event().wait()

