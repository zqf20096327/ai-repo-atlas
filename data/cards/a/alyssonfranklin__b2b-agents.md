# alyssonfranklin/b2b-agents

⭐ 23 · Python · 推送 2026-06-09 · [GitHub](https://github.com/alyssonfranklin/b2b-agents) · [官网](https://www.linkedin.com/in/alyssonfranklin/) · 个人维护

**面向 B2B 企业的 56 个专业 agent 库及跨平台编译管线**

收录 56 个覆盖工程、产品、营销、设计、运营、测试等领域的专业 agent，以 Claude .md 文件为事实源，通过管线抽取为中立格式（neutral/*.agent.yaml），再由适配器编译到 Claude Code、OpenAI Agents SDK 或 Custom GPT。提供 company-builder agent 通过约 9 个问题的 intake 生成定制公司目录并自动选择编译目标；能力受限平台会收到列明降级内容的构建报告。agent 以推理档位（fast/balanced/deep）声明而非硬编码模型，声明保持平台中立。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一次编写 agent，编译到 Claude Code / OpenAI Agents SDK / Custom GPT 三类目标
- company-builder 通过 intake 问题生成定制公司配置并自动编译
- 受限平台输出降级报告，列明被扁平化或丢弃的内容
- agent 按 fast/balanced/deep 推理档位声明，映射到各平台对应模型

## 适用场景

- 为 B2B 初创或企业团队部署多领域 AI agent 系统
- 把同一套 agent 库迁移到不同的 agent 平台运行
- 按公司业务上下文定制 agent 集合并生成安装路径

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: Author your agents once. Ship them to **Claude Code**, the **OpenAI Agents SDK**, or a
> L16: bindings, orchestration mechanism). A small pipeline compiles the neutral source to each
> L78: python3 scripts/extract_neutral.py --src .       --out neutral      # agents → neutral

## 星数曲线

```mermaid
xychart-beta
    title "alyssonfranklin/b2b-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `50f814d2a04f` · [字段定义](../../DATASET.md)*
