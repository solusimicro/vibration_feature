def estimate_mtbf(base_mtbf_hours, health_index):
    """
    base_mtbf_hours: OEM / historical MTBF
    health_index: 0–1
    """
    return round(base_mtbf_hours * health_index, 1)
# MTBF estimation service
# This service estimates the Mean Time Between Failures (MTBF) based on a base MTBF and the health index of the machinery.