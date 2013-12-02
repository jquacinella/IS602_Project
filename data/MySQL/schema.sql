CREATE  TABLE IF NOT EXISTS `%s`.`%s` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `AREA` ENUM('Mountain','Mississippi','Northeast','West','Oklahoma','Delaware','San Jose-Monterey','Minnesota','West South Central','Illinois','Arkansas','New Mexico','New Hampshire','Indiana','Maryland','Louisiana','Idaho','Wyoming','Tennessee','Arizona','Iowa','San Francisco-Oakland','Midwest','Michigan','Kansas','Utah','Virginia','Oregon','Seattle-Puget Sound','Connecticut','Montana','California','Massachusetts','Los Angeles','United States (comparable to ICD-O-2)','South Carolina','East South Central','Atlanta','East North Central','Wisconsin','Vermont','Georgia','North Dakota','Pennsylvania','West Virginia','New England','Florida','Alaska','Detroit','Hawaii','Middle Atlantic','Nebraska','Kentucky','Missouri','Ohio','Alabama','New York','South','South Dakota','Colorado','South Atlantic','New Jersey','Washington','North Carolina','West North Central','District of Columbia','Texas','Nevada','Pacific','Maine','Rhode Island') NULL ,
  `AGE_ADJUSTED_CI_LOWER` FLOAT NULL ,
  `AGE_ADJUSTED_CI_UPPER` FLOAT NULL ,
  `AGE_ADJUSTED_RATE` FLOAT NULL ,
  `COUNT` INT NULL ,
  `EVENT_TYPE` ENUM('Incidence', 'Mortality') NULL ,
  `POPULATION` INT NULL ,
  `RACE` ENUM('American Indian/Alaska Native', 'Asian/Pacific Islander', 'All Races', 'Hispanic', 'Black', 'White') NULL ,
  `SEX` ENUM('Male', 'Female', 'Male and Female') NULL ,
  `SITE` ENUM('All Cancer Sites Combined','Brain and Other Nervous System','Cervix','Colon and Rectum','Corpus and Uterus, NOS','Esophagus','Female Breast','Female Breast, <i>in situ</i>','Hodgkin Lymphoma','Kaposi Sarcoma','Kidney and Renal Pelvis','Larynx','Leukemias','Liver and Intrahepatic Bile Duct','Lung and Bronchus','Melanomas of the Skin','Mesothelioma','Myeloma','Non-Hodgkin Lymphoma','Oral Cavity and Pharynx','Ovary','Pancreas','Prostate','Stomach','Testis','Thyroid','Urinary Bladder') NULL ,
  `YEAR` INT NULL ,
  `CRUDE_CI_LOWER` FLOAT NULL ,
  `CRUDE_CI_UPPER` FLOAT NULL ,
  `CRUDE_RATE` FLOAT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB