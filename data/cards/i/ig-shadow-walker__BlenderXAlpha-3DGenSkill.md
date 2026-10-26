# ig-shadow-walker/BlenderXAlpha-3DGenSkill

⭐ 30 · JavaScript · MIT · 推送 2026-07-21 · [GitHub](https://github.com/ig-shadow-walker/BlenderXAlpha-3DGenSkill) · 个人维护

**让 AI 编码 agent 在 Blender 中按英文描述生成并布置 3D 场景**

面向 Claude Code、Cursor、OpenAI Codex 的 Agent Skill：把 3D 生成服务（默认 Alpha3D，可换 Tripo 或 Meshy）与 Blender MCP 桥接器连接起来。用户用自然语言描述场景，agent 拆分为单个资产、先给出 credit 成本表并等待确认，再逐个生成 GLB 模型，导入正在运行的 Blender，按真实世界尺寸缩放、落地并布局。支持复用已生成模型、用 Blender 图元替代简单几何体、视口截图自查与修正。生成需消耗服务商真实 credit，需本机运行 agent 与 Blender 同机配合。

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

- 文本/图片/多视图生成 3D 模型并导入实时 Blender 场景
- 生成前展示逐资产成本表，经确认才消耗 credit
- 智能来源分配：主角资产用 AI 生成、平面/立方体用免费 Blender 图元
- 可选自动绑骨、重拓扑、UV 展开、重贴图等精修流程

## 适用场景

- 用一句英文在 Blender 里搭出游戏关卡或小村庄等场景
- 向现有场景中按位置语义添加道具（如'放一盏灯在桌上'）
- 生成概念图（FLUX）后再转为 3D 模型

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L5: An Agent Skill for Claude Code, also usable in Cursor and OpenAI Codex, that connects an AI 3D provider (Alpha3D by 
> L60: This skill is pure orchestration. It plugs two MCP connectors together and does the scene reasoning in between.
> L71: 1. **Your chosen 3D provider's MCP** (Alpha3D by default, or Tripo or Meshy) generates the actual 3D models and han

## 星数曲线

```mermaid
xychart-beta
    title "ig-shadow-walker/BlenderXAlpha-3DGenSkill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2e636240bd26` · [字段定义](../../DATASET.md)*
