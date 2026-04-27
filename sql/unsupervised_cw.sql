SELECT
    local_authority,
    --- Metrics
    PERCENTILE_CONT(0.5)
        WITHIN GROUP (ORDER BY co2_emissions_current)
        AS median_co2_emissions_current,
    PERCENTILE_CONT(0.5)
        WITHIN GROUP (ORDER BY energy_consumption_current)
        AS median_energy_consumption_current,
    PERCENTILE_CONT(0.5)
        WITHIN GROUP (ORDER BY heating_cost_current)
        AS median_heating_cost_current,
    PERCENTILE_CONT(0.5)
        WITHIN GROUP (ORDER BY hot_water_cost_current)
        AS median_hot_water_cost_current,
     PERCENTILE_CONT(0.5)
        WITHIN GROUP (ORDER BY lighting_cost_current)
        AS median_lighting_cost_current,
    --- Efficiency
    PERCENTILE_CONT(0.5)
        WITHIN GROUP (
            ORDER BY co2_emissions_current / total_floor_area
        ) AS median_co2_per_m2,
    PERCENTILE_CONT(0.5)
        WITHIN GROUP (
          ORDER BY energy_consumption_current / total_floor_area)
        AS median_energy_consumption_per_m2,
    PERCENTILE_CONT(0.5)
        WITHIN GROUP (
          ORDER BY heating_cost_current / total_floor_area)
        AS median_heating_cost_per_m2,
    PERCENTILE_CONT(0.5)
        WITHIN GROUP (
          ORDER BY hot_water_cost_current / total_floor_area)
        AS median_hot_water_cost_per_m2,
     PERCENTILE_CONT(0.5)
        WITHIN GROUP (
          ORDER BY lighting_cost_current / total_floor_area)
        AS median_lighting_cost_per_m2
FROM energy.energy_certificates
WHERE co2_emissions_current IS NOT NULL
  AND energy_consumption_current IS NOT NULL
  AND heating_cost_current IS NOT NULL
  AND hot_water_cost_current IS NOT NULL
  AND lighting_cost_current IS NOT NULL
  AND total_floor_area IS NOT NULL
  AND total_floor_area > 0
  AND inspection_date >= '2021-01-01'
GROUP BY local_authority
ORDER BY local_authority;
