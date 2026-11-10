CREATE PROCEDURE spRegistrarSponsor
(
    @strNombreEmpresa VARCHAR(200),
    @strContacto VARCHAR(200),
    @strCorreo VARCHAR(200)
)
AS
BEGIN

    INSERT INTO tblSponsor
    (
        strNombreEmpresa,
        strContacto,
        strCorreo
    )
    VALUES
    (
        @strNombreEmpresa,
        @strContacto,
        @strCorreo
    );

END
GO

CREATE PROCEDURE spRegistrarEvento
(
    @strNombreEvento VARCHAR(300),
    @dtFechaInicio DATETIME,
    @dtFechaFin DATETIME,
    @intSponsorId INT
)
AS
BEGIN

    INSERT INTO tblEvento
    (
        strNombreEvento,
        dtFechaInicio,
        dtFechaFin,
        intSponsorId
    )
    VALUES
    (
        @strNombreEvento,
        @dtFechaInicio,
        @dtFechaFin,
        @intSponsorId
    );

END
GO

CREATE PROCEDURE spObtenerSponsorsActivos
AS
BEGIN

    SELECT
        intSponsorId,
        strNombreEmpresa,
        strContacto,
        strCorreo
    FROM tblSponsor
    WHERE bitActivo = 1;

END
GO

CREATE PROCEDURE spResumenParticipantes
AS
BEGIN

    SELECT
        E.strNombreEvento,
        STRING_AGG(
            P.strNombre,
            ', '
        ) AS Participantes
    FROM tblEvento E
    INNER JOIN tblParticipante P
        ON P.intEventoId = E.intEventoId
    GROUP BY E.strNombreEvento;

END
GO