import pytest

from test_game_by_data.load_utils import LoadUtils


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(params=LoadUtils.loadData("test_hero_create.yaml")['volume_success'])
def get_hero_volume_success(request):
    print(request.param)
    request.param = request.param + 1
    print(request.param)
    yield request.param
    print("测试用例执行完成")


@pytest.fixture(params=LoadUtils.loadData("test_hero_create.yaml")['volume_fail'])
def get_hero_volume_fail(request):
    print(request.param)
    request.param = request.param + 1
    print(request.param)
    yield request.param
    print("测试用例执行完成")
