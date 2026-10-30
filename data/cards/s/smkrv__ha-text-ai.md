# smkrv/ha-text-ai

⭐ 85 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/smkrv/ha-text-ai) · [官网](https://github.com/smkrv/ha-text-ai) · 个人维护 · 中文 README

**Home Assistant 的多 LLM 问答集成：让自动化调用大模型**

面向 Home Assistant 的自定义集成，支持在自动化、脚本与开发者工具中向 OpenAI、Anthropic Claude、DeepSeek、Google Gemini 及任意 OpenAI 兼容端点提问。核心机制：按实例保留会话历史（深度 1-20 可配、JSON 文件 1MB 自动轮转）、通过 response_variable 绕过 255 字符状态上限返回完整回复、支持按 schema 的结构化 JSON 输出、每请求可覆盖模型/温度/system prompt，并以传感器属性暴露 token、延迟与错误统计。仅支持 UI 配置，需 Home Assistant 2024.12.0+。经 HACS 或手动放入 custom_components 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 provider 接入：OpenAI/Anthropic/DeepSeek/Gemini 及 OpenAI 兼容端点
- response_variable 返回完整回复，绕过 255 字符状态上限
- 按 schema 的结构化 JSON 输出
- token/延迟/成功率等使用指标以传感器属性暴露

## 适用场景

- 在自动化中向大模型提问并把回复用于后续步骤（如通知）
- 生成符合自定义 JSON schema 的结构化结果
- 用 Markdown 卡片在仪表盘展示问答记录

## 场景标签

`模型网关` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L10: Ask OpenAI, Anthropic Claude, DeepSeek and Google Gemini models questions from your automations and scripts. The in
> L22: - **Multi-provider support**: OpenAI, Anthropic Claude, DeepSeek, Google Gemini, plus any OpenAI-compatible endpoin
> L141: After configuration you get one entity per instance, named `sensor.ha_text_ai_<name>`. It is a status sensor: it s

## 星数曲线

```mermaid
xychart-beta
    title "smkrv/ha-text-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 83 --> 86
    line [84, 85, 85]
```

2026-10-18 84 → 2026-10-30 85（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `88dad0deecda` · [字段定义](../../DATASET.md)*
