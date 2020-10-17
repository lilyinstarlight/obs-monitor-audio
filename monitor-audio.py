import obspython as obs


def script_description():
    return '<b>Monitor Audio</b><hr/>Monitor all audio sources and enforce monitoring with new sources as they are shown.<br/><br/>Made by Lily Foster &lt;lily@lily.flowers&gt;'


def script_load(settings):
    # monitor all shown sources on load
    sources = obs.obs_enum_sources()
    for source in sources:
        if obs.obs_source_showing(source) and obs.obs_source_get_type(source) == obs.OBS_SOURCE_TYPE_INPUT:
            monitor_source(source)
    obs.source_list_release(sources)

    # connect to global 'source_show' to monitor all added sources when added to scene
    obs.signal_handler_connect(obs.obs_get_signal_handler(), 'source_show', monitor_source_callback)


def monitor_source_callback(calldata):
    source = obs.calldata_source(calldata, 'source')
    if not source:
        return

    if obs.obs_source_get_type(source) == obs.OBS_SOURCE_TYPE_INPUT:
        monitor_source(source)


def monitor_source(source):
    print(f'Monitoring "{obs.obs_source_get_name(source)}"')
    obs.obs_source_set_monitoring_type(source, obs.OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT)
