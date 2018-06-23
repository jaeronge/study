Transaction
=========

Transaction & Auto Commit
Transaction: All or Nothing
ACID: Atomicity,Consistency,Isolation,Durability
Read Lock, Shared Lock(공유 Lock) & Write Lock, Exclusive Lock( 베타적 Lock)
Lock Level: row, page, table, database
Lock에 의해 발생하는 Blocking & Dead Lock
blocking: short transaction, timeout, fast query, appropriate isolation level
Transaction Isolation Level
Low Isolation level
Dirty Read : non commit data read -> roll back
Non-Repeatable Read: data check -> update -> changed data
Phantom Read: data check -> insert -> new phantom data
Level 
Read Uncommitted
Read Committed
Repeatable Read
Serializable Read

