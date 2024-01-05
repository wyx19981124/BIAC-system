pragma circom 2.0.0;

include "./keccak.circom";

// for a input & output of 32 bytes:
component main = Keccak(8*8, 32*8);