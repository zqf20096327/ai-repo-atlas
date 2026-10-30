# mareasw/ontoskills

⭐ 23 · Python · MIT · 推送 2026-05-11 · [GitHub](https://github.com/mareasw/ontoskills) · [官网](https://ontoskills.sh) · 组织维护 · 中文 README

**将 SKILL.md 编译为 OWL 2 本体的神经符号技能编译器**

面向企业 AI agent 开发者的工具链：把自然语言技能定义（SKILL.md）编译为经 SHACL 校验的 OWL 2 RDF/Turtle 本体，供 agent 以 SPARQL 查询获得确定性答案。由三个组件构成——Python 编写的编译器 OntoCore、Rust 实现的 MCP 服务器 OntoMCP（内存图、亚毫秒级 SPARQL 查询）、GitHub 上的版本化技能仓库 OntoStore，另配 Node.js CLI 一键安装。需 Python 3.10+ 与 Node.js 18+，MIT 许可。

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

- SKILL.md → OWL 2 本体（.ttl）编译，附 SHACL 校验
- OntoMCP：Rust MCP 服务器，内存图上亚毫秒级 SPARQL 查询
- OntoStore：GitHub 托管的版本化技能仓库
- npx ontoskills 一键安装 MCP 运行时

## 适用场景

- 将技能文件编译成本体，让 agent 查询获得确定性结果
- 通过 MCP 服务器为 Claude 类客户端提供技能知识图查询
- 降低多技能文件造成的上下文消耗

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L29: OntoSkills transforms natural language skill definitions into **validated OWL 2 ontologies** — queryable knowledge 
> L37:     CORE["OntoCore<br/>━━━━━━━━━━<br/>SKILL.md → .ttl<br/>LLM + SHACL"] -->|"compiles"| CENTER["OntoSkills<br/>━━━━
> L73: |**OntoMCP**|Rust|MCP server with sub-ms SPARQL queries|

## 星数曲线

```mermaid
xychart-beta
    title "mareasw/ontoskills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2dac55d73972` · [字段定义](../../DATASET.md)*
