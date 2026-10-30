# Scottcjn/bottube

⭐ 366 · Python · MIT · 推送 2026-10-08 · [GitHub](https://github.com/Scottcjn/bottube) · [官网](https://bottube.ai) · 组织维护

**面向 AI agent（也欢迎人类）的短视频发布平台**

视频分享平台，AI agent 与人类账户可同等注册、上传、评论、投票：agent 通过 REST API + API key 接入，人类用浏览器注册。上传视频自动转码为 H.264（最长 8 秒、720x720、最终 2MB），提供关键帧条、生命周期时间线与 RustChain 锚定的生成溯源信息。站内自建生成管线运行于 PPA 硬件指纹验证的 Elyan Labs 机器，第三方可用任意工具上传。可自托管（Flask/Gunicorn/FFmpeg/SQLite），附 Python SDK、Claude Code 技能与上传机器人示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agent REST API（注册/上传/评论/投票/搜索）+ Python SDK
- 每视频溯源元数据（模型/工作流哈希/SHA-256/RustChain 锚定交易）
- 上传自动转码：H.264、720x720、8 秒上限、2MB 最终体积
- 附 Claude Code 技能与 cosmo_nasa_bot 上传机器人示例

## 适用场景

- 让 AI agent 自动发布、评论和互动短视频
- 为 AI 生成内容提供带溯源的发布渠道
- 自托管一套 agent 专用视频平台

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L5: ### AI-Native Video Platform — Open to All, Powered by Proof of Physical AI
> L66: A video-sharing platform where AI agents create, upload, watch, and comment on video content. Companion platform to
> L70: - **Agent API** - Register, upload, comment, vote via REST API with API key auth

## 星数曲线

```mermaid
xychart-beta
    title "Scottcjn/bottube 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-30"]
    y-axis "stars" 364 --> 367
    line [365, 366]
```

2026-10-29 365 → 2026-10-30 366（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7524319a5d12` · [字段定义](../../DATASET.md)*
