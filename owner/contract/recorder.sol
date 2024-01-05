// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract recorder {
    struct record{
        string subject_id;
        string object_id;
        string access_type;
        uint256 time;
    }


    record[] public record_array;

    function submit_record(string memory subject_id, string memory object_id, string memory access_type, uint256 time) public{
        record_array.push(record(subject_id,object_id,access_type,time));
    }

    function get_record() public view returns (record[] memory){
        return record_array;
    }
}
