{{config(
    materialized='table'
)}}

SELECT 
city,
DATE(weather_time_local) as date,
round(AVG(temperature)::numeric,2) as avg_temperature,
round(AVG(wind_speed)::numeric,2) as avg_wind_speed
FROM {{ ref('stg_weather_data') }}

GROUP BY 
city,
DATE(weather_time_local)
ORDER BY 
city,
DATE(weather_time_local)