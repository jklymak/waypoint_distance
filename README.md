# waypoint_distance

Simple distance along a route calculator.  Given a set of waypoints, and ship positions, calculate the distance along the line (from first waypoint) and distance across track.

```python
import waypoint_distance as wd

along, across = wd.get_simple_distance(wplons, wplats, shiplon, shiplat, central_lat=50.0)
```

Note the calculation is for *small* geographic areas where a Cartesian projection is valid.  i.e. we are not taking into account changing dx with latitude.