# HMAKT99/AKF

⭐ 20 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/HMAKT99/AKF) · [官网](https://akf.dev) · 个人维护

**为 AI 生成的文件附带可信元数据的文件格式与工具链**

AKF 是一种将信任元数据（置信度、验证证据、来源链、合规标记）嵌入 AI 生成文件的文件格式，README 类比为『AI 的 EXIF』。面向 AI 编码 agent 与多 agent 团队：agent 验证后用 `akf stamp` 打戳，后续 agent 用 `akf check` 免去重复验证；戳可携带可重放的探针命令（如 pytest）供证伪复核。提供 Python/TypeScript 库、CLI、MCP 服务器（11 个工具）、后台自动打戳 watcher、shell hook、VS Code/GitHub Action/Office 扩展及 LangChain/LlamaIndex/CrewAI 集成包，支持 docx/pdf/html/png 等多种格式嵌入与 EU AI Act 合规审计命令。

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

- 信任元数据随文件传播：置信度、证据、来源链、合规标记
- 可证伪的 replay 探针：下个 agent 重跑命令而非信任签名
- MCP 服务器提供 11 个工具（check/replay/stamp/audit 等）
- 10 类安全检测（幻觉风险、知识洗白、信任降级链等）与信任计算公式

## 适用场景

- 让跨会话、跨工具的 AI agent 复用已验证结论，避免重复验证
- 自动为 AI 编辑的文件附带来源与置信元数据
- 对文件运行 EU AI Act 合规审计
- 多 agent 委派时设置信任上限，防止信任膨胀

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L45: Agents redo work constantly: re-read files, re-run tests, re-derive conclusions — because nothing tells them what w
> L115: AKF is designed **agent-first**. One-line APIs for checking, stamping, streaming, and auditing.
> L147: AKF ships an MCP server so any AI agent can create, validate, scan, and audit trust metadata.

## 星数曲线

```mermaid
xychart-beta
    title "HMAKT99/AKF 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `daf45d2f0e1a` · [字段定义](../../DATASET.md)*
