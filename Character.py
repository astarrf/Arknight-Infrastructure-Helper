# 这里是角色的框架
class Skill:
    def __init__(self, name, init_efficiency, efficiency_func):
        self.name = name  # 技能名字
        self.init_efficiency = init_efficiency  # 初始效率
        self.efficiency = init_efficiency  # 实时效率
        self.efficiency_func = efficiency_func  # 技能效率函数

    def update_efficiency(self, info_dict):
        """
        更新技能效率。
        """
        info_dict['current_efficiency'] = self.efficiency
        self.efficiency = self.efficiency_func(info_dict)

    def get_efficiency(self):
        """
        获取技能效率。
        """
        return self.efficiency


class Character:
    def __init__(self, name, skills: Skill, mood=24):
        self.name = name  # 干员名字
        self.skills = skills  # 技能
        self.mood = mood  # 初始心情值
        self.efficiency = 0  # 实时效率

    def get_name(self):
        """
        获取干员的名字。
        """
        return self.name

    def get_mood(self):
        """
        获取干员的心情值。
        """
        return self.mood

    def update_mood(self, mood):
        """
        更新干员的心情值。
        """
        self.mood = mood

    def update_efficiency(self, info_dict):
        """
        更新干员的动态技能效率，基于其他干员和在流水线上的时间。
        """
        # 示例逻辑，根据实际需要调整
        for skill in self.skills:
            skill.update_efficiency(info_dict)
        self.efficiency = sum([skill.get_efficiency()
                              for skill in self.skills])
