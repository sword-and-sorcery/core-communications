
#pragma once


#include <functional>
#include "messages/board_status.pb.h"

struct Address {};

void subscribe(Address&, std::function<void (sword_and_sorcery::BoardStatus&)> callback);
