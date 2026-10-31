# pixelpainter/comfyui-mute-bypass-by-ID

⭐ 14 · JavaScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/pixelpainter/comfyui-mute-bypass-by-ID) · [官网](https://registry.comfy.org/nodes/comfyui-mute-bypass-by-id) · 个人维护

**ComfyUI 自定义节点：按节点 ID 静音/旁路任意节点（含嵌套子图）**

ComfyUI 扩展节点包，含 5 个自定义节点：Single（单开关可扩至 20 个目标）、A/B（双路切换，最多 10 对）、Stacker（主控面板，汇总已有节点并提供全局 Mute/Bypass 覆盖），以及两个为兼容旧工作流保留的 legacy 节点（Triple、AA/BB）。按节点 ID 或名称选取目标，可穿透嵌套 Subgraph；开关是标准 ComfyUI widget，可链接或提升到 Subgraph 顶层。通过 ComfyUI Manager、comfy-cli 或手动 clone 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按节点 ID/名称静音或旁路工作流中任意节点，含嵌套 Subgraph
- Stacker 主控面板汇总多个控制节点，支持全局覆盖与一键恢复原状态
- Single 可扩展至 20 个目标，A/B 支持最多 10 对同时切换
- 开关为标准 widget，可链接或提升到 Subgraph 作为顶层开关

## 适用场景

- 迭代时临时关闭保存/预览分支，出图时再启用
- 从顶层控制 Subgraph 内部深层节点的启停
- 大工作流中用主控面板一键旁路所有可选分支做快速测试渲染

## 场景标签

 · 领域:图像生成/ComfyUI 工具

## 证据(README 行号)

> L12: **Mute or bypass any node in your workflow by its node ID or Name** — even nodes buried inside nested Subgraphs — f
> L14: This pack includes **5 custom nodes**:

## 星数曲线

```mermaid
xychart-beta
    title "pixelpainter/comfyui-mute-bypass-by-ID 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e1cc0ab8cd31` · [字段定义](../../DATASET.md)*
