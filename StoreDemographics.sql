-- What is the relationship between store trading duration and revenue? (together)


--SELECT * 
--FROM Sales.vStoreWithDemographics;

Select 
	BusinessEntityID,
	Name,
	AnnualRevenue,
	BankName,
	BusinessType,
	YearOpened,
	NumberEmployees,
	SquareFeet
FROM
Sales.vStoreWithDemographics;

--yearopened will tell us the store trading duration and annualrevenue for revenue



