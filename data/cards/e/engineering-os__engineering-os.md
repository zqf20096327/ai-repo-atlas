# engineering-os/engineering-os

⭐ 34 · TypeScript · Apache-2.0 · 推送 2026-06-15 · [GitHub](https://github.com/engineering-os/engineering-os) · [官网](https://engineering-os.github.io/engineering-os/) · 组织维护

**给 AI 代码编辑器提供项目持久记忆的 MCP 知识引擎**

面向 Claude Code、Cursor、Codex 等 MCP 兼容编辑器的项目知识层：通过 eos init 索引代码库、识别架构与服务依赖图，AI 工具经 MCP 协议调用 eos_context 即时获取项目知识，调用 eos_learn 持久化新学到的信息。支持跨仓库关联、团队共享配置（workspace yaml 入 git）、增量索引与持续重索引，并内置安全扫描（密钥/注入/CVE）与预索引代码搜索。npm 全局安装，需 Node.js >= 18，无需 API key 与云端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- eos init 索引代码库并构建服务依赖图
- 经 MCP 协议提供 eos_context / eos_learn 等工具，知识跨会话持久化
- 多仓库关联与团队共享 workspace 配置
- 持续安全扫描（密钥、注入、依赖 CVE）与预索引代码搜索

## 适用场景

- 让 AI 编辑器记住架构决策与项目惯例，避免每次会话重新解释
- 多仓库项目中让 AI 看到服务间依赖，减少跨服务破坏性修改
- 团队通过 git 共享同一套项目知识与约定

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: Stop re-explaining your architecture every session. Engineering OS gives Claude Code, Cursor, Codex, and any MCP-com
> L38:     │ MCP Protocol (stdio)
> L45: 3. AI calls `eos_context` and gets full project knowledge instantly

## 星数曲线

```mermaid
xychart-beta
    title "engineering-os/engineering-os 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-27 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cdea9ed2cee1` · [字段定义](../../DATASET.md)*
