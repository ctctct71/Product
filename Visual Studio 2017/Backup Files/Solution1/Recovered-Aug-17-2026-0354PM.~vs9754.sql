select * from inKala

where KalaPK in('6e6de43b-08d0-49a6-8d15-ac5100f65ac8',
'a53ceb7c-a41e-49be-abb0-ac5100f7331a',
'0593ab96-ad08-4f77-91f7-ad3a010808a8',
'9c37d6b6-43f2-405e-9de5-a9be01045c17',
'74acc5d3-5ee5-4888-93eb-abf300af7dc2',
'7cd77079-6b2d-40fd-b4bc-a86a00dc07d9',
'c2b6ff8d-d455-471b-b871-a3c10124961e',
'36921211-debd-4865-9fc2-a8c000a37f2a')



select* from inAnbar
where AnbarPK = '20bd30b1-e87a-4786-88ec-ac8d00cde01f'

select SodoorDate from inSanadAnbar
inner join saFactor on inSanadAnbar.SanadAnbarPK = saFactor.HavalePK
where HesabdariSal = 1404 and FactorNo like '68%'


select KalaName from saFactor
join inSanadAnbar on inSanadAnbar.SanadAnbarPK = saFactor.HavalePK
join inSanadAnbarItem on inSanadAnbarItem.SanadAnbarPK = inSanadAnbar.SanadAnbarPK	
join inKala on inkala.KalaPK = inSanadAnbarItem.KalaPK 
where saFactor.FactorNo =732988 and inkala.KalaCode = 30620001


select MoshtariNo from saMoshtari
join saFactor on saMoshtari.MoshtariPK = safactor.MoshtariPK
join inSanadAnbar on inSanadAnbar.SanadAnbarPK = saFactor.HavalePK
where inSanadAnbar.HesabdariSal = 1404
and samoshtari.MoshtariNo not in ( select MoshtariNo from saMoshtari where HesabdariSal = 1403 )


select * from saFactor
where FactorNo in (select FactorNo from saFactor join saFactorItems on saFactorItems.FactorPK =saFactor.FactorPK 
group by FactorNo having COUNT(saFactorItems.KalaPK)> 80 )


select FactorNo from saFactor
where FactorDate > '1405/01/01'
select * from inSanadAnbar
where HesabdariSal =1405

select * from inKala
where kalacode like '2000%'

select MoshtariPK ,count(*)as abc from saFactor
group by MoshtariPK
order by abc desc

select inkala.KalaName , safactoritems.Tedad , saMoshtari.MoshtariNo from saFactor
join samoshtari on saFactor.moshtaripk = samoshtari.MoshtariPK
join saFactorItems on safactor.FactorPK = saFactorItems.FactorPK
join inKala on inKala.KalaPK = saFactorItems.KalaPK
where inkala.KalaName like '%?%'

select factorno from saFactor
join saFactorItems on saFactor.FactorPK = saFactorItems.FactorPK
join inkala on inkala.KalaPK = saFactorItems.KalaPK
where kalacode between 10400000 and 10400005

select (Tedad * ArzehKolItem) as mablagh, FactorNo from saFactorItems
join saFactor on safactor.FactorPK = saFactorItems.FactorPK

select MoshtariPK , count(*)as tedadfac from saFactor
group by MoshtariPK
having COUNT(*) > 5
order by tedadfac

select * from inKala
where Vazn = (select MAX(vazn) from inKala)

select * from inKala
where Vazn > (select AVG(Vazn) from inKala)


select MoshtariNo from saMoshtari
join saFactor on saMoshtari.MoshtariPK = saFactor.MoshtariPK
join saFactorItems on saFactorItems.FactorPK = saFactor.FactorPK
where Tedad > (select AVG(tedad) from saFactorItems)


select KalaName,AnbarName,
case  
	when hesabdarisal = 1405 then '05'
	when hesabdarisal = 1404 then '04'
	when hesabdarisal = 1403 then '03'
	else 'nemidonam'
