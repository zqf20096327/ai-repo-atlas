# agarwalvivek29/grafana-lookout

⭐ 3 · TypeScript · Apache-2.0 · 推送 2026-11-16 · [GitHub](https://github.com/agarwalvivek29/grafana-lookout) · 个人维护

**面向自托管 Grafana 的 AI 助手插件：用自然语言查询指标日志并给可点链接**

以 Grafana 应用插件形式安装于自托管 Grafana，读取仪表盘、变量与时间范围，通过 Grafana LLM 插件调用用户配置的 OpenAI 兼容端点。功能包括：事故归因并附面板截图与 Explore 查询链接、解释面板、搜索仪表盘、生成 PromQL、以提案方式构建/编辑/重排仪表盘（Apply 前不保存、可 Undo）、汇总 Loki 日志。每个工具以登录用户身份在浏览器内只读执行；面板截图预览需 Grafana Image Renderer。要求 Grafana 13.2+ 与支持工具调用的模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 回答附带可核验链接：匹配面板截图或 Explore 查询
- 仪表盘变更为提案模式，Apply 前不保存且可 Undo
- 工具以登录用户身份经 Grafana API 只读执行，工具结果仅作数据不作指令
- 支持 OpenRouter/OpenAI/本地 Ollama 等 OpenAI 兼容端点

## 适用场景

- 值班排障时用自然语言定位支付超时类事故的根因
- 让 AI 按服务指标一键生成带标签页的 APM 仪表盘草稿
- 区分真实故障与预期内的 not-found 日志噪音
- 在私有网络内用本地模型避免数据外发

## 场景标签

`AI 助手` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L8: An open-source AI assistant for Grafana. Ask about your metrics, logs, traces and dashboards in plain
> L12: Lookout is a regular app plugin for self-hosted Grafana. It needs no Grafana Cloud account and no
> L157: - A model that supports tool calling, behind an OpenAI-compatible API.

## 星数曲线

```mermaid
xychart-beta
    title "agarwalvivek29/grafana-lookout 星数(近 2 点)"
    x-axis ["2026-11-19", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-19 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `0249d82f651a` · [字段定义](../../DATASET.md)*
