// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract publish {
    struct zkp_token{
        string ID;
        string AR;
        uint256 et;
        uint256[2] _pA;
        uint256[2][2] _pB;
        uint256[2] _pC;
        uint256[256] _pubSignals;
        string r;
    }


    zkp_token[] public zkp_token_array;

    function submit_proof(string memory ID, string memory AR, uint256 et, uint256[2] memory _pA, uint256[2][2] memory _pB, uint256[2] memory _pC, uint256[256] memory _pubSignals, string memory r) public{
        zkp_token_array.push(zkp_token(ID,AR,et,_pA,_pB,_pC,_pubSignals,r));
    }

    function get_proof() public view returns (zkp_token[] memory){
        return zkp_token_array;
    }
}