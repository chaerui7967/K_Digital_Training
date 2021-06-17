# insert, delete

use tip;

select * from tips where tips.day = '';

select * from tips;

# insert

insert into tips (total_bill, tip, sex, smoker, day, time, size)
values ('16.99', '1.01', 'Female', 'No', 'Sun', 'Dinner', '2');

insert into tips (total_bill, tip, sex, smoker, day, time, size)
values ('10.34', '1.66', 'Male', 'null', 'Sun', 'Dinner', '3');

select * from tips where tips.smoker = 'null';

insert into tips (total_bill, tip, sex, smoker, day, time, size)
value ('20.65', '3.35', 'Male', 'No', '', 'Dinner', '4'),
('20.65', '3.35', 'Male', 'No', '', 'Dinner', '5');

insert into tips (total_bill, tip, sex, smoker, day, time, size)
values ('10.34', '1.66', Null, 'No', 'Sun', 'Dinner', '3'),
('10.34', '1.66', Null, 'No', 'Sun', 'Dinner', '3'),
('10.34', '1.66', 'Male', 'No', 'Sun', Null, '3'),
('10.34', '1.66', 'Male', 'No', 'Sun', 'Dinner', Null);


select * from tips where tips.day = '';


# delete

delete from tips where tips.smoker = 'null';
delete from tips where tips.day = '';