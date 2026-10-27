# alFrame/ComfyUI-AF-Find-Nodes

⭐ 25 · JavaScript · GPL-3.0 · 推送 2026-09-01 · [GitHub](https://github.com/alFrame/ComfyUI-AF-Find-Nodes) · 个人维护

**ComfyUI 工作流节点查找与统计扩展**

ComfyUI 前端扩展（纯 JavaScript 实现，无其他扩展依赖），提供四种搜索模式：按 Node-ID 定位报错节点并高亮居中、按标题/颜色/标识搜索、按节点包与节点类型搜索（后两者为实验性），另有 Inspector 模式反向显示节点 ID。Stats 标签统计工作流中各节点包的用量占比并可导出清单；Updates 标签比对工作流与已安装节点版本，批量更新节点且保留连接与参数，更新前可自动备份。当前不支持子图（Subgraph）内搜索。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按 Node-ID/标题/节点包/节点类型四种模式查找并高亮定位节点
- 工作流统计：节点总数、节点包数量与占比，可导出清单
- 比对节点版本并批量更新，保留连接、参数与样式，支持自动备份
- 纯 JavaScript 实现，不依赖其他扩展

## 适用场景

- 根据控制台报错的 Node-ID 快速定位问题节点
- 在大型工作流中按自定义标题或节点类型查找节点
- 梳理工作流中各节点包的使用情况并导出文档
- 将工作流中的旧版本节点更新到已安装的最新版本

## 场景标签

 · 领域:AI 工作流工具/ComfyUI 生态

## 证据(README 行号)

> L2: A ComfyUI extension that allows you to find and locate nodes by their ID, title, pack, or type in complex workflows.
> L238: - Pure JavaScript implementation

## 星数曲线

```mermaid
xychart-beta
    title "alFrame/ComfyUI-AF-Find-Nodes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3208e3fe737c` · [字段定义](../../DATASET.md)*
