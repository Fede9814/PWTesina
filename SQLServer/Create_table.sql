CREATE TABLE [dbo].[Car_Information](
	[CarBirthTime] [datetime] NOT NULL,
	[IDVehicle] [nvarchar](15) NOT NULL,
	[Gender] [nvarchar](10) NOT NULL,
	[Age] [int] NOT NULL,
	[Name] [nvarchar](25) NOT NULL,
	[Surname] [nvarchar](25) NOT NULL,
	[Plate] [nvarchar](10) NOT NULL,
	[Region] [nvarchar](10) NOT NULL,
	[Model] [nvarchar](50) NOT NULL,
	[Displacement] [nvarchar](10) NOT NULL,
	[CarTax] [nvarchar](15) NOT NULL,
	[Insurance] [nvarchar](15) NOT NULL,
)