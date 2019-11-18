# Long Gone // Writeup

## Problem

*That data? No it's long gone. It's basically history*

*http://us-central-1.ritsec.club/l/chromebin*

Authors: Degenerat3, knif3

## Solution

After downloading the file, if you check it properties, you will see it's a `tar` file.

Let's extract it : `tar -xvf chromebin`

Now go to `Chrome/User Data/Default`, you will see `History`. It's a sqlite3 file.

Open it : `sqlite3 History`, we need to see tables : `.tables`

The `keyword_search_terms` looks like interesting then do : `select * from keyword_search_terms ;`

Keywords aren't interesting except a link. Just open it.

`curl us-central-1.ritsec.club/l/relaxfizzblur`

**FLAG**: `RITSEC{SP00KY_BR0WS3R_H1ST0RY}`
