# cem-akkaya/ThermoForgeDemo

⭐ 10 · C++ · NOASSERTION · 推送 2025-12-15 · [GitHub](https://github.com/cem-akkaya/ThermoForgeDemo) · [官网](https://github.com/cem-akkaya/ThermoForge) · 个人维护

**面向 UE 开发者的热学模拟插件示例项目**

ThermoForge 插件的 Unreal Engine 5 示例工程：插件提供热成像视图、实时热传播与渗透、季节与昼夜温度变化、材质热属性（渗透性/隔热）、基于网格单元的 CPU 优化与多线程烘焙。示例关卡包含热源、热体积、测试控件与多人联网示例，逻辑集中在第三人称角色蓝图中，可用按键模拟昼夜/季节循环并切换热视觉视图。需下载工程并在 IDE 中构建后在 Unreal Editor 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时热传播、渗透与季节/昼夜温度模拟
- EQS 查询按冷热评分选择位置，NPC 通过感知对热刺激做出反应
- 热数据支持多人联网复制
- 网格单元 CPU 优化与多线程烘焙/热追踪

## 适用场景

- 在 UE 项目中接入热学模拟玩法
- 参考蓝图示例制作对温度有反应的 NPC 行为
- 测试多人游戏中热数据的网络复制

## 场景标签

 · 领域:游戏开发/物理模拟

## 证据(README 行号)

> L7: This repository contains a **demo project** for the ThermoForge Plugin, an Unreal Engine plugin for thermal simulati
> L22: The demo level includes several thermal volumes, sources, and a simple AI that reacts to heat via perception and EQ
> L37: - **Simple AI logic** that demonstrates how NPCs can perceive and react to thermal stimuli.

## 星数曲线

```mermaid
xychart-beta
    title "cem-akkaya/ThermoForgeDemo 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-16 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `00fc1a1a0d8a` · [字段定义](../../DATASET.md)*
