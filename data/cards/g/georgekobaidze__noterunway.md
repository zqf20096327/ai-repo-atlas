# georgekobaidze/noterunway

⭐ 14 · TypeScript · 推送 2026-04-18 · [GitHub](https://github.com/georgekobaidze/noterunway) · [官网](https://noterunway.pilotronica.com/) · 个人维护

**AI 辅助的 Notion 工作区清理与管理工具**

浏览器端的 Notion 工作区管理工具：通过 OAuth 连接工作区，运行 7 个核心工具，包括工作区健康仪表盘、语义重复页检测、规则式垃圾页回收、失效链接检测、敏感信息扫描（正则+可选 AI 深扫）、依赖关系图可视化，以及基于 agent 循环的自然语言问答与操作。AI 部分由 Vercel AI SDK 驱动，通过 Notion MCP 执行写入，支持 OpenAI/Anthropic/xAI/Google 四家 BYOK（密钥仅存浏览器）。所有破坏性操作需用户批准，数据留在 Notion 不落库。需 Node.js ≥20.9 自行部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个核心工具：重复检测、垃圾回收、死链、敏感信息、依赖图、语义问答等
- agent 式 Semantic Ask：自然语言分解为工具调用，最多 10 步循环，SSE 流式输出
- 敏感信息扫描覆盖 13 种正则模式（API 密钥/私钥/信用卡等），结果部分脱敏
- BYOK 多供应商支持（OpenAI/Anthropic/xAI/Google），密钥仅存 localStorage

## 适用场景

- 清理 Notion 中的重复页、空页和长期未编辑的陈旧页面
- 排查误存到 Notion 的 API 密钥与个人敏感信息
- 通过对话让 AI 分析工作区并代为执行归档/创建/改名等操作

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L24: **NoteRunway** is a browser-based tool that helps Notion power users clean up, audit, and manage their workspace us
> L39: NoteRunway includes **7 core tools**, split into read-only scanners and AI-powered actions.
> L55: > **AI Required:** No

## 星数曲线

```mermaid
xychart-beta
    title "georgekobaidze/noterunway 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `705e45782a93` · [字段定义](../../DATASET.md)*
