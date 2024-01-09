# BIAC System

## Introduction
This BIAC System is a blockchain-based access control system that utilizes zero-knowledge proof technology. It ensures robust anonymity for account information and mitigates security concerns related to behavior, habits, and record privacy for both objects and subjects.

## Features
- **Blockchain-Based**: Leverages the security and transparency of blockchain technology.
- **Zero-Knowledge Proofs**: Ensures user anonymity and privacy.
- **Modular Design**: Separate modules for resource owners and subjects.

## Installation
To use the BIAC System, you need to first install the prerequisites.

### Prerequisites
- **Circom**: A compiler for zk-SNARK circuits.
- **Snarkjs**: A tool for generating and verifying zk-SNARK proofs.
- **Geth**: An Ethereum client for running a full Ethereum node.

Install these tools by following the instructions on their respective websites.

## Usage
The BIAC System is structured into different folders, each designated for specific roles.

### Directory Structure
- `circuit/`: Contains all zk-SNARK circuits.
- `owner/`: For the resource owner's operations.
- `subject/`: For the subject's operations.

### Usage Steps
1. **Deploy Clients**: Deploy clients for different roles to different devices.
2. **Configure Network Settings**: Set up IP addresses for SSH and the server.
3. **Initialization and Registration**: Start the blockchain environment and register the subject with the resource owner using `owner/access_control_list.py`.
4. **Resource Owner Operations**: Execute `owner/owner_operation.py` for managing the server.
5. **Subject Operations**: Generate and submit a `zkp_token` using `subject/subject_operation.py`.
6. **Resource Access Request**: Subjects access the resource owner's server with the necessary information including ID and random value.
7. **IoT Device Access**: Subjects can access IoT devices if their request is accepted.
8. **Access Logging**: Resource owners can maintain an access log  in the contract for security and monitoring.

## Contribution
Contributions to the BIAC System are welcome. Please follow the standard fork, branch, and pull request workflow.

## Support
For support or additional information, please feel free to email the author: wu.yuxiao.ws9@is.naist.jp.
