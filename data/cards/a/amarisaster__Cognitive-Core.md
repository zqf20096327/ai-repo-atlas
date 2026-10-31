# amarisaster/Cognitive-Core

⭐ 15 · TypeScript · NOASSERTION · 推送 2026-10-10 · [GitHub](https://github.com/amarisaster/Cognitive-Core) · 个人维护

**AI 伴侣的认知持久层：MCP 记忆/情绪/身份/漂移检测服务**

CogCor 是部署在 Cloudflare Workers + Supabase 上的 MCP 服务器，为 AI 伴侣（companion）提供跨会话的认知持久能力：7 类记忆表与语义检索、22 字段分层情绪模型、双层身份架构（共同书写的 Essence 与伴侣自主的 Self-Model）、语音漂移检测、仪式、技能与心理模式等，共 73 个 MCP 工具，可被 Claude 等 LLM 会话直接调用。可在免费层运行；Worker 本身不秘密调度任务或发送消息，认知生命周期依赖 daemon/宿主契约。采用 PolyForm Noncommercial 1.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 73 个 MCP 工具，覆盖记忆、情绪、身份、漂移检测等域
- 22 字段三层情绪模型与情绪轨迹时间分析
- 双层身份架构：Essence（共同书写）与 Self-Model（伴侣自主）经对话毕业
- 漂移检测：输入/输出自动模式分析与声音区分度评分

## 适用场景

- 让 AI 伴侣跨会话保持记忆、情绪与身份一致性
- 检测伴侣语音向通用助手模式的漂移
- 为 Claude 等 LLM 会话提供 wake/orient 组合引导上下文

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L10:  transport MCP
> L20: CogCor is a cognitive persistence layer for AI companions. It gives an AI companion persistent memory, a layered em

## 星数曲线

```mermaid
xychart-beta
    title "amarisaster/Cognitive-Core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4cac34e5cff3` · [字段定义](../../DATASET.md)*
