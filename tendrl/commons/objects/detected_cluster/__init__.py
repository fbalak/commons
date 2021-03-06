from tendrl.commons import etcdobj
from tendrl.commons import objects


class DetectedCluster(objects.BaseObject):
    def __init__(self, detected_cluster_id=None, sds_pkg_name=None,
                 sds_pkg_version=None, *args, **kwargs):
        super(DetectedCluster, self).__init__(*args, **kwargs)

        self.value = 'nodes/%s/DetectedCluster'
        self.detected_cluster_id = detected_cluster_id
        self.sds_pkg_name = sds_pkg_name
        self.sds_pkg_version = sds_pkg_version
        self._etcd_cls = _DetectedClusterEtcd


class _DetectedClusterEtcd(etcdobj.EtcdObj):
    """A table of the Detected cluster, lazily updated"""
    __name__ = 'nodes/%s/DetectedCluster'
    _tendrl_cls = DetectedCluster

    def render(self):
        self.__name__ = self.__name__ % NS.node_context.node_id
        return super(_DetectedClusterEtcd, self).render()
