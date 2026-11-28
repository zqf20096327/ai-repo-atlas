# Hue-Jhan/AI-Defence-system

⭐ 10 · Python · CC0-1.0 · 推送 2025-12-08 · [GitHub](https://github.com/Hue-Jhan/AI-Defence-system) · 个人维护

**基于 Arduino 与人脸识别的投掷食物防御装置**

Arduino+PC 组成的机器人防御装置：摄像头读取画面，用 Haar 级联模型检测人脸并经 LBPH 训练识别已知用户；未知人脸持续 2.5 秒后标记为敌对，其坐标经 numpy 换算为角度，驱动伺服与步进电机瞄准，并通过继电器点燃燃气发射软质果实。README 提供零件清单、3D 打印件、三个 Python 脚本说明与组装步骤，并附警示不要复刻该项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Haar 级联检测+LBPH 人脸识别，500 张照片训练生成 Trainer.yml
- 置信度阈值与临时/永久名单机制（known/permanent hostile）
- 伺服+步进电机双轴跟踪，坐标到角度由 numpy 计算
- 继电器控制高压发生器完成燃气发射

## 适用场景

- 复现一个基于人脸识别的机器人瞄准发射项目
- 学习 OpenCV 人脸检测/识别与 Arduino 电机控制的联动
- 作为 stepper/伺服电机控制的代码参考

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L52: This system is based on the Haarscade model, which has to be trained first, i explained the way this model works on
> L61: The actual tracking implemented in the ```defense-system.py``` is more complex, the camera constantly takes picture


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `2a2116f59d6b` · [字段定义](../../DATASET.md)*
