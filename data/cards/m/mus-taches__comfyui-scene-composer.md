# mus-taches/comfyui-scene-composer

⭐ 80 · Python · MIT · 推送 2025-12-18 · [GitHub](https://github.com/mus-taches/comfyui-scene-composer) · [官网](https://civitai.com/models/902456) · 个人维护

**ComfyUI 自定义节点集：随机程序化生成 NSFW 场景工作流**

面向 ComfyUI 的自定义节点集合，用于以随机程序化生成方式构建显式 NSFW 场景工作流。v0.3.x 改用新的子图系统以简化工作流并减少对其他自定义节点的依赖，旧工作流预期会失效，需以仓库的 workflow.json 为基础；部分旧功能（如 CivitAI 元数据解析器）暂时移除。安装途径包括 ComfyUI Manager 导入、Comfy Registry CLI 或手动克隆到 custom_nodes 并安装依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一组用于随机程序化场景生成的 ComfyUI 节点
- v0.3.x 采用子图系统，减少自定义节点依赖
- 提供 workflow.json 作为起步工作流
- MIT 许可证

## 适用场景

- 在 ComfyUI 中搭建随机程序化生成的场景工作流
- 基于示例工作流调参观察生成效果

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L6: A collection of ComfyUI nodes to create explicit NSFW scenes with random procedural generation.
> L24: Clone this repo in `custom_nodes` situated in your ComfyUI install folder.

## 星数曲线

```mermaid
xychart-beta
    title "mus-taches/comfyui-scene-composer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 79 --> 81
    line [80, 80]
```

2026-10-18 80 → 2026-10-29 80（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `9f362f5f14e0` · [字段定义](../../DATASET.md)*
