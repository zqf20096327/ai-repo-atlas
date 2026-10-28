# nekyialabs/resonant-mind

⭐ 32 · JavaScript · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/nekyialabs/resonant-mind) · 组织维护

**给 AI agent 的持久认知基础设施：MCP 记忆/身份/情感服务**

运行在 Cloudflare Workers 上的 Postgres 支撑 MCP 服务器，为长期运行的 AI 提供持久记忆与认知状态：47 个按“行为区域”组织的 MCP 工具，覆盖语义检索（pgvector）、视觉记忆（R2）、身份（Spine）、关系（Bonds）、梦境与驱力等；一个定时“潜意识”守护进程每 30 分钟代谢记忆（情绪、留存、巩固、身份提案等）。要求 Node.js 22+、Neon Postgres、Hyperdrive、R2 与 Gemini API key。采用源码可得许可：非商业使用免费，商业使用需另行购买许可。

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

- 47 个 MCP 工具按 Regions（行为类型）组织
- 每 30 分钟运行的潜意识记忆代谢守护进程
- pgvector 语义检索与 R2 视觉记忆
- 故障关闭式鉴权与 HMAC 签名图片 URL 等安全设计

## 适用场景

- 为长期运行的 AI agent 提供持久记忆与身份连续性
- 通过 MCP 接入语义检索、情景记忆与关系数据
- 在 Cloudflare Workers 上自托管认知后端

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L12: - 47 MCP tools organised by kinds of act
> L104: The 47-tool registry is the source of truth. It covers:

## 星数曲线

```mermaid
xychart-beta
    title "nekyialabs/resonant-mind 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-28 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0a22606d20a5` · [字段定义](../../DATASET.md)*
