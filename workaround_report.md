# RTI workaround report

## Generated date: 2026-09-14

## Baseline Connext Micro version: 4.0.0_ER738

**Workaround Report -- snippets with context and line numbers**

- Scope: collected `workaround#` occurrences from all files under `common/templates`, `common/fix_psl`.
- Total items found: 46
- Categories: COMMON (30), HAE (14), VTT (2)

Category definitions:
- **COMMON**: Mandatory patch.
- **HAE**: For Autoever only; not a mandatory patch.
- **VTT**: For virtual target (internal only); not a mandatory patch.

Below are code snippets (about +/-5 lines) around each `workaround#` occurrence. Items are grouped by category in this order: COMMON, HAE, VTT.

### COMMON (30)

1) File: common/templates/.workaround/patch_arcgen_types.py (L2)  
"""workaround#COMMON - APIT-495 """  

```text
L1: #!/usr/bin/env python3
L2: """workaround#COMMON - APIT-495 """
L3: """Patch DDS XML primitive type names for rtiarcgen compatibility.
L4: 
L5: The source XML may use the newer type names from
L6: rti_dds_topic_types_definitions.xsd. Some rtiarcgen paths still resolve the
L7: deprecated IDL-style names correctly, so this script writes a patched copy for
```

2) File: common/templates/.workaround/patch_dpse_appgen.py (L9)  
"""workaround#COMMON - MAG-424 """  

```text
L4: # Baseline version: Micro430er738.
L5: # Not officially supported by RTI Technical Support.
L6: # Must NOT be applied directly to controller mass-production development.
L7: # See README.md for details.
L8: 
L9: """workaround#COMMON - MAG-424 """
L10: """Patch DPSE-mode Appgen.h/.c files with the correct include and dds_ prefix.
L11: 
L12: rtiddsmag run without -deployment/-applicationType produces <xmlName>Appgen.h/.c
L13: that (a) #include the wrong header for the type plugin, and (b) reference
L14: "<TypeName>TypePlugin_get" instead of "dds_<TypeName>TypePlugin_get".
```

3) File: common/templates/.workaround/patch_unused_conversions.py (L2)  
"""workaround#COMMON - APIT-499"""  

```text
L1: #!/usr/bin/env python3
L2: """workaround#COMMON - APIT-499"""
L3: """Comment conversion blocks for DDS types unused by a deployment."""
L4: import argparse
L5: import re
L6: import xml.etree.ElementTree as ET
L7: 
```

4) File: common/templates/autosar/application/autosar_model/application.arxml.vm (L196)  
Workaround#COMMON - MICRO-14138 - delete duplated port inteface definition  

```text
L191:           </CODE-DESCRIPTORS>
L192:           <BEHAVIOR-REF DEST="SWC-INTERNAL-BEHAVIOR">/ComponentTypes/${systemModel.appName}Type/${systemModel.appName}Type_InternalBehavior</BEHAVIOR-REF>
L193:         </SWC-IMPLEMENTATION>
L194:       </ELEMENTS>
L195:     </AR-PACKAGE> ## End of ComponentTypes
L196:     <!-- Workaround#COMMON - MICRO-14138 - delete duplated port inteface definition -->
L197:     <!--
L198:     ## - - - - - - - - - - - - - - - - -
L199:     ## Port Interfaces                 |
L200:     ## - - - - - - - - - - - - - - - - -
L201:     <AR-PACKAGE>
```

5) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter.c.vm (L44)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L39:  *============================================================================*/
L40: 
L41: /**
L42:  * @brief Current DDS initialization state (NOT configurable)
L43:  */
L44:  /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L45: DdsCdd_InitState_t dds_cdd_init_state = DdsCdd_InitState_Uninitialized;
L46: 
L47: /*==============================================================================
L48:  *                     SW-C RUNNABLE IMPLEMENTATIONS
L49:  *============================================================================*/
```

6) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter.h.vm (L36)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L31: /**
L32:  * @brief DDS initialization state tracking
L33:  */
L34: typedef enum
L35: {
L36:     /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L37:     //DdsCdd_InitState_TcpIpNotReady = 0,
L38:     //DdsCdd_InitState_TcpIpReady,
L39:     DdsCdd_InitState_Uninitialized = 0,
L40: 
L41:     DdsCdd_InitState_SystemPropertiesSet,
```

7) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter.h.vm (L129)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L124:  * 
L125:  * Sets system properties and creates DDS entities.
L126:  */
L127: void DdsCdd_Adapter_Init(void);
L128: 
L129: /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L130: /**
L131:  * @brief Enable DDS entities
L132:  * 
L133:  * Enables DDS entities after creation.
L134:  */
```

8) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L80)  
/* workaround#COMMON - MICRO-14139- Some RTI Micro 4.3.0 header sets do not expose these prototypes publicly. */  

```text
L75: ${hashtag}if defined(_MSC_VER) && !defined(__at)
L76: ${hashtag}define __at(address)
L77: ${hashtag}endif
L78: ${hashtag}endif
L79: 
L80: /* workaround#COMMON - MICRO-14139- Some RTI Micro 4.3.0 header sets do not expose these prototypes publicly. */
L81: RTI_BOOL OSPSL_AutosarSystem_get_property(struct OSAPI_SystemAutosar *property);
L82: RTI_BOOL OSPSL_AutosarSystem_set_property(struct OSAPI_SystemAutosar *property);
L83: 
L84: #end
L85: 
```

9) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L192)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L187:             RTI_TRUE; /* TODO: Default is not thread safe, change to true if using multithread */
L188:     
L189:     /* Connext DDS Micro will use Resources as synchronization method */
L190:     system_property.psl_property.sync_type = OSAPI_AUTOSAR_SYNCKIND_RESOURCES;
L191:     system_property.psl_property.mutex_resource_id = ${autosarConfig.getMutexResourceId()};
L192:     /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L193:     system_property.psl_property.timer_resource_id = OsResource_DdsTimer;
L194:     system_property.psl_property.netio_resource_id = OsResource_DdsNetio;
L195:     
L196:     /* AUTOSAR synchronization configuration - Resources only */
L197:     system_property.psl_property.semaphore_max_count = 0;
```

10) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L260)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L255:  * @post DDS entities created but disabled if successful
L256:  */
L257: void DdsCdd_Adapter_Init(void)
L258: {
L259:     sint8 retval;
L260:     /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L261:     //printf("DDS_Init: Start Init DDS \n");
L262: 
L263:     /* Check if TcpIp is ready */
L264:     //if (dds_cdd_init_state == DdsCdd_InitState_TcpIpNotReady || 
L265:     //    dds_cdd_init_state == DdsCdd_InitState_Error)
```

11) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L272)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L267:     //    printf("DDS_Init: TcpIp not ready or error state\n");
L268:     //    return;
L269:     //}
L270: 
L271:     /* Set system properties */
L272:     /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L273:     //if (dds_cdd_init_state == DdsCdd_InitState_TcpIpReady)
L274:     //{
L275:         printf("DDS_Init: Setting system properties\n");
L276:         if (0 != SetSystemProperties())
L277:         {
```

12) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L282)  
/* Workaround#COMMON - PLATFORMS-6163 - PIL option error */  

```text
L277:         {
L278:             printf("DDS_Init: Failed to set system properties\n");
L279:             dds_cdd_init_state = DdsCdd_InitState_Error;
L280:             return;
L281:         }
L282:         /* Workaround#COMMON - PLATFORMS-6163 - PIL option error */
L283: ${hashtag}if 0
L284:         //original implementation
L285:         else if(RTI_TRUE != OSAPI_System_initialize())
L286:         {
L287:             printf("DDS_Init: OSAPI_System initialization failed\n");
```

13) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L339)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L334: 
L335: ## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
L336: ## macro to define the DdsCdd_Adapter_Enable_DDSEntities function
L337: ## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
L338: #macro( ddsCddAdapterC_DdsCdd_Adapter_Enable_DDSEntities  )
L339: /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L340: /**********************************************************************************************************************
L341:  * DdsCdd_Adapter_Enable_DDSEntities()
L342:  *********************************************************************************************************************/
L343: /**
L344:  * @brief Enable DDS entities
```

14) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L382)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L377: 
L378: ## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
L379: ## macro to define the DdsCdd_Adapter_Run function
L380: ## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
L381: #macro( ddsCddAdapterC_DdsCdd_Adapter_Run )
L382: /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L383: /**********************************************************************************************************************
L384:  * DdsCdd_Adapter_Run()
L385:  *********************************************************************************************************************/
L386: /**
L387:  * @brief Maintain DDS timer
```

15) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L457)  
/* Convert DDS type (dds_${type}) to AUTOSAR type (${type}) */ /* workaround#COMMON - MICRO-13937 - delete & of rte_data */  

```text
L452:     if (is_valid)
L453:     {
L454:         /* Valid sample received */
L455:         printf("DdsCdd_Adapter_Read_${topic}: Valid sample received\n");
L456: 
L457:         /* Convert DDS type (dds_${type}) to AUTOSAR type (${type}) */ /* workaround#COMMON - MICRO-13937 - delete & of rte_data */
L458:         ${type}_dds_to_rte(&dds_sample, rte_data);
L459:         return 0;
L460:     }
L461:     else
L462:     {
```

16) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L577)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L572: {
L573:     printf("[RTI] DDS_LocalIpAddrAssignmentChg %u:%u!\n", LocalAddrId, State);
L574:     NETIO_Autosar_update_ip_assignment_state(LocalAddrId, State);
L575:     if((State == TCPIP_IPADDR_STATE_ASSIGNED))
L576:     {
L577:         /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L578:         //if ((dds_cdd_init_state == DdsCdd_InitState_TcpIpNotReady) && (LocalAddrId == 0))
L579:         //{
L580:         //    printf("TCP/IP is ready - allow DDS initialization\n");
L581:         //    dds_cdd_init_state = DdsCdd_InitState_TcpIpReady;
L582:         //}
```

17) File: common/templates/autosar/CDD/autosar_gen/DdsCdd.c.vm (L119)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L114:             #end
L115:         #end
L116:     #end
L117: #end
L118: 
L119: /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L120: /**********************************************************************************************************************
L121:  *
L122:  * Runnable Entity Name: TimerTick
L123:  *
L124:  *---------------------------------------------------------------------------------------------------------------------
```

18) File: common/templates/autosar/CDD/autosar_gen/DdsCdd.c.vm (L164)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L159: /**********************************************************************************************************************
L160:  * DO NOT CHANGE THIS COMMENT!           << End of runnable implementation >>               DO NOT CHANGE THIS COMMENT!
L161:  *********************************************************************************************************************/
L162: }
L163: 
L164: /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L165: /**********************************************************************************************************************
L166:  *
L167:  * Runnable Entity Name: TimerUpdate
L168:  *
L169:  *---------------------------------------------------------------------------------------------------------------------
```

19) File: common/templates/autosar/CDD/autosar_gen/DdsCdd.c.vm (L270)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L265: {
L266: /**********************************************************************************************************************
L267:  * DO NOT CHANGE THIS COMMENT!           << Start of runnable implementation >>             DO NOT CHANGE THIS COMMENT!
L268:  * Symbol: DdsCddStart
L269:  *********************************************************************************************************************/
L270:     /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L271:     /* Enable DDS Entities */
L272:     DdsCdd_Adapter_Enable_DDSEntities();
L273: 
L274: /**********************************************************************************************************************
L275:  * DO NOT CHANGE THIS COMMENT!           << End of runnable implementation >>               DO NOT CHANGE THIS COMMENT!
```

20) File: common/templates/autosar/CDD/autosar_gen/DdsCdd.c.vm (L289)  
/* workaround#COMMON - MICRO-14137 - wrong position, DdsCdd_Init placed outside. */  

```text
L284:             #end
L285:         #end
L286:     #end
L287: #end
L288: 
L289: /* workaround#COMMON - MICRO-14137 - wrong position, DdsCdd_Init placed outside. */
L290: ${hashtag}if 0
L291: ${hashtag}define DdsCdd_STOP_SEC_CODE
L292: ${hashtag}include "DdsCddType_MemMap.h" /* PRQA S 5087 */ /* MD_MSR_MemMap */
L293: ${hashtag}endif
L294: 
```

