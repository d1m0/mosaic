import dropbox
from dropbox import Dropbox
from time import time
import os
import ntpath

token = "FILL ME IN"

dropBoxAcc = Dropbox(token)

# strip out the filename of an input path
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


# given a filename and a user, return a new filename with the username and current time prefixed
# TODO
# def convertFName(user, fname):



# upload a file to the dropbox token from a filepath.

# dropbox has two upload methods: a simple one, for small files (< 150 MB),
# and a more complicated one for 150 MB chunks. dynamically choose the method
# based off the input file size.

# returns the upload result.

# TODO: make robust to upload failures
def uploadFileFromPath(file_path):
    prefix = "/user_videos/"
    dest_path = prefix + path_leaf(file_path)
    CHUNK_SIZE = 128 * 1024 * 1024 #128 MB chunks

    with open(file_path) as f:
        file_size = os.path.getsize(file_path)

        if file_size <= CHUNK_SIZE:

            # print "starting small upload"
            # print dropBoxAcc.files_upload(f, dest_path)
            return dropBoxAcc.files_upload(f, dest_path)

        else:


            # print "starting large upload"
            num_chunks = file_size/CHUNK_SIZE
            # print "CHUNKS: ", num_chunks
            counter = 0


            upload_session_start_result = dropBoxAcc.files_upload_session_start(
                f.read(CHUNK_SIZE)
            )

            # print upload_session_start_result
            # print "Uploaded chunk ", counter
            counter += 1
            # print f.tell()



            cursor = dropbox.files.UploadSessionCursor(
                session_id=upload_session_start_result.session_id,
                offset=f.tell()
            )
            commit = dropbox.files.CommitInfo(path=dest_path)

            while f.tell() < file_size:

                if ((file_size - f.tell()) <= CHUNK_SIZE):

                    # dropBoxAcc.files_upload_session_append_v2(
                    #     f.read(CHUNK_SIZE),
                    #     cursor,
                    #     True
                    # )
                    # cursor.offset = f.tell()
                    # print f.tell()
                    # nxt =
                    # print len(nxt)
                    # print cursor
                    # print commit

                    return dropBoxAcc.files_upload_session_finish(
                        f.read(CHUNK_SIZE),
                        cursor,
                        commit
                    )

                    # print "Uploaded chunk ", counter

                    # print "done!"

                else:
                    dropBoxAcc.files_upload_session_append_v2(
                        f.read(CHUNK_SIZE),
                        cursor
                    )
                    # print "Uploaded chunk ", counter
                    # counter += 1
                    cursor.offset = f.tell()
                    # print f.tell()
