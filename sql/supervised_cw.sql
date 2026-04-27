WITH single_vehicle_accidents AS (
  SELECT accident_index --- collision_index
  FROM dft.stats19_vehicles --- dft.stats19_vehicle
  WHERE substr(accident_index, 1, 4)::int > 2018 ---substr(collision_index, 1, 4)::int > 2018
  GROUP BY accident_index --- collision_index
  HAVING COUNT(DISTINCT vehicle_reference) = 1
),
no_pedestrian_accidents AS (
  SELECT sva.accident_index ---sva.collision_index
  FROM single_vehicle_accidents sva
  LEFT JOIN dft.stats19_casualties c --- dft.stats19_casualty c
    ON sva.accident_index = c.accident_index --- sva.collision_index = c.collision_index
   AND c.casualty_type = 0
  GROUP BY sva.accident_index --- sva.collision_index
  HAVING COUNT(c.casualty_reference) = 0
),

passenger_flag AS (
  SELECT
    npa.accident_index, --- npa.collision_index,
    CASE
      WHEN COUNT(
        CASE WHEN c.casualty_type = 2 THEN 1 END
      ) > 0 THEN 1
      ELSE 0
    END AS passenger_injured
  FROM no_pedestrian_accidents npa
  LEFT JOIN dft.stats19_casualties c --- dft.stats19_casualty c
    ON  npa.accident_index = c.accident_index --- npa.collision_index = c.collision_index
  GROUP BY npa.accident_index --- npa.collision_index
),
vehicle_features AS (
  SELECT
    accident_index, --- collision_index,
    MAX(engine_capacity_cc) AS engine_capacity_cc,
    MAX(age_of_vehicle)     AS vehicle_age,
    MAX(age_of_driver)      AS driver_age
  FROM dft.stats19_vehicles --- dft.stats19_vehicle
  GROUP BY accident_index --- collision_index
)
SELECT
  a.accident_index, --- a.collision_index,
  pf.passenger_injured,
  EXTRACT(DOY  FROM a.obs_date) AS day_of_year, ---EXTRACT(DOY  FROM a.datetime) AS day_of_year,
  EXTRACT(HOUR FROM a.obs_date) AS hour_of_day, ---EXTRACT(HOUR FROM a.datetime) AS hour_of_day,
  a.speed_limit_mph, --- a.speed_limit,
  a.light_conditions,
  a.weather_conditions,
  a.road_surface_conditions,
  a.urban_or_rural_area,
  vf.engine_capacity_cc,
  vf.vehicle_age,
  vf.driver_age
FROM passenger_flag pf
JOIN dft.stats19_accidents a --- dft.stats19_collision a
  ON pf.accident_index = a.accident_index --- pf.collision_index = a.collision_index
LEFT JOIN vehicle_features vf
  ON pf.accident_index = vf.accident_index; --- pf.collision_index = vf.collision_index;