21) File: common/templates/autosar/CDD/autosar_gen/DdsCdd.c.vm (L302)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L297:  *********************************************************************************************************************/
L298: 
L299:   FUNC(void, DdsCdd_CODE) DdsCdd_Init(void) 
L300: {
L301:   /* TODO: Create entities once micro allows doing so before rte*/
L302:   /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L303:   /* Initialize DDS adapter layer */
L304:   DdsCdd_Adapter_Init();    //This function will be called by EcuM directly before StartOs.
L305: }
L306: 
L307: /* workaround#HAE - right position and senction name */
```

22) File: common/fix_psl/psl_fix_14110/code_patch_rules.toml (L3)  
marker = "workaround#COMMON - MICRO-14110"  

```text
L1: source_root = "C:\RTI\rti_connext_drive-4.0.0\rti_connext_dds-7.3.1\rti_connext_dds_micro-4.3.0_ER738\src\rti_me_psl\netiopsl\udp"
L2: output_root = "_patched_tmp"
L3: marker = "workaround#COMMON - MICRO-14110"
L4: # The following features are disabled when Micro is compiled with the CERT flags:
L5: # binding the send socket 
L6: # monitoring the network stack for state changes for sockets and interfaces
L7: # Must handle the case where the TcpIp stack comes up before Micro.
L8: # These features must also be enabled with for the Cert profile. It is not clear why they are disabled.
```

23) File: common/fix_psl/psl_fix_6094/src/rti_me_psl/ospsl/autosar/autosarMutex.c (L30)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L25:  * \file
L26:  * \brief AutoSAR implementation of OSAPI mutex routines
L27:  */
L28: #include "autosarMutex.h"
L29: 
L30: /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L31: #include "dds_cdd_adapter.h"
L32: extern DdsCdd_InitState_t dds_cdd_init_state;
L33: 
L34: /* Global mutex lock */
L35: RTI_PRIVATE struct OSAPI_Mutex OSAPI_AutosarMutex_fv_GlobalMutex = OSAPI_MUTEX_INITIALIZER;
```

24) File: common/fix_psl/psl_fix_6094/src/rti_me_psl/ospsl/autosar/autosarMutex.c (L243)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L238: FUNC(RTI_BOOL, SOAD_CODE)
L239: OSAPI_Mutex_take(P2VAR(struct OSAPI_Mutex, AUTOMATIC, SOAD_APPL_DATA) mutex)
L240: {
L241:     StatusType ret_value;
L242:     RTI_BOOL success = RTI_FALSE;
L243:     /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L244:     OSAPI_ThreadId self; //= OSAPI_Thread_self();
L245: 
L246:     OSAPI_PRECONDITION(mutex == NULL_PTR,return RTI_FALSE,
L247:                        OSAPI_Log_entry_add_pointer("mutex",mutex,RTI_TRUE);)
L248: 
```

25) File: common/fix_psl/psl_fix_6094/src/rti_me_psl/ospsl/autosar/autosarMutex.c (L249)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L244:     OSAPI_ThreadId self; //= OSAPI_Thread_self();
L245: 
L246:     OSAPI_PRECONDITION(mutex == NULL_PTR,return RTI_FALSE,
L247:                        OSAPI_Log_entry_add_pointer("mutex",mutex,RTI_TRUE);)
L248: 
L249:     /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L250:     if (dds_cdd_init_state < DdsCdd_InitState_EntitiesCreated) return RTI_TRUE;   
L251:     self = OSAPI_Thread_self();
L252: 
L253:     /* check recursion using internal state of the singleton */
L254:     if (OSAPI_Mutex_is_owned(mutex))
```

26) File: common/fix_psl/psl_fix_6094/src/rti_me_psl/ospsl/autosar/autosarMutex.c (L298)  
/* workaround#COMMON - PLATFORMS-6094 - task overrun issue */  

