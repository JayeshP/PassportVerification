# PassportVerification
Small app to simulation passport doc verification process.

You can play around with adding number of worker for doc verification, police verification and biometric information.

How to run ?
python main.py <no of doc verification worker> <no. of police verification workers> <no. of biometric worker>

What do we achieve ?
Play around with number of worker, average time to do verication and you can get nice metrics for average waiting time required for a person. Also you can get free time for a worker too.

person enters -> doc verification -> police verification -> biometric info -> exit
