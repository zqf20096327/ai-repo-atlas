# lovelybbq/comfyui-custom-node-color

⭐ 31 · JavaScript · MIT · 推送 2026-01-02 · [GitHub](https://github.com/lovelybbq/comfyui-custom-node-color) · 个人维护

**ComfyUI 节点颜色自定义扩展：可视化取色器与 HEX/RGB 工具节点**

面向 ComfyUI 用户的自定义节点，提供 GUI 取色器修改节点与工作流分组的背景颜色，支持饱和度/色相面板、屏幕取色（Chrome/Edge/Opera）、HEX/RGB 输入、最多 14 个收藏色（FIFO）、4 种节点形状与批量着色，按 C 键快捷打开。另含两个功能节点：Hex Color Input 生成 HEX 字符串，Convert HEX To RGB 解析 HEX 为 RGB 通道并容错处理。可通过 ComfyUI Manager 或手动 git clone 安装；README 标注 NODES 2.0 未测试兼容性，Firefox 不支持取色 API。

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

- GUI 取色器修改节点/分组颜色，支持屏幕取色（Chrome/Edge/Opera）
- 多选节点批量应用颜色与形状，收藏色 FIFO 队列（上限 14 个）
- 4 种节点形状选择与更深色头部样式选项
- Hex Color Input 与 Convert HEX To RGB 两个颜色数据处理节点，容错无效 HEX 输入

## 适用场景

- 为 ComfyUI 工作流节点着色以做视觉分组与整理
- 在流程中生成或解析 HEX/RGB 颜色数据
- 批量调整多个节点的颜色和形状样式

## 场景标签

 · 领域:ComfyUI/可视化工作流工具

## 证据(README 行号)

> L3: > **A modern, GUI-based color picker and utility suite for ComfyUI.** > Change node colors with style, pick colors f
> L26: This tool allows you to visually change the background color of any node in your workflow.

## 星数曲线

```mermaid
xychart-beta
    title "lovelybbq/comfyui-custom-node-color 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ac2e7df17229` · [字段定义](../../DATASET.md)*
