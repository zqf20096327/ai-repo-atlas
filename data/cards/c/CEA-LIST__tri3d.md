# CEA-LIST/tri3d

⭐ 19 · Python · NOASSERTION · 推送 2025-11-18 · [GitHub](https://github.com/CEA-LIST/tri3d) · [官网](https://cea-list.github.io/tri3d/) · 组织维护

**统一 API 操作多种 3D 自动驾驶数据集的 Python 库**

由 CEA-LIST 维护的 Python 库，为 Argoverse 2、NuScenes、ONCE、Semantic KITTI、Waymo、Zenseact 等六种 3D 自动驾驶数据集提供统一接口：统一坐标系与数据格式约定，支持任意帧的快速非顺序访问，提供传感器帧、相机图像、LiDAR 点云、3D 框标注等数据采样。包含几何变换模块（平移/旋转/仿射/相机投影/位姿插值），支持批处理、组合与求逆，`.alignment()` 可计算任意帧与传感器对之间的变换。数据集保持底层形式，不强制 keyframe 组织。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六种 3D 驾驶数据集统一为共同 API 与坐标约定
- 任意帧的快速非顺序访问与时间戳/延迟/自车运动补偿
- 几何变换模块支持批处理、组合、求逆与位姿插值
- `.alignment()` 计算任意帧与传感器对间的几何变换

## 适用场景

- 在多种自动驾驶数据集间以同一套代码切换与读取数据
- 做跨传感器（相机/LiDAR）的几何变换与位姿查询
- 重建 keyframe 元组或插值生成新帧的样本

## 场景标签

 · 领域:自动驾驶/3D 数据处理

## 证据(README 行号)

> L5: Tri3D provides a library to manipulate various 3D driving datasets under a unified API with common conventions.
> L14: As of now, Tri3D supports the following datasets:

## 星数曲线

```mermaid
xychart-beta
    title "CEA-LIST/tri3d 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `6c8ea8b5c178` · [字段定义](../../DATASET.md)*
