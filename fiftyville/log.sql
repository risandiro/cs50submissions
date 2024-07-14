-- Keep a log of any SQL queries you execute as you solve the mystery.

------------------------------------------------------------------------------------------------------------------------------------

-- SELECT description FROM crime_scene_reports WHERE street = "Humphrey Street" AND day = "28" AND month = "7";

-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted
-- today with three witnesses who were present at the time – each of their interview transcripts
-- mentions the bakery. Littering took place at 16:36. No known witnesses.

------------------------------------------------------------------------------------------------------------------------------------

-- SELECT transcript FROM interviews WHERE transcript LIKE "%bakery%" AND month = "7" AND day = "28";

-- Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have
-- security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.

-- I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived
-- at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

-- As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
-- In the call, I heard the thief say that they're planning to take the earliest flight out of Fiftyville tomorrow.
-- The thief then asked the person on the other end of the phone to purchase the flight ticket.

------------------------------------------------------------------------------------------------------------------------------------

-- SELECT license_plate, minute FROM bakery_security_logs WHERE month = "7" AND day = "28" AND activity = "exit" AND hour = "10" AND minute < 25;

-- +---------------+--------+
-- | license_plate | minute |
-- +---------------+--------+
-- | 5P2BI95       | 16     |
-- | 94KL13X       | 18     |
-- | 6P58WS2       | 18     |
-- | 4328GD8       | 19     |
-- | G412CB7       | 20     |
-- | L93JTIZ       | 21     |
-- | 322W7JE       | 23     |
-- | 0NTHK55       | 23     |
-- +---------------+--------+

------------------------------------------------------------------------------------------------------------------------------------

-- SELECT account_number FROM atm_transactions WHERE atm_location = "Leggett Street" AND month = "7" AND day = "28" AND transaction_type = "withdraw";

-- +----------------+
-- | account_number |
-- +----------------+
-- | 28500762       |
-- | 28296815       |
-- | 76054385       |
-- | 49610011       |
-- | 16153065       |
-- | 25506511       |
-- | 81061156       |
-- | 26013199       |
-- +----------------+

------------------------------------------------------------------------------------------------------------------------------------
