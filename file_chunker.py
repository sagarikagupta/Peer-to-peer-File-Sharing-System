class FileChunker:
    def __init__(self, file_path):
        """
        Location of the original book to break into pages

        Path of the file that needs to be broken into chunks.
        """
        self.file_path = file_path

    
    def file_chunker(self, chunk_size=512):

        """
        This reads the file and splits it into smaller parts of 512 bytes each.

        Like tearing pages from a book.

        These chunks (pages) will be shared with the neighbors.
        """

        chunks = [] # List of pieces of the file (pages of the book, should be 512 bytes each)
        with open(self.file_path, 'rb') as f:
            while chunk := f.read(chunk_size): # Reads 512 bytes at a time
                chunks.append(chunk) # Adds each 512 byte chunk to the list
            
        return chunks
        
    
    def reassemble_file(self, chunks, output_file):
        """
        Reassembles the file from the chunks.

        Like putting the pages back together to form the book.
        """
        with open(output_file, 'wb') as f:
            for chunk in chunks:
                f.write(chunk) # Writes each chunk back to the file (reassembles the pages to form the book)

