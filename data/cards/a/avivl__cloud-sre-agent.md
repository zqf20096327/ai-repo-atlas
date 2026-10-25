# avivl/cloud-sre-agent

⭐ 53 · Go · MIT · 推送 2026-06-29 · [GitHub](https://github.com/avivl/cloud-sre-agent) · 个人维护

**给运维/SRE：LLM 驱动的日志事件检测与自动修复代理（Go）**

用 Go 编写的自主 SRE 代理：从文件或 Pub/Sub 读取日志，滑动窗口阈值检测触发事件后，经 LLM 三阶段流水线（triage→根因分析→生成修复补丁），补丁经代码校验后以本地文件、GitHub PR 或 GitLab MR 交付。LLM 后端支持 Gemini(Vertex/Developer API)、OpenAI、Anthropic、Ollama、stub，按端口适配器架构组织。面向 HIPAA 敏感环境：提示输入经脱敏，外部 LLM 默认拒绝（fail-closed）。可部署为 Cloud Run worker pool，也提供无凭据的离线 stub 快速上手。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- triage→分析→修复补丁的 LLM 流水线，输出 GitHub PR / GitLab MR / 本地文件
- 多 LLM 后端（Gemini/OpenAI/Anthropic/Ollama/stub）与主备回退路由
- HIPAA 设计：提示脱敏、BAA 门控、外部 LLM 默认启动拒绝
- stub 提供者支持无 API key 离线端到端运行

## 适用场景

- 监控云日志流并自动生成修复补丁开 PR
- 在 HIPAA 合规约束下用 LLM 做 SRE 根因分析
- 本地离线先跑通流水线再接入生产日志源

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: An LLM-driven SRE agent, written in Go. It ingests logs, detects incidents from
> L25: 3. The **pipeline** runs the incident through three LLM stages — triage
> L27:  (concrete code patch). Every prompt input is sanitized first; the generated

## 星数曲线

```mermaid
xychart-beta
    title "avivl/cloud-sre-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-25 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3ca67ad2ad80` · [字段定义](../../DATASET.md)*