```text
L293:     RTI_BOOL success = RTI_FALSE;
L294: 
L295:     OSAPI_PRECONDITION(mutex == NULL_PTR,return RTI_FALSE,
L296:                        OSAPI_Log_entry_add_pointer("mutex",mutex,RTI_TRUE);)
L297: 
L298:     /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L299:     if (dds_cdd_init_state < DdsCdd_InitState_EntitiesCreated) return RTI_TRUE;
L300: 
L301:     if (!OSAPI_Mutex_is_owned(mutex))
L302:     {
L303:         return RTI_FALSE;
```

27) File: common/fix_psl/repository/srcC/ospsl/autosar/autosarMutex.c (L30)  
/* workaround#COMMON - task overrun issue */  

```text
L25:  * \file
L26:  * \brief AutoSAR implementation of OSAPI mutex routines
L27:  */
L28: #include "autosarMutex.h"
L29: 
L30: /* workaround#COMMON - task overrun issue */
L31: #include "dds_cdd_adapter.h"
L32: extern DdsCdd_InitState_t dds_cdd_init_state;
L33: 
L34: /* Global mutex lock */
L35: RTI_PRIVATE struct OSAPI_Mutex OSAPI_AutosarMutex_fv_GlobalMutex = OSAPI_MUTEX_INITIALIZER;
```

28) File: common/fix_psl/repository/srcC/ospsl/autosar/autosarMutex.c (L243)  
/* workaround#COMMON - task overrun issue */  

```text
L238: FUNC(RTI_BOOL, SOAD_CODE)
L239: OSAPI_Mutex_take(P2VAR(struct OSAPI_Mutex, AUTOMATIC, SOAD_APPL_DATA) mutex)
L240: {
L241:     StatusType ret_value;
L242:     RTI_BOOL success = RTI_FALSE;
L243:     /* workaround#COMMON - task overrun issue */
L244:     OSAPI_ThreadId self; //= OSAPI_Thread_self();
L245: 
L246:     OSAPI_PRECONDITION(mutex == NULL_PTR,return RTI_FALSE,
L247:                        OSAPI_Log_entry_add_pointer("mutex",mutex,RTI_TRUE);)
L248: 
```

29) File: common/fix_psl/repository/srcC/ospsl/autosar/autosarMutex.c (L249)  
/* workaround#COMMON - task overrun issue */  

```text
L244:     OSAPI_ThreadId self; //= OSAPI_Thread_self();
L245: 
L246:     OSAPI_PRECONDITION(mutex == NULL_PTR,return RTI_FALSE,
L247:                        OSAPI_Log_entry_add_pointer("mutex",mutex,RTI_TRUE);)
L248: 
L249:     /* workaround#COMMON - task overrun issue */
L250:     if (dds_cdd_init_state < DdsCdd_InitState_EntitiesCreated) return RTI_TRUE;   
L251:     self = OSAPI_Thread_self();
L252: 
L253:     /* check recursion using internal state of the singleton */
L254:     if (OSAPI_Mutex_is_owned(mutex))
```

30) File: common/fix_psl/repository/srcC/ospsl/autosar/autosarMutex.c (L298)  
/* workaround#COMMON - task overrun issue */  

```text
L293:     RTI_BOOL success = RTI_FALSE;
L294: 
L295:     OSAPI_PRECONDITION(mutex == NULL_PTR,return RTI_FALSE,
L296:                        OSAPI_Log_entry_add_pointer("mutex",mutex,RTI_TRUE);)
L297: 
L298:     /* workaround#COMMON - task overrun issue */
L299:     if (dds_cdd_init_state < DdsCdd_InitState_EntitiesCreated) return RTI_TRUE;
L300: 
L301:     if (!OSAPI_Mutex_is_owned(mutex))
L302:     {
L303:         return RTI_FALSE;
```

### HAE (14)

31) File: common/templates/.workaround/patch_missing_part_hkmc.py (L2)  
"""workaround#HAE"""  

```text
L1: #!/usr/bin/env python3
L2: """workaround#HAE"""
L3: """Patch a raw HKMC DDS System XML with the parts a fresh customer export
L4: is missing, entirely from built-in templates (no reference XML needed):
L5: 
L6: - The root xsi:noNamespaceSchemaLocation, pointed at the local Micro install
L7:   schema instead of the community.rti.com URL.
```

