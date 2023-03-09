'''10.B.3: ASSIGNMENT
PROBLEM STATEMENT
Scikitlearn
READ ME
=======
Problem Statement: Intrusion Detection Systems (IDSs) and Intrusion Prevention Systems (IPSs) are the most important defense tools against the sophisticated and ever-growing network attacks. Given network flow data, can we detect different network attacks? (Download the attached file & unzip to fetch the data)

Network attacks : There are different types of network attacks such as DoS Hulk, DoS GoldenEye, DoS slowloris, DoS Slowhttptest.

Features : Total 80 features are taken from network flow data, including Label.

ID : record id

Label : BENIGN(Normal), DoS(Attack)

Packet info : 'Total Fwd Packets','Total Backward Packets', 'Total Length of Fwd Packets',

	          'Total Length of Bwd Packets', 'Fwd Packet Length Max',

	          'Fwd Packet Length Min', 'Fwd Packet Length Mean',

	          'Fwd Packet Length Std', 'Bwd Packet Length Max',

	          'Bwd Packet Length Min', 'Bwd Packet Length Mean',

	          'Bwd Packet Length Std'

Payload info : 'Flow Bytes/s', 'Flow Packets/s',

              'Flow IAT Mean', 'Flow IAT Std', 'Flow IAT Max', 'Flow IAT Min',

              'Fwd IAT Total', 'Fwd IAT Mean', 'Fwd IAT Std', 'Fwd IAT Max',

              'Fwd IAT Min', 'Bwd IAT Total', 'Bwd IAT Mean', 'Bwd IAT Std',

              'Bwd IAT Max', 'Bwd IAT Min', 'Fwd PSH Flags', 'Bwd PSH Flags',

              'Fwd URG Flags', 'Bwd URG Flags', 'Fwd Header Length',

              'Bwd Header Length', 'Fwd Packets/s', 'Bwd Packets/s',

              'Min Packet Length', 'Max Packet Length', 'Packet Length Mean',

              'Packet Length Std', 'Packet Length Variance', 'FIN Flag Count',

              'SYN Flag Count', 'RST Flag Count', 'PSH Flag Count', 'ACK Flag Count',

              'URG Flag Count', 'CWE Flag Count', 'ECE Flag Count', 'Down/Up Ratio',

              'Average Packet Size', 'Avg Fwd Segment Size', 'Avg Bwd Segment Size',

              'Fwd Header Length.1', 'Fwd Avg Bytes/Bulk', 'Fwd Avg Packets/Bulk',

              'Fwd Avg Bulk Rate', 'Bwd Avg Bytes/Bulk', 'Bwd Avg Packets/Bulk',

              'Bwd Avg Bulk Rate', 'Subflow Fwd Packets', 'Subflow Fwd Bytes',

              'Subflow Bwd Packets', 'Subflow Bwd Bytes', 'Init_Win_bytes_forward',

              'Init_Win_bytes_backward', 'act_data_pkt_fwd', 'min_seg_size_forward'

Session info : 'Active Mean', 'Active Std', 'Active Max', 'Active Min', 'Idle Mean',

              'Idle Std', 'Idle Max', 'Idle Min'



What to Do?

===========
Build a Machine Learning model which can detect the network attacks.
Submission Details

==================

- A zip file containing your code (.ipynb file or .py file or r notebook), with final model and prediction results in .csv format.

END OF ASSESSMENT

sklearn test.zip sklearn test.zip6 November 2020, 3:58 PM
Submission status
'''