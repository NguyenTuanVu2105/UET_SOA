from .progress_bar import *


class ConnectionError(RequestException):
    """A Connection error occurred."""


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
early_py_version = sys.version_info[:2] < (2, 7)


class Downloader(object):

    def __init__(self, url):
        self._url = url
        self._filename = None
        self._sess = requests.session()

    @property
    def url(self):
        """abac"""
        return self._url

    @property
    def filename(self):
        if not self._filename:
            self._filename = self._generate_filename()
        return self._filename

    @property
    def unsafe_filename(self):
        if not self._filename:
            self._filename = self._generate_unsafe_filename()
        return self._filename

    def _generate_filename():
        pass

    def _generate_unsafe_filename():
        pass

    def download(self, filepath="", unsafe=False, quiet=False, callback=lambda *x: None):
        savedir = filename = ""
        retVal = {}

        if filepath and os.path.isdir(filepath):
            savedir, filename = filepath, self.filename if not unsafe else self.unsafe_filename

        elif filepath:
            savedir, filename = os.path.split(filepath)

        else:
            filename = self.filename if not unsafe else self.unsafe_filename

        filepath = os.path.join(savedir, filename)

        if filepath and filepath.endswith('.vtt'):
            filepath_vtt2srt = filepath.replace('.vtt', '.srt')
            if os.path.isfile(filepath_vtt2srt):
                retVal = {"status": True, "msg": "already downloaded"}
                sys.stdout.write(fg + '[' + fr + '-' + fg + '] : %s\n' % (retVal['msg']))
                return retVal

        if os.path.isfile(filepath):
            retVal = {"status": True, "msg": "already downloaded"}
            sys.stdout.write(fg + '[' + fr + '-' + fg + '] : %s\n' % (retVal['msg']))
            return retVal

        temp_filepath = filepath + ".part"

        self._active = True
        bytes_to_be_downloaded = 0
        fmode, offset = "wb", 0
        chunksize, bytesdone, t0 = 16384, 0, time.time()
        headers = {'User-Agent': HEADERS.get('User-Agent')}
        if os.path.exists(temp_filepath):
            offset = os.stat(temp_filepath).st_size

        if offset:
            offset_range = 'bytes={}-'.format(offset)
            headers['Range'] = offset_range
            bytesdone = offset
            fmode = "ab"

        status_string = ('  {:,} Bytes [{:.2%}] received. Rate: [{:4.0f} '
                         'KB/s].  ETA: [{:.0f} secs]')

        if early_py_version:
            status_string = ('  {0:} Bytes [{1:.2%}] received. Rate:'
                             ' [{2:4.0f} KB/s].  ETA: [{3:.0f} secs]')

        try:
            try:
                response = self._sess.get(self.url, headers=headers, stream=True, timeout=10)
            except ConnectionError as error:
                retVal = {'status': False, 'msg': 'ConnectionError: %s' % (str(error))}
                sys.stdout.write(fg + '[' + fr + '-' + fg + '] : %s\n' % (retVal['msg']))
                return retVal
            with response:
                if response.ok:
                    bytes_to_be_downloaded = total = int(response.headers.get('Content-Length'))
                    if bytesdone > 0:
                        bytes_to_be_downloaded = bytes_to_be_downloaded + bytesdone
                    total = bytes_to_be_downloaded
                    with open(temp_filepath, fmode) as media_file:
                        is_malformed = False
                        for chunk in response.iter_content(chunksize):
                            if not chunk:
                                break
                            media_file.write(chunk)
                            elapsed = time.time() - t0
                            bytesdone += len(chunk)
                            if elapsed:
                                try:
                                    rate = ((float(bytesdone) - float(offset)) / 1024.0) / elapsed
                                    eta = (total - bytesdone) / (rate * 1024.0)
                                except ZeroDivisionError:
                                    is_malformed = True
                                    try:
                                        os.unlink(temp_filepath)
                                    except Exception:
                                        pass
                                    retVal = {"status": False,
                                              "msg": "ZeroDivisionError : it seems, file has malfunction or is zero byte(s) .."}
                                    sys.stdout.write(fg + '[' + fr + '-' + fg + '] : %s\n' % (retVal['msg']))
                                    break
                            else:
                                rate = 0
                                eta = 0

                            if not is_malformed:
                                progress_stats = (
                                    bytesdone, bytesdone * 1.0 / total, rate, eta)

                                if not quiet:
                                    status = status_string.format(*progress_stats)
                                    sys.stdout.write(
                                        "\r" + status + ' ' * 4 + "\r")
                                    sys.stdout.flush()

                                if callback:
                                    callback(total, *progress_stats)
                if not response.ok:
                    code = response.status_code
                    reason = response.reason
                    retVal = {
                        "status": False, "msg": "Error returned HTTP Code %s: %s" % (code, reason)}
                    sys.stdout.write(fg + '[' + fr + '-' + fg + '] : %s\n' % (retVal['msg']))

        except KeyboardInterrupt as error:
            raise error
        except Exception as error:
            retVal = {"status": False,
                      "msg": "Reason : {}".format(str(error))}
            sys.stdout.write(fg + '[' + fr + '-' + fg + '] : %s\n' % (retVal['msg']))

            return retVal
        if os.path.isfile(temp_filepath):
            total_bytes_done = os.stat(temp_filepath).st_size
            if total_bytes_done == bytes_to_be_downloaded:
                self._active = False
            if total_bytes_done < bytes_to_be_downloaded:
                self._active = True
                self.download(filepath=filepath,
                              unsafe=unsafe,
                              quiet=quiet)

        if not self._active:
            os.rename(temp_filepath, filepath)
            retVal = {"status": True, "msg": "download"}
        sys.stdout.write("\n")
        return retVal