32) File: common/templates/.workaround/patch_missing_part_hkmc.py (L259)  
element.append(ET.Comment(" Workaround#HAE "))  

```text
L254:         " [REQUIRED] Heap size/name must match MCU memory design; edit start_address if the platform requires an explicit address. "
L255:     ))
L256:     ET.SubElement(element, "size").text = str(heap_size)
L257:     start_address = ET.SubElement(element, "start_address")
L258:     start_address.text = " "
L259:     element.append(ET.Comment(" Workaround#HAE "))
L260:     ET.SubElement(element, "name").text = heap_name
L261:     autosar.append(ET.Comment(" [REQUIRED] Set DDS-dedicated OS resource name allocated in AUTOSAR OS config. "))
L262:     ET.SubElement(autosar, "mutex_resource_id").text = mutex_resource_id
L263:     autosar.append(ET.Comment(" [REQUIRED] Set to the highest index used in TcpIp local_addr_id configuration. "))
L264:     ET.SubElement(autosar, "max_local_addr_id").text = str(max_local_addr_id)
```

33) File: common/templates/.workaround/patch_receiver_init_values.py (L2)  
"""workaround#HAE - mobilgene cannot interpret RECORD-VALUE-SPECIFICATION"""  

```text
L1: #!/usr/bin/env python3
L2: """workaround#HAE - mobilgene cannot interpret RECORD-VALUE-SPECIFICATION"""
L3: """Create typed port initialization constants in DdsCddType.arxml."""
L4: import argparse
L5: import os
L6: import tempfile
L7: import xml.etree.ElementTree as ET
```

34) File: common/templates/autosar/application/autosar_model/application.arxml.vm (L65)  
Workaround#HAE - delete unnecessary elements  

```text
L60:                   <DATA-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE">/PortInterfaces/${topic}/${type}</DATA-ELEMENT-REF>
L61:                   <HANDLE-OUT-OF-RANGE>NONE</HANDLE-OUT-OF-RANGE>
L62:                   <USES-END-TO-END-PROTECTION>false</USES-END-TO-END-PROTECTION>
L63:                   <ALIVE-TIMEOUT>0</ALIVE-TIMEOUT>
L64:                   <ENABLE-UPDATE>false</ENABLE-UPDATE>
L65:                   <!-- Workaround#HAE - delete unnecessary elements
L66:                   <FILTER>
L67:                     <DATA-FILTER-TYPE>ALWAYS</DATA-FILTER-TYPE>
L68:                   </FILTER>
L69:                   -->
L70:                   <HANDLE-NEVER-RECEIVED>false</HANDLE-NEVER-RECEIVED>
L71:                   <INIT-VALUE>
L72:                     <RECORD-VALUE-SPECIFICATION>
L73:                       <FIELDS>
L74:                         <NUMERICAL-VALUE-SPECIFICATION>
```

35) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter.c.vm (L77)  
/* Workaround#HAE - mobilgene naming rule, prefix TcpIp_ */  

```text
L72: /*==============================================================================
L73:  *                        SOCKET OWNER INTEGRATION
L74:  *============================================================================*/
L75: 
L76: /* TcpIp_[SocketOwnerName]GetSocket - TODO: update if using different SocketOwner name */
L77: /* Workaround#HAE - mobilgene naming rule, prefix TcpIp_ */
L78: ${hashtag}define DDSCDD_SOCKET_OWNER_GET_SOCKET   TcpIp_TcpIp_DdsCddGetSocket   /* TcpIp_socket_name = TcpIp_DdsCdd */
L79: 
L80: #ddsCddAdapterC_DdsCdd_GetSocket()
L81: 
L82: #ddsCddAdapterC_DdsCdd_LocalIpAddrAssignmentChg()
```

36) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L126)  
/* Workaround#HAE - MICRO-14140 - empty start_address doesn't need at() */  

