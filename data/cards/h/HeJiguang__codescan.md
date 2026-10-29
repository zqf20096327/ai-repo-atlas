# HeJiguang/codescan

⭐ 22 · Python · MIT · 推送 2026-04-02 · [GitHub](https://github.com/HeJiguang/codescan) · 个人维护 · 中文 README

**AI 辅助的代码安全扫描器，支持 MCP 与 Codex 集成**

面向合并前审查的代码安全扫描工具：先运行确定性规则扫描，再用 LLM 分析（LangChain 统一 DeepSeek/OpenAI/Anthropic 等提供商，LangGraph 组成 rule_scan→llm_scan→merge 流水线）深化上下文，输出结构化安全发现，支持文件、目录、GitHub 仓库与 Git diff 扫描，生成 HTML/JSON/文本报告。通过 MCP 服务器和可安装的 codescan-review 技能接入 Codex 等编程 agent，另有桌面 GUI。README 声明它不是完整 SAST 平台，缺少深度数据流分析，高严重度发现需人工确认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性规则扫描 + LLM 深化分析的结构化输出流水线
- MCP 服务器与 Codex 技能层，供编程 agent 直接调用
- 支持文件/目录/GitHub 仓库/Git diff 四种扫描对象，输出 HTML/JSON/文本报告
- LangChain 统一 DeepSeek、OpenAI、Anthropic 及 OpenAI 兼容端点

## 适用场景

- 合并代码前做第二道安全审查
- 让 Codex 等 agent 通过 MCP 在审查流程中调用结构化扫描
- 维护者对仓库做轻量安全分诊，无需部署大型平台

## 场景标签

`代码审查` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L7: AI-assisted code security scanning for files, repositories, Git diffs, and coding agents.
> L27: - Start with deterministic rule-based signal
> L28: - Use LLM analysis to deepen context and explanation

## 星数曲线

```mermaid
xychart-beta
    title "HeJiguang/codescan 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2899a6e987bd` · [字段定义](../../DATASET.md)*
