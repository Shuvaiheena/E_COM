create table customer_details(
  id BIGSERIAL PRIMARY KEY,
  Name VARCHAR(30),
  email VARCHAR(50),
  mobile BIGINT,
  address TEXT,
  code VARCHAR(20),
  gender VARCHAR(20),
  date_created TIMESTAMP,
  customer_age BIGINT,
  active_state INTEGER DEFAULT 0
);
--post
{
  "Name" : "heena",
"Email" : "heena@gmail.com",
"Mobile" : 9567177821,
"Address" : "pulamenthole, Malappuram",
"Gender" : "Female",
"Date" : "2023-07-11",
"Age" : 26
}
--put
{
"Id" : 3,
"Name" : "heena",
"Email" : "heena@gmail.com",
"Mobile" : 9567177821,
"Address" : "pulamenthole, Malappuram",
"Gender" : "Female",
"Date" : "2023-07-11",
"Age" : 26
}
--patch
{
"Id" : 3
}

create table product_details(
  prod_id BIGSERIAL PRIMARY KEY,
  prod_name VARCHAR(30),
  prod_code VARCHAR(20),
  prod_date TIMESTAMP,
  prod_age BIGINT,
  prod_active INTEGER DEFAULT 0
);

{
"Name" : "Key",
"Code" : "KEY01",
"Date" : "2023-02-15",
"Customer_mobile" : 9567177820
}
{
"Name" : "Key",
"Code" : "KEY02",
"Date" : "2023-07-16",
"Customer_mobile" : 9567177820
}
PARAMS = {'Customer_mobile':9995259369}
data = requests.get(url = url,params = PARAMS)
alter table product_details add column customer_id BIGINT REFERENCES customer_details(id);

insert into product_details (prod_name,prod_code,prod_date,prod_age,prod_active) values ('Hat','HAT01','2023-01-20',5,1);