```text
L121: /**
L122:  * @brief Static heap area 1 buffer
L123:  * 
L124:  * Pre-allocated static buffer for DDS memory management.
L125:  */
L126:  /* Workaround#HAE - MICRO-14140 - empty start_address doesn't need at() */
L127:     #foreach( $heap in $heaps )
L128:     #set( $heapStartAddress = "$!heap.getStartAddress()" )
L129:     #if( $heapStartAddress.trim().length() > 0 )
L130: static char heap_area${foreach.count}[DDSCDD_${heap.getName().toUpperCase()}_SIZE] __at(${heap.getStartAddress()});
L131:     #else
```

37) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L185)  
/* workaround#HAE - enable use_udp_thread */  

```text
L180:     
L181:     /* Configure static memory heap areas */
L182:     system_property.psl_property.number_of_heap_areas = DDSCDD_NUMBER_OF_HEAP_AREAS;
L183:     system_property.psl_property.heap_area_size = heap_area_size;
L184:     system_property.psl_property.heap_area = (const char **)heap_area;
L185:     /* workaround#HAE - enable use_udp_thread */
L186:     system_property.psl_property.enable_thread_safe_heap =
L187:             RTI_TRUE; /* TODO: Default is not thread safe, change to true if using multithread */
L188:     
L189:     /* Connext DDS Micro will use Resources as synchronization method */
L190:     system_property.psl_property.sync_type = OSAPI_AUTOSAR_SYNCKIND_RESOURCES;
```

38) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L213)  
/* workaround#HAE - enable use_udp_thread */  

```text
L208:     ${hashtag}else
L209:         system_property.psl_property.max_receive_sockets = 2;  /* Unicast only */
L210:     ${hashtag}endif
L211:     
L212:     /* Disable internal UDP buffers - use AUTOSAR TcpIp stack buffers */
L213:     /* workaround#HAE - enable use_udp_thread */
L214:     system_property.psl_property.number_of_rcv_buffers = 8u;
L215:     system_property.psl_property.rcv_buffer_size = 1500u;
L216:     
L217:     /* Set AUTOSAR TcpIp integration callbacks */
L218:     system_property.psl_property.get_socket = DdsCdd_GetSocket;
```

39) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L225)  
/* workaround#HAE - enable use_udp_thread */  

```text
L220:     system_property.psl_property.max_local_addr_id = ${autosarConfig.getMaxLocalAddrId()};
L221: 
L222:     system_property.psl_property.send_local_addr_id = ${autosarConfig.getSendLocalAddrId()};
L223:     
L224:     /* Configure UDP thread handling - use synchronous mode for AUTOSAR */
L225:     /* workaround#HAE - enable use_udp_thread */
L226:     system_property.psl_property.use_udp_thread = TRUE;
L227:     system_property.psl_property.dds_rxindication =
L228:             DdsCddRxIndication;  /* TODO: Default name for dds rx indication, change if using custom callback */
L229: 
L230:     if (!OSPSL_AutosarSystem_set_property(&system_property))
```

40) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.h.vm (L117)  
/* workaround#HAE */  

```text
L112:     ${hashtag}include "Std_Types.h"
L113:     ${hashtag}include "Os_Cfg.h"
L114:     ${hashtag}include "TcpIp.h"
L115:     ${hashtag}include "Rte_DdsCddType.h"  /* Provides ${inputFilePlugin} type definition and RTE function signatures */
L116: 
L117:     /* workaround#HAE */
L118:     /* RTI DDS Micro includes are intentionally kept out of this public header.
L119:     * Include them in implementation files only to avoid macro conflicts with
L120:     * AUTOSAR compiler abstraction (e.g., CONST/VAR macros). */
L121:     ${hashtag}ifndef VVIRTUALTARGET
L122:     ${hashtag}include "dds_impl.h"
```

41) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.h.vm (L125)  
/* workaround#HAE - add an user_stub header file */  

```text
L120:     * AUTOSAR compiler abstraction (e.g., CONST/VAR macros). */
L121:     ${hashtag}ifndef VVIRTUALTARGET
L122:     ${hashtag}include "dds_impl.h"
L123:     ${hashtag}endif
L124: 
L125:     /* workaround#HAE - add an user_stub header file */
L126:     ${hashtag}include "dds_cdd_userstub.h" //SHOULD BE CREATED EXTERNALLY
L127: #end
L128: 
L129: ## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
L130: ## macro to declare write functions that RTE will call when application writes to RTE
```

