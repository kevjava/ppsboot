

from dataclasses import dataclass, field
from enum import Enum
from typing_extensions import Self
from ppsboot.utils.solution import Solution


class PacketType(Enum):
    OPERATOR0 = 0
    OPERATOR1 = 1
    OPERATOR2 = 2
    OPERATOR3 = 3
    LITERAL = 4
    OPERATOR5 = 5
    OPERATOR6 = 6
    OPERATOR7 = 7


class LengthType(Enum):
    BITS = 0
    PACKETS = 1


@dataclass
class Packet():
    bin_data: str = field(repr=False)
    pkt_version: int
    pkt_type: PacketType
    subpackets: list[Self] = field(default_factory=list)
    value: int = 0

    def __init__(self, bin_data: str):
        self.bin_data = bin_data

    def sum_versions(self):
        return self.pkt_version + sum([p.sum_versions() for p in self.subpackets])


class PacketParser():
    @staticmethod
    def _parse_literal_value(bin_data: str) -> int:
        print("Parsing literal")
        value, done = 0, False
        while not done:
            done = bin_data[0] == '0'
            value = (value << 4) | int(bin_data[1:5], 2)
            bin_data = bin_data[5:]
        return value

    @staticmethod
    def _parse_bits(bin_data: str) -> list[Packet]:
        print("Parsing", len(bin_data), "bits", bin_data)
        return [PacketParser.parse(bin_data)]

    @staticmethod
    def _parse_packets(num_packets: int, bin_data: str) -> list[Packet]:
        print("Parsing packets")
        packets = []
        for _ in range(num_packets):
            pkt = PacketParser._parse_next(bin_data)
            packets.append(pkt)
            bin_data = bin_data[len(pkt.bin_data):]
        return packets

    @staticmethod
    def _parse_operator(bin_data: str) -> list[Packet]:
        print("Parsing operator: ", bin_data)
        length_type = LengthType(int(bin_data[0], 2))
        match length_type:
            case LengthType.BITS:
                num_bits = int(bin_data[1:16], 2)
                return PacketParser._parse_bits(bin_data[16:16+num_bits])
            case LengthType.PACKETS:
                num_packets = int(bin_data[1:12], 2)
                return PacketParser._parse_packets(num_packets, bin_data[12:])

    @staticmethod
    def _parse_next(bin_data: str) -> Packet:
        print("Parsing next", bin_data)
        p = Packet(bin_data)
        p.pkt_version = int(bin_data[0:3], 2)
        p.pkt_type = PacketType(int(bin_data[3:6], 2))
        match p.pkt_type:
            case PacketType.LITERAL:
                p.value = PacketParser._parse_literal_value(p.bin_data[6:])
                p.subpackets = []
            case _:
                p.subpackets = PacketParser._parse_operator(bin_data[6:])
        return p

    @staticmethod
    def parse(hex_data: str) -> Packet:
        nibbles = [bin(int(x, 16))[2:].zfill(4) for x in hex_data]
        bin_data = ''.join(nibbles)  # TODO: combine the last line and this one.
        return PacketParser._parse_next(bin_data)


class Day16(Solution):

    def __init__(self):
        super().__init__(16, 'ppsboot/days/d16/input_test.txt')

    def load_input(self, filename: str) -> list[str]:
        with open(filename) as f:
            return [list(line.strip()) for line in f.readlines()]

    def part1(self, input: list[str]) -> int:
        """ Returns the solution to part 1. """
        print(input)
        for line in input:
            packet = PacketParser.parse(line)
            print(packet)
        return packet.sum_versions()
