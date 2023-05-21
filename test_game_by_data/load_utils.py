import pytest
import yaml


class LoadUtils:

    @classmethod
    def loadData(self, yaml_path):
        return yaml.safe_load(open(yaml_path))


# @pytest.fixture(params=LoadUtils.loadData("test_hero_create.yaml")['volume_fail'])
# def get_hero_volume_fail(request):
#     print(request.param)
#     request.param = request.param + 1
#     print(request.param)
#     yield request.param
#     print("测试用例执行完成")

if __name__ == '__main__':
    # print(LoadUtils.loadData("test_hero_create.yaml"))
    print(get_hero_volume_fail)