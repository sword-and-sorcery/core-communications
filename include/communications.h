
#pragma once

#include <functional>
#include "messages/board_status.h"

struct Address {};

void subscribe(Address, std::function<void (BoardStatus&)> callback);
