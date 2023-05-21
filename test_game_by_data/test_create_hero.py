import allure
import pytest

from game.hero_management import HeroManagement
from test_game_by_data.conftest import get_hero_volume_success, get_hero_volume_fail
from test_game_by_data.load_utils import LoadUtils


"""
作业内容
针对英雄管理系统的增加功能，完成等价类与边界值的测试。要求测试数据使用单独的文件维护。
使用参数化减少代码量，提高代码的可维护性。
原有需求发生变化，边界值都增加1（变为最大值100，最小值2）。如何在不改变原始测试数据情况下，还能依然完成对修改需求后的测试（使用fixture）。
编写自动化测试用例，结合 Allure 与截图技术等自动生成带截图与操作步骤的测试报告。
将有效等价类和无效等价类的场景分别用标签进行分类。
"""

class Test_hero:
    @allure.title("创建英雄_test_create_hero_name_success")
    @pytest.mark.run(order=2)
    @pytest.mark.SUCCESS
    @pytest.mark.parametrize("name", LoadUtils.loadData("test_hero_create.yaml")["name_success"], ids=["姓名_success"])
    def test_create_hero_name_success(self, name):
        hero_management = HeroManagement()
        hero_management.create_hero(name, 20, 20)
        res = hero_management.find_hero(name)
        assert res.get("name") == "jinx"

    @allure.title("创建英雄_test_create_hero_name_fail")
    @pytest.mark.FAIL
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name", LoadUtils.loadData("test_hero_create.yaml")["name_fail"], ids=["姓名_fail"])
    def test_create_hero_name_fail(self, name):
        hero_management = HeroManagement()
        hero_management.create_hero(name, 20, 20)
        res = hero_management.find_hero(name)
        assert res == False

    @allure.title("创建英雄_test_create_hero_volume_success")
    @pytest.mark.run(order=1)
    @pytest.mark.SUCCESS
    # @pytest.mark.parametrize("volume", get_hero_volume_success, ids=["血量_success_1", "血量_success_2", "血量_success_98", "血量_success_99"])
    def test_create_hero_volume_success(self, get_hero_volume_success):
        hero_management = HeroManagement()
        hero_management.create_hero("volume_success", get_hero_volume_success, 20)
        res = hero_management.find_hero("volume_success")
        assert res.get("volume") == get_hero_volume_success

    @allure.title("创建英雄_test_create_hero_volume_fail")
    @pytest.mark.FAIL
    @pytest.mark.run(order=1)
    # @pytest.mark.parametrize("volume", LoadUtils.loadData("test_hero_create.yaml")["volume_fail"], ids=["血量_fail_0", "血量_fail_100", "血量_fail_-1"])
    def test_create_hero_volume_fail(self, get_hero_volume_fail):
        hero_management = HeroManagement()
        hero_management.create_hero("volume_fail", get_hero_volume_fail, 20)
        res = hero_management.find_hero("volume_fail")
        assert res == False

    @allure.title("创建英雄_test_create_hero_power_success")
    @pytest.mark.SUCCESS
    @pytest.mark.parametrize("power", LoadUtils.loadData("test_hero_create.yaml")["power_success"], ids=["战斗力_success"])
    def test_create_hero_power_success(self, power):
        hero_management = HeroManagement()
        hero_management.create_hero("power_success", 20, power)
        res = hero_management.find_hero("power_success")
        assert res.get("power") == power

    @allure.title("创建英雄_test_create_hero_power_fail")
    @pytest.mark.FAIL
    @pytest.mark.parametrize("power", LoadUtils.loadData("test_hero_create.yaml")["power_fail"], ids=["战斗力_fail_0", "战斗力_fail_-1", "战斗力_fail_0.001", "战斗力_fail_e"])
    def test_create_hero_power_fail(self, power):
        hero_management = HeroManagement()
        hero_management.create_hero("power_fail", 20, power)
        res = hero_management.find_hero("power_fail")
        assert res == False


