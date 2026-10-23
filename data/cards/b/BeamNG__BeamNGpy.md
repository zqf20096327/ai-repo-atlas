# BeamNG/BeamNGpy

⭐ 395 · Python · MIT · 推送 2026-08-20 · [GitHub](https://github.com/BeamNG/BeamNGpy) · [官网](https://beamng.tech) · 组织维护

**远程控制 BeamNG.tech 驾驶模拟器的 Python API 库**

BeamNG 官方维护的 Python 库，以客户端-服务器方式连接 BeamNG.tech（BeamNG.drive 的科研/工业分支），实现对仿真和车辆的远程控制：转向/灯光/换挡等底层输入、配置仿真器自带 AI 驾驶（到点、跟车、轨迹跟随）、采集相机/激光雷达/IMU/超声波等传感器数据（可加噪声）、读取道路网络与场景对象，支持多客户端各自控制一辆车。前置条件是安装 BeamNG.tech（科研/学术用途按申请发放，商用需联系授权），且两方版本需匹配。通过 pip（PyPI）或 conda（conda-forge）安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 远程控制仿真中的车辆（转向、灯光、换挡等）
- 配置仿真器自带 AI 驾驶：到点、跟车、遍历地图、自定义轨迹
- 相机/激光雷达/IMU/超声波等传感器数据采集，可模拟噪声
- 多客户端同时连接同一仿真，各自控制车辆

## 适用场景

- 为自动驾驶算法搭建传感器数据采集与测试环境
- 在仿真的道路网络中生成与回放驾驶场景
- 多进程协同控制多车进行对抗或编队实验

## 场景标签

 · 领域:自动驾驶/仿真

## 证据(README 行号)

> L7: **BeamNGpy** is an official library providing a Python API to [BeamNG.tech][11],
> L36: Besides manual control, BeamNG.tech ships with its own AI to control vehicles.
> L87: Usage of BeamNGpy requires BeamNG.tech to be installed. For commercial use,

## 星数曲线

```mermaid
xychart-beta
    title "BeamNG/BeamNGpy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 394 --> 396
    line [395, 395]
```

2026-10-18 395 → 2026-10-23 395（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `196d554fcea3` · [字段定义](../../DATASET.md)*
