from typing import NamedTuple
from randoutils import format_binary

LVL_CMD_LOAD_RAW_DATA_AND_JUMP = "LOAD_RAW_DATA_AND_JUMP"
LVL_CMD_LOAD_RAW_DATA_AND_JUMP_PLUS_CALL = "LOAD_RAW_DATA_AND_JUMP_PLUS_CALL"
LVL_CMD_END_LEVEL_DATA = "END_LEVEL_DATA"
LVL_CMD_DELAY_FRAMES = "DELAY_FRAMES"
LVL_CMD_DELAY_FRAMES_2 = "DELAY_FRAMES_2"
LVL_CMD_JUMP_TO_ADDRESS = "JUMP_TO_ADDRESS"
LVL_CMD_PUSH = "PUSH"
LVL_CMD_POP = "POP"
LVL_CMD_PUSH_SCRIPT_0X = "PUSH_SCRIPT_0X"
LVL_CMD_CONDITIONAL_POP = "CONDITIONAL_POP"
LVL_CMD_CONDITIONAL_JUMP = "CONDITIONAL_JUMP"
LVL_CMD_CONDITIONAL_PUSH = "CONDITIONAL_PUSH"
LVL_CMD_CONDITIONAL_SKIP = "CONDITIONAL_SKIP"
LVL_CMD_SKIP_NEXT = "SKIP_NEXT"
LVL_CMD_NOP = "NOP"
LVL_CMD_SET_ACCU_FROM_ASM = "SET_ACCU_FROM_ASM"
LVL_CMD_SET_ACCU_FROM_ROUTINE = "SET_ACCU_FROM_ROUTINE"
LVL_CMD_SET_ACCU = "SET_ACCU"
LVL_CMD_PUSH_POOL = "PUSH_POOL"
LVL_CMD_POP_POOL = "POP_POOL"
LVL_CMD_ROM_TO_RAM = "ROM_TO_RAM"
LVL_CMD_ROM_TO_SEGMENT = "ROM_TO_SEGMENT"
LVL_CMD_MIO0_DECOMPRESS = "MIO0_DECOMPRESS"
LVL_CMD_CREATE_DEMO = "CREATE_DEMO"
LVL_CMD_MIO0_DECOMPRESS_TEXTURES = "MIO0_DECOMPRESS_TEXTURES"
LVL_CMD_START_LOAD_SEQ = "START_LOAD_SEQ"
LVL_CMD_LEVEL_AND_MEMORY_CLEANUP = "LEVEL_AND_MEMORY_CLEANUP"
LVL_CMD_END_LOAD_SEQ = "END_LOAD_SEQ"
LVL_CMD_ALLOCATE_LEVEL_DATA_FROM_POOL = "ALLOCATE_LEVEL_DATA_FROM_POOL"
LVL_CMD_START_AREA = "START_AREA"
LVL_CMD_END_AREA = "END_AREA"
LVL_CMD_LOAD_POLY_WITHOUT_GEO = "LOAD_POLY_WITHOUT_GEO"
LVL_CMD_LOAD_POLY_WITH_GEO = "LOAD_POLY_WITH_GEO"
LVL_CMD_PLACE_OBJECT = "PLACE_OBJECT"
LVL_CMD_LOAD_MARIO = "LOAD_MARIO"
LVL_CMD_CONNECT_WARPS = "CONNECT_WARPS"
LVL_CMD_CONNECT_PAINTING = "CONNECT_PAINTING"
LVL_CMD_CONNECT_INSTANT_WARP = "CONNECT_INSTANT_WARP"
LVL_CMD_LOAD_COLLISION = "LOAD_COLLISION"
LVL_CMD_SETUP_RENDER_ROOM = "SETUP_RENDER_ROOM"
LVL_CMD_SHOW_DIALOG = "SHOW_DIALOG"
LVL_CMD_SET_DEFAULT_TERRAIN = "SET_DEFAULT_TERRAIN"
LVL_CMD_FADE_COLOR = "FADE_COLOR"
LVL_CMD_SET_MUSIC = "SET_MUSIC"
LVL_CMD_SET_MUSIC_SPECIAL = "SET_MUSIC_SPECIAL"
LVL_CMD_PLACE_MACRO_OBJECTS = "PLACE_MACRO_OBJECTS"
LVL_CMD_PLACE_JET_STREAM = "PLACE_JET_STREAM"


