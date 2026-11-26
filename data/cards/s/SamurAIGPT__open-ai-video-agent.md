# SamurAIGPT/open-ai-video-agent

⭐ 10 · Python · MIT · 推送 2026-08-27 · [GitHub](https://github.com/SamurAIGPT/open-ai-video-agent) · 组织维护

**给 AI 助手加载的开源视频制作技能工作流集**

一组可移植的指令与参考资料（AGENTS.md 与多个自包含 SKILL.md），为 Claude Code、Codex、Cursor 等 AI 助手提供视频生产工作流：策划、分镜、生成、角色一致性、剪辑、字幕、口播/虚拟人视频等 27 类。仓库本身不托管渲染服务、不发布内容；执行需通过 MCP 或 REST 连接兼容的媒体生成服务（当前适配 Muapi），生成调用可能产生费用，内置预算确认与审批规则。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 27 个自包含 SKILL.md 视频工作流，含策略路由、分镜、口播、广告创意翻拍等
- provider-neutral 能力映射（media.generate_video 等 16 项）可对接 MCP 或 REST
- 付费调用前的预算确认、余额检查与小批量验证流程
- MODELS.md 提供按日期更新的模型选型决策指南

## 适用场景

- 让已有的 AI 助手把产品简介转成 9:16 广告创意与草稿视频
- 把长视频切片、竖屏重构并生成字幕候选
- 为短剧、3D 科普、无脸解说等制作分镜并生成镜头

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L10: Connect a compatible media generation and editing service when you want the
> L11: assistant to execute the workflow. The repository itself is a portable set of
> L57: |Claude Code|Keep `AGENTS.md` in the project and add selected skill folders to `.claude/skills/`.|

## 星数曲线

```mermaid
xychart-beta
    title "SamurAIGPT/open-ai-video-agent 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-29 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `d46888024e1e` · [字段定义](../../DATASET.md)*
