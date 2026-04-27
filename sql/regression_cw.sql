SELECT co2_emissions_current, total_floor_area, built_form
FROM (
  SELECT co2_emissions_current, total_floor_area, built_form,
         ROW_NUMBER() OVER (
            PARTITION BY building_reference_number
            ORDER BY inspection_date DESC
        ) AS rn
  FROM energy.energy_certificates
  WHERE local_authority = 'E07000041' AND inspection_date >= '2022-01-01'
) t
WHERE rn = 1;