end as 'nm' ,
case
 when FactorStatus = 'true'then 'Y'
 else '----'
end
from safactor
join inSanadAnbar on saFactor.HavalePK = inSanadAnbar.SanadAnbarPK
join inSanadAnbarItem on inSanadAnbar.SanadAnbarPK = inSanadAnbarItem.SanadAnbarPK	
join saFactorItems on saFactorItems.KalaPK = inSanadAnbarItem.KalaPK
join inKala on inKala.KalaPK = inSanadAnbarItem.KalaPK
join inAnbar on inAnbar.AnbarPK = inSanadAnbar.AnbarPK

select KalaName , 
case 
	when  ArzehKolItem > 5000000 then 'geroon'
	when  ArzehKolItem < 5000000 then 'arzoon'
	else '----'
end as'gheymat'
from saFactor	
join saFactorItems on saFactorItems.FactorPK = saFactor.FactorPK
join inKala on inKala.KalaPK = saFactorItems.KalaPK	


select factorno , MoshtariNo  ,
case 
	when noefactor = 1 then 'forosh' 
	when noefactor = -1then ' marjooyi'
end as 'chiye'
from saFactor
join saMoshtari on saMoshtari.MoshtariPK = saFactor.MoshtariPK	

select anbarname , count(factorpk)as 'tedad factor' ,
case 
	when count(factorpk) > 10 then 'faal'
	when count(factorpk) < 10 then 'gheyre faal'
	
end as 'tedad'
from safactor
join inAnbar on inAnbar.AnbarPK = saFactor.AnbarPK
group by AnbarName

select Anbarname from inAnbar

select IsPish from saFactor
where Ispish = 1

select IsFormal from saFactor
where IsFormal = 1

select KalaCode from inKala
where KalaCode like '10%'

select SodoorDate from saFactor
order by SodoorDate desc

select KalaName from inKala
order by KalaName 

select  top 10 FactorPK , SodoorDate
from saFactor
order by SodoorDate desc

select top 5 KalaName from inKala
join saFactorItems on saFactorItems.KalaPK = inKala.KalaPK
join saFactor on saFactor.FactorPK = saFactorItems.FactorPK
order by SodoorDate

select distinct AnbarName
from inAnbar
join saFactor on saFactor.AnbarPK = inAnbar.AnbarPK
where  NoeFactor = 1 and FactorStatus = 3

select distinct MoshtariNo 
from saMoshtari
join saFactor on saFactor.MoshtariPK = saMoshtari.MoshtariPK
where NoeFactor = 1 and FactorStatus = 3

select FactorNo 
from saFactor
order by FactorNo desc 

select AVG(tedad)
from saFactorItems

select count(FactorPK) as nu, MoshtariNo
from saMoshtari
join saFactor on saFactor.MoshtariPK = saMoshtari.MoshtariPK
group by MoshtariNo
order by nu desc

select count (KalaPK) as tedad ,
case 
	when NoeFactor = 1 then 'forosh'
	when NoeFactor = -1 then ' marjoo'
	else 'chi'
end as 'number factor'
from saFactor
join saFactorItems on saFactorItems.FactorPK = saFactor.FactorPK
group by NoeFactor
 
 select count(KalaName)as 'tedad kala' , factorno ,KalaName
 from inKala
 join saFactorItems on saFactorItems.KalaPK = inKala.KalaPK
 join saFactor on saFactor.FactorPK = saFactorItems.FactorPK
 group by FactorNo,KalaName

select FactorPK ,AnbarName
from saFactor
join inAnbar on inAnbar.AnbarPK = saFactor.AnbarPK	

select inSanadAnbar.SanadAnbarPK , KalaName
from inSanadAnbar
join inSanadAnbarItem on inSanadAnbarItem.SanadAnbarPK = inSanadAnbar.SanadAnbarPK
join inKala on inKala.KalaPK =inSanadAnbarItem.KalaPK


