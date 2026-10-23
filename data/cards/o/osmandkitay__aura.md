# osmandkitay/aura

⭐ 106 · TypeScript · MIT · 推送 2026-03-13 · [GitHub](https://github.com/osmandkitay/aura) · 个人维护

**让网站以声明式 manifest 向 AI agent 暴露操作能力的开放协议**

AURA 是一个开放协议规范，配套 npm 包与参考实现：网站在 /.well-known/aura.json 发布 manifest，声明 capabilities（动词）、resources（名词）与 HttpAction（RFC 6570 URL 模板、JSON Pointer 参数映射），agent 读取后直接调用声明的 HTTP 端点，替代 UI 抓取；可选 AURA-State 头描述会话上下文。manifest 是描述性而非授权性，鉴权与校验由服务端执行。提供 TypeScript 类型、JSON Schema、aura-validate CLI、Next.js 参考服务器与 Node.js 参考客户端（后者用 OpenAI API 规划动作）。规范标注为实验性 v1.0，可能有破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- manifest 声明 capabilities/resources/HttpAction，agent 直接调用声明的 HTTP 端点
- AURA-State 头提供会话级能力上下文（advisory，服务端为准）
- npm 包提供 TypeScript 类型、JSON Schema 与 aura-validate CLI
- 含 Next.js 参考服务器与 Node.js 参考客户端（agent/crawler/test-workflow）

## 适用场景

- 网站向 AI agent 暴露可调用能力，替代脆弱的页面抓取
- 为 LLM 工具调用方提供可审计的小型动作清单
- 用 CLI 校验本站 manifest 的合法性与引用一致性

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: AURA is an open protocol for making a website's capabilities machine-readable and explicitly permissioned to act on.
> L21: AURA (Agent-Usable Resource Assertion) is a small, explicit contract between a website and an AI agent. A site publ

## 星数曲线

```mermaid
xychart-beta
    title "osmandkitay/aura 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-23 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8d912ca3e329` · [字段定义](../../DATASET.md)*