42) File: common/templates/autosar/CDD/autosar_gen/DdsCdd.c.vm (L66)  
/* workaround#HAE - section naming rule */  

```text
L61: /**********************************************************************************************************************
L62:  * DO NOT CHANGE THIS COMMENT!           << End of include and declaration area >>          DO NOT CHANGE THIS COMMENT!
L63:  *********************************************************************************************************************/
L64: 
L65: 
L66: /* workaround#HAE - section naming rule */
L67: ${hashtag}ifdef VVIRTUALTARGET
L68: ${hashtag}define DdsCdd_START_SEC_CODE
L69: ${hashtag}else
L70: ${hashtag}define DdsCddType_START_SEC_CODE
L71: ${hashtag}endif
```

43) File: common/templates/autosar/CDD/autosar_gen/DdsCdd.c.vm (L307)  
/* workaround#HAE - right position and senction name */  

```text
L302:   /* workaround#COMMON - PLATFORMS-6094 - task overrun issue */
L303:   /* Initialize DDS adapter layer */
L304:   DdsCdd_Adapter_Init();    //This function will be called by EcuM directly before StartOs.
L305: }
L306: 
L307: /* workaround#HAE - right position and senction name */
L308: ${hashtag}ifdef VVIRTUALTARGET
L309: ${hashtag}define DdsCdd_STOP_SEC_CODE
L310: ${hashtag}else
L311: ${hashtag}define DdsCddType_STOP_SEC_CODE
L312: ${hashtag}endif
```

44) File: common/templates/autosar/CDD/dds_impl/dds_impl_macro.h.vm (L56)  
/* workaround#HAE - don't use serialprintf */  

```text
L51:     ${hashtag}include "#headerInclude()${typeFilePrefix}.h"  /* DDS type definition generated from IDL */
L52:              
L53:         ${hashtag}if (OSAPI_ENABLE_LOG == 1 && OSAPI_ENABLE_TRACE == 1)
L54:             /* TODO: Depend on each platform, change to appropriate logging function */
L55:             //${hashtag}define printf serialprintf
L56:             /* workaround#HAE - don't use serialprintf */
L57:             ${hashtag}define printf(...) do {} while(0) 
L58:         /* Woraround#VTT - cprintf */
L59:         ${hashtag}elif VVIRTUALTARGET
L60:             extern void CANoeAPI_Printf(const char*, ...);
L61:             ${hashtag}define cprintf CANoeAPI_Printf
```

### VTT (2)

45) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L48)  
/* Workaround#VTT */  

```text
L43: ## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
L44: ## macro to include necessary headers for the adapter implementation
L45: ## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
L46: #macro( ddsCddAdapterC_IncludeHeaders $inputFilePlugin)
L47: 
L48: /* Workaround#VTT */
L49: /* Pull RTI/Windows headers first to avoid AUTOSAR macro pollution. */
L50: ${hashtag}if defined(_WIN32) || defined(_WIN64) || defined(RTI_WIN32)
L51: ${hashtag}define SetEvent Win32_SetEvent
L52: ${hashtag}include "../dds_impl/dds_impl.h"
L53: ${hashtag}undef SetEvent
```

46) File: common/templates/autosar/CDD/adaptation/dds_cdd_adapter_macro.c.vm (L72)  
/* Workaround#VTT */  

```text
L67: 
L68: ${hashtag}ifndef netio_common_h
L69: ${hashtag}include "netio/netio_common.h"
L70: ${hashtag}endif
L71: 
L72: /* Workaround#VTT */
L73: /* __at(address) is a target-specific placement extension not supported by MSVC. */
L74: ${hashtag}if defined(_WIN32) || defined(_WIN64) || defined(RTI_WIN32)
L75: ${hashtag}if defined(_MSC_VER) && !defined(__at)
L76: ${hashtag}define __at(address)
L77: ${hashtag}endif
```
