# MaraScott/ComfyUI_MaraScott_Nodes

⭐ 180 · Python · NOASSERTION · 推送 2025-11-12 · [GitHub](https://github.com/MaraScott/ComfyUI_MaraScott_Nodes) · [官网](https://www.marascott.ai/) · 个人维护

**ComfyUI 社区节点集：通用总线管理与逐块放大/细化**

面向 ComfyUI 用户的自定义节点扩展集合，包含 AnyBus 通用总线节点（动态最多 25 输入/输出，带 profile 同步机制）、McBoaty 放大/细化节点集（Upscaler、TilePrompter、Refiner、LargeRefiner 四节点，按切片细化图像用于印刷）、McInpainty 局部重绘，以及文本拼接、循环、多行转列表等辅助节点。McBoaty 已在 SD1.5、SDXL、SD3 测试通过，可选用视觉 LLM 生成切片提示词。README 顶部声明 McBoaty v6 损坏并求助修复。

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

- AnyBus 动态总线最多 25 输入/输出，profile 机制同步同流程节点
- McBoaty 按切片（per-tile）细化提示词与去噪级别，面向印刷放大场景
- 支持 SetNode/GetNode 与部分 Reroute 节点连接
- 附带 ForLoop、文本拼接、多行转列表等辅助节点

## 适用场景

- 整理 ComfyUI 工作台中杂乱的连线
- 放大并逐块细化图像用于印刷输出
- 构建带循环和子循环的工作流

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L9: **ComfyUI_MaraScott_nodes** is an extension set designed to improve the readability of ComfyUI workflows and enhance
> L99: The AnyBus Node (AKA UniversalBus Node) is designed to provide a Universal Bus Node based on AnyType Input/Output.

## 星数曲线

```mermaid
xychart-beta
    title "MaraScott/ComfyUI_MaraScott_Nodes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 179 --> 181
    line [180, 180]
```

2026-10-18 180 → 2026-10-25 180（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4295f6f70af1` · [字段定义](../../DATASET.md)*
