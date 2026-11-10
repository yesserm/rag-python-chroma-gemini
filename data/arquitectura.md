# Arquitectura del sistema de eventos

El sistema administra sponsors, eventos y participantes.

## Registro de sponsors

Los sponsors son registrados mediante el procedimiento:

spRegistrarSponsor

La información se almacena en la tabla:

tblSponsor

## Registro de eventos

Los eventos se almacenan en la tabla:

tblEvento

y se relacionan con sponsors mediante:

intSponsorId

## Participantes

Los participantes se registran para eventos específicos.

La relación entre participantes y eventos se encuentra en:

tblParticipante

## Reportes

Los reportes utilizan STRING_AGG para consolidar participantes por evento.

El procedimiento encargado es:

spResumenParticipantes