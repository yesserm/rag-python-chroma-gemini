CREATE TABLE tblCatUsuario
(
    intUsuarioId INT PRIMARY KEY IDENTITY,
    strNombre VARCHAR(200),
    strCorreo VARCHAR(200),
    dtFechaRegistro DATETIME DEFAULT GETDATE(),
    bitActivo BIT DEFAULT 1
);
GO

CREATE TABLE tblSponsor
(
    intSponsorId INT PRIMARY KEY IDENTITY,
    strNombreEmpresa VARCHAR(200),
    strContacto VARCHAR(200),
    strCorreo VARCHAR(200),
    dtFechaRegistro DATETIME DEFAULT GETDATE(),
    bitActivo BIT DEFAULT 1
);
GO

CREATE TABLE tblEvento
(
    intEventoId INT PRIMARY KEY IDENTITY,
    strNombreEvento VARCHAR(300),
    dtFechaInicio DATETIME,
    dtFechaFin DATETIME,
    intSponsorId INT,
    FOREIGN KEY (intSponsorId)
        REFERENCES tblSponsor(intSponsorId)
);
GO

CREATE TABLE tblParticipante
(
    intParticipanteId INT PRIMARY KEY IDENTITY,
    strNombre VARCHAR(200),
    strCorreo VARCHAR(200),
    intEventoId INT,
    FOREIGN KEY (intEventoId)
        REFERENCES tblEvento(intEventoId)
);
GO