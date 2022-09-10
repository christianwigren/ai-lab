SELECT
	--c.PersonId
	--p.Gender
	CASE
		WHEN p.Gender = 'Man' THEN '0'
		WHEN p.Gender = 'Woman' THEN '1'
	END AS Gender
	,DATEDIFF(YY,p.BirthDate,GETDATE()) as Age
	,CASE
		WHEN p.EmploymentStatus IS NULL THEN '0'
		WHEN p.EmploymentStatus = 'HögstaAvgift' THEN '1'
		WHEN p.EmploymentStatus = 'AnställdYrkesverksam' THEN '2'
		WHEN p.EmploymentStatus = 'Arbetslös' THEN '3'
		WHEN p.EmploymentStatus = 'LågSjukFledig' THEN '4'
		WHEN p.EmploymentStatus = 'LägstaAvgift' THEN '5'
		WHEN p.EmploymentStatus = 'SjukFledig' THEN '6'
		WHEN p.EmploymentStatus = 'Studerande' THEN '7'
	END AS EmploymentStatus
	,CASE
		WHEN p.NotificationType = 'Individual' THEN '0'
		WHEN p.NotificationType = 'Collective' THEN '1'
	END AS NotificationType
	,CAST(pr.Amount as INTEGER) AS Debt
	,CASE
		WHEN sr.Amount IS NULL THEN '0'
		WHEN sr.Amount IS NOT NULL THEN '1'
	END AS HasPaid
	FROM CommunicationLog c 
	INNER JOIN Person p ON p.Id = c.PersonId
	cross apply ( select top 1 *
              from PaymentReminder pr
              where pr.PersonId = c.PersonId
			  and pr.CreatedDate < c.CreatedDate
              order by pr.CreatedDate desc
            ) pr
	outer apply ( select top 1 *
              from SubLedgerRow sr
              where sr.PersonId = c.PersonId
			  AND sr.CreatedDate > c.CreatedDate
			  AND DATEADD(day, -10, sr.CreatedDate) < c.CreatedDate
			  AND sr.ArticleName = 'Swish Handel'
              order by pr.CreatedDate desc
            ) sr
	inner join PaymentReminderSwish prs ON prs.PaymentReminderId = pr.Id
