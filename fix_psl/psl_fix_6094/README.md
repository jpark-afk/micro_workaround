# Workaround#COMMON - PLATFORMS-6094

This workaround covers the platforms tracked by PLATFORMS-6094.

## Purpose

During `DdsCdd_Init` initialization, the workaround prevents the PSL mutex path from using AUTOSAR `OsResource` synchronization before DDS entities have been created.

The patched mutex implementation treats mutex take/give operations as successful while `dds_cdd_init_state` is earlier than `DdsCdd_InitState_EntitiesCreated`. This avoids calling `GetResource` or `ReleaseResource` during the early DdsCdd initialization phase.

## Scope

- Applies to AUTOSAR PSL sources under this patch folder.
- Intended for environments affected by PLATFORMS-6094.
- Keeps normal `OsResource` synchronization behavior after DdsCdd entity creation is complete.
