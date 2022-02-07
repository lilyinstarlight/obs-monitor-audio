import obspython as obs


settings = None


def script_description():
    return '<b>Monitor Audio</b><hr/>Monitor audio sources as they are shown.<br/><br/>Made by Lily Foster &lt;lily@lily.flowers&gt;'


def script_load(settings_):
    global settings

    settings = settings_

    # monitor all shown sources on load
    sources = obs.obs_enum_sources()
    for source in sources:
        if obs.obs_source_showing(source) and obs.obs_source_get_type(source) == obs.OBS_SOURCE_TYPE_INPUT:
            monitor_source(source)
    obs.source_list_release(sources)

    # connect to 'source_show' event to monitor all added sources when shown
    obs.signal_handler_connect(obs.obs_get_signal_handler(), 'source_show', monitor_source_callback)


def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_editable_list(props, 'ignored', 'Ignored Sources', obs.OBS_EDITABLE_LIST_TYPE_STRINGS, None, None)

    return props


def monitor_source_callback(calldata):
    source = obs.calldata_source(calldata, 'source')
    if not source:
        return

    if obs.obs_source_get_type(source) == obs.OBS_SOURCE_TYPE_INPUT:
        monitor_source(source)


def monitor_source(source):
    ignored = obs.obs_data_get_array(settings, 'ignored')

    for idx in range(obs.obs_data_array_count(ignored)):
        ignored_source_data = obs.obs_data_array_item(ignored, idx)
        ignored_source = str(obs.obs_data_get_string(ignored_source_data, 'value'))
        obs.obs_data_release(ignored_source_data)

        if ignored_source.strip() == obs.obs_source_get_name(source).strip():
            print(f'Ignoring "{obs.obs_source_get_name(source)}"')
            break
    else:
        print(f'Monitoring "{obs.obs_source_get_name(source)}"')
        obs.obs_source_set_monitoring_type(source, obs.OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT)

    obs.obs_data_array_release(ignored)
