'''
̹�˴�ս��Ϸ������
1.��Ŀ����Щ��
2.ÿ��������Щ����

1.̹���ࣨ�ҷ�̹�ˣ��з�̹�ˣ�
  1.1.���
  1.2.�ƶ�
  1.3.��ʾ̹����
2.�ӵ���
   2.1.�ƶ�
   2.2.��ʾ�ӵ��ķ���
3.ǽ����
  3.1.���ԣ��Ƿ����ͨ��
4.��ըЧ����
  չʾ��ըЧ��
5��Ч��
  ��������
6����
  6.1.��ʼ��Ϸ
  6.2.������Ϸ
'''


class MainGame():
    def __init__(self):
        pass

    # ��ʼ��Ϸ
    def startGame(self):
        pass

    # ������Ϸ
    def endGame(self):
        pass


class Tank():
    def __init__(self):
        pass

    # �ƶ�
    def move(self):
        pass

    # ���
    def shot(self):
        pass

    # չʾ̹�˵ķ���
    def displayTank(self):
        pass

# �ҷ�̹��
class MyTank(Tank):
    def __init__(self):
        pass

# �з�̹��
class EnemyTank(Tank):
    def __init__(self):
        pass

# �ӵ���
class Bullet():
    def __init__(self):
        pass

    # �ƶ�����
    def move(self):
        pass

    # չʾ�ӵ��ķ���
    def displayBullet(self):
        pass

# ǽ����
class Wall():
    def __init__(self):
        pass
    # չʾǽ�ڵķ���
    def displayWall(self):
        pass

class Explode():
    def __init__(self):
        pass

    # չʾ��ըЧ���ķ���
    def displayExplode(self):
        pass


class Music():
    def __init__(self):
        pass

    # ��������
