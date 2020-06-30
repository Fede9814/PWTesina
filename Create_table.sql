CREATE TABLE [dbo].[Car_Information](
	[CarBirthTime] [datetime] NOT NULL,
	[IDVehicle] [nvarchar](15) NOT NULL,
	[Gender] [nvarchar](1) NOT NULL,
	[Age] [int] NOT NULL,
	[Name] [nvarchar](15) NOT NULL,
	[Surname] [nvarchar](15) NOT NULL,
	[Plate] [nvarchar](7) NOT NULL,
	[Region] [nvarchar](2) NOT NULL,
	[Model] [nvarchar](15) NOT NULL,
	[Displacement] [nvarchar](4) NOT NULL,
	[CarTax] [nvarchar](10) NOT NULL,
	[Insurance] [nvarchar](10) NOT NULL,
)