select FactorNo , AnbarName ,count(FactorItemsPK) as tedad
from saFactor
join inAnbar on inAnbar. AnbarPK = saFactor.AnbarPK
join saFactorItems on saFactorItems.FactorPK = saFactor.FactorPK
group by FactorNo , AnbarName , FactorItemsPK
order by tedad desc

select saFactorItems.KalaPK , sum(tedad)as tedad , kalaname
from saFactorItems
join inKala on inKala.KalaPK = saFactorItems.KalaPK
group by safactoritems.KalaPK , KalaName
order by tedad desc

select count(FactorItemsPK)as hp ,FactorNo
from saFactorItems
join saFactor on saFactor.FactorPK = saFactorItems.FactorPK
group by FactorNo
order by hp desc

select MoshtariNo ,  count (factorno) as td
from saMoshtari
join saFactor on saFactor.MoshtariPK = saMoshtari.MoshtariPK
group by MoshtariNo
order by td desc

select FactorNo , SodoorDate , safactor.AnbarPK, Tedad, sum(tedad) as td	
from saFactor
join saFactorItems on saFactor.FactorPK = saFactorItems.FactorPK
group by FactorNo , SodoorDate ,saFactor.AnbarPK, Tedad

select KalaName , sum(tedad)as td , tedad
from inKala
join saFactorItems on saFactorItems.KalaPK = inkala.KalaPK
join saFactor on saFactor.FactorPK = saFactorItems.FactorPK
group by KalaName ,Tedad
order by td desc

select AnbarName ,count( kalaname) as td
from inAnbar
join inSanadAnbar on inAnbar.AnbarPK = inSanadAnbar.AnbarPK
join inSanadAnbarItem on inSanadAnbarItem.SanadAnbarPK =inSanadAnbar.SanadAnbarPK
join inKala on inKala.KalaPK = inSanadAnbarItem.KalaPK
group by AnbarName
order by td desc

select top 10 sum(tedad) as td, KalaName
from saFactorItems
join inKala on inkala.KalaPK = saFactorItems.KalaPK
group by KalaName
order by td desc

select MoshtariNo , count (FactorItemsPK) as tdad
from saMoshtari
join saFactor on saFactor.MoshtariPK = saMoshtari.MoshtariPK
join saFactorItems on saFactorItems.FactorPK = saFactor.FactorPK
group by MoshtariNo
order by tdad desc

select SodoorDate ,count (FactorNo) as td
from saFactor
group by SodoorDate
order by SodoorDate desc


select COUNT (distinct saFactorItems.KalaPK) as td , KalaName
from saFactorItems
join inKala on inKala.KalaPK = saFactorItems.KalaPK
group by KalaName , inKala.KalaPK
having COUNT (saFactorItems.KalaPK) > 100
order by td desc

select count(distinct saFactorItems.FactorItemsPK) as tedad,saFactor.FactorPK , factorno
from saFactorItems
join saFactor on saFactor.FactorPK = saFactorItems.FactorPK
group by safactor.FactorNo , saFactor.FactorPK
having count(safactoritems.factoritemspk) > 5
order by tedad desc


select saFactorItems.KalaPK , inKala.KalaName
from saFactorItems
join saFactor on saFactorItems.FactorPK = saFactor.FactorPK
join inKala on inkala.KalaPK = saFactorItems.KalaPK
group by saFactorItems.KalaPK , inKala.KalaName
having COUNT(distinct saFactor.AnbarPK) = (select COUNT (distinct AnbarPK) from inAnbar) 

select FactorNo , SodoorDate , anbarname , count(factoritemspk) as td , KalaName , count(saFactorItems.KalaPK) as ts 
from saFactor
join saFactorItems on saFactor.FactorPK = saFactorItems.FactorPK
join inAnbar on saFactor.AnbarPK = inAnbar.AnbarPK
join inKala on inKala. KalaPK = saFactorItems.KalaPK
group by FactorItemsPK , saFactorItems.KalaPK , FactorNo , AnbarName , SodoorDate , KalaName
order by ts desc , td desc