""" Names for all LEVEL segment functions in SM64 """
LVL_CMD_IDS = {
  0x00: LVL_CMD_LOAD_RAW_DATA_AND_JUMP,
  0x01: LVL_CMD_LOAD_RAW_DATA_AND_JUMP_PLUS_CALL,
  0x02: LVL_CMD_END_LEVEL_DATA,
  0x03: LVL_CMD_DELAY_FRAMES,
  0x04: LVL_CMD_DELAY_FRAMES_2,
  0x05: LVL_CMD_JUMP_TO_ADDRESS,
  0x06: LVL_CMD_PUSH,
  0x07: LVL_CMD_POP,
  0x0A: LVL_CMD_PUSH_SCRIPT_0X,
  0x0B: LVL_CMD_CONDITIONAL_POP,
  0x0C: LVL_CMD_CONDITIONAL_JUMP,
  0x0D: LVL_CMD_CONDITIONAL_PUSH,
  0x0E: LVL_CMD_CONDITIONAL_SKIP,
  0x0F: LVL_CMD_SKIP_NEXT,
  0x10: LVL_CMD_NOP,
  0x11: LVL_CMD_SET_ACCU_FROM_ASM,
  0x12: LVL_CMD_SET_ACCU_FROM_ROUTINE,
  0x13: LVL_CMD_SET_ACCU,
  0x14: LVL_CMD_PUSH_POOL,
  0x15: LVL_CMD_POP_POOL,
  0x16: LVL_CMD_ROM_TO_RAM,
  0x17: LVL_CMD_ROM_TO_SEGMENT,
  0x18: LVL_CMD_MIO0_DECOMPRESS,
  0x19: LVL_CMD_CREATE_DEMO,
  0x1A: LVL_CMD_MIO0_DECOMPRESS_TEXTURES,
  0x1B: LVL_CMD_START_LOAD_SEQ,
  0x1C: LVL_CMD_LEVEL_AND_MEMORY_CLEANUP,
  0x1D: LVL_CMD_END_LOAD_SEQ,
  0x1E: LVL_CMD_ALLOCATE_LEVEL_DATA_FROM_POOL,
  0x1F: LVL_CMD_START_AREA,
  0x20: LVL_CMD_END_AREA,
  0x21: LVL_CMD_LOAD_POLY_WITHOUT_GEO,
  0x22: LVL_CMD_LOAD_POLY_WITH_GEO,
  0x24: LVL_CMD_PLACE_OBJECT,
  0x25: LVL_CMD_LOAD_MARIO,
  0x26: LVL_CMD_CONNECT_WARPS,
  0x27: LVL_CMD_CONNECT_PAINTING,
  0x28: LVL_CMD_CONNECT_INSTANT_WARP,
  0x2E: LVL_CMD_LOAD_COLLISION,
  0x2F: LVL_CMD_SETUP_RENDER_ROOM,
  0x30: LVL_CMD_SHOW_DIALOG,
  0x31: LVL_CMD_SET_DEFAULT_TERRAIN,
  0x33: LVL_CMD_FADE_COLOR,
  0x36: LVL_CMD_SET_MUSIC,
  0x37: LVL_CMD_SET_MUSIC_SPECIAL,
  0x39: LVL_CMD_PLACE_MACRO_OBJECTS,
  0x3B: LVL_CMD_PLACE_JET_STREAM,
}

class Level(NamedTuple):
  address_start: int # start of level command area on ROM
  address_end: int # end of level command area on ROM
  level_id: int # not course-id
  name: str # human readable name
  level_area: int = 0 # area this levels painting is in

  @property
  def address(self):
    return (self.address_start, self.address_end)

class LevelCommand(NamedTuple):
  identifier: int # int identifying the command
  name: str = None # name for command
  length: int = 0
  data: bytes = None # command specific data bytes
  position: int = None # memory position
  highlight: bool = False

  @staticmethod
  def from_id(cmd_id, *args, **kwargs):
    if cmd_id in LVL_CMD_IDS:
      return LevelCommand(cmd_id, LVL_CMD_IDS[cmd_id], *args, **kwargs)
    else:
      return LevelCommand(cmd_id)

  def __str__(self):
    prefix = "[ UNKNOWN POSITION ]"
    if self.position is not None:
      prefix = f"[{hex(self.position-2)} / {self.position}]"
    
    ident = self.name or f'UNKNOWN ({hex(self.identifier)})'
    length = f'({self.length + 2})'

    data = "NO DATA"
    highlight = "****" if self.highlight else ""

    if self.data is not None:
      data = format_binary( bytes([self.identifier, self.length + 2]) + self.data )
    output = " ".join([highlight, prefix, ident, length, data])
    return output