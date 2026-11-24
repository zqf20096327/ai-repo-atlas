# mustaf4-saglam/SecDataForge

⭐ 3 · Python · 推送 2026-10-18 · [GitHub](https://github.com/mustaf4-saglam/SecDataForge) · 个人维护

**面向 LLM 训练者的土耳其语网络安全数据集生成工具**

从 GitHub Advisory 与 OSV 等公开安全数据源采集漏洞通告，经标准化、去重后，可选通过 LLM 生成土耳其语翻译、防护建议与问答对，最终以 JSONL/CSV 导出用于 LLM 训练与评估。带 CLI（typer）与 Streamlit 管理面板，记录、处理状态与质检结果存于 SQLite；LLM 集成默认关闭，所有 LLM 输出进入人工审核队列，且源数据的关键字段（CVE、版本、严重级等）不允许被改动。README 明确声明本项目不是聊天机器人。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 GitHub Advisory Database 与 OSV API 采集并分页、去重、断点续传（--resume/--full-history/--since）
- LLM 可选增强：土耳其语翻译、防护建议、问答对，默认关闭，输出全部进入人工审核队列
- 数据带 license_status 策略：unknown/restricted 记录默认不进入可导出数据集
- 支持六种 LLM 提供方（ollama/openai_compatible/gemini/claude/huggingface/evren），经 Pydantic 校验输出

## 适用场景

- 为土耳其语安全领域 LLM 微调构建数据集
- 定期增量采集安全通告并维护本地漏洞数据仓库
- 按许可策略筛选可再分发的训练数据

## 场景标签

`网络安全` `微调` · 领域:学习与行业

## 证据(README 行号)

> L5: SecDataForge, açık siber güvenlik kaynaklarından veri toplar, standartlaştırır,
> L21: - Ollama / OpenAI uyumlu API: isteğe bağlı LLM bağlantısı (kapalı varsayılan)

## 星数曲线

```mermaid
xychart-beta
    title "mustaf4-saglam/SecDataForge 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-22 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `a841854d9e21` · [字段定义](../../DATASET.md)*
