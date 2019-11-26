# findme // Writeup

## Problem

*Find me! Challenge created by Security Risk Advisors for RITSEC CTF*

## Solution

Open the dumped network traffic with Wireshark for example. Don't look at the base64 encoded image or you will get rick-rolled.

If you decode the client packet you will get a youtube video and it's useless.

`aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQo=`

But if you decode the server client you will get a gzip compressed data file.

`H4sIAFSZx10AA+3OMQuCQBiH8Zv9FPcFgrvUcw2kIWgydzG1EkQPvZui757S0lSTRPD8lmd43+F/6cqrWJmaGRMt1Ums3vtitkKHsdGJDqNtKJSeGwup1h628JMrRymFP/ve+Q9/X+5/Kjvkp316t1Vpp0KNReuKuq17V9x21jb9IwjSPDtuKukGWXXD1AS/XgwAAAAAAAAAAAAAAAAAWDwB38XEewAoAAA=`

![first](./images/first.png)

So uncompress it, `mv new_file new_file.gz ; gunzip -d new_file.gz`. After that you will get a tar archived file.

Extract it : `tar -xvf new_file`, you will get `flag` file, so , `cat flag`.
