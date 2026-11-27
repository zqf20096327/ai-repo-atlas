# frenchmarcel/auralis

⭐ 3 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/frenchmarcel/auralis) · [官网](https://auralis.readthedocs.io) · 个人维护

**房间声学混合可听化引擎：模拟并双耳聆听房间声音**

Auralis 加载房间模型、指定材质并放置声源与听者，输出双耳脉冲响应、多普勒移动声源与 ISO 3382 参数。采用混合架构：过渡频率以下由 GPU 上的 FDTD 波动求解器捕获房间模式、干涉与衍射，以上由声线追踪与虚源法覆盖，经交叉频率合成单一脉冲响应并用实测头部模型渲染到耳机。在柏林工业大学 BRAS 基准的四个房间及反射/衍射场景上验证，材质取自 BRAS 数据且未对测量调参；支持 GPU 缺失时回退到 CPU 与纯 Python 并给出明确提示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- FDTD 波动求解器 + 声线追踪/虚源法的混合引擎，交叉频率拼接
- 在 TU Berlin BRAS 基准上验证，含反射与衍射场景
- 双耳脉冲响应渲染、移动声源多普勒效应、ISO 3382 参数输出
- GPU→CPU→纯 Python 逐级回退，失败明确提示

## 适用场景

- 在装修或设计前试听房间的声学效果
- 为房间声学研究生成可与 BRAS 对比的双耳脉冲响应
- 模拟移动声源（含多普勒）在房间内的听感

## 场景标签

 · 领域:声学仿真/科研工具

## 证据(README 行号)

> L9: Auralis simulates the sound of a room and lets you listen to it. Load a
> L18: Auralis is a hybrid engine. Below a transition frequency, a **wave solver**


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `b79ffffb0453` · [字段定义](../../DATASET.md)*
