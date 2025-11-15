{{config(
    materialized='table',
    unique_key='id',
)}}

with source as(
    SELECT * 
    FROM {{ source('dev', 'raw_weather_data')}}
),

de_dub as (
    select *,
    row_number() over (partition by time order by inserted_at desc) as rn
    from source
)

  

SELECT  
     id,
     city,
     temperature,
     weather_description,
     wind_speed,
     time as weather_time_local,
    (inserted_at + (utc_offset || ' hours')::interval) as inserted_at_local
 FROM de_dub
 WHERE rn = 1