SELECT
    inKala.KalaPK,
    inKala.KalaName,
    SUM(saFactorItems.Tedad) AS TotalSale
FROM saFactorItems 
JOIN inKala 
    ON inKala.KalaPK = saFactorItems.KalaPK
GROUP BY
    inKala.KalaPK,
    inKala.KalaName
HAVING  SUM(saFactorItems.Tedad) >( SELECT AVG(TotalSale) FROM ( SELECT  SUM(Tedad) AS TotalSale FROM saFactorItems  GROUP BY KalaPK) AS T )
ORDER BY TotalSale DESC;

SELECT
    inKala.KalaPK , inKala.KalaName,
    COUNT(saFactorItems.FactorItemsPK) AS SaleCount,
    SUM(saFactorItems.Tedad) AS TotalSale
FROM saFactorItems 
JOIN inKala ON inKala.KalaPK = saFactorItems.KalaPK
GROUP BY
    inKala.KalaPK,
    inKala.KalaName
ORDER BY
    TotalSale DESC;

SELECT
    MoshtariPK,
    MIN(FactorDate) AS FirstPurchase , 
	FactorNo
FROM saFactor
GROUP BY MoshtariPK , FactorNo

select FactorNo , SodoorDate , Anbarname
from saFactor
join inAnbar on saFactor.AnbarPK = inAnbar.AnbarPK
where SodoorDate ='1405/02/07'

select  top 10 factordate, FactorNo , anbarname 
from saFactor
join inAnbar on inAnbar.AnbarPK = saFactor.AnbarPK
order by FactorDate desc


select FactorNo , Anbarname , 
ROW_NUMBER() over(partition by anbarname order by factordate desc) as rn
from saFactor 
join inAnbar on inAnbar.AnbarPK = saFactor.AnbarPK 

select FactorNo , MoshtariNo ,count(FactorItemsPK) as ted
from saFactor
join saFactorItems on saFactorItems.FactorPK = saFactor.FactorPK
join saMoshtari on saMoshtari.MoshtariPK = saFactor.MoshtariPK
group by FactorNo , MoshtariNo
order by ted desc

select FactorNo , count(FactorItemsPK) as ted , AnbarName , COUNT(kalapk) as th
from saFactor
join saFactorItems on saFactorItems.FactorPK = saFactor.FactorPK
join inAnbar on inAnbar.AnbarPK = saFactor.AnbarPK
where NoeFactor = 1 and FactorStatus = 3 
group by FactorNo, AnbarName
order by ted desc

select FactorNo , kalaname
from saFactor
join saFactorItems on saFactorItems.FactorPK = saFactorItems.FactorPK
join inKala on inKala.KalaPK = saFactorItems.KalaPK
where saFactorItems.KalaPK not in ( select distinct	saFactorItems.KalaPK from saFactorItems where NoeFactor = 1 and FactorStatus = 3 and SodoorDate >=DATEADD(DAY,-30,GETDATE()))
order by KalaName


SELECT DISTINCT KalaCode , moshtaripk 		
from inKala
join saFactorItems on saFactorItems.KalaPK = inKala.KalaPK
join saFactor on saFactor.FactorPK = saFactorItems.FactorPK
where KalaCode = 10000212 and not exists ( select KalaCode from inKala where KalaCode = 1022222)



declare @i as int
set @i = 12
select @i

declare @empname as nvarchar(10) = 'ted'
select @empname + N'hi'

declare @t as int = 1111
select @t * SerialNo  
from inSanadAnbar
where SerialNo = 10800


select
CAST('1393/07/10' as date),
convert (date, '1393/07/10')
from saFactor

