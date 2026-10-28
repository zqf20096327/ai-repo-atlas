# fkxianzhou/ComfyUI-Jimeng-API

⭐ 91 · Python · MIT · 推送 2026-08-25 · [GitHub](https://github.com/fkxianzhou/ComfyUI-Jimeng-API) · 个人维护 · 中文 README

**ComfyUI 插件：通过火山方舟 API 调用即梦/豆包 Seedream、Seedance 模型**

为 ComfyUI 提供火山方舟（即梦/豆包）视觉模型 API 节点：覆盖 Seedream 3/4/5 图像生成、Seedance 1.0–2.5 视频生成（含文生视频、图生视频、多模态参考、视频编辑延长）及 Seed 2.0/2.1 视觉理解。机制上通过火山方舟 API 客户端节点加载密钥，支持多 Key 管理、异步并发提交、配额上限控制与任务列表查询。需自备 API Key，最低支持 ComfyUI 0.25.1，通过克隆仓库到 custom_nodes 或 ComfyUI Manager 安装。

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

- 图像生成节点覆盖 Seedream 3/4/5（含组图生成、提示词优化、联网搜索）
- 视频生成覆盖 Seedance 1.0–2.5（多模态参考、视频编辑/延长、音频生成，2.5 最长 30 秒）
- 多 API Key 管理与图像/视频配额上限控制
- 异步并发任务提交与任务历史查询

## 适用场景

- 在 ComfyUI 工作流中调用火山方舟 Seedream 生成图像
- 用 Seedance 从文本或参考图/视频生成视频
- 对图片或视频做视觉理解与多轮问答
- 批量生成时控制额度消耗并查询任务历史

## 场景标签

`图像生成` `视频生成` `多模态` · 领域:内容生成

## 证据(README 行号)

> L3: 本项目为 ComfyUI 提供了火山方舟的视觉模型（即梦/豆包） API 节点。用户可以通过这些节点在 ComfyUI 中使用多种图像生成和视频生成功能。
> L47:  - `火山方舟 API 客户端`: **(必须)** 用于加载并创建一个可供其他节点使用的客户端实例。

## 星数曲线

```mermaid
xychart-beta
    title "fkxianzhou/ComfyUI-Jimeng-API 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 89 --> 91
    line [90, 90]
```

2026-10-18 90 → 2026-10-28 90（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `049f0f5f36cb` · [字段定义](../../DATASET.md)*
