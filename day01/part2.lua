local nums_map = {
	one = 1,
	two = 2,
	three = 3,
	four = 4,
	five = 5,
	six = 6,
	seven = 7,
	eight = 8,
	nine = 9,
}

local function get_first_digit(str)
	for i = 1, #str do
		local digit = tonumber(str:sub(i, i))
		if digit ~= nil then
			return digit
		end

		for key, value in pairs(nums_map) do
			if str:sub(i, i + #key - 1) == key then
				return value
			end
		end
	end
end

local function get_last_digit(str)
	for i = #str, 1, -1 do
		local digit = tonumber(str:sub(i, i))
		if digit ~= nil then
			return digit
		end

		for key, value in pairs(nums_map) do
			if str:sub(i, i + #key - 1) == key then
				return value
			end
		end
	end
end

local sum = 0

for line in io.lines("input.txt") do
	sum = sum + 10 * get_first_digit(line) + get_last_digit(line)
end

print(sum)
