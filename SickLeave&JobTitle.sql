--What is the relationship between sick leave and Job Title (PersonType)?
-- Person.Person (job title)
-- HumanResource.Employee (sickleave)

SELECT *
FROM Person.Person;

SELECT *
FROM HumanResources.Employee;

--left joining persontype and name details of the employee to human resources information to identify employees

SELECT 
    p.PersonType, 
    p.FirstName, 
    p.LastName,
    h.OrganizationLevel,
    h.JobTitle,
    h.Birthdate,
    h.MaritalStatus,
    h.Gender,
    h.HireDate,
    h.VacationHours,
    h.SickLeaveHours
FROM 
    Person.Person AS p
LEFT JOIN 
    HumanResources.Employee AS h
    ON p.BusinessEntityID = h.BusinessEntityID
WHERE
h.SickLeaveHours IS NOT NULL;
--have to filter to not including null values so only accounting those whos sick leave is registered/ is currently employee of AdventureWorks
--person type examples EM = Employee, SP = Sales Person, SC = Store Contact, VC = Vendor Contact, GC = General Contact, IN = Individual Customer
--since SC, VC and IN are not considered employees then they are not accounted in